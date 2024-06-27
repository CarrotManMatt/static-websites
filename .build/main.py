""""""

from collections.abc import Sequence

__all__: Sequence[str] = ("build_site", "PROJECT_ROOT")

from pathlib import Path

PROJECT_ROOT: Path = Path(__file__).parent.parent


def build_site(*, root_directory: Path) -> None:
    """"""
    raise NotImplementedError
    # 1. Glob through all files
    # 2. Check if contains HTML5up Copyright
    # 3. Django render
    # 4. Minify
    # 5. Add copyright if needed
    # 6. write to file


if __name__ == "__main__":
    build_site(root_directory=PROJECT_ROOT / "website")
