""""""

from typing import TYPE_CHECKING

import htpy as h

from components import component_base, component_body, component_site_copyright

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence
    from typing import Final


__all__: "Sequence[str]" = ("PAGES_MAP",)


PAGES_MAP: "Final[Mapping[str, h.HTMLElement]]" = {
    "index.html": component_base(
        body=component_body(
            header=(
                h.div(class_=("row", "mx-0", "mt-4"))[
                    h.div(class_=("w-auto", "mx-auto"))[
                        h.div(class_=("col", "col-auto"))[
                            h.a(class_=("text-reset", "text-decoration-none"), href="")[
                                h.img(
                                    src="/static/images/Logo.png",
                                    alt="a carrot within a blue car",
                                    height="100vh",
                                    width="100%",
                                )
                            ]
                        ]
                    ]
                ],
                h.h1(class_=("text-center", "fs-1", "my-0", "pb-1"))["Car Points Game"],
            ),
            main=(
                h.h1(class_=("text-center", "fs-3", "mb-0"), id="counter"),
                (
                    h.div(class_=("row", "mx-0", "mt-2" if counter != 1 else ""))[
                        h.div(class_=("w-auto", "mx-auto"))[
                            h.button(
                                type="button",
                                class_=("btn", "btn-success", "fw-bold"),
                                onclick=f"increase({counter})",
                            )["+"],
                            h.p(
                                class_=("d-inline", "fs-5", "align-middle", "mx-2"),
                                id=f"button-{counter}",
                            ),
                            h.button(
                                type="button",
                                disabled=True,
                                onclick=f"decrease({counter})",
                                class_=("btn", "btn-danger", "fw-bold", "decrease"),
                            )["-"],
                        ]
                    ]
                    for counter in range(1, 10)
                ),
                h.div(class_=("row", "mx-0", "mt-4"))[
                    h.div(class_=("w-auto", "mx-auto"))[
                        h.div(onclick="names()")[
                            h.input(
                                class_=("form-check-input",),
                                type="radio",
                                name="namesOrPoints",
                                id="names",
                                checked=True,
                            ),
                            h.label(class_=("ms-1", "form-check-label"), for_="names")[
                                "Category Names"
                            ],
                        ],
                        h.div(class_=("mt-2",), onclick="points()")[
                            h.input(
                                class_=("form-check-input",),
                                type="radio",
                                name="namesOrPoints",
                                id="points",
                            ),
                            h.label(class_=("ms-1", "form-check-label"), for_="points")[
                                "Points Rewarded"
                            ],
                        ],
                    ]
                ],
            ),
            footer=h.p(class_=("text-center", "fs-5", "my-3"))[
                component_site_copyright(classes=("text-secondary", "text-decoration-none"))
            ],
            scripts=h.script(type="text/javascript")["names()"],
        ),
        page_title="Car Points Game",
        page_description="CarrotManMatt's web car points counting game.",
        site_url="https://car-points.carrotmanmatt.com",
        page_meta_image="https://car-points.carrotmanmatt.com/static/Logo.png",
        page_content_type="game",
        page_keywords_extend=(
            "game",
            "car-points",
            "overtaking",
            "undertaking",
            "vehicles",
            "video game",
        ),
        stylesheets=h.link(
            href="/static/bootstrap-5.2.0-dist/css/bootstrap.min.css", rel="stylesheet"
        ),
        extra_head=(
            h.link(rel="stylesheet", type="text/css", href="/static/styles/main.css"),
            h.script(src="/static/scripts/main.js", type="text/javascript"),
        ),
    ),
}
