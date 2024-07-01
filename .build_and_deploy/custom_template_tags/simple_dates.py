""""""

from collections.abc import Sequence

__all__: Sequence[str] = ("current_year", "carrotmanmatt_age")


import datetime

from dateutil.relativedelta import relativedelta
from django import template

register: template.Library = template.Library()


@register.simple_tag
def current_year() -> int:
    return datetime.datetime.now(tz=datetime.UTC).year


@register.simple_tag
def carrotmanmatt_age() -> int:
    return relativedelta(
        datetime.datetime.now(tz=datetime.UTC),
        datetime.datetime(year=2004, month=8, day=7, tzinfo=datetime.UTC),
    ).years
