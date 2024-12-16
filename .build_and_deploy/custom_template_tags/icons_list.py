"""Custom Django template tags for retrieving details about CarrotManMatt's link icons."""

from typing import TYPE_CHECKING, NamedTuple

from django import template
from django.utils.safestring import mark_safe

if TYPE_CHECKING:
    from collections.abc import Sequence

    from django.utils.safestring import SafeString

__all__: "Sequence[str]" = ("generate_icons_details_list",)

register: template.Library = template.Library()


class IconDetails(NamedTuple):
    label: "SafeString"
    font_awesome_icon_name: "SafeString"
    link_href: "SafeString"


@register.simple_tag
def generate_icons_details_list() -> "Sequence[IconDetails]":
    """Generate the list of icon details for use on CarrotManMatt's main website."""
    return [
        IconDetails(
            label=mark_safe("GitHub"),  # noqa: S308
            font_awesome_icon_name=mark_safe("brands fa-github"),  # noqa: S308
            link_href=mark_safe("https://github.carrotmanmatt.com"),  # noqa: S308
        ),
        IconDetails(
            label=mark_safe("Twitch"),  # noqa: S308
            font_awesome_icon_name=mark_safe("brands fa-twitch"),  # noqa: S308
            link_href=mark_safe("https://twitch.carrotmanmatt.com"),  # noqa: S308
        ),
        IconDetails(
            label=mark_safe("Reddit"),  # noqa: S308
            font_awesome_icon_name=mark_safe("brands fa-reddit"),  # noqa: S308
            link_href=mark_safe("https://reddit.carrotmanmatt.com"),  # noqa: S308
        ),
        IconDetails(
            label=mark_safe("Instagram"),  # noqa: S308
            font_awesome_icon_name=mark_safe("brands fa-instagram"),  # noqa: S308
            link_href=mark_safe("https://instagram.carrotmanmatt.com"),  # noqa: S308
        ),
        IconDetails(
            label=mark_safe("YouTube"),  # noqa: S308
            font_awesome_icon_name=mark_safe("brands fa-youtube"),  # noqa: S308
            link_href=mark_safe("https://youtube.carrotmanmatt.com"),  # noqa: S308
        ),
        IconDetails(
            label=mark_safe("Stack&nbsp;Overflow"),  # noqa: S308
            font_awesome_icon_name=mark_safe("brands fa-stack-overflow"),  # noqa: S308
            link_href=mark_safe("https://stackoverflow.carrotmanmatt.com"),  # noqa: S308
        ),
        IconDetails(
            label=mark_safe("Email"),  # noqa: S308
            font_awesome_icon_name=mark_safe("solid fa-envelope"),  # noqa: S308
            link_href=mark_safe("mailto:matt@carrotmanmatt.com"),  # noqa: S308
        ),
    ]
