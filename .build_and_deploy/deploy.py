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
    raise NotImplementedError


def deploy_all_sites(site_paths: Set[Path], *, remote_ip: str | None = None, remote_ssh_key: str | None = None, remote_user_name: str | None = None, remote_directory: str | None = None, dry_run: bool = False) -> Set[str]:  # noqa: E501
    """"""
    logger.debug("Begin deploying all sites.")

    deployed_sites: dict[str, CaughtException | None] = {}

    site_path: Path
    for site_path in site_paths:
        formatted_site_name: str = (
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
            deployed_sites[formatted_site_name] = caught_exception
            continue
        else:
            deployed_sites[formatted_site_name] = None

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
