""""""

from typing import TYPE_CHECKING

import htpy as h

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Sequence


__all__: "Sequence[str]" = ("components",)


def base(  # noqa: PLR0913
    page_title: str = "CarrotManMatt.com",
    page_description: str = "CarrotManMatt's personal website.",
    page_meta_image: str = "https://carrotmanmatt.com/static/website_icon.png",
    page_content_type: str = "article",
    page_keywords: "Iterable[str]" = ("CarrotManMatt",),
    site_url: str = "https://carrotmanmatt.com",
    after_body: h.Node | None = None,
    copyright_comment_func: "Callable[[], str] | None" = None,
    stylesheets: h.Node = h.link(href="/static/css/main.css", rel="stylesheet"),  # noqa: B008
    viewport_meta: h.Node = h.meta(  # noqa: B008
        content="width=device-width, initial-scale=1", name="viewport"
    ),
) -> h.Element:
    """"""
    return h.html(lang="en-GB")[
        h.comment(copyright_comment_func()) if copyright_comment_func is not None else None,
        h.head[
            h.title[page_title],
            h.meta(content=page_title, property="og:title"),
            h.meta(content=page_description, property="og:description"),
            h.meta(content=site_url, property="og:url"),
            h.meta(content=page_meta_image, property="og:image"),
            h.meta(content=page_content_type, property="og:type"),
            h.meta(content=page_meta_image, name="twitter:card"),
            h.meta(content="#ff9f0e", data_react_helmet="true", name="theme-color"),
            h.meta(content=page_title, itemprop="name"),
            h.meta(content=page_description, itemprop="description"),
            h.meta(content=page_description, name="description"),
            h.meta(content=", ".join(page_keywords), name="keywords"),
            h.meta(charset="utf-8"),
            h.meta(content="IE=edge", http_equiv="X-UA-Compatible"),
            viewport_meta,
            stylesheets,
            h.link(href="/favicon.ico", rel="shortcut icon", type="image/png"),
        ],
        h.body,
        after_body,
    ]
