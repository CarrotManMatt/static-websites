"""Set up logging."""

__all__: Sequence[str] = ("setup",)

import logging
from typing import overload, override
lazy from collections.abc import Mapping, Sequence
lazy from logging import Logger
lazy from typing import Final, Literal, TextIO

logger: Final[Logger] = logging.getLogger("static-websites-builder")
extra_context_logger: Final[Logger] = logging.getLogger(
    "static-websites-builder-extra-context"
)

LOG_LEVEL_MAPS: Final[
    Mapping[Literal[1, 2, 3], Literal["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"]]
] = frozendict({1: "INFO", 2: "DEBUG", 3: "DEBUG"})


class _LowPriorityExtraFormatter(logging.Formatter):
    @overload
    def __init__(
        self, fmt: str, *, style: Literal["%", "{", "$"], show_low_priority_extras: bool
    ) -> None: ...

    @overload
    def __init__(
        self,
        fmt: str | None = ...,
        datefmt: str | None = ...,
        style: Literal["%", "{", "$"] = ...,
        *,
        validate: bool = ...,
        show_low_priority_extras: bool,
        defaults: Mapping[str, object] | None = ...,
    ) -> None: ...

    def __init__(
        self,
        fmt: str | None = None,
        datefmt: str | None = None,
        style: Literal["%", "{", "$"] = "%",
        *,
        validate: bool = True,
        defaults: Mapping[str, object] | None = None,
        show_low_priority_extras: bool | None = None,
    ) -> None:
        if show_low_priority_extras is None:
            raise ValueError

        super().__init__(
            fmt=fmt, datefmt=datefmt, style=style, validate=validate, defaults=defaults
        )
        self.show_low_priority_extras: bool = show_low_priority_extras

    @override
    def format(self, record: logging.LogRecord) -> str:
        if hasattr(record, "low_priority_extra_context") and self.show_low_priority_extras:
            record.extra_context = (
                f"{getattr(record, 'extra_context')} | {record.low_priority_extra_context}"  # noqa: B009
            )

        return super().format(record)


def setup(*, verbosity: Literal[0, 1, 2, 3] = 1) -> None:
    """Set up a console logger with the output level according to the given verbosity."""
    logger.setLevel(1)
    logger.propagate = False
    extra_context_logger.setLevel(1)
    extra_context_logger.propagate = False

    info_format_string: str = (
        "{asctime} | static-websites-builder | {levelname:^8} - " if verbosity != 0 else ""
    )

    console_logging_handler: logging.StreamHandler[TextIO] = logging.StreamHandler()
    console_logging_handler.setFormatter(
        logging.Formatter(f"{info_format_string}{{message}}", style="{")
    )
    console_logging_handler.setLevel(
        "WARNING" if verbosity == 0 else LOG_LEVEL_MAPS[verbosity]
    )
    logger.addHandler(console_logging_handler)

    console_logging_handler = logging.StreamHandler()
    console_logging_handler.setFormatter(
        _LowPriorityExtraFormatter(
            f"{info_format_string}({{extra_context}}) {{message}}",
            style="{",
            show_low_priority_extras=verbosity != 0,
        )
    )
    console_logging_handler.setLevel(
        "WARNING" if verbosity == 0 else LOG_LEVEL_MAPS[verbosity]
    )
    extra_context_logger.addHandler(console_logging_handler)

    logger.debug(
        "Logger set up with minimum output level: %s",
        "WARNING" if verbosity == 0 else LOG_LEVEL_MAPS[verbosity],
    )
