""""""

from collections.abc import Sequence

__all__: Sequence[str] = ("SimpleValidator", "Hostname", "Username")


import abc
import re
import socket
from pathlib import Path
from typing import TypeVar, Generic, override, final, overload

T = TypeVar("T")


class SimpleValidator(abc.ABC, Generic[T]):
    """"""

    @classmethod
    def clean(cls, value: T) -> T:
        """"""
        return value

    @classmethod
    @final
    def validate(cls, value: T) -> None:
        """"""
        cls._validate(value=cls.clean(value))

    @classmethod
    @abc.abstractmethod
    def _validate(cls, value: T) -> None:
        """"""

    def __init__(self, value: T, /) -> None:
        self.validate(value)

        self._value: T = self.clean(value)

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return repr(self._value)

    def __bool__(self) -> bool:
        return bool(self._value)


class _StrippedStringValidator(SimpleValidator[str], abc.ABC):
    @classmethod
    @override
    def clean(cls, value: str) -> str:
        return value.strip()

    @overload
    def __rtruediv__(self, other: Path) -> Path: ...

    @overload
    def __rtruediv__(self, other: object) -> object: ...

    def __rtruediv__(self, other: object) -> object:
        if isinstance(other, Path):
            return other / self._value

        return NotImplemented


class Hostname(_StrippedStringValidator):
    """"""

    @classmethod
    @override
    def _validate(cls, value: str) -> None:
        hostname_error: socket.gaierror
        try:
            socket.gethostbyname(value)
        except socket.gaierror as hostname_error:
            raise ValueError("Invalid hostname.") from hostname_error


class Username(_StrippedStringValidator):
    """"""

    @classmethod
    @override
    def _validate(cls, value: str) -> None:
        match: re.Match[str] | None = re.fullmatch(
            r"\A[a-z_](?:[a-z0-9_-]{0,31}|[a-z0-9_-]{0,30}\$)\Z",
            value,
        )
        if not match:
            raise ValueError("Invalid username.")
