"""infratek-consulting.com static site definition."""

from pathlib import PurePosixPath
from typing import TYPE_CHECKING

import htpy as h
from markupsafe import Markup

from components import component_base

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence
    from typing import Final


__all__: Sequence[str] = ("PAGES_MAP",)


_SITE_DESCRIPTION: Final[str] = Markup("Delivering successful IT change and transformation")
COMPANY_NAME: Final[str] = Markup("InfraTek Consulting Ltd.")
_SITE_TITLE: Final[str] = COMPANY_NAME
_SITE_URL: Final[str] = "https://infratek-consulting.com"
_LINKEDIN_REDIRECT_URL: Final[str] = "https://linkedin.com/in/stevenorton"


PAGES_MAP: Final[Mapping[PurePosixPath, h.HTMLElement]] = {
    PurePosixPath("index.html"): component_base(
        body=h.body(class_="w-element cn033n5 cajgq1a c1tnfgn4 cpd3ydb c60459u")[
            h.div(class_="w-element cajgq1a c14l0slq c1oqod1n cn033n5 c1tnfgn4 cpd3ydb")[
                h.header(
                    class_=(
                        "w-element cnjpzz9 c18volup c1dxf3lp c5ap768 c1eewiqx c1mbpodk "
                        "c1epc58g chxqgsh czsdghz c19uc0ya cshpc3m c9108rz c1hkfodp c12ftnpc "
                        "c6yu8ui c15710u3 czxrtsf c5iako8 c1mig878"
                    )
                )[
                    h.img(
                        class_="w-image ca23ba1 cpxwbrc c1lm51dm",
                        alt=(
                            f"Logo for {COMPANY_NAME} featuring a blue square with "
                            'white stylised letters "iFT" on the left, next to pixelated grey '
                            'text reading "InfraTek" over a thin line and the word '
                            '"CONSULTING" in widely spaced, light uppercase letters.'
                        ),
                        width="3457",
                        height="668",
                        sizes="100vw",
                        srcset=(
                            "/static/images/Wide_Logo.png 16w, "
                            "/static/images/Wide_Logo.png 32w, "
                            "/static/images/Wide_Logo.png 48w, "
                            "/static/images/Wide_Logo.png 64w, "
                            "/static/images/Wide_Logo.png 96w, "
                            "/static/images/Wide_Logo.png 128w, "
                            "/static/images/Wide_Logo.png 256w, "
                            "/static/images/Wide_Logo.png 384w, "
                            "/static/images/Wide_Logo.png 640w, "
                            "/static/images/Wide_Logo.png 750w, "
                            "/static/images/Wide_Logo.png 828w, "
                            "/static/images/Wide_Logo.png 1080w, "
                            "/static/images/Wide_Logo.png 1200w, "
                            "/static/images/Wide_Logo.png 1920w, "
                            "/static/images/Wide_Logo.png 2048w, "
                            "/static/images/Wide_Logo.png 3840w"
                        ),
                        src="/static/images/Wide_Logo.png",
                        decoding="async",
                        loading="lazy",
                    ),
                    h.ul(
                        class_=(
                            "w-element ca6w5wd cnjpzz9 c18volup c1yq0ia6 czl3p1r c1xcub5i "
                            "come4xu c1nre2cz c8i3f13 cajgq1a czxrtsf c5iako8 ciic47k"
                        )
                    )[
                        h.li(
                            class_=(
                                "w-element cb7h0fs c1dxf3lp czl3p1r cc0p71j c1ginzaf c1hkfodp "
                                "ccf2xlf cuzqjos"
                            )
                        )[
                            h.a(
                                href="mailto:info@infratek-consulting.com",
                                class_="w-element c1kimxow c1gvfhvq chjd3qo",
                            )["info@infratek-consulting.com"]
                        ],
                        h.li(
                            class_=(
                                "w-element cb7h0fs cc0p71j c1dxf3lp czl3p1r c1pxr0dd c1ginzaf "
                                "c6041pg c1op3y0d c19tgo6g cixa8sr c1hkfodp c12ftnpc cgmp2cu "
                                "cp8xhzs cd0aev9 c1vdhfq5 c1395t0l ccf2xlf cuzqjos"
                            )
                        )[
                            h.a(
                                href="tel:+447711824367",
                                class_="w-element c1kimxow c1gvfhvq chjd3qo",
                            )["07711 824367"]
                        ],
                        h.li(
                            class_=(
                                "w-element cb7h0fs cc0p71j c1dxf3lp czl3p1r c1pxr0dd c12ftnpc "
                                "cn033n5 czkkky5 clpo7tq c1395t0l"
                            )
                        )[
                            h.a(
                                class_="w-element c1kimxow cfijjxm c1rpijsf c1p6xz3y c6d58ts",
                                href=_LINKEDIN_REDIRECT_URL,
                                target="_blank",
                                rel="noopener noreferrer",
                            )[
                                h.svg(
                                    height="800px",
                                    width="800px",
                                    version="1.1",
                                    id="Layer_1",
                                    xmlns="http://www.w3.org/2000/svg",
                                    xlink="http://www.w3.org/1999/xlink",
                                    viewbox="0 0 382 382",
                                    space="preserve",
                                    class_="w-element clli3ba c1ttpun5",
                                )[
                                    h.path(
                                        d=(
                                            "M347.445,0H34.555C15.471,0,0,15.471,0,"
                                            "34.555v312.889C0,366.529,15.471,382,34.555,"
                                            "382h312.889\n	"
                                            "C366.529,382,382,366.529,382,347.444V34.555C382,"
                                            "15.471,366.529,0,347.445,0z M118.207,329.844c0,"
                                            "5.554-4.502,10.056-10.056,10.056\n	"
                                            "H65.345c-5.554,"
                                            "0-10.056-4.502-10.056-10.056V150.403c0-5.554,"
                                            "4.502-10.056,10.056-10.056h42.806\n	c5.554,0,"
                                            "10.056,4.502,10.056,10.056V329.844z M86.748,"
                                            "123.432c-22.459,"
                                            "0-40.666-18.207-40.666-40.666S64.289,42.1,86.748,"
                                            "42.1\n	s40.666,18.207,40.666,40.666S109.208,"
                                            "123.432,86.748,123.432z M341.91,330.654c0,"
                                            "5.106-4.14,9.246-9.246,9.246H286.73\n	c-5.106,"
                                            "0-9.246-4.14-9.246-9.246v-84.168c0-12.556,"
                                            "3.683-55.021-32.813-55.021c-28.309,0-34.051,"
                                            "29.066-35.204,42.11v97.079\n	c0,5.106-4.139,"
                                            "9.246-9.246,9.246h-44.426c-5.106,"
                                            "0-9.246-4.14-9.246-9.246V149.593c0-5.106,"
                                            "4.14-9.246,9.246-9.246h44.426\n	c5.106,0,"
                                            "9.246,4.14,9.246,9.246v15.655c10.497-15.753,"
                                            "26.097-27.912,59.312-27.912c73.552,0,73.131,"
                                            "68.716,73.131,106.472\n	L341.91,"
                                            "330.654L341.91,330.654z"
                                        ),
                                        class_="w-element clw3zqv",
                                    )
                                ]
                            ]
                        ],
                    ],
                ],
                h.div(
                    class_=(
                        "w-element cnjpzz9 c1dxf3lp czl3p1r c18volup cjcykmj crc4sl1 c1f7a3ac "
                        "c5epv9p cmxiv8v c1txvh0z cbwc20q cq4sgcm cngbs3v c8vdx5f cj0i0rb "
                        "c1f48zct cn8o2ra cg0fcfp c199j28c cmpjcja c1ab4mg4 cum0i76 caaurwn"
                    )
                )[
                    h.h2(
                        class_=(
                            "w-element come4xu c1nre2cz c1dmfnzf c1h1288n cgdjfbm c3wl2rw "
                            "c1oojmny c1px0kxe coom5xy"
                        )
                    )[_SITE_DESCRIPTION]
                ],
                h.div(class_="w-element cnjpzz9 cc0p71j c1dxf3lp czl3p1r c1mbpodk c1eewiqx")[
                    h.div(
                        class_=(
                            "w-element cnjpzz9 c18volup c1dxf3lp czl3p1r c1mbpodk c1r6f7dq "
                            "c1ovucpf co38mhz c1u5ro6g c1rpuiy0 c1rjvaro c1q9fes4 ccsmn8 "
                            "cxtsxow c1924sa8 c16st3bd"
                        )
                    )[
                        h.img(
                            class_="w-image c15nvwk1 c2qve27 c17qeny c1jybra4",
                            alt=(
                                "Overhead view of a wooden table shared by several people "
                                "working on laptops, smartphones, notebooks, and audio "
                                "accessories among snacks and drinks."
                            ),
                            width="1920",
                            height="1280",
                            sizes="100vw",
                            srcset=(
                                "/static/images/Tabletop.webp 16w, "
                                "/static/images/Tabletop.webp 32w, "
                                "/static/images/Tabletop.webp 48w, "
                                "/static/images/Tabletop.webp 64w, "
                                "/static/images/Tabletop.webp 96w, "
                                "/static/images/Tabletop.webp 128w, "
                                "/static/images/Tabletop.webp 256w, "
                                "/static/images/Tabletop.webp 384w, "
                                "/static/images/Tabletop.webp 640w, "
                                "/static/images/Tabletop.webp 750w, "
                                "/static/images/Tabletop.webp 828w, "
                                "/static/images/Tabletop.webp 1080w, "
                                "/static/images/Tabletop.webp 1200w, "
                                "/static/images/Tabletop.webp 1920w, "
                                "/static/images/Tabletop.webp 2048w, "
                                "/static/images/Tabletop.webp 3840w"
                            ),
                            src="/static/images/Tabletop.webp",
                            decoding="async",
                            loading="lazy",
                        ),
                        h.div(
                            class_=(
                                "w-element c15nvwk1 c1p1mnpe cqvxnpf c1epc58g chxqgsh cnjpzz9 "
                                "cc0p71j c1dxf3lp czl3p1r ch50ks2 c4vp7ws c1k6wmiy"
                            )
                        )[
                            h.h1(class_="w-element clli3ba come4xu c1nre2cz")["What we do..."],
                            h.p(
                                class_=(
                                    "w-element clli3ba come4xu c1nre2cz cgi21ub c1lk3hb1 "
                                    "c1q8o5b"
                                )
                            )[
                                "Operating as an independent IT consultancy focusing on "
                                "project & programme delivery, as well as service "
                                "transformation and IT operations improvement assignments."
                            ],
                            h.div(class_="w-element cnjpzz9 cc0p71j c1dxf3lp czl3p1r clli3ba")[
                                h.a(
                                    href="mailto:info@infratek-consulting.com",
                                    class_=(
                                        "w-element cw8vi2e c102m9ht c15nvwk1 cgdjfbm c47zz6h "
                                        "c17kn64z cgi21ub c1gvfhvq caelw59"
                                    ),
                                )["Get in touch"]
                            ],
                        ],
                    ]
                ],
                h.div(
                    class_=(
                        "w-element c147bno4 cngbs3v c8vdx5f cj0i0rb cn8o2ra c199j28c c1f48zct "
                        "cg0fcfp cbwc20q cq4sgcm c1dm8csm cjcykmj crc4sl1 c1f7a3ac c5epv9p "
                        "cnjpzz9 cc0p71j c1dxf3lp czl3p1r c1mbpodk c1eewiqx cs6gguw cafj5ft "
                        "c14l0slq c1oqod1n"
                    )
                )[
                    h.div(
                        class_=(
                            "w-element cnjpzz9 cc0p71j c5ap768 c7einh9 cqv7yqr c1u5ro6g "
                            "c1rpuiy0 c19hoazm c1rjvaro c1wynxth c1yeqpms c1ginzaf c1pxr0dd "
                            "cbv6l2s c1rpsxlw c1f75i1v ck61r7u c1mi6zqd c1x5vc3u cgrt8l4 "
                            "c10pdv1p caw3wh7"
                        )
                    )[
                        h.div(class_="w-element cnjpzz9 cc0p71j czl3p1r ch50ks2 c4vp7ws")[
                            h.h1(class_="w-element come4xu c1nre2cz")["Contact us"],
                            h.ul(
                                class_=(
                                    "w-element ca6w5wd cnjpzz9 c1xcub5i come4xu c1nre2cz "
                                    "c1cqgdcg c1dxf3lp czl3p1r c1eg23wy c1dfxw2z"
                                )
                            )[
                                h.li(class_="w-element cw8vi2e c17ifwgt")[
                                    h.a(
                                        href="tel:+447711824367",
                                        class_=(
                                            "w-element c1kimxow cgi21ub c1bgv8ie c1ttpun5 "
                                            "c1epc58g chxqgsh clli3ba cgdjfbm c1gvfhvq "
                                            "c102m9ht"
                                        ),
                                    )["Call Us"]
                                ],
                                h.li(class_="w-element cw8vi2e c17ifwgt")[
                                    h.a(
                                        href="mailto:info@infratek-consulting.com",
                                        class_=(
                                            "w-element c1kimxow cgi21ub c1ttpun5 c1epc58g "
                                            "chxqgsh clli3ba cgdjfbm c1gvfhvq c102m9ht"
                                        ),
                                    )["Email Us"]
                                ],
                            ],
                            h.h3(class_="w-element come4xu c1nre2cz cwbxxyh")[
                                "Business Hours"
                            ],
                            h.ul(
                                class_=(
                                    "w-element ca6w5wd c1xcub5i come4xu c1nre2cz cnjpzz9 "
                                    "cc0p71j c5ap768 c1eewiqx c1mbpodk c1u5ro6g c1rpuiy0"
                                )
                            )[
                                h.li(class_="w-element cb7h0fs c18volup c5ap768")[
                                    h.p(class_="w-element come4xu c1nre2cz")["Mon - Fri"],
                                    h.p(class_="w-element come4xu c1nre2cz")[
                                        "9:00 am - 5:00 pm"
                                    ],
                                ],
                                h.li(class_="w-element cb7h0fs c18volup c5ap768")[
                                    h.p(class_="w-element come4xu c1nre2cz")["Sat - Sun"],
                                    h.p(class_="w-element come4xu c1nre2cz")["Closed"],
                                ],
                            ],
                        ],
                        h.a(
                            href=_LINKEDIN_REDIRECT_URL,
                            class_="w-element c1kimxow c2cb6r5 c1uvycdr",
                        )[
                            h.svg(
                                height="800px",
                                width="800px",
                                version="1.1",
                                id="Layer_1",
                                xmlns="http://www.w3.org/2000/svg",
                                xlink="http://www.w3.org/1999/xlink",
                                viewbox="0 0 382 382",
                                space="preserve",
                                class_="w-element c1ttpun5 clli3ba",
                            )[
                                h.path(
                                    d=(
                                        "M347.445,0H34.555C15.471,0,0,15.471,0,"
                                        "34.555v312.889C0,366.529,15.471,382,34.555,"
                                        "382h312.889\n	C366.529,382,382,366.529,382,"
                                        "347.444V34.555C382,15.471,366.529,0,347.445,0z "
                                        "M118.207,329.844c0,5.554-4.502,10.056-10.056,"
                                        "10.056\n	H65.345c-5.554,"
                                        "0-10.056-4.502-10.056-10.056V150.403c0-5.554,"
                                        "4.502-10.056,10.056-10.056h42.806\n	c5.554,0,"
                                        "10.056,4.502,10.056,10.056V329.844z M86.748,"
                                        "123.432c-22.459,0-40.666-18.207-40.666-40.666S64.289,"
                                        "42.1,86.748,42.1\n	s40.666,18.207,40.666,"
                                        "40.666S109.208,123.432,86.748,123.432z M341.91,"
                                        "330.654c0,5.106-4.14,9.246-9.246,9.246H286.73\n	"
                                        "c-5.106,0-9.246-4.14-9.246-9.246v-84.168c0-12.556,"
                                        "3.683-55.021-32.813-55.021c-28.309,0-34.051,"
                                        "29.066-35.204,42.11v97.079\n	c0,5.106-4.139,"
                                        "9.246-9.246,9.246h-44.426c-5.106,"
                                        "0-9.246-4.14-9.246-9.246V149.593c0-5.106,4.14-9.246,"
                                        "9.246-9.246h44.426\n	c5.106,0,9.246,4.14,9.246,"
                                        "9.246v15.655c10.497-15.753,26.097-27.912,"
                                        "59.312-27.912c73.552,0,73.131,68.716,73.131,"
                                        "106.472\n	L341.91,330.654L341.91,330.654z"
                                    ),
                                    class_="w-element clw3zqv",
                                )
                            ]
                        ],
                    ]
                ],
            ],
            h.footer(class_="w-element")[
                h.ul(
                    class_=(
                        "w-element ca6w5wd c1xcub5i come4xu c1nre2cz cnjpzz9 c1dxf3lp czl3p1r "
                        "c18volup c39y0kn c102m9ht c47zz6h c17kn64z c1jywr2v ciodwr4 ck1aqmz"
                    )
                )[
                    h.li(class_="w-element c1bb622m c1nzsc5v c17ywm2f")[
                        Markup("&copy; 2026 All Rights Reserved")
                    ],
                    h.li(
                        class_=(
                            "w-element c1bb622m c1nzsc5v c1lkpj3b c17ywm2f cvhtrm7 c1lc8dit "
                            "c9eg06w c1gue4ip c1txv56f c1m96bp c1hx352w c1ggdnsd"
                        )
                    )[COMPANY_NAME],
                    h.li(
                        class_=(
                            "w-element c1bb622m c1nzsc5v c1lkpj3b cb7h0fs c18volup c1dxf3lp "
                            "czl3p1r c7iqsth clx6vvg"
                        )
                    )[
                        h.span(class_="w-element")["Designed and hosted by"],
                        h.a(
                            href="https://carrotmanmatt.com/",
                            class_="w-element c1kimxow c102m9ht c1gvfhvq cuzqjos",
                            target="_blank",
                            rel="noopener noreferrer",
                        )["CarrotManMatt.com"],
                    ],
                ]
            ],
        ],
        page_title=_SITE_TITLE,
        page_description=_SITE_DESCRIPTION,
        page_meta_image=f"{_SITE_URL}/static/images/Square_Logo.png",
        page_content_type="website",
        page_keywords=(
            "IT consultancy",
            "IT project management",
            "IT programme delivery",
            "IT service transformation",
            "IT operations improvement",
            "independent IT consultant",
            "IT change management",
            "IT operational efficiency",
            "digital transformation strategy",
            "IT infrastructure consulting",
            "IT service management consultancy",
            "independent IT project and programme delivery",
            "IT service transformation consultant",
            "IT operations optimization for business",
            "IT delivery partner",
        ),
        theme_colour_primary="#048cc1",
        theme_colour_secondary="#92969b",
        site_url=_SITE_URL,
        favicon_png_sizes={96},
        stylesheets_extend=(
            h.link(
                rel="preload",
                href="/static/fonts/poppins-v24-latin-700.woff2",
                as_="font",
                crossorigin="anonymous",
            ),
            h.link(
                rel="preload",
                href="/static/fonts/poppins-v24-latin-regular.woff2",
                as_="font",
                crossorigin="anonymous",
            ),
            h.link(
                rel="preload",
                href="/static/fonts/poppins-v24-latin-italic.woff2",
                as_="font",
                crossorigin="anonymous",
            ),
            h.link(
                rel="preload",
                href="/static/fonts/poppins-v24-latin-700italic.woff2",
                as_="font",
                crossorigin="anonymous",
            ),
            h.link(rel="preload", href="/static/images/Consultancy_0.png", as_="image"),
            h.link(rel="preload", href="/static/images/Consultancy_1.png", as_="image"),
        ),
        extra_head=(
            h.script(id="vike_globalContext", type="application/json")["{}"],
            h.script(src="/static/js/entry-server-routing.js", type="module", async_=True),
            h.link(
                rel="modulepreload",
                href="/static/js/pages_index.js",
                as_="script",
                type="text/javascript",
            ),
        ),
    )
}
