""""""

from collections.abc import Sequence

__all__: Sequence[str] = ("current_year", "carrotmanmatt_age")


from django import template

register: template.Library = template.Library()


@register.simple_tag
def current_year() -> int:
    return 2024  # TODO: Get from aware datetime


@register.simple_tag
def carrotmanmatt_age() -> int:
    return 19  # TODO: Get from aware datetime
