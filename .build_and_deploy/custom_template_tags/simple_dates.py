"""Custom Django template tags for rendering dates within Django templates."""

import datetime
from typing import TYPE_CHECKING

from dateutil.relativedelta import relativedelta
from django import template

if TYPE_CHECKING:
    from collections.abc import Sequence

__all__: "Sequence[str]" = ("carrotmanmatt_age", "current_year")

register: template.Library = template.Library()


@register.simple_tag
def current_year() -> int:
    """
    Get the current year as an integer.

    The current year will be retrieved
    based on a timezone-aware understanding of the current date,
    according to the server this build script is running on.

    This tag is more useful than Django's inbuilt 'now' tag
    because it has no requirement of a valid Django settings file.
    """
    return datetime.datetime.now(tz=datetime.UTC).year


@register.simple_tag
def carrotmanmatt_age() -> int:
    """Get CarrotManMatt's current age as an integer for use in rendered HTML pages."""
    return relativedelta(
        datetime.datetime.now(tz=datetime.UTC),
        datetime.datetime(year=2004, month=7, day=8, tzinfo=datetime.UTC),
    ).years
