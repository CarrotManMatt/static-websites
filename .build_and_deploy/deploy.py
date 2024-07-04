""""""

from collections.abc import Sequence

__all__: Sequence[str] = ("deploy_single_site", "deploy_all_sites")


import logging
import os
import subprocess
import traceback
from collections.abc import Set
from logging import Logger
from pathlib import Path
from subprocess import CalledProcessError, CompletedProcess
from typing import TYPE_CHECKING, Final, Literal

from utils.validators import Hostname, Username

if TYPE_CHECKING:
    from utils import CaughtException

logger: Final[Logger] = logging.getLogger("static-website-builder")


def _get_posix_remote_directory(raw_remote_directory: Path | None, *, site_name: str, remote_username: Username | None = None) -> str:  # noqa: E501
    if raw_remote_directory is not None:
        if remote_username:
            return (
                    Path("/home") / remote_username / raw_remote_directory / site_name
            ).as_posix()

        relative_posix: str = (raw_remote_directory / site_name).as_posix()

        if relative_posix.startswith("/"):
            return relative_posix

        return f"/{relative_posix}"

    if remote_username:
        return (Path("/home") / remote_username / site_name).as_posix()

    return (Path("/") / site_name).as_posix()


def deploy_single_site(site_path: Path, *, verbosity: Literal[0, 1, 2, 3] = 1, remote_hostname: Hostname, remote_username: Username | None = None, remote_directory: Path | None = None, dry_run: bool = False) -> None:  # noqa: E501
    """"""
    FORMATTED_SITE_NAME: Final[str] = (
        site_path.parent.name if site_path.name == "deploy" else site_path.name
    )

    logger.debug(f"({FORMATTED_SITE_NAME}) Begin deploying single site.")

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

    logger.debug(
        f"({FORMATTED_SITE_NAME}) Successfully retrieved resolved remote directory path.",
    )

    logger.debug(
        (
            f"({"dry_run=True | " if dry_run else ""}"
            f"{FORMATTED_SITE_NAME}) "
            f"Beginning {"mock " if dry_run else ""}upload of `deploy/` directory "
            "to remote server."
        ),
    )

    # noinspection SpellCheckingInspection
    rsync_args: list[str] = [
        "rsync",
        "--recursive",
        "--times",
        "--copy-links",
        "--copy-dirlinks",
        "--compress",
        "--checksum",
        "--delete",
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
                f"{f"{remote_username}@" if remote_username else ""}"
                f"{remote_hostname}:"
                f"{POSIX_REMOTE_DIRECTORY}"
            ),
        ),
    )

    no_rsync_command_error: FileNotFoundError
    try:
        process_output: CompletedProcess[str] = subprocess.run(  # noqa: S603,PLW1510
            rsync_args,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError as no_rsync_command_error:
        raise RuntimeError(
            f"{"rsync"!r} command not found. (Ensure it is installed on your system.)",
        ) from no_rsync_command_error

    if process_output.stdout:
        logger.debug(
            f"({FORMATTED_SITE_NAME}) rsync subprocess stdout:\n{process_output.stdout.strip()}\n",
        )

    if process_output.stderr:
        logger.debug(
            f"({FORMATTED_SITE_NAME}) rsync subprocess stderr:\n{process_output.stderr.strip()}\n",
        )

    if process_output.returncode != 0:
        raise RuntimeError(f"{"rsync"!r} command failed: exit code {process_output.returncode}")

    logger.debug(f"({FORMATTED_SITE_NAME}) Completed deploying single site successfully.")


def deploy_all_sites(site_paths: Set[Path], *, verbosity: Literal[0, 1, 2, 3] = 1, remote_hostname: Hostname | None = None, remote_username: Username | None = None, remote_directory: Path | None = None, dry_run: bool = False) -> Set[str]:  # noqa: E501
    """"""
    logger.debug("Begin deploying all sites.")

    deployed_sites: dict[str, CaughtException | None] = {}

    if not dry_run and not remote_hostname:
        raise ValueError(f"No {"remote_hostname"!r} was specified.")

    real_hostname: Hostname = (
        Hostname("192.168.0.1") if remote_hostname is None else remote_hostname
    )

    logger.debug(
        (
            f"{"(dry_run=True) " if dry_run else ""}"
            f"Opening {"mock " if dry_run else ""}connection to remote deployment server."
        ),
    )

    site_path: Path
    for site_path in site_paths:
        FORMATTED_SITE_NAME: str = (
            site_path.parent.name if site_path.name == "deploy" else site_path.name
        )

        caught_exception: CaughtException
        try:
            deploy_single_site(
                site_path,
                verbosity=verbosity,
                remote_hostname=real_hostname,
                remote_username=remote_username,
                remote_directory=remote_directory,
                dry_run=dry_run,
            )
        except (ValueError, RuntimeError, AttributeError, TypeError, OSError, CalledProcessError) as caught_exception:  # noqa: E501
            deployed_sites[FORMATTED_SITE_NAME] = caught_exception
            continue
        else:
            deployed_sites[FORMATTED_SITE_NAME] = None

    site_name: str
    deployment_outcome: CaughtException | None
    for site_name, deployment_outcome in deployed_sites.items():
        if deployment_outcome is None:
            continue

        traceback_messages: Sequence[str] = traceback.format_exception(deployment_outcome)

        logger.error(f"(Deployment Failed | {site_name}) {traceback_messages[-1].strip()}")
        logger.debug(f"({site_name}) {"".join(traceback_messages[:-1]).strip()}\n")

    deployed_site_names: Set[str] = {
        site_name
        for site_name, deployment_outcome
        in deployed_sites.items()
        if deployment_outcome is None
    }

    if deployed_site_names:
        logger.info("Deploying all sites completed successfully.")

    return deployed_site_names
