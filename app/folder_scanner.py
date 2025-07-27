from __future__ import annotations

"""Utilities for scanning directories and filtering files."""

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence

__all__ = ["FileInfo", "scan_directory"]


@dataclass
class FileInfo:
    """Metadata about a discovered file."""

    path: Path
    relative_path: Path
    extension: str
    size: int


DEFAULT_EXTENSIONS = {
    ".py",
    ".cs",
    ".md",
    ".ipynb",
    #".json",
    ".yaml",
    ".yml",
    ".toml",
    ".cfg",
}

EXCLUDE_DIRS = {
    ".git",
    "__pycache__",
    ".env",
    ".venv",
    "node_modules",
}


def _is_excluded(path: Path, exclude_dirs: Iterable[str]) -> bool:
    """Return True if the path contains any of the excluded directories."""
    for part in path.parts:
        if part in exclude_dirs:
            return True
    return False


def scan_directory(
    base_path: Path,
    allowed_extensions: Sequence[str] | None = None,
    exclude_dirs: Sequence[str] | None = None,
) -> List[FileInfo]:
    """Recursively scan ``base_path`` and return matching ``FileInfo`` objects."""

    if not base_path.is_dir():
        raise NotADirectoryError(f"{base_path} is not a directory")

    allowed = {ext.lower() for ext in (allowed_extensions or DEFAULT_EXTENSIONS)}
    excluded = set(exclude_dirs or EXCLUDE_DIRS)

    results: List[FileInfo] = []

    for path in base_path.rglob("*"):
        if path.is_file() and path.suffix.lower() in allowed:
            if _is_excluded(path, excluded):
                continue
            info = FileInfo(
                path=path,
                relative_path=path.relative_to(base_path),
                extension=path.suffix.lower(),
                size=path.stat().st_size,
            )
            results.append(info)
    return results
