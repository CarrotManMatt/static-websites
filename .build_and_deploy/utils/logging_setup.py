""""""

from collections.abc import Sequence

__all__: Sequence[str] = ("setup",)

import logging
from logging import Logger
from typing import Final, Literal


logger: Final[Logger] = logging.getLogger("static-website-builder")


def setup(*, verbosity: Literal[0, 1, 2, 3] = 1) -> None:
    """"""
    raise NotImplementedError
