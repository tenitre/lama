"""
Entry point for the Codebase Task Runner CLI.

This script provides a command-line interface for running tasks across a
codebase using a local LLM. It loads model configuration, scans the
target directory, chunks files to respect token limits, sends them to the
LLM via Ollama, and writes the combined results to the ``outputs``
directory.
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import Any, Dict

from app.config_loader import load_config, get_model_config
from app.folder_scanner import scan_directory
from app.ollama_client import OllamaClient
from app.task_dispatcher import TaskDispatcher
from app.output_writer import OutputWriter


def build_parser() -> argparse.ArgumentParser:
    """Configure and return the argument parser.

    Returns
    -------
    argparse.ArgumentParser
        The configured argument parser.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Codebase Task Runner: process codebases using a local LLM via Ollama"
        )
    )
    parser.add_argument(
        "--path",
        type=str,
        default=".",
        help="Path to the project directory to process.",
    )
    parser.add_argument(
        "--ask",
        type=str,
        required=False,
        help=(
            "Task description to execute on the codebase (e.g., 'Generate documentation')."
        ),
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="Optional model name override defined in config/models.json.",
    )
    return parser


def main() -> None:
    """Main entry point for CLI execution."""
    parser = build_parser()
    args = parser.parse_args()

    # Initialise logging. The logging configuration here is minimal;
    # downstream modules should configure their own loggers as needed.
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    # Resolve the configuration file path relative to this file. We use
    # the config directory to store LLM model definitions.
    config_path = Path(__file__).parent / "config" / "models.json"
    if not config_path.exists():
        logging.error("Model configuration file not found at %s", config_path)
        raise SystemExit(1)

    config = load_config(config_path)
    model_name = args.model or config.get("default_model")
    try:
        model = get_model_config(config, model_name)
    except KeyError as exc:
        logging.error("Model '%s' not found in configuration.", model_name)
        raise SystemExit(1) from exc

    logging.info("Using model '%s' with endpoint %s", model_name, model.get("url"))

    base_path = Path(args.path).resolve()
    ask = args.ask or "Generate documentation"

    logging.info("Scanning %s", base_path)
    files = scan_directory(base_path)
    logging.info("Found %d files", len(files))

    client = OllamaClient(model.get("url"))
    dispatcher = TaskDispatcher(client, model_name, model.get("token_limit", 32000))
    writer = OutputWriter(Path("outputs"))

    for file_info in files:
        logging.info("Processing %s", file_info.relative_path)
        result = dispatcher.run_task_on_file(file_info.path, ask)
        stem = file_info.relative_path.stem
        lower = ask.lower()
        if "test" in lower:
            writer.write_tests(stem, result)
        elif "todo" in lower:
            writer.write_todos(stem, result)
        else:
            writer.write_docs(stem, result)

    logging.info("Task completed")


if __name__ == "__main__":
    main()
