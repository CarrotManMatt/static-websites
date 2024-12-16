"""Validator classes that hold values guaranteed to be valid."""

import abc
import re
import socket
from pathlib import Path
from typing import TYPE_CHECKING, final, overload, override

if TYPE_CHECKING:
    from collections.abc import Sequence
    from typing import Final

__all__: "Sequence[str]" = ("Hostname", "SimpleValidator", "Username")


class SimpleValidator[T](abc.ABC):
    """Validator class that holds a value guaranteed to be valid."""

    @classmethod
    @abc.abstractmethod
    def _get_wrapped_type(cls) -> type[T]:
        """
        Return the wrapped type.

        This is used for generic isinstance checks,
        when the wrapped type is not known at compile time.
        """

    @classmethod
    def clean(cls, value: object) -> T:
        """
        Transform the incoming value as necessary to become a valid value.

        This can be overridden by validator subclasses.
        By default, it will just check that the value has the same type as the wrapped type,
        then return the value unchanged.
        """
        if not isinstance(value, cls._get_wrapped_type()):
            raise TypeError

        return value

    @classmethod
    @final
    def validate(cls, value: T) -> None:
        """
        Perform custom validation on the wrapped value.

        This is a fixed shortcut function that calls cls._validate() on the cleaned value.
        """
        cls._validate(value=cls.clean(value))

    @classmethod
    @abc.abstractmethod
    def _validate(cls, value: T) -> None:
        """Perform custom validation on the wrapped value."""

    def __init__(self, value: T, /) -> None:
        """Validate and store the cleaned wrapped value."""
        self.validate(value)

        self._value: T = self.clean(value)

    def __str__(self) -> str:
        """Return the string representation of the wrapped validated value."""
        return str(self._value)

    def __repr__(self) -> str:
        """Return the developer-focussed representation of the wrapped validated value."""
        return repr(self._value)

    def __bool__(self) -> bool:
        """Return the truthiness of the wrapped validated value."""
        return bool(self._value)


class _StrippedStringValidator(SimpleValidator[str], abc.ABC):
    @classmethod
    @override
    def _get_wrapped_type(cls) -> type[str]:
        return str

    @classmethod
    @override
    def clean(cls, value: object) -> str:
        return super().clean(value).strip()

    @overload
    def __rtruediv__(self, other: Path) -> Path: ...

    @overload
    def __rtruediv__(self, other: object) -> object: ...

    def __rtruediv__(self, other: object) -> object:
        """
        Perform right-division with another object.

        Because this wrapper holds a string object, if the other object is a Path,
        the Path division can be applied to the wrapped string.
        """
        if isinstance(other, Path):
            return other / self._value

        return NotImplemented


class Hostname(_StrippedStringValidator):
    """Wrapper validator holding an SSH hostname or IP address string."""

    @classmethod
    @override
    def _validate(cls, value: str) -> None:
        hostname_error: socket.gaierror
        try:
            socket.gethostbyname(value)
        except socket.gaierror as hostname_error:
            INVALID_HOSTNAME_MESSAGE: Final[str] = "Invalid hostname."
            raise ValueError(INVALID_HOSTNAME_MESSAGE) from hostname_error


class Username(_StrippedStringValidator):
    """Wrapper validator holding an SSH remote username string."""

    @classmethod
    @override
    def _validate(cls, value: str) -> None:
        match: re.Match[str] | None = re.fullmatch(
            r"\A[a-z_](?:[a-z0-9_-]{0,31}|[a-z0-9_-]{0,30}\$)\Z",
            value,
        )
        if not match:
            INVALID_USERNAME_MESSAGE: Final[str] = "Invalid username."
            raise ValueError(INVALID_USERNAME_MESSAGE)
