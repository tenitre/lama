"""
Entry point for the Codebase Task Runner CLI.

This script provides a thin command‐line interface around the core
functionality of the codebase runner. It loads model configuration
information, parses command line arguments, and prepares the execution
context for future task operations. At this stage the runner only
handles configuration and does not yet implement scanning, token
counting, or LLM interaction. These will be added in subsequent
tasks.
"""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any, Dict

from app.config_loader import load_config, get_model_config


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
    # Future tasks: scanning, token calculation, chunking, and LLM communication.
    # For now we simply print out the selected model and exit.


if __name__ == "__main__":
    main()