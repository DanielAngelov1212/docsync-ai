from pathlib import Path

DEFAULT_EXCLUDED_DIRS = frozenset({
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    "build",
    "dist",
})


def discover_python_files(
    root: str | Path,
    *,
    excluded_dirs: frozenset[str] = DEFAULT_EXCLUDED_DIRS,
) -> list[Path]:
    root = Path(root).resolve(strict=True)

    if not root.is_dir():
        raise NotADirectoryError(f"Not a directory: {root}")

    python_files = []
    directories = [root]

    while directories:
        directory = directories.pop()

        for path in directory.iterdir():
            if path.is_symlink():
                continue

            if path.is_dir():
                if path.name not in excluded_dirs:
                    directories.append(path)

            elif path.is_file() and path.suffix == ".py":
                python_files.append(path)

    return sorted(python_files)