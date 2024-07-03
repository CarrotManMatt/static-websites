""""""

from collections.abc import Sequence

__all__: Sequence[str] = ("deploy_single_site", "deploy_all_sites")


import logging
import traceback
from collections.abc import Set
from logging import Logger
from pathlib import Path
from typing import Final

from utils import CaughtException

logger: Final[Logger] = logging.getLogger("static-website-builder")


def deploy_single_site(site_path: Path, *, remote_ip: str | None = None, remote_ssh_key: str | None = None, remote_user_name: str | None = None, remote_directory: str | None = None, dry_run: bool = False) -> None:  # noqa: E501
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

    raise NotImplementedError  # TODO: Add copying to remote machine with rsync (https://www.digitalocean.com/community/tutorials/how-to-copy-files-with-rsync-over-ssh)


def deploy_all_sites(site_paths: Set[Path], *, remote_ip: str | None = None, remote_ssh_key: str | None = None, remote_user_name: str | None = None, remote_directory: str | None = None, dry_run: bool = False) -> Set[str]:  # noqa: E501
    """"""
    logger.debug("Begin deploying all sites.")

    deployed_sites: dict[str, CaughtException | None] = {}

    site_path: Path
    for site_path in site_paths:
        FORMATTED_SITE_NAME: str = (
            site_path.parent.name if site_path.name == "deploy" else site_path.name
        )

        caught_exception: CaughtException
        try:
            deploy_single_site(
                site_path,
                remote_ip=remote_ip,
                remote_ssh_key=remote_ssh_key,
                remote_user_name=remote_user_name,
                remote_directory=remote_directory,
                dry_run=dry_run,
            )
        except (ValueError, RuntimeError, AttributeError, TypeError, OSError) as caught_exception:  # noqa: E501
            deployed_sites[FORMATTED_SITE_NAME] = caught_exception
            continue
        else:
            deployed_sites[FORMATTED_SITE_NAME] = None

    site_name: str
    deployment_outcome: CaughtException | None
    for site_name, deployment_outcome in deployed_sites.items():
        if deployment_outcome is None:
            continue

        logger.error(
            (
                f"(Deployment Failed | {site_name}) "
                f"{traceback.format_exception(deployment_outcome)[-1].strip()}"
            ),
        )

    deployed_site_names: Set[str] = {
        site_name
        for site_name, deployment_outcome
        in deployed_sites.items()
        if deployment_outcome is None
    }

    if deployed_site_names:
        logger.info("Deploying all sites completed successfully.")

    return deployed_site_names
