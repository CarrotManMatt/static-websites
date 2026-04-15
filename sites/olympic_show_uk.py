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
            h.div(class_="primary-container")[
                h.img(id="logo", src="/static/images/Logo.png"),
                h.h1["Welcome Aboard!"],
                h.div(class_="links-container")[
                    h.a(href="/audition/pack")[
                        "Audition Pack",
                        h.i(class_="fa-solid fa-arrow-up-right-from-square fa-sm"),
                    ],
                    h.a(href="/audition/signup")[
                        "Audition Sign-Ups",
                        h.i(class_="fa-solid fa-arrow-up-right-from-square fa-sm"),
                    ],
                ],
                h.div(class_="links-container")[
                    h.a(href="https://www.instagram.com/3bugsfringe")[
                        "@3bugsfringe", h.i(class_="fa-brands fa-instagram")
                    ]
                ],
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
        favicon_png_sizes={96},
        stylesheets_extend=(
            h.link(
                href="/static/fontawesome-free-7.2.0-web/css/fontawesome.css", rel="stylesheet"
            ),
            h.link(href="/static/fontawesome-free-7.2.0-web/css/solid.css", rel="stylesheet"),
            h.link(href="/static/fontawesome-free-7.2.0-web/css/brands.css", rel="stylesheet"),
        ),
    )
}
