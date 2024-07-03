""""""

from collections.abc import Sequence

__all__: Sequence[str] = ("SimpleValidator", "Hostname", "PrivateSSHKey", "Username")


import abc
import re
import socket
from typing import TypeVar, Generic, override, final

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


class _StrippedStringValidator(SimpleValidator[str], abc.ABC):
    @classmethod
    @override
    def clean(cls, value: str) -> str:
        return value.strip()


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


class PrivateSSHKey(_StrippedStringValidator):
    """"""

    @classmethod
    @override
    def _validate(cls, value: str) -> None:
        match: re.Match[str] | None = re.fullmatch(
            r"\A\s*(?P<hyphens>-{2,7})(?P<has_space> ?)BEGIN (?P<key_type>[A-Z]{2,6}|[A-Za-z](?=.*[0-9])[A-Za-z0-9]{1,6}) PRIVATE KEY(?P=has_space)(?P=hyphens)(?:\r?\n)?\s*\S+(?:.*\S+)?\s*(?:\r?\n)?(?P=hyphens)(?P=has_space)END (?P=key_type) PRIVATE KEY(?P=has_space)(?P=hyphens)\s*\Z",
            value,
        )
        if not match:
            raise ValueError("Invalid private SSH key.")


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
