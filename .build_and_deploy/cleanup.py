"""Clean-up temporary build folders."""

from collections.abc import Sequence

__all__: Sequence[str] = ("cleanup_single_site", "cleanup_all_sites")


import logging
import shutil
from logging import Logger
from pathlib import Path
from typing import Final

from utils import PROJECT_ROOT

logger: Final[Logger] = logging.getLogger("static-website-builder")


def cleanup_single_site(*, site_root_directory: Path) -> None:
    """"""
    logger.debug(
        (
            f"({site_root_directory.relative_to(PROJECT_ROOT).as_posix()}) "
            "Begin clean-up of single site."
        ),
    )

    if not site_root_directory.is_dir():
        PATH_IS_NOT_DIRECTORY_MESSAGE: Final[str] = (
            f"Path to site's root directory is not a directory: {site_root_directory}"
        )
        raise ValueError(PATH_IS_NOT_DIRECTORY_MESSAGE)

    deploy_dir: Path = site_root_directory / "deploy"
    if deploy_dir.exists():
        shutil.rmtree(deploy_dir)

    logger.debug(
        (
            f"({site_root_directory.relative_to(PROJECT_ROOT).as_posix()}) "
            "Completed clean-up of single site successfully."
        ),
    )


def cleanup_all_sites() -> None:
    """"""
    logger.debug("Running clean-up on all sites.")

    site_subdirectory: Path
    for site_subdirectory in PROJECT_ROOT.iterdir():
        if not site_subdirectory.is_dir() or site_subdirectory.stem.startswith("."):
            continue

        cleanup_single_site(site_root_directory=site_subdirectory)

    logger.debug("Successfully completed clean-up on all sites.")
