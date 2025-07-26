"""Tests for the folder scanning utilities."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.folder_scanner import scan_directory, FileInfo


def test_scan_directory_filters_extensions(tmp_path):
    (tmp_path / "a").mkdir()
    (tmp_path / "a" / "file.py").write_text("print('hi')", encoding="utf-8")
    (tmp_path / "a" / "notes.txt").write_text("ignore", encoding="utf-8")
    results = scan_directory(tmp_path)
    assert len(results) == 1
    info = results[0]
    assert info.relative_path == Path("a/file.py")
    assert info.extension == ".py"


def test_scan_directory_excludes_dirs(tmp_path):
    (tmp_path / "node_modules").mkdir()
    (tmp_path / "node_modules" / "bad.py").write_text("print('bad')", encoding="utf-8")
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "good.py").write_text("print('ok')", encoding="utf-8")
    results = scan_directory(tmp_path)
    paths = {info.relative_path for info in results}
    assert Path("src/good.py") in paths
    assert Path("node_modules/bad.py") not in paths
