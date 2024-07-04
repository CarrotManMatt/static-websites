"""Set up logging."""

from collections.abc import Sequence

__all__: Sequence[str] = ("setup",)


import logging
from collections.abc import Mapping
from logging import Logger
from typing import Final, Literal, TextIO

logger: Final[Logger] = logging.getLogger("static-website-builder")
extra_context_logger: Final[Logger] = logging.getLogger("static-website-builder-extra-context")

LOG_LEVEL_MAPS: Final[Mapping[Literal[1, 2, 3], Literal["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"]]] = {  # noqa: E501
    1: "INFO",
    2: "DEBUG",
    3: "DEBUG",
}


def setup(*, verbosity: Literal[0, 1, 2, 3] = 1) -> None:
    """Set up a console logger with the output level according to the given verbosity."""
    logger.setLevel(1)
    logger.propagate = False
    extra_context_logger.setLevel(1)
    extra_context_logger.propagate = False

    if verbosity != 0:
        # noinspection SpellCheckingInspection
        info_format_string: str = "{asctime} | static-website-builder | {levelname:^8} - "

        console_logging_handler: logging.StreamHandler[TextIO] = logging.StreamHandler()
        console_logging_handler.setFormatter(
            logging.Formatter(f"{info_format_string}{{message}}", style="{"),
        )
        # noinspection PyTypeChecker
        console_logging_handler.setLevel(LOG_LEVEL_MAPS[verbosity])
        logger.addHandler(console_logging_handler)

        console_logging_handler = logging.StreamHandler()
        console_logging_handler.setFormatter(
            logging.Formatter(
                f"{info_format_string}({{extra_context}}) {{message}}",
                style="{",
            ),
        )
        # noinspection PyTypeChecker
        console_logging_handler.setLevel(LOG_LEVEL_MAPS[verbosity])
        extra_context_logger.addHandler(console_logging_handler)

        # noinspection PyTypeChecker
        logger.debug(
            "Logger set up with minimum output level: %s",
            LOG_LEVEL_MAPS[verbosity],
        )
