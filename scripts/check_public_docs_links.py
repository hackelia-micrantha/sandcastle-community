#!/usr/bin/env python3
"""Check repository-local Markdown link targets without network access.

This is a deliberately bounded check: inline Markdown links, not rendered HTML,
remote URL availability, reference-style definitions, or heading anchors.
"""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


PUBLIC_MARKDOWN_GLOBS = ("*.md", "docs/**/*.md")
REMOTE_SCHEMES = frozenset({"https", "http", "mailto"})
CODE_FENCE_PREFIXES = (chr(96) * 3, "~" * 3)
INLINE_LINK = re.compile(
    r"""!?\[[^\]\n]+\]\(\s*(?P<target><[^>\n]+>|[^\s)]+))(?:\s+(?:"[^"\n]*"|'[^'\n]*'))?\s*\)"""
)


def check_public_links(root: Path) -> list[str]:
    root = root.resolve()
    findings: list[str] = []
    documents = sorted({p for pattern in PUBLIC_MARKDOWN_GLOBS for p in root.glob(pattern)})
    if not documents:
        return ["No public Markdown documents found"]

    for document in documents:
        fence: str | None = None
        for number, line in enumerate(document.read_text(encoding="utf-8").splitlines(), 1):
            stripped = line.lstrip()
            if stripped.startswith(CODE_FENCE_PREFIXES):
                marker = stripped[0]
                if fence is None:
                    fence = marker
                elif fence == marker:
                    fence = None
                continue
            if fence is not None:
                continue

            for match in INLINE_LINK.finditer(line):
                href = match.group("target").strip("<>")
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
