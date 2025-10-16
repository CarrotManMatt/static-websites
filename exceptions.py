"""Custom exception classes to be used within this project."""

import abc
from typing import TYPE_CHECKING, override

from typed_classproperties import classproperty

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence
    from collections.abc import Set as AbstractSet
    from typing import Final

__all__: Sequence[str] = ("BaseError", "MutuallyExclusiveArgsError")


class BaseError(BaseException, abc.ABC):
    """Base exception parent class."""

    @classproperty
    @abc.abstractmethod
    def DEFAULT_MESSAGE(cls) -> str:
        """The message to be displayed alongside this exception class if none is provided."""

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
                        for attribute_name, attribute_value in attributes.items()
                    }
                )
            })"""

        return formatted


class MutuallyExclusiveArgsError(BaseError, ValueError):
    """Exception class for when two or more mutually exclusive arguments are provided."""

    @classproperty
    @override
    def DEFAULT_MESSAGE(cls) -> str:
        return "Two or more mutually exclusive arguments were provided."

    @override
    def __init__(
        self,
        message: str | None = None,
        mutually_exclusive_arguments: AbstractSet[AbstractSet[str]] | None = None,
    ) -> None:
        self.mutually_exclusive_arguments: AbstractSet[AbstractSet[str]] | None = (
            mutually_exclusive_arguments
        )

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
    def format_mutually_exclusive_arguments_to_message(
        cls, mutually_exclusive_arguments: AbstractSet[AbstractSet[str]]
    ) -> str:
        """Create the exception message based on the set of mutually exclusive arguments."""
        if not mutually_exclusive_arguments:
            CANNOT_CONSTRUCT_MESSAGE_WITHOUT_ARGUMENTS_MESSAGE: Final[str] = (
                "Cannot construct exception message without any argument values."
            )
            raise ValueError(CANNOT_CONSTRUCT_MESSAGE_WITHOUT_ARGUMENTS_MESSAGE)

        no_argument_values_provided_exception: ValueError = ValueError(
            f"No argument values provided to {cls.__name__}.",
        )

        remaining_arguments: Iterator[AbstractSet[str]] = iter(mutually_exclusive_arguments)

        first_argument: AbstractSet[str] = next(remaining_arguments)
        if not first_argument:
            raise no_argument_values_provided_exception

        constructed_message: str = f"argument `{'`/`'.join(first_argument)}` not allowed"

        if len(mutually_exclusive_arguments) == 1:
            return constructed_message + " on its own"

        second_argument: AbstractSet[str] = next(remaining_arguments)
        if not second_argument:
            raise no_argument_values_provided_exception

        constructed_message += f" with argument `{'`/`'.join(second_argument)}`"

        argument: AbstractSet[str]
        for argument in remaining_arguments:
            if not argument:
                raise no_argument_values_provided_exception

            constructed_message += f"or with argument `{'`/`'.join(second_argument)}`"

        return constructed_message
