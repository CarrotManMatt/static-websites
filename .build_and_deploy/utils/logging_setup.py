""""""

from collections.abc import Sequence

__all__: Sequence[str] = ("setup",)

import logging
from collections.abc import Mapping
from logging import Logger
from typing import Final, Literal, TextIO

logger: Final[Logger] = logging.getLogger("static-website-builder")

LOG_LEVEL_MAPS: Final[Mapping[Literal[1, 2, 3], Literal["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"]]] = {  # noqa: E501
    1: "INFO",
    2: "DEBUG",
    3: "DEBUG",
}


def setup(*, verbosity: Literal[0, 1, 2, 3] = 1) -> None:
    """"""
    logger.setLevel(1)
    logger.propagate = False

    if verbosity != 0:
        console_logging_handler: logging.StreamHandler[TextIO] = logging.StreamHandler()

        # noinspection SpellCheckingInspection
        console_logging_handler.setFormatter(
            logging.Formatter(
                "{asctime} | {name} | {levelname:^8} - {message}",
                style="{",
            ),
        )
        # noinspection PyTypeChecker
        console_logging_handler.setLevel(LOG_LEVEL_MAPS[verbosity])
        logger.addHandler(console_logging_handler)

        # noinspection PyTypeChecker
        logger.debug(f"Logger set up with minimum output level: {LOG_LEVEL_MAPS[verbosity]}")
