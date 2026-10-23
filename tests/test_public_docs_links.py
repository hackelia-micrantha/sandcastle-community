"""Regression tests for the public offline documentation link gate."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.check_public_docs_links import check_public_links


class PublicDocsLinkChecks(unittest.TestCase):
    def setUp(self) -> None:
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "repository"
        self.root.mkdir()

    def write(self, path: str, content: str) -> Path:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return target

    def test_existing_relative_encoded_and_fragment_targets(self) -> None:
        self.write("docs/guide.md", "[root](../README.md)\n")
        self.write("docs/space name.md", "text\n")
        self.write(
            "README.md",
            "[guide](docs/guide.md#example)\n"
            "[space](docs/space%20name.md)\n"
            "[docs](docs/)\n"
            "[remote](https://example.org/path)\n"
            "[mail](mailto:security@example.org)\n"
            "[section](#overview)\n",
        )
        self.assertEqual([], check_public_links(self.root))

    def test_missing_local_target_fails(self) -> None:
        self.write("README.md", "[missing](docs/not-found.md)\n")
        self.assertIn("missing link target", "\n".join(check_public_links(self.root)))

    def test_rejects_relative_escape(self) -> None:
        self.write("README.md", "[escape](../private.md)\n")
        self.assertIn("escapes repository", "\n".join(check_public_links(self.root)))

    def test_rejects_symlink_escape(self) -> None:
        target = self.root.parent / "private.md"
        target.write_text("private", encoding="utf-8")
        (self.root / "linked.md").symlink_to(target)
        self.write("README.md", "[linked](linked.md)\n")
        self.assertIn("escapes repository", "\n".join(check_public_links(self.root)))

    def test_rejects_absolute_and_unsafe_scheme(self) -> None:
        self.write("README.md", "[absolute](/docs/guide.md)\n[unsafe](javascript:alert)\n")
        result = "\n".join(check_public_links(self.root))
        self.assertIn("absolute link", result)
        self.assertIn("unsupported link scheme", result)

    def test_ignores_fenced_code_examples(self) -> None:
        self.write("README.md", "~~~markdown\n[example](missing.md)\n~~~\n")
        self.assertEqual([], check_public_links(self.root))

    def test_fails_without_public_markdown(self) -> None:
        self.assertIn("No public Markdown", "\n".join(check_public_links(self.root)))


if __name__ == "__main__":
    unittest.main()
