""""""

from collections.abc import Sequence

__all__: Sequence[str] = ("generate_icons_details_list",)


from typing import NamedTuple

from django import template
from django.utils.safestring import SafeString, mark_safe

register: template.Library = template.Library()


class IconDetails(NamedTuple):
    label: SafeString
    font_awesome_icon_name: SafeString
    link_href: SafeString


@register.simple_tag
def generate_icons_details_list() -> Sequence[IconDetails]:
    return [
        IconDetails(
            label=mark_safe("GitHub"),
            font_awesome_icon_name=mark_safe("brands fa-github"),
            link_href=mark_safe("https://github.carrotmanmatt.com"),
        ),
        IconDetails(
            label=mark_safe("Twitch"),
            font_awesome_icon_name=mark_safe("brands fa-twitch"),
            link_href=mark_safe("https://twitch.carrotmanmatt.com"),
        ),
        IconDetails(
            label=mark_safe("Reddit"),
            font_awesome_icon_name=mark_safe("brands fa-reddit"),
            link_href=mark_safe("https://reddit.carrotmanmatt.com"),
        ),
        IconDetails(
            label=mark_safe("Instagram"),
            font_awesome_icon_name=mark_safe("brands fa-instagram"),
            link_href=mark_safe("https://instagram.carrotmanmatt.com"),
        ),
        IconDetails(
            label=mark_safe("YouTube"),
            font_awesome_icon_name=mark_safe("brands fa-youtube"),
            link_href=mark_safe("https://youtube.carrotmanmatt.com"),
        ),
        IconDetails(
            label=mark_safe("Stack&nbsp;Overflow"),
            font_awesome_icon_name=mark_safe("brands fa-stack-overflow"),
            link_href=mark_safe("https://stackoverflow.carrotmanmatt.com"),
        ),
        IconDetails(
            label=mark_safe("Email"),
            font_awesome_icon_name=mark_safe("solid fa-envelope"),
            link_href=mark_safe("mailto:matt@carrotmanmatt.com"),
        ),
    ]
