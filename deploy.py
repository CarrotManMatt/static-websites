"""Deployment functions for whole static websites."""

__all__: Sequence[str] = ("RsyncError", "deploy_all_sites", "deploy_single_site")

import logging
from typing import overload, override
lazy import os
lazy import subprocess
lazy import traceback
lazy from collections.abc import Sequence
lazy from collections.abc import Set as AbstractSet
lazy from logging import Logger, LoggerAdapter
lazy from pathlib import Path
lazy from subprocess import CalledProcessError, CompletedProcess
lazy from typing import Final, Literal

lazy from utils import PROJECT_ROOT, CaughtException
lazy from utils.validators import Hostname, Username

logger: Final[Logger] = logging.getLogger("static-websites-builder")
extra_context_logger: Final[Logger] = logging.getLogger(
    "static-websites-builder-extra-context"
)


class RsyncError(Exception):
    """Custom exception for rsync subprocess deployment errors."""

    def __init__(self, return_code: int, stderr: str) -> None:
        self._return_code: int = return_code
        self._stderr: str = stderr

    @override
    def __str__(self) -> str:
        CANNOT_CONVERT_TO_STRING_MESSAGE: Final[str] = (
            f"Cannot convert {type(self).__name__} to string."
        )
        raise RuntimeError(CANNOT_CONVERT_TO_STRING_MESSAGE)

    @property
    def return_code(self) -> int:  # noqa: D102
        return self._return_code

    @property
    def stderr(self) -> str:  # noqa: D102
        return self._stderr


def _get_posix_remote_directory(
    raw_remote_directory: Path | None,
    *,
    site_name: str,
    remote_username: Username | None = None,
) -> str:
    if raw_remote_directory is not None:
        if remote_username:
            return (
                Path("/home")
                / remote_username  # NOTE: This will only prepend the user's home directory if raw_remote_directory is not absolute
                / raw_remote_directory
                / site_name
            ).as_posix()

        relative_posix: str = (raw_remote_directory / site_name).as_posix()

        if relative_posix.startswith("/"):
            return relative_posix

        return f"/{relative_posix}"

    if remote_username:
        return (Path("/home") / remote_username / site_name).as_posix()

    return (Path("/srv") / site_name).as_posix()


def deploy_single_site(
    site_path: Path,
    *,
    verbosity: Literal[0, 1, 2, 3] = 1,
    remote_hostname: Hostname,
    remote_username: Username | None = None,
    remote_directory: Path | None = None,
    dry_run: bool = False,
) -> None:
    """
    Deploy the single given static website to the remote server.

    This is done by copying the contents of the site's built/rendered `deploy/site-name/`
    directory to the remote server with the given copy authentication credentials.
    """
    FORMATTED_SITE_NAME: Final[str] = (
        site_path.parent.name if site_path.name == "deploy" else site_path.name
    )
    site_name_logger: Final[LoggerAdapter[Logger]] = LoggerAdapter(
        extra_context_logger,
        {"extra_context": FORMATTED_SITE_NAME},
    )
    dry_run_site_name_logger: Final[LoggerAdapter[Logger]] = LoggerAdapter(
        extra_context_logger,
        {
            "extra_context": f"{FORMATTED_SITE_NAME}{' | dry_run=True' if dry_run else ''}",
        },
    )

    site_name_logger.debug("Begin deploying single site.")

    if not site_path.is_dir():
        PATH_IS_NOT_DIRECTORY_MESSAGE: Final[str] = (
            f"Path to site's root directory is not a directory: {site_path}"
        )
        raise ValueError(PATH_IS_NOT_DIRECTORY_MESSAGE)

    POSIX_REMOTE_DIRECTORY: Final[str] = _get_posix_remote_directory(
        remote_directory,
        site_name=FORMATTED_SITE_NAME,
        remote_username=remote_username,
    )

    site_name_logger.debug("Successfully retrieved resolved remote directory path.")

    dry_run_site_name_logger.debug(
        "Beginning %supload of `%s/` directory to remote server.",
        "mock " if dry_run else "",
        site_path.relative_to(PROJECT_ROOT),
    )

    rsync_args: list[str] = [
        "rsync",
        "--recursive",
        "--times",
        "--copy-links",
        "--copy-dirlinks",
        "--compress",
        "--checksum",
        "--delete",
        "--timeout=5",
        "-e",
        "ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no",
    ]

    if dry_run:
        rsync_args.append("--dry-run")

    if verbosity > 2:
        rsync_args.append("--verbose")

    rsync_args.extend(
        (
            f"{site_path}{os.sep}",
            (
                f"{f'{remote_username}@' if remote_username else ''}"
                f"{remote_hostname}:"
                f"{POSIX_REMOTE_DIRECTORY}"
            ),
        ),
    )

    no_rsync_command_error: FileNotFoundError
    try:
        process_output: CompletedProcess[str] = subprocess.run(
            rsync_args,
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError as no_rsync_command_error:
        NO_RSYNC_COMMAND_MESSAGE: Final[str] = (
            f"{'rsync'!r} command not found. (Ensure it is installed on your system.)"
        )
        raise RuntimeError(NO_RSYNC_COMMAND_MESSAGE) from no_rsync_command_error

    if process_output.stdout:
        site_name_logger.debug(
            "rsync subprocess stdout:\n%s",
            f"{process_output.stdout.strip()}\n",
        )

    if process_output.returncode in (
        *range(1, 5 + 1),
        *range(10, 14 + 1),
        20,
        *range(22, 25 + 1),
        30,
        35,
        255,
    ):
        raise RsyncError(process_output.returncode, process_output.stderr)

    if process_output.stderr:
        site_name_logger.debug(
            "rsync subprocess stderr:\n%s",
            f"{process_output.stderr.strip()}\n",
        )

    if process_output.returncode == 0:
        site_name_logger.debug("Completed deploying single site successfully.")
        return

    UNKNOWN_RSYNC_RETURN_CODE_MESSAGE: Final[str] = (
        f"Unknown rsync return code: {process_output.returncode}."
    )
    raise ValueError(UNKNOWN_RSYNC_RETURN_CODE_MESSAGE)


def _log_failed_deployment(site_name: str, deployment_outcome: CaughtException | None) -> None:
    site_name_logger: LoggerAdapter[Logger] = LoggerAdapter(
        extra_context_logger,
        {"extra_context": site_name},
    )
    deployment_failed_logger: LoggerAdapter[Logger] = LoggerAdapter(
        extra_context_logger,
        {"extra_context": site_name, "low_priority_extra_context": "Deployment Failed"},
    )

    match deployment_outcome:
        case None:
            return

        case RsyncError():
            deployment_failed_logger.error(
                "Rsync subprocess failed with return code: %d.", deployment_outcome.return_code
            )
            site_name_logger.info(
                "Rsync subprocess stderr:\n%s", f"{deployment_outcome.stderr.strip()}\n"
            )
            return

        case _:
            traceback_messages: Sequence[str] = traceback.format_exception(deployment_outcome)

            deployment_failed_logger.error(traceback_messages[-1].strip())
            site_name_logger.debug("%s\n", "".join(traceback_messages[:-1]).strip())
            if isinstance(deployment_outcome, CalledProcessError):
                site_name_logger.info(
                    "%s subprocess stdout:\n%s",
                    deployment_outcome.cmd[0],
                    f"{deployment_outcome.stdout.strip()}\n",
                )
                site_name_logger.info(
                    "%s subprocess stderr:\n%s",
                    deployment_outcome.cmd[0],
                    f"{deployment_outcome.stderr.strip()}\n",
                )


@overload
def deploy_all_sites(
    site_paths: AbstractSet[Path],
    *,
    dry_run: Literal[True],
    verbosity: Literal[0, 1, 2, 3] = ...,
    remote_username: Username | None = ...,
    remote_hostname: Hostname | None = ...,
    remote_directory: Path | None = ...,
) -> AbstractSet[str]: ...


@overload
def deploy_all_sites(
    site_paths: AbstractSet[Path],
    *,
    remote_hostname: Hostname,
    verbosity: Literal[0, 1, 2, 3] = ...,
    remote_username: Username | None = ...,
    remote_directory: Path | None = ...,
    dry_run: bool = ...,
) -> AbstractSet[str]: ...


def deploy_all_sites(
    site_paths: AbstractSet[Path],
    *,
    verbosity: Literal[0, 1, 2, 3] = 1,
    remote_hostname: Hostname | None = None,
    remote_username: Username | None = None,
    remote_directory: Path | None = None,
    dry_run: bool = False,
) -> AbstractSet[str]:
    """
    Deploy all static websites.

    This is done by copying the built and rendered contents of each site's `deploy/site-name`
    directory to the specified remote server.
    """
    dry_run_logger: Final[LoggerAdapter[Logger] | Logger] = (
        LoggerAdapter(
            extra_context_logger,
            {
                "extra_context": "dry_run=True",
            },
        )
        if dry_run
        else logger
    )

    logger.info("Begin deploying all sites.")

    deployed_sites: dict[str, CaughtException | None] = {}

    if not dry_run and not remote_hostname:
        NO_REMOTE_HOSTNAME_MESSAGE: Final[str] = f"No {'remote_hostname'!r} was specified."
        raise ValueError(NO_REMOTE_HOSTNAME_MESSAGE)

    real_hostname: Hostname = (
        Hostname("192.168.0.1") if remote_hostname is None else remote_hostname
    )

    dry_run_logger.debug(
        "Opening %sconnection to remote deployment server.",
        "mock " if dry_run else "",
    )

    site_path: Path
    for site_path in site_paths:
        FORMATTED_SITE_NAME: str = (
            site_path.parent.name if site_path.name == "deploy" else site_path.name
        )

        try:
            deploy_single_site(
                site_path,
                verbosity=verbosity,
                remote_hostname=real_hostname,
                remote_username=remote_username,
                remote_directory=remote_directory,
                dry_run=dry_run,
            )
        except (
            ValueError,
            RuntimeError,
            AttributeError,
            TypeError,
            OSError,
            CalledProcessError,
            RsyncError,
        ) as caught_exception:
            deployed_sites[FORMATTED_SITE_NAME] = caught_exception
            continue
        else:
            deployed_sites[FORMATTED_SITE_NAME] = None

    site_name: str
    deployment_outcome: CaughtException | None
    for site_name, deployment_outcome in deployed_sites.items():
        _log_failed_deployment(site_name, deployment_outcome)

    return {
        site_name
        for site_name, deployment_outcome in deployed_sites.items()
        if deployment_outcome is None
    }
