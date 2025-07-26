"""Tests for the output writer utilities."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.output_writer import OutputWriter


def test_write_docs(tmp_path):
    writer = OutputWriter(tmp_path)
    path = writer.write_docs("sample", "hello")
    assert path.exists()
    text = path.read_text(encoding="utf-8")
    assert "hello" in text
    assert path.suffix == ".md"
    assert path.parent.name == "docs"


def test_write_tests(tmp_path):
    writer = OutputWriter(tmp_path)
    path = writer.write_tests("sample", "// test")
    assert path.exists()
    assert path.suffix == ".cs"
    assert path.parent.name == "tests"


def test_write_todos(tmp_path):
    writer = OutputWriter(tmp_path)
    path = writer.write_todos("sample", "todo")
    assert path.exists()
    assert path.suffix == ".txt"
    assert path.parent.name == "todos"
