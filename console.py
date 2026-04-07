"""Console entry point for the static websites builder and deployment script."""

import logging
import os
import sys
from pathlib import Path
from typing import TYPE_CHECKING, overload

import build
import cleanup
import deploy
from utils import logging_setup, validators

if TYPE_CHECKING:
    from collections.abc import Sequence
    from collections.abc import Set as AbstractSet
    from logging import Logger
    from typing import Final, Literal

__all__: Sequence[str] = ("run",)


logger: Final[Logger] = logging.getLogger("static-websites-builder")
ENVIRONMENT_VARIABLE_PREFIX: Final[str] = "STATIC_WEBSITES_BUILDER_"


def _get_boolean_env_variable(
    environment_variable_name: str, *, default: bool = False
) -> bool:
    raw_boolean: str = os.environ.get(
        f"{ENVIRONMENT_VARIABLE_PREFIX}{environment_variable_name.upper()}",
        "true" if default else "false",
    )

    match raw_boolean.lower().strip():
        case "true":
            return True
        case "false":
            return False
        case _:
            INVALID_BOOLEAN_MESSAGE: Final[str] = f"Invalid boolean value: {raw_boolean!r}."
            raise ValueError(INVALID_BOOLEAN_MESSAGE)


def _get_verbosity_env_variable(*, is_dry_run: bool) -> Literal[0, 1, 2, 3]:
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


@overload
def _get_validated_string_environment_variable(
    environment_variable_name: str, validator: type[Path]
) -> Path | None: ...


@overload
def _get_validated_string_environment_variable[T: validators.SimpleValidator[str]](
    environment_variable_name: str, validator: type[T]
) -> T | None: ...


def _get_validated_string_environment_variable[T: validators.SimpleValidator[str]](
    environment_variable_name: str, validator: type[T | Path]
) -> T | Path | None:
    raw_value: str | None = os.environ.get(
        f"{ENVIRONMENT_VARIABLE_PREFIX}{environment_variable_name}"
    )
    if raw_value is None:
        return None

    raw_value = raw_value.strip("\n\r\t .-_")

    if not raw_value:
        return None

    return validator(raw_value)


def run() -> int:
    """Run the static websites builder and deployment script."""
    if sys.argv[1:]:
        UNEXPECTED_ARGUMENTS_MESSAGE: Final[str] = (
            f"Unexpected arguments: {', '.join(repr(arg) for arg in sys.argv[1:])}"
        )
        raise RuntimeError(UNEXPECTED_ARGUMENTS_MESSAGE)

    dry_run: bool = _get_boolean_env_variable("DRY_RUN")

    verbosity: Literal[0, 1, 2, 3] = _get_verbosity_env_variable(is_dry_run=dry_run)

    logging_setup.setup(verbosity=verbosity)

    remote_hostname: validators.Hostname | None = _get_validated_string_environment_variable(
        "REMOTE_IP", validators.Hostname
    )
    if remote_hostname is None and not dry_run:
        MISSING_REMOTE_IP_MESSAGE: Final[str] = (
            f'No "{ENVIRONMENT_VARIABLE_PREFIX}REMOTE_IP" was specified '
            f"when using {ENVIRONMENT_VARIABLE_PREFIX}DRY_RUN=False."
        )
        raise RuntimeError(MISSING_REMOTE_IP_MESSAGE)

    remote_username: validators.Username | None = _get_validated_string_environment_variable(
        "REMOTE_USERNAME", validators.Username
    )
    remote_directory: Path | None = _get_validated_string_environment_variable(
        "REMOTE_DIRECTORY", Path
    )

    try:
        built_site_paths: AbstractSet[Path] = build.build_all_sites()

        if not built_site_paths:
            logger.warning("All sites failed to build. (Or no sites exist.)")
            return 1

        deployed_site_names: AbstractSet[str] = deploy.deploy_all_sites(
            built_site_paths,
            verbosity=verbosity,
            remote_hostname=remote_hostname,  # type: ignore[arg-type]
            remote_username=remote_username,
            remote_directory=remote_directory,
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
