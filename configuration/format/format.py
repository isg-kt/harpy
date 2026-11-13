"""
File: configuration/format/format.py
Brief: Code and documentation formatting hub utility.

This file is part of the Harpy project and is licensed under the
3-Clause BSD License;
For more information, see LICENSE.txt.
"""

import sys
import argparse
import pathlib
import os
import subprocess


def _parse_command_line_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments required for the code and documentation
    formatting tool.

    Returns:
        argparse.Namespace: Parsed command-line arguments containing
        target and root directory paths.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="Format Hub",
        usage=(
            "python3 configuration/format/format.py "
            "--target TARGET"
            "--root ROOT_DIRECTORY"
        ),
        description="Formats the Harpy's code and documentation.",
    )

    parser.add_argument(
        "--target",
        nargs="?",
        default="all",
        choices=["cpp", "py", "doc", "all"],
        help="Specify which component to format (default: all)",
    )
    parser.add_argument(
        "--root", required=True, help="Root directory of the project"
    )

    return parser.parse_args()


def _run_clang_format(project_root: pathlib.Path) -> None:
    """
    Formats C++ source files using clang-format, respecting git ignore
    rules and batching requests to prevent command-line length limits.

    Args:
        project_root (pathlib.Path): Absolute path to the root directory
        of the project.

    Returns:
        None
    """
    git_files: list[str] = []

    try:
        result: subprocess.CompletedProcess[str] = subprocess.run(
            [
                "git",
                "ls-files",
                "--cached",
                "--others",
                "--exclude-standard",
            ],
            cwd=project_root,
            capture_output=True,
            text=True,
            check=True,
        )
        git_files = result.stdout.splitlines()
    except subprocess.CalledProcessError as error:
        print(
            f"Error: failed to list git files: {error}", file=sys.stderr
        )
        sys.exit(1)

    filtered_source_files: list[pathlib.Path] = []
    valid_extensions: tuple[str, ...] = (".cpp", ".cppm", ".h")

    for file_path_string in git_files:
        if file_path_string.endswith(valid_extensions):
            full_path: pathlib.Path = project_root / file_path_string

            if full_path.exists():
                filtered_source_files.append(full_path)

    if not filtered_source_files:
        print("No C++ files found for formatting.")
        return

    print(
        f"Formatting {len(filtered_source_files)} C++ files with "
        "clang-format..."
    )

    base_command_list: list[str] = [
        "clang-format",
        "-i",
        f"--style=file:{project_root / '.clang-format'}",
    ]
    base_length: int = sum(
        len(argument) + 1 for argument in base_command_list
    )
    max_byte_limit: int = 4096
    current_batch_list: list[str] = []
    current_batch_length: int = base_length
    sub_result: subprocess.CompletedProcess[bytes]

    for file_path in filtered_source_files:
        file_path_string: str = str(file_path)
        path_length: int = len(file_path_string) + 1

        if current_batch_list and (
            current_batch_length + path_length > max_byte_limit
        ):
            sub_result = subprocess.run(
                base_command_list + current_batch_list,
                cwd=project_root,
            )

            if sub_result.returncode != 0:
                print("Error: clang-format failed.", file=sys.stderr)
                sys.exit(sub_result.returncode)

            current_batch_list = [file_path_string]
            current_batch_length = base_length + path_length
        else:
            current_batch_list.append(file_path_string)
            current_batch_length += path_length

    if current_batch_list:
        sub_result = subprocess.run(
            base_command_list + current_batch_list,
            cwd=project_root,
        )

        if sub_result.returncode != 0:
            print("Error: clang-format failed.", file=sys.stderr)
            sys.exit(sub_result.returncode)


def _run_black(project_root: pathlib.Path) -> None:
    """
    Formats Python source files using the Black formatter based on the
    project's pyproject.toml configuration.

    Args:
        project_root (pathlib.Path): Absolute path to the root directory
        of the project.

    Returns:
        None
    """
    print(f"Formatting Python files with black...")
    pyproject_toml_path: pathlib.Path = project_root / "pyproject.toml"

    command_list: list[str] = [
        "black",
        "--config",
        str(pyproject_toml_path),
        str(project_root),
    ]

    result: subprocess.CompletedProcess[bytes] = subprocess.run(
        command_list,
        cwd=project_root,
    )

    if result.returncode != 0:
        print("Error: black failed.", file=sys.stderr)
        sys.exit(result.returncode)


def _run_prettier(project_root: pathlib.Path) -> None:
    """
    Formats documentation and web asset files using Prettier, respecting
    git ignore rules.

    Args:
        project_root (pathlib.Path): Absolute path to the root directory
        of the project.

    Returns:
        None
    """
    print(f"Formatting Documentation files with prettier...")

    git_ignore_path: pathlib.Path = project_root / ".gitignore"

    command_list: list[str] = [
        "npm",
        "exec",
        "--",
        "prettier",
        "--write",
        "--ignore-unknown",
        "--ignore-path",
        str(git_ignore_path),
        str(project_root),
    ]

    result: subprocess.CompletedProcess[bytes] = subprocess.run(
        command_list,
        cwd=project_root,
    )

    if result.returncode != 0:
        print("Error: prettier failed.", file=sys.stderr)
        sys.exit(result.returncode)


def _run_rstfmt(project_root: pathlib.Path) -> None:
    """
    Formats reStructuredText files using rstfmt, respecting git ignore
    rules and batching requests to prevent command-line length limits.

    Args:
        project_root (pathlib.Path): Absolute path to the root directory
        of the project.

    Returns:
        None
    """
    git_files: list[str] = []

    try:
        result: subprocess.CompletedProcess[str] = subprocess.run(
            [
                "git",
                "ls-files",
                "--cached",
                "--others",
                "--exclude-standard",
            ],
            cwd=project_root,
            capture_output=True,
            text=True,
            check=True,
        )
        git_files = result.stdout.splitlines()
    except subprocess.CalledProcessError as error:
        print(
            f"Error: failed to list git files: {error}", file=sys.stderr
        )
        sys.exit(1)

    filtered_source_files: list[pathlib.Path] = []
    valid_extensions: tuple[str, ...] = (".rst",)

    for file_path_string in git_files:
        if file_path_string.endswith(valid_extensions):
            full_path: pathlib.Path = project_root / file_path_string

            if full_path.exists():
                filtered_source_files.append(full_path)

    if not filtered_source_files:
        print("No reStructuredText files found for formatting.")
        return

    print(
        f"Formatting {len(filtered_source_files)} reStructuredText files with "
        "rstfmt..."
    )

    base_command_list: list[str] = ["rstfmt"]
    base_length: int = sum(
        len(argument) + 1 for argument in base_command_list
    )
    max_byte_limit: int = 4096
    current_batch_list: list[str] = []
    current_batch_length: int = base_length
    sub_result: subprocess.CompletedProcess[bytes]

    for file_path in filtered_source_files:
        file_path_string: str = str(file_path)
        path_length: int = len(file_path_string) + 1

        if current_batch_list and (
            current_batch_length + path_length > max_byte_limit
        ):
            sub_result = subprocess.run(
                base_command_list + current_batch_list,
                cwd=project_root,
            )

            if sub_result.returncode != 0:
                print("Error: rstfmt failed.", file=sys.stderr)
                sys.exit(sub_result.returncode)

            current_batch_list = [file_path_string]
            current_batch_length = base_length + path_length
        else:
            current_batch_list.append(file_path_string)
            current_batch_length += path_length

    if current_batch_list:
        sub_result = subprocess.run(
            base_command_list + current_batch_list,
            cwd=project_root,
        )

        if sub_result.returncode != 0:
            print("Error: rstfmt failed.", file=sys.stderr)
            sys.exit(sub_result.returncode)


def format() -> None:
    """
    Coordinates and executes the formatting tasks based on the specified
    target component.

    Returns:
        None
    """
    arguments: argparse.Namespace = _parse_command_line_arguments()
    target: str = arguments.target
    project_root: pathlib.Path = pathlib.Path(
        os.path.abspath(arguments.root)
    )

    if target in ("cpp", "all"):
        _run_clang_format(project_root)
    if target in ("py", "all"):
        _run_black(project_root)
    if target in ("doc", "all"):
        _run_prettier(project_root)
        _run_rstfmt(project_root)


if __name__ == "__main__":
    try:
        format()
    except Exception as exception:
        print(f"Error during formatting: {exception}", file=sys.stderr)
        sys.exit(1)
