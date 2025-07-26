"""Utilities for writing task outputs to files."""

from __future__ import annotations

import logging
from pathlib import Path
from datetime import datetime

__all__ = ["OutputWriter"]

logger = logging.getLogger(__name__)


class OutputWriter:
    """Write task results to organized output directories."""

    def __init__(self, base_dir: Path) -> None:
        self.base_dir = base_dir
        self.docs_dir = base_dir / "docs"
        self.tests_dir = base_dir / "tests"
        self.todos_dir = base_dir / "todos"

    def _write(self, directory: Path, name: str, extension: str, content: str) -> Path:
        directory.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.utcnow().isoformat()
        header = f"Generated on {timestamp}"
        if extension == ".md":
            header = f"<!-- {header} -->\n"
        elif extension == ".cs":
            header = f"// {header}\n"
        else:
            header = f"# {header}\n"
        path = directory / f"{name}{extension}"
        path.write_text(f"{header}{content}\n", encoding="utf-8")
        if path.exists():
            logger.info("Wrote %s", path)
        else:
            logger.error("Failed to write %s", path)
        return path

    def write_docs(self, name: str, content: str) -> Path:
        """Write documentation markdown."""
        return self._write(self.docs_dir, name, ".md", content)

    def write_tests(self, name: str, content: str) -> Path:
        """Write C# unit tests."""
        return self._write(self.tests_dir, name, ".cs", content)

    def write_todos(self, name: str, content: str) -> Path:
        """Write TODO report."""
        return self._write(self.todos_dir, name, ".txt", content)
