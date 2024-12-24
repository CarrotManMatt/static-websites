"""Console entry point for the static websites builder and deployment script."""

import logging
import os
import sys
from typing import TYPE_CHECKING

import build
import cleanup
import deploy
from utils import logging_setup

if TYPE_CHECKING:
    from collections.abc import Sequence
    from collections.abc import Set as AbstractSet
    from logging import Logger
    from pathlib import Path
    from typing import Final, Literal

__all__: "Sequence[str]" = ("run",)

logger: "Final[Logger]" = logging.getLogger("static-websites-builder")
ENVIRONMENT_VARIABLE_PREFIX: "Final[str]" = "STATIC_WEBSITES_BUILDER_"


def _get_true_dry_run() -> bool:
    raw_dry_run: str = os.environ.get(f"{ENVIRONMENT_VARIABLE_PREFIX}DRY_RUN", "false").lower()

    if raw_dry_run == "true":
        return True

    if raw_dry_run == "false":
        return False

    raise ValueError


def _get_true_verbosity(*, is_dry_run: bool) -> "Literal[0, 1, 2, 3]":
    raw_verbosity: int = int(os.environ.get(f"{ENVIRONMENT_VARIABLE_PREFIX}VERBOSITY", "0"))
    if raw_verbosity < 0 and is_dry_run:
        MUTUALLY_EXCLUSIVE_MESSAGE: Final[str] = (
            f"The environment variable {ENVIRONMENT_VARIABLE_PREFIX}VERBOSITY "
            f"cannot be less than 0 when {ENVIRONMENT_VARIABLE_PREFIX}DRY_RUN is enabled."
        )
        raise ValueError(MUTUALLY_EXCLUSIVE_MESSAGE)

    if raw_verbosity > 2:
        return 3

    if raw_verbosity == 2:
        return 3

    if raw_verbosity == 1:
        return 2

    if raw_verbosity == 0:
        if is_dry_run:
            return 2

        return 1

    if raw_verbosity == -1:
        return 0

    if raw_verbosity < -1:
        return 0

    raise ValueError


def run() -> int:
    """Run the static websites builder and deployment script."""
    dry_run: bool = _get_true_dry_run()

    verbosity: Literal[0, 1, 2, 3] = _get_true_verbosity(is_dry_run=dry_run)

    # noinspection PyUnboundLocalVariable
    logging_setup.setup(verbosity=verbosity)

    try:
        built_site_paths: AbstractSet[Path] = build.build_all_sites()

        if not built_site_paths:
            logger.warning("All sites failed to build. (Or no sites exist.)")
            return 1

        deployed_site_names: AbstractSet[str] = deploy.deploy_all_sites(
            built_site_paths,
            verbosity=verbosity,
            remote_hostname=os.environ.get(f"{ENVIRONMENT_VARIABLE_PREFIX}REMOTE_IP", None),
            remote_username=os.environ.get(
                f"{ENVIRONMENT_VARIABLE_PREFIX}REMOTE_USERNAME", None
            ),
            remote_directory=os.environ.get(
                f"{ENVIRONMENT_VARIABLE_PREFIX}REMOTE_DIRECTORY", None
            ),
            dry_run=dry_run,
        )

        if not deployed_site_names:
            logger.warning("All sites failed to deploy.")
            return 1

        sys.stdout.write(",".join(deployed_site_names))
        return 0

    finally:
        if dry_run:
            cleanup.cleanup_all_sites(dry_run=dry_run)


if __name__ == "__main__":
    raise SystemExit(run())
