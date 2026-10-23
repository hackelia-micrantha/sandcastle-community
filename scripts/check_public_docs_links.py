#!/usr/bin/env python3
"""Check repository-local Markdown link targets without network access.

Deliberately bounded: inline Markdown links, not rendered HTML, remote URL
availability, reference-style definitions, or heading anchors.
"""

from html import unescape
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


PUBLIC_MARKDOWN_GLOBS = ("*.md", "docs/**/*.md")
REMOTE_SCHEMES = frozenset({"https", "http", "mailto"})
FENCE_MARKER = re.compile(r"^ {0,3}(?P<marker>\x60{3,}|~{3,})(?P<rest>.*)$")
INLINE_CODE = re.compile(r"(?<![\\\x60])(\x60+)(?!\x60)(.*?)(?<!\\)\1(?!\x60)")
INLINE_LINK = re.compile(
    r"""(?<!\\)!?\[[^\]\n]*\]\(\s*(?P<target><[^>\n]+>|[^\s)]+)(?:\s+(?:"[^"\n]*"|'[^'\n]*'))?\s*\)"""
)


def check_public_links(root: Path) -> list[str]:
    root = root.resolve()
    findings: list[str] = []
    documents = sorted({p for pattern in PUBLIC_MARKDOWN_GLOBS for p in root.glob(pattern)})
    if not documents:
        return ["No public Markdown documents found"]

    for document in documents:
        fence: tuple[str, int] | None = None
        for number, line in enumerate(document.read_text(encoding="utf-8").splitlines(), 1):
            marker_match = FENCE_MARKER.match(line)
            if fence is not None:
                if marker_match:
                    marker = marker_match.group("marker")
                    if (
                        marker[0] == fence[0]
                        and len(marker) >= fence[1]
                        and not marker_match.group("rest").strip()
                    ):
                        fence = None
                continue

            # Markdown fences permit at most three leading spaces. Four
            # spaces or a tab is an indented code line, not a fence opener.
            if line.startswith(("    ", "\t")):
                continue
            if marker_match:
                marker = marker_match.group("marker")
                fence = (marker[0], len(marker))
                continue

            # Mask inline code spans without masking links next to them.
            prose = INLINE_CODE.sub(lambda match: " " * len(match.group()), line)
            for match in INLINE_LINK.finditer(prose):
                # CommonMark decodes character references in destinations.
                # Decode before URI classification to reject disguised schemes.
                href = unescape(match.group("target").strip("<>"))
                if href.startswith(("#", "//")):
                    continue
                parsed = urlsplit(href)
                if parsed.scheme:
                    if parsed.scheme.lower() not in REMOTE_SCHEMES:
                        findings.append(
                            f"{document.relative_to(root)}:{number}: unsupported link scheme: {href}"
                        )
                    continue
                if not parsed.path:
                    continue

                path = Path(unquote(parsed.path))
                if path.is_absolute():
                    findings.append(f"{document.relative_to(root)}:{number}: absolute link: {href}")
                    continue
                target = (document.parent / path).resolve()
                if not target.is_relative_to(root):
                    findings.append(f"{document.relative_to(root)}:{number}: link escapes repository: {href}")
                elif not target.exists():
                    findings.append(f"{document.relative_to(root)}:{number}: missing link target: {href}")
    return findings


if __name__ == "__main__":
    problems = check_public_links(Path(__file__).resolve().parents[1])
    if problems:
        raise SystemExit("\n".join(problems))
    print("Public Markdown local links: OK")
