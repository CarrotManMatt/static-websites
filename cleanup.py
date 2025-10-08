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

__all__: Sequence[str] = ("cleanup_all_sites",)

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
