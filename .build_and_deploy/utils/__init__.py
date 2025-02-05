"""Common utils made available for use throughout this project."""

from pathlib import Path
from typing import TYPE_CHECKING

from git import InvalidGitRepositoryError, Repo

if TYPE_CHECKING:
    from collections.abc import Sequence
    from subprocess import CalledProcessError
    from typing import Final

    from git import PathLike

    type CaughtException = (
        ValueError | RuntimeError | AttributeError | TypeError | OSError | CalledProcessError
    )

__all__: "Sequence[str]" = ("PROJECT_ROOT", "CaughtException")


def _get_project_root() -> Path:
    try:
        raw_project_root: PathLike | str | None = Repo(
            Path.cwd(),
            search_parent_directories=True,
        ).working_tree_dir
    except InvalidGitRepositoryError:
        raw_project_root = None

    if raw_project_root is None:
        return _get_readme_root()

    return Path(raw_project_root)


def _get_readme_root() -> Path:
    project_root: Path = Path.cwd().resolve()

    for _ in range(8):
        project_root = project_root.parent

        if any(path.stem == "README" for path in project_root.iterdir()):
            return project_root

    # noinspection PyFinal
    NO_ROOT_DIRECTORY_MESSAGE: Final[str] = "Could not locate project root directory."
    raise FileNotFoundError(NO_ROOT_DIRECTORY_MESSAGE)


PROJECT_ROOT: "Final[Path]" = _get_project_root()
