"""Clean up temporary build/deploy directories."""

__all__: Sequence[str] = ("cleanup_all_sites",)

import logging
lazy import shutil
lazy from collections.abc import Sequence
lazy from logging import Logger, LoggerAdapter
lazy from pathlib import Path
lazy from typing import Final

from utils import PROJECT_ROOT

logger: Final[Logger] = logging.getLogger("static-websites-builder")
extra_context_logger: Final[Logger] = logging.getLogger(
    "static-websites-builder-extra-context"
)


def cleanup_all_sites(*, dry_run: bool = True) -> None:
    """Delete any temporary build/deploy directories created for all sites."""
    dry_run_logger: Final[LoggerAdapter[Logger] | Logger] = (
        LoggerAdapter(extra_context_logger, {"extra_context": "dry_run=True"})
        if dry_run
        else logger
    )

    dry_run_logger.debug("Running clean-up on all sites.")

    deploy_dir: Path = PROJECT_ROOT / "deploy"
    if deploy_dir.exists():
        shutil.rmtree(deploy_dir)

    dry_run_logger.debug("Successfully completed clean-up on all sites.")
