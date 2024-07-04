"""Custom exception classes to be used within this project."""

from collections.abc import Sequence

__all__: Sequence[str] = ("BaseError", "MutuallyExclusiveArgsError")


import abc
from collections.abc import Iterator, Set
from typing import Final, override

from classproperties import classproperty


class BaseError(BaseException, abc.ABC):
    """Base exception parent class."""

    # noinspection PyMethodParameters,PyPep8Naming
    @classproperty
    @abc.abstractmethod
    def DEFAULT_MESSAGE(cls) -> str:  # noqa: N802,N805
        """The message to be displayed alongside this exception class if none is provided."""  # noqa: D401

    @override
    def __init__(self, message: str | None = None) -> None:
        """Initialise a new exception with the given error message."""
        self.message: str = message or self.DEFAULT_MESSAGE

        super().__init__(self.message)

    @override
    def __repr__(self) -> str:
        """Generate a developer-focused representation of the exception's attributes."""
        formatted: str = self.message

        attributes: dict[str, object] = self.__dict__
        attributes.pop("message")
        if attributes:
            formatted += f""" ({
                ", ".join(
                    {
                        f"{attribute_name}={attribute_value!r}"
                        for attribute_name, attribute_value
                        in attributes.items()
                    }
                )
            })"""

        return formatted


class MutuallyExclusiveArgsError(BaseError, ValueError):
    """Exception class for when two or more mutually exclusive arguments are provided."""

    # noinspection PyMethodParameters,PyPep8Naming
    @classproperty
    @override
    def DEFAULT_MESSAGE(cls) -> str:  # noqa: N805
        return "Two or more mutually exclusive arguments were provided."

    @override
    def __init__(self, message: str | None = None, mutually_exclusive_arguments: Set[Set[str]] | None = None) -> None:  # noqa: E501
        self.mutually_exclusive_arguments: Set[Set[str]] | None = mutually_exclusive_arguments

        super().__init__(
            (
                message
                if message or not mutually_exclusive_arguments
                else self.format_mutually_exclusive_arguments_to_message(
                    mutually_exclusive_arguments,
                )
            ),
        )

    @classmethod
    def format_mutually_exclusive_arguments_to_message(cls, mutually_exclusive_arguments: Set[Set[str]]) -> str:  # noqa: E501
        """Create the exception message based on the set of mutually exclusive arguments."""
        if not mutually_exclusive_arguments:
            CANNOT_CONSTRUCT_MESSAGE_WITHOUT_ARGUMENTS_MESSAGE: Final[str] = (
                "Cannot construct exception message without any argument values."
            )
            raise ValueError(CANNOT_CONSTRUCT_MESSAGE_WITHOUT_ARGUMENTS_MESSAGE)

        no_argument_values_provided_exception: ValueError = ValueError(
            f"No argument values provided to {cls.__name__}.",
        )

        remaining_arguments: Iterator[Set[str]] = iter(mutually_exclusive_arguments)

        first_argument: Set[str] = next(remaining_arguments)
        if not first_argument:
            raise no_argument_values_provided_exception

        constructed_message: str = f"argument `{"`/`".join(first_argument)}` not allowed"

        if len(mutually_exclusive_arguments) == 1:
            return constructed_message + " on its own"

        second_argument: Set[str] = next(remaining_arguments)
        if not second_argument:
            raise no_argument_values_provided_exception

        constructed_message += f" with argument `{"`/`".join(second_argument)}`"

        argument: Set[str]
        for argument in remaining_arguments:
            if not argument:
                raise no_argument_values_provided_exception

            constructed_message += f"or with argument `{"`/`".join(second_argument)}`"

        return constructed_message
