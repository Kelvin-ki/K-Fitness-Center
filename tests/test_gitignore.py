"""
Tests for .gitignore — K Fitness Center repository.

Validates that the .gitignore added in this PR correctly defines the expected
ignore patterns for Python bytecode and cache directories.
"""

import os
import re
import unittest

GITIGNORE_PATH = os.path.join(os.path.dirname(__file__), "..", ".gitignore")


def read_gitignore() -> str:
    with open(GITIGNORE_PATH, encoding="utf-8") as f:
        return f.read()


class TestGitignorePatterns(unittest.TestCase):
    """Core pattern presence tests."""

    def setUp(self):
        self.content = read_gitignore()

    def test_file_exists(self):
        """The .gitignore file must exist at the repository root."""
        self.assertTrue(os.path.isfile(GITIGNORE_PATH), ".gitignore not found at repository root")

    def test_file_is_not_empty(self):
        """The .gitignore must not be empty."""
        self.assertGreater(len(self.content.strip()), 0)

    def test_pycache_directory_pattern_present(self):
        """__pycache__/ must be listed to exclude Python bytecode cache directories."""
        self.assertIn("__pycache__/", self.content)

    def test_pyc_cod_pattern_present(self):
        """*.py[cod] must be listed to exclude compiled Python files (.pyc, .pyo, .pyd)."""
        self.assertIn("*.py[cod]", self.content)

    def test_pycache_pattern_on_own_line(self):
        """__pycache__/ must appear on its own line, not embedded in another pattern."""
        lines = self.content.splitlines()
        pycache_lines = [ln.strip() for ln in lines if "__pycache__/" in ln]
        self.assertTrue(
            any(ln == "__pycache__/" for ln in pycache_lines),
            "__pycache__/ must be a standalone pattern line",
        )

    def test_pyc_cod_pattern_on_own_line(self):
        """*.py[cod] must appear on its own line."""
        lines = self.content.splitlines()
        pyc_lines = [ln.strip() for ln in lines if "*.py[cod]" in ln]
        self.assertTrue(
            any(ln == "*.py[cod]" for ln in pyc_lines),
            "*.py[cod] must be a standalone pattern line",
        )

    def test_both_patterns_present(self):
        """Both Python-related ignore patterns must exist together."""
        self.assertIn("__pycache__/", self.content)
        self.assertIn("*.py[cod]", self.content)


class TestGitignoreEdgeCases(unittest.TestCase):
    """Boundary and regression checks."""

    def setUp(self):
        self.content = read_gitignore()
        self.lines = self.content.splitlines()

    def test_no_crlf_line_endings(self):
        """File must use Unix line endings (LF), not Windows CRLF."""
        self.assertNotIn("\r", self.content, ".gitignore should not contain carriage returns (CRLF)")

    def test_file_ends_with_newline(self):
        """Well-formed text files should end with a newline character."""
        self.assertTrue(self.content.endswith("\n"), ".gitignore should end with a trailing newline")

    def test_no_secret_paths_accidentally_ignored(self):
        """The .gitignore must not accidentally exclude .env files or credential files."""
        sensitive_patterns = [".env", "credentials", "secrets", "id_rsa", "*.pem"]
        for pattern in sensitive_patterns:
            with self.subTest(pattern=pattern):
                self.assertNotIn(pattern, self.content)

    def test_pyc_bracket_pattern_covers_pyc(self):
        """Verify the [cod] character-class pattern logically covers .pyc extension."""
        # The pattern *.py[cod] should match filenames ending in .pyc, .pyo, .pyd.
        import fnmatch
        for ext in ("example.pyc", "example.pyo", "example.pyd"):
            with self.subTest(filename=ext):
                self.assertTrue(fnmatch.fnmatch(ext, "*.py[cod]"), f"Pattern *.py[cod] should match {ext}")

    def test_pycache_pattern_does_not_match_plain_files(self):
        """__pycache__/ (with trailing slash) applies to directories, not plain files named __pycache__."""
        # The slash suffix means git only ignores directories; a plain file should not be caught.
        # Verify that the pattern in the file retains the trailing slash.
        lines = self.content.splitlines()
        pycache_entry = next((ln.strip() for ln in lines if "__pycache__" in ln), None)
        self.assertIsNotNone(pycache_entry, "__pycache__ entry must exist")
        self.assertTrue(
            pycache_entry.endswith("/"),
            "__pycache__ pattern must end with / to target directories only",
        )

    def test_non_python_source_files_not_ignored(self):
        """Common source files (.html, .css, .md, .js) must not be accidentally excluded."""
        for ext_pattern in ("*.html", "*.css", "*.md", "*.js"):
            with self.subTest(pattern=ext_pattern):
                self.assertNotIn(ext_pattern, self.content)

    def test_no_negation_of_pycache_pattern(self):
        """No negation rule (!) should re-include __pycache__ after ignoring it."""
        lines = [ln.strip() for ln in self.content.splitlines()]
        negation_lines = [ln for ln in lines if ln.startswith("!") and "__pycache__" in ln]
        self.assertEqual(len(negation_lines), 0, "No rule should re-include __pycache__")


if __name__ == "__main__":
    unittest.main()