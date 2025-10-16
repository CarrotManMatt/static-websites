"""Generic HTML component constructors for use across sites."""

from collections.abc import Iterable
from typing import TYPE_CHECKING

import htpy as h
from markupsafe import Markup

import utils

if TYPE_CHECKING:
    from collections.abc import Sequence
    from typing import Final


__all__: Sequence[str] = (
    "component_base",
    "component_body",
    "component_icons_list",
    "component_site_copyright",
)


def component_icons_list() -> h.Node:
    """Generate the icons list for links to social media."""
    return (
        h.li[h.a(href=link, class_=("icon", *classes))[h.span(class_=("label",))[label]]]
        for link, classes, label in (
            ("https://github.carrotmanmatt.com", ("brands", "fa-github"), "GitHub"),
            ("https://twitch.carrotmanmatt.com", ("brands", "fa-twitch"), "Twitch"),
            ("https://reddit.carrotmanmatt.com", ("brands", "fa-reddit"), "Reddit"),
            ("https://instagram.carrotmanmatt.com", ("brands", "fa-instagram"), "Instagram"),
            ("https://youtube.carrotmanmatt.com", ("brands", "fa-youtube"), "YouTube"),
            (
                "https://stackoverflow.carrotmanmatt.com",
                ("brands", "fa-stack-overflow"),
                Markup("Stack&nbsp;Overflow"),
            ),
            ("mailto:matt@carrotmanmatt.com", ("solid", "fa-envelope"), "Email"),
        )
    )


def component_site_copyright(
    *,
    classes: h.Attribute | None = None,
    styles: h.Attribute | None = None,
    extra_tags: h.Node | None = None,
) -> h.Element:
    """Generate the copyright link to return to the main webpage from site footers."""
    return h.a(class_=classes, href="https://carrotmanmatt.com", style=styles)[
        Markup("©&nbsp;CarrotManMatt&nbsp;2022-{:d}").format(utils.get_current_year()),
        extra_tags,
    ]


def component_body(
    *,
    main: h.Node,
    header: h.Node | None = None,
    footer: h.Node | None = None,
    scripts: h.Node | None = None,
) -> h.Element:
    """Generate the main body component."""
    return h.body[
        h.header[header] if header is not None else None,
        h.main[main],
        h.footer[footer] if footer is not None else None,
        scripts,
    ]


def component_base(  # noqa: PLR0913
    *,
    body: h.Node,
    page_title: h.Attribute = "CarrotManMatt.com",
    page_title_prefix: str | int | bool | None = None,
    page_description: h.Attribute = "CarrotManMatt's personal website.",
    page_meta_image: h.Attribute = "https://carrotmanmatt.com/static/website_icon.png",
    page_content_type: h.Attribute = "article",
    page_keywords: h.Attribute = "CarrotManMatt",
    page_keywords_extend: str | int | bool | None | Iterable[str | int | bool] = None,
    site_url: h.Attribute = "https://carrotmanmatt.com",
    after_body: h.Node | None = None,
    copyright_comment: h.Node | None = None,
    stylesheets: h.Node = h.link(href="/static/css/main.css", rel="stylesheet"),  # noqa: B008
    stylesheets_extend: h.Node | None = None,
    viewport_meta: h.Node = h.meta(  # noqa: B008
        content="width=device-width, initial-scale=1", name="viewport"
    ),
    extra_head: h.Node | None = None,
) -> h.HTMLElement:
    """Generate base site component."""
    if page_title_prefix is not None:
        if not isinstance(page_title, (str, int, bool)):
            INVALID_PAGE_TITLE_TYPE_MESSAGE: Final[str] = (
                f"Cannot use 'page_title_prefix' with type of 'page_title': {type(page_title)}"
            )
            raise TypeError(INVALID_PAGE_TITLE_TYPE_MESSAGE)

        page_title = f"{page_title_prefix} | {page_title}"
        del page_title_prefix

    if page_keywords_extend is not None:
        if not isinstance(page_keywords, (str, int, bool, Iterable)):
            INVALID_PAGE_KEYWORDS_TYPE_MESSAGE: Final[str] = (
                "Cannot use 'page_keywords_extend' with type of 'page_keywords': "
                f"{type(page_keywords)}"
            )
            raise TypeError(INVALID_PAGE_KEYWORDS_TYPE_MESSAGE)

        page_keywords = f"{page_keywords},{
            page_keywords_extend
            if isinstance(page_keywords_extend, (str, int, bool))
            else ','.join(str(page_keyword) for page_keyword in page_keywords_extend)
        }"
        del page_keywords_extend

    if stylesheets_extend is not None:
        stylesheets = (stylesheets, stylesheets_extend)
        del stylesheets_extend

    return h.html(lang="en-GB")[
        copyright_comment,
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
            h.meta(content=page_keywords, name="keywords"),
            h.meta(charset="utf-8"),
            h.meta(content="IE=edge", http_equiv="X-UA-Compatible"),
            viewport_meta,
            stylesheets,
            h.link(href="/favicon.ico", rel="shortcut icon", type="image/png"),
            h.link(href="/apple-touch-icon.png", rel="apple-touch-icon", sizes="180x180"),
            h.link(href="/favicon-32x32.png", rel="icon", sizes="32x32", type="image/png"),
            h.link(href="/favicon-16x16.png", rel="icon", sizes="16x16", type="image/png"),
            h.link(href="/site.webmanifest", rel="manifest"),
            h.link(color="#ff9f0e", href="/safari-pinned-tab.svg", rel="mask-icon"),
            h.meta(content="#ff9f0e", name="msapplication-TileColor"),
            h.meta(content="#ffbb56", name="theme-color"),
            extra_head,
        ],
        body,
        after_body,
    ]
