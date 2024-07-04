"""Console entry point for the static websites builder & deployment script."""

from collections.abc import Sequence

__all__: Sequence[str] = ("run",)


import logging
import sys
from argparse import ArgumentParser, Namespace
from collections.abc import Set
from logging import Logger
from pathlib import Path
from typing import TYPE_CHECKING, Final, Literal

import build
import cleanup
import deploy
from exceptions import MutuallyExclusiveArgsError
from utils import logging_setup
from utils.validators import Hostname, Username

if TYPE_CHECKING:
    # noinspection PyProtectedMember,PyUnresolvedReferences
    from argparse import _MutuallyExclusiveGroup as MutuallyExclusiveGroup

logger: Final[Logger] = logging.getLogger("static-website-builder")


def _add_remote_arguments_to_parser(arg_parser: ArgumentParser) -> ArgumentParser:
    arg_parser.add_argument(
        "remote-ip",
        type=Hostname,
        help="The IP address or hostname of the webserver to deploy static websites to.",
    )

    if arg_parser.usage:
        arg_parser.usage += "\n       REMOTE_IP"

    return arg_parser


def _set_up_arg_parser(given_arguments: Sequence[str] | None = None) -> ArgumentParser:
    arg_parser: ArgumentParser = ArgumentParser(
        prog="build-and-deploy-static-websites",
        description="Render all sites HTML pages & deploy to given webserver.",
        usage=(
            "[-h/--help]\n       "
            "[-d/--remote-directory REMOTE_DIRECTORY]\n       "
            "[-u/--remote-user REMOTE_USER]\n       "
            "[-D/--dry-run]\n       "
            "[-v/--verbose | -q/--quiet]"
        ),
    )

    arg_parser.add_argument(
        "-d",
        "--remote-directory",
        type=Path,
        help=(
            "The remote directory of the webserver to deploy static websites to. "
            "(This is relative to the home directory of the remote user "
            "and will have the site names appended to it.)"
        ),
    )

    arg_parser.add_argument(
        "-u",
        "--remote-user",
        type=Username,
        help=(
            "The username on the webserver to deploy static websites to. "
            "(Defaults to the root user if not specified.)"
        ),
    )

    arg_parser.add_argument(
        "-D",
        "--dry-run",
        action="store_true",
        help=(
            "Perform all operations apart from saving rendered files "
            "or the final deployment of the static websites."
        ),
    )

    verbosity_args_group: MutuallyExclusiveGroup = arg_parser.add_mutually_exclusive_group()

    verbosity_args_group.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        dest="verbosity",
        help="Increase output verbosity. (Mutually exclusive with `--quiet`.)",
    )

    verbosity_args_group.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Produce no output while running. (Mutually exclusive with `--verbose`.)",
    )

    known_parsed_args: Namespace
    remaining_arg_values: Sequence[str]
    known_parsed_args, remaining_arg_values = arg_parser.parse_known_args(given_arguments)

    if not known_parsed_args.dry_run or remaining_arg_values:
        return _add_remote_arguments_to_parser(arg_parser)

    return arg_parser


def _get_true_verbosity(raw_verbosity: int, *, is_quiet: bool, is_dry_run: bool) -> Literal[0, 1, 2, 3]:  # noqa: E501
    if is_quiet and is_dry_run:
        raise MutuallyExclusiveArgsError(
            mutually_exclusive_arguments={{"-q", "--quiet"}, {"-D", "--dry-run"}},
        )

    raw_verbosity = 0 if is_quiet else raw_verbosity + 1

    if raw_verbosity > 3:
        return 3

    if raw_verbosity == 3:
        return 3

    if raw_verbosity == 2:
        return 2

    if raw_verbosity == 1:
        return 1

    if raw_verbosity == 0:
        if is_dry_run:
            return 1

        return 0

    raise ValueError


def run(argv: Sequence[str] | None = None) -> int:
    """Run the static websites builder & deployment script."""
    arg_parser: ArgumentParser = _set_up_arg_parser(argv)

    parsed_args: Namespace = arg_parser.parse_args(argv)

    try:
        verbosity: Literal[0, 1, 2, 3] = _get_true_verbosity(
            parsed_args.verbosity,
            is_quiet=parsed_args.quiet,
            is_dry_run=parsed_args.dry_run,
        )
    except MutuallyExclusiveArgsError as mutually_exclusive_args_error:
        arg_parser.error(mutually_exclusive_args_error.message)

    # noinspection PyUnboundLocalVariable
    logging_setup.setup(verbosity=verbosity)

    try:
        built_site_paths: Set[Path] = build.build_all_sites()

        if not built_site_paths:
            logger.warning("All sites failed to build. (Or no sites exist.)")
            return 1

        deployed_site_names: Set[str] = deploy.deploy_all_sites(
            built_site_paths,
            verbosity=verbosity,
            remote_hostname=getattr(parsed_args, "remote-ip", None),
            remote_username=parsed_args.remote_user,
            remote_directory=parsed_args.remote_directory,
            dry_run=parsed_args.dry_run,
        )

        if not deployed_site_names:
            logger.warning("All sites failed to deploy.")
            return 1

        sys.stdout.write(",".join(deployed_site_names))
        return 0

    finally:
        if parsed_args.dry_run:
            cleanup.cleanup_all_sites(dry_run=parsed_args.dry_run)


if __name__ == "__main__":
    raise SystemExit(run())
