"""Console entry point for the static websites builder & deployment script."""

from collections.abc import Sequence

__all__: Sequence[str] = ("run",)


from argparse import ArgumentParser, Namespace

import build
import deploy
from utils import logging_setup


def _add_remote_arguments_to_parser(arg_parser: ArgumentParser) -> ArgumentParser:
    arg_parser.add_argument(
        "remote-ip",
        help="The IP address of the webserver to deploy static websites to.",
    )

    arg_parser.add_argument(
        "remote-ssh-key",
        help="The private SSH key of the webserver to deploy static websites to.",
    )

    return arg_parser


def _set_up_arg_parser(given_arguments: Sequence[str] | None = None) -> ArgumentParser:
    arg_parser: ArgumentParser = ArgumentParser(
        prog="build-and-deploy-static-websites",
        description="Render all sites HTML pages & deploy to given webserver.",
        usage=(
            "[-h] "
            "[-D REMOTE_DIRECTORY] "
            "[-U REMOTE_USER] "
            "[--dry-run] "
            "[remote-ip && remote-ssh-key]"
        ),
    )

    arg_parser.add_argument(
        "-D",
        "--remote-directory",
        help="The remote directory of the webserver to deploy static websites to.",
    )

    arg_parser.add_argument(
        "-U",
        "--remote-user",
        help="The username on the webserver to deploy static websites to.",
    )

    arg_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform all operations apart from the final deployment of the static websites.",
    )

    arg_parser.add_argument(
        "-v"
        "--verbose",
        action="count",  # TODO: Add max number
        help="",  # TODO: Add help
    )

    arg_parser.add_argument(  # TODO: Add to mutually exclusive group
        "-q"
        "--quiet",
        action="store_true",
        help="",  # TODO: Add help
    )

    known_parsed_args: Namespace
    remaining_arg_values: Sequence[str]
    known_parsed_args, remaining_arg_values = arg_parser.parse_known_args(given_arguments)

    if not known_parsed_args.dry_run or remaining_arg_values:
        return _add_remote_arguments_to_parser(arg_parser)

    return arg_parser


def run(argv: Sequence[str] | None = None) -> int:
    """Run the static websites builder & deployment script."""
    arg_parser: ArgumentParser = _set_up_arg_parser(argv)

    parsed_args: Namespace = arg_parser.parse_args(argv)

    logging_setup.setup(verbosity=3)  # TODO: Use verbosity parse args

    deploy.deploy_all_sites(
        build.build_all_sites(),
        remote_ip=parsed_args.remote_ip,
        remote_ssh_key=parsed_args.remote_ssh_key,
        remote_directory=parsed_args.remote_directory,
        remote_user_name=parsed_args.remote_user,
        dry_run=parsed_args.dry_run,
    )

    return 0
