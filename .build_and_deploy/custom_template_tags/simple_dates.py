""""""

from collections.abc import Sequence

__all__: Sequence[str] = ("current_year", "carrotmanmatt_age")


import datetime

from dateutil.relativedelta import relativedelta
from django import template

register: template.Library = template.Library()


@register.simple_tag
def current_year() -> int:
    return datetime.date.today().year


@register.simple_tag
def carrotmanmatt_age() -> int:
    return relativedelta(
        datetime.date.today(),
        datetime.date(2004, 8, 7),
    ).years
