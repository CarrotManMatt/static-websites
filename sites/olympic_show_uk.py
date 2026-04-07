"""olympic-show.uk static site definition."""

from pathlib import PurePosixPath
from typing import TYPE_CHECKING

import htpy as h

from components import component_base

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence
    from typing import Final


__all__: Sequence[str] = ("PAGES_MAP",)


PAGES_MAP: Final[Mapping[PurePosixPath, h.HTMLElement]] = {
    PurePosixPath("index.html"): component_base(
        body=h.body[
            h.div(class_="container")[
                h.img(src="/static/images/Logo.png"), h.h1["Coming Soon!"]
            ]
        ],
        page_title="Olympic - 3BUGS Fringe",
        page_description=(
            "Step back in time aboard Olympic to discover heroism and heartbreak.\n"
            "Show dates: 13th, 14th & 15th June 2026 "
            "@ University of Birmingham Guild of Students"
        ),
        page_meta_image="https://olympic-show.uk/static/images/Logo.png",
        page_content_type="website",
        page_keywords=(
            "olympic",
            "ship",
            "theatre",
            "amateur-dramatics",
            "guild-of-students",
            "birmingham",
            "show",
            "play",
            "student-written",
        ),
        site_url="https://olympic-show.uk",
    )
}
