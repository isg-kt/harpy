"""
File: configuration/documentation/doxyfile.py
Brief: Doxyfile preprocessor and configuration generator.

This file is part of the Harpy project and is licensed under the
3-Clause BSD License;
For more information, see LICENSE.txt.
"""

import sys
import argparse
import os
import pathlib
import multiprocessing


def _parse_command_line_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments required for Doxyfile preprocessing.

    Returns:
        argparse.Namespace: Parsed command-line arguments containing root
        and build paths.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="Doxyfile Preprocessor",
        usage=(
            "python3 configuration/documentation/doxyfile.py "
            "--root ROOT_DIRECTORY_PATH "
            "--build BUILD_DIRECTORY_PATH"
        ),
        description="Preprocess Doxyfile template.",
    )

    parser.add_argument(
        "--root", required=True, help="Root directory of the project"
    )
    parser.add_argument(
        "--build",
        required=True,
        help="Build directory for the output Doxyfile",
    )

    return parser.parse_args()


def _parse_gitignore(root_path: str) -> list[str]:
    """
    Parses the project's .gitignore file to extract exclusion paths for
    Doxygen.

    Args:
        root_path (str): Absolute path to the root directory of the
        project.

    Returns:
        list[str]: List of absolute paths or patterns extracted from
        .gitignore.
    """
    gitignore_path: pathlib.Path = pathlib.Path(root_path) / ".gitignore"
    excluded_items: list[str] = []

    if not gitignore_path.exists():
        return excluded_items

    with open(gitignore_path, "r", encoding="UTF-8") as gitignore_file:
        for line in gitignore_file:
            stripped_line: str = line.strip()

            if not stripped_line or stripped_line.startswith("#"):
                continue

            clean_pattern: str = stripped_line.lstrip("/")
            full_path: pathlib.Path = (
                pathlib.Path(root_path) / clean_pattern
            )

            excluded_items.append(str(full_path))

    return excluded_items


def preprocess_doxyfile() -> None:
    """
    Preprocesses the Doxyfile template by replacing variables and writing
    the output.

    Returns:
        None
    """
    paths: argparse.Namespace = _parse_command_line_arguments()
    script_directory: pathlib.Path = (
        pathlib.Path(__file__).resolve().parent
    )
    root_path: str = os.path.abspath(paths.root)
    build_path: str = os.path.abspath(paths.build)
    template_path: pathlib.Path = script_directory / "Doxyfile.in"
    output_path: pathlib.Path = pathlib.Path(build_path) / "Doxyfile"

    if not template_path.exists():
        print(
            f"Error: Template file not found at {template_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    cpu_count: int = multiprocessing.cpu_count()

    ignored_paths: list[str] = _parse_gitignore(root_path)
    ignored_paths.append(str(pathlib.Path(build_path)))
    exclude_string: str = " \\\n                  ".join(ignored_paths)

    with open(template_path, "r", encoding="UTF-8") as template_file:
        content = template_file.read()

    content = content.replace("$HARPY_ROOT_DIRECTORY$", root_path)
    content = content.replace("$NPROC$", str(cpu_count))
    content = content.replace("EXCLUDE =", f"EXCLUDE = {exclude_string} ")

    os.makedirs(build_path, exist_ok=True)

    with open(output_path, "w", encoding="UTF-8") as build_file:
        build_file.write(content)


if __name__ == "__main__":
    try:
        preprocess_doxyfile()
    except Exception as exception:
        print(f"Error processing Doxyfile: {exception}", file=sys.stderr)
        sys.exit(1)
