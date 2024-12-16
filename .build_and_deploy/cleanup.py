"""Clean up temporary build/deploy directories."""

import logging
import shutil
from logging import LoggerAdapter
from typing import TYPE_CHECKING, Final

from utils import PROJECT_ROOT

if TYPE_CHECKING:
    from collections.abc import Sequence
    from logging import Logger
    from pathlib import Path
    from typing import Final

__all__: "Sequence[str]" = ("cleanup_all_sites", "cleanup_single_site")

logger: "Final[Logger]" = logging.getLogger("static-website-builder")
extra_context_logger: "Final[Logger]" = logging.getLogger(
    "static-website-builder-extra-context"
)


def cleanup_single_site(*, site_root_directory: "Path", dry_run: bool = True) -> None:
    """Delete any temporary build/deploy directories created for a single given site."""
    FORMATTED_SITE_NAME: Final[str] = (
        site_root_directory.parent.name
        if site_root_directory.name == "deploy"
        else site_root_directory.name
    )
    dry_run_site_name_logger: Final[LoggerAdapter[Logger]] = LoggerAdapter(
        extra_context_logger,
        {
            "extra_context": f"{FORMATTED_SITE_NAME}{" | dry_run=True" if dry_run else ""}",
        },
    )

    dry_run_site_name_logger.debug("Begin clean-up of single site.")

    if not site_root_directory.is_dir():
        PATH_IS_NOT_DIRECTORY_MESSAGE: Final[str] = (
            f"Path to site's root directory is not a directory: {site_root_directory}"
        )
        raise ValueError(PATH_IS_NOT_DIRECTORY_MESSAGE)

    deploy_dir: Path = site_root_directory / "deploy"
    if deploy_dir.exists():
        shutil.rmtree(deploy_dir)

    dry_run_site_name_logger.debug("Completed clean-up of single site successfully.")


def cleanup_all_sites(*, dry_run: bool = True) -> None:
    """Delete any temporary build/deploy directories created for all sites."""
    dry_run_logger: Final[LoggerAdapter[Logger] | Logger] = (
        LoggerAdapter(
            extra_context_logger,
            {"extra_context": "dry_run=True"},
        )
        if dry_run
        else logger
    )

    dry_run_logger.debug("Running clean-up on all sites.")

    site_subdirectory: Path
    for site_subdirectory in PROJECT_ROOT.iterdir():
        if not site_subdirectory.is_dir() or site_subdirectory.stem.startswith("."):
            continue

        cleanup_single_site(site_root_directory=site_subdirectory, dry_run=dry_run)

    dry_run_logger.debug(
        "Successfully completed clean-up on all sites.",
    )
