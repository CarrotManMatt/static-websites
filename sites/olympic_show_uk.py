"""olympic-show.uk static site definition."""

from pathlib import PurePosixPath
from typing import TYPE_CHECKING

import htpy as h
from markupsafe import Markup

from components import component_base

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence
    from typing import Final


__all__: Sequence[str] = ("PAGES_MAP",)


_show_description: str = Markup(
    "Step&nbsp;back&nbsp;in&nbsp;time aboard&nbsp;The&nbsp;Olympic, "
    "to&nbsp;discover heroism&nbsp;and&nbsp;heartbreak."
)
_show_dates: str = Markup(
    "Show&nbsp;dates: 19th,&nbsp;20th&nbsp;&amp;&nbsp;21st&nbsp;June&nbsp;2026 "
    "Doors&nbsp;-&nbsp;7pm,&nbsp;Show&nbsp;-&nbsp;7:30pm "
    "Amos&nbsp;Room&nbsp;@&nbsp;University&nbsp;of&nbsp;Birmingham Guild&nbsp;of&nbsp;Students"
)
_site_description: str = Markup("{}\n{}").format(_show_description, _show_dates)
_site_title: str = Markup("Olympic - 3BUGS Fringe")
_logo_location: str = "/static/images/Logo.png"
_site_url: str = "https://olympic-show.uk"


PAGES_MAP: Final[Mapping[PurePosixPath, h.HTMLElement]] = {
    PurePosixPath("index.html"): component_base(
        body=h.body(
            class_=(
                "w-element ccp4ayz c1bzhbzh c1302fnh c1ajrpif c1fjw25m c15vmzu4 c1mdww5 "
                "c171p6yf c16ys4xd c18sjf55"
            )
        )[
            h.div(
                class_=(
                    "w-element c15vmzu4 c1mdww5 cu52st3 c171p6yf ca9ya4b c1v5aa9w c8mdnw5 "
                    "c18kgj1i ca3r2u7 ck5ipzl cgb3bj"
                )
            )[
                h.div(
                    class_=(
                        "w-element c1fjw25m ccpzds6 cur4pzc c171p6yf celrdu8 cz48kyy cmyd10q "
                        "ckeo1df c15vmzu4 c14m3ca4 cmcx9xc c16bjgbz c1fa8gcm"
                    )
                )[
                    h.img(
                        alt=(
                            "Olympic 3BUGS show logo; "
                            "Black and white illustration of a steam ocean-liner "
                            "inside a turquoise circle."
                        ),
                        width="917",
                        height="917",
                        src=_logo_location,
                        class_="w-image cgb3bj cd086ag c1grhjej",
                        sizes="100vw",
                        srcset=(
                            f"{_logo_location} 16w, {_logo_location} 32w, "
                            f"{_logo_location} 48w, {_logo_location} 64w, "
                            f"{_logo_location} 96w, {_logo_location} 128w, "
                            f"{_logo_location} 256w, {_logo_location} 384w, "
                            f"{_logo_location} 640w, {_logo_location} 750w, "
                            f"{_logo_location} 828w, {_logo_location} 1080w, "
                            f"{_logo_location} 1200w, {_logo_location} 1920w"
                        ),
                        decoding="async",
                        loading="lazy",
                    ),
                    h.h1(
                        class_=(
                            "w-element ca4u039 ckr079c cmvx7u0 c19yn05d cj9275l ctk8l4v "
                            "c1756ujc cpl9jjd"
                        )
                    )["Olympic"],
                    h.p(
                        class_=(
                            "w-element ckr079c ca4u039 c1b5291m c1bleucc c18ygeq2 cz0qqdo "
                            "c1p7rcrf c1ozzal9"
                        )
                    )[_show_description],
                    h.p(
                        class_=(
                            "w-element ckr079c ca4u039 c19102et c1bleucc c9895ho c622mpl "
                            "cz0qqdo c1p7rcrf c1tgzf95"
                        )
                    )[_show_dates],
                    h.ul(
                        class_=(
                            "w-element c1n5tuq8 c1fjw25m cnzpwoq crpyobo c15vmzu4 c1idw5j2 "
                            "c1rwodom c12n57os cli8a60 cgtv1h1 c168ej5r c1xruc57"
                        )
                    )[
                        h.li(
                            class_=(
                                "w-element cu52st3 caaqcxl c18y1yfe c1uom0t8 c1b3o6vr cc1a8ib "
                                "cryncd3 cd3i0tr c21ee66 c1l6ehxo cbvcuo2 c69pgid c79tq8k "
                                "c1gh997e"
                            )
                        )[
                            h.a(
                                href="/script",
                                class_=(
                                    "w-element c19y3cjm c1lglyie c14wber8 cwfy5au cusinh7 "
                                    "c1hya6s0 cq6mi0e c15vmzu4 c1idw5j2 crpyobo c1u759pa "
                                    "c1gm7vb"
                                ),
                            )[
                                h.span(class_="w-element ca4u039 cj9275l")["Script"],
                                h.svg(
                                    xmlns="http://www.w3.org/2000/svg",
                                    viewbox="0 0 640 640",
                                    class_="w-element czzn447",
                                )[
                                    h.path(
                                        fill="rgb(255, 255, 255)",
                                        d=(
                                            "M32 176C32 134.5 63.6 100.4 104 96.4L104 96L384 "
                                            "96C437 96 480 139 480 192L480 368L304 368C264.2 "
                                            "368 232 400.2 232 440L232 500C232 524.3 212.3 "
                                            "544 188 544C163.7 544 144 524.3 144 500L144 "
                                            "272L80 272C53.5 272 32 250.5 32 224L32 "
                                            "176zM268.8 544C275.9 530.9 280 515.9 280 500L280 "
                                            "440C280 426.7 290.7 416 304 416L552 416C565.3 "
                                            "416 576 426.7 576 440L576 464C576 508.2 540.2 "
                                            "544 496 544L268.8 544zM112 144C94.3 144 80 158.3 "
                                            "80 176L80 224L144 224L144 176C144 158.3 129.7 "
                                            "144 112 144z"
                                        ),
                                        class_="w-element",
                                    )
                                ],
                            ]
                        ],
                        h.li(
                            class_=(
                                "w-element cu52st3 caaqcxl c18y1yfe c1uom0t8 c1b3o6vr cc1a8ib "
                                "cryncd3 cd3i0tr c21ee66 c1l6ehxo cbvcuo2 c69pgid c79tq8k "
                                "c1gh997e"
                            )
                        )[
                            h.a(
                                href="/reserve-ticket",
                                class_=(
                                    "w-element c19y3cjm c1lglyie c14wber8 c1hya6s0 cvp7t4m "
                                    "cwfy5au cusinh7 c15vmzu4 c1idw5j2 crpyobo c1u759pa "
                                    "c1gm7vb"
                                ),
                            )[
                                h.span(class_="w-element ca4u039 cryncd3 cj9275l")[
                                    "Ticket Reservation Form"
                                ],
                                h.svg(
                                    xmlns="http://www.w3.org/2000/svg",
                                    viewbox="0 0 640 640",
                                    class_="w-element czzn447",
                                )[
                                    h.path(
                                        fill="rgb(255, 255, 255)",
                                        d=(
                                            "M96 128C60.7 128 32 156.7 32 192L32 256C32 264.8 "
                                            "39.4 271.7 47.7 274.6C66.5 281.1 80 299 80 "
                                            "320C80 341 66.5 358.9 47.7 365.4C39.4 368.3 32 "
                                            "375.2 32 384L32 448C32 483.3 60.7 512 96 512L544 "
                                            "512C579.3 512 608 483.3 608 448L608 384C608 "
                                            "375.2 600.6 368.3 592.3 365.4C573.5 358.9 560 "
                                            "341 560 320C560 299 573.5 281.1 592.3 "
                                            "274.6C600.6 271.7 608 264.8 608 256L608 192C608 "
                                            "156.7 579.3 128 544 128L96 128zM448 400L448 "
                                            "240L192 240L192 400L448 400zM144 224C144 206.3 "
                                            "158.3 192 176 192L464 192C481.7 192 496 206.3 "
                                            "496 224L496 416C496 433.7 481.7 448 464 448L176 "
                                            "448C158.3 448 144 433.7 144 416L144 224z"
                                        ),
                                        class_="w-element",
                                    )
                                ],
                            ]
                        ],
                    ],
                    h.div(data_ws_subject_for="_Rcm_", class_="w-video-animation")[
                        h.video(
                            src="/trailer",
                            preload="auto",
                            muted="",
                            playsinline="",
                            crossorigin="anonymous",
                            controls="",
                            class_="w-video",
                            data_ws_video_id=":R9sm:",
                        )
                    ],
                    h.style[
                        "#_Rcm_ {\n"
                        "    position: fixed;\n"
                        "    visibility: hidden;\n"
                        "    pointer-events: none;\n"
                        "    top: -10000px;\n"
                        "    right: 10000px;\n"
                        "    contain: strict;\n"
                        "}\n\n"
                        "#_Rcm_-sample {\n"
                        "    position: fixed;\n"
                        "    visibility: hidden;\n"
                        "    pointer-events: none;\n"
                        "    top: -9000px;\n"
                        "    right: 9000px;\n"
                        "    willchange: translate, scale, opacity;\n"
                        "    contain: strict;\n"
                        "}"
                    ],
                    h.div(id="_Rcm_", inert="true", data_ws_no_initial_animation=""),
                    h.div(id="_Rcm_-sample", inert="true", data_ws_no_initial_animation=""),
                    h.p(
                        class_=(
                            "w-element ckr079c ca4u039 c1b5291m c1bleucc c18ygeq2 cz0qqdo "
                            "c1p7rcrf c1ozzal9"
                        )
                    )[" VIP Tickets also available!"],
                ],
                h.div(
                    class_=(
                        "w-element cu52st3 crpyobo c15vmzu4 c1idw5j2 c1wn952 c1vkag4l cqwcqsc "
                        "cdo4qik cojcney cps8nlr cfhahb3 ckeo1df"
                    )
                )[
                    h.ul(
                        class_=(
                            "w-element c1fjw25m crpyobo c15vmzu4 c1idw5j2 c1n5tuq8 c1hqmyru "
                            "c5nxebr cli8a60 c1ea5oib cfn7izm"
                        )
                    )[
                        h.li(
                            title="3BUGS Instagram",
                            class_=(
                                "w-element c9qatxj cu52st3 c1wycskj c1b6fejg chod0up c15sgzwk "
                                "c1jya48a c1lfbz0f cr4uoqw c5ak6ng cutr2ab c1fy5onp c1tl8ptz "
                                "c8bvo9r c1jv23ot css9i3k c1p33r1k"
                            ),
                        )[
                            h.a(
                                href="https://instagram.com/3bugsfringe",
                                class_="w-element cvcfi7n",
                            )[
                                h.svg(
                                    xmlns="http://www.w3.org/2000/svg",
                                    viewbox="0 0 640 640",
                                    class_="w-element ck5ipzl",
                                )[
                                    h.path(
                                        d=(
                                            "M320.3 205C256.8 204.8 205.2 256.2 205 "
                                            "319.7C204.8 383.2 256.2 434.8 319.7 435C383.2 "
                                            "435.2 434.8 383.8 435 320.3C435.2 256.8 383.8 "
                                            "205.2 320.3 205zM319.7 245.4C360.9 245.2 394.4 "
                                            "278.5 394.6 319.7C394.8 360.9 361.5 394.4 320.3 "
                                            "394.6C279.1 394.8 245.6 361.5 245.4 320.3C245.2 "
                                            "279.1 278.5 245.6 319.7 245.4zM413.1 200.3C413.1 "
                                            "185.5 425.1 173.5 439.9 173.5C454.7 173.5 466.7 "
                                            "185.5 466.7 200.3C466.7 215.1 454.7 227.1 439.9 "
                                            "227.1C425.1 227.1 413.1 215.1 413.1 200.3zM542.8 "
                                            "227.5C541.1 191.6 532.9 159.8 506.6 133.6C480.4 "
                                            "107.4 448.6 99.2 412.7 97.4C375.7 95.3 264.8 "
                                            "95.3 227.8 97.4C192 99.1 160.2 107.3 133.9 "
                                            "133.5C107.6 159.7 99.5 191.5 97.7 227.4C95.6 "
                                            "264.4 95.6 375.3 97.7 412.3C99.4 448.2 107.6 480 "
                                            "133.9 506.2C160.2 532.4 191.9 540.6 227.8 "
                                            "542.4C264.8 544.5 375.7 544.5 412.7 542.4C448.6 "
                                            "540.7 480.4 532.5 506.6 506.2C532.8 480 541 "
                                            "448.2 542.8 412.3C544.9 375.3 544.9 264.5 542.8 "
                                            "227.5zM495 452C487.2 471.6 472.1 486.7 452.4 "
                                            "494.6C422.9 506.3 352.9 503.6 320.3 503.6C287.7 "
                                            "503.6 217.6 506.2 188.2 494.6C168.6 486.8 153.5 "
                                            "471.7 145.6 452C133.9 422.5 136.6 352.5 136.6 "
                                            "319.9C136.6 287.3 134 217.2 145.6 187.8C153.4 "
                                            "168.2 168.5 153.1 188.2 145.2C217.7 133.5 287.7 "
                                            "136.2 320.3 136.2C352.9 136.2 423 133.6 452.4 "
                                            "145.2C472 153 487.1 168.1 495 187.8C506.7 217.3 "
                                            "504 287.3 504 319.9C504 352.5 506.7 422.6 495 "
                                            "452z"
                                        ),
                                        class_="w-element",
                                    )
                                ]
                            ]
                        ],
                        h.li(
                            title="Contact Us",
                            class_=(
                                "w-element c9qatxj cu52st3 c1wycskj c1b6fejg chod0up c15sgzwk "
                                "c1jya48a c1lfbz0f cr4uoqw c5ak6ng cutr2ab c1fy5onp c1tl8ptz "
                                "c8bvo9r css9i3k c1p33r1k c1jv23ot"
                            ),
                        )[
                            h.a(
                                href="mailto:info@olympic-show.uk", class_="w-element cvcfi7n"
                            )[
                                h.svg(
                                    xmlns="http://www.w3.org/2000/svg",
                                    viewbox="0 0 640 640",
                                    class_="w-element ck5ipzl",
                                )[
                                    h.path(
                                        d=(
                                            "M125.4 128C91.5 128 64 155.5 64 189.4C64 190.3 "
                                            "64 191.1 64.1 192L64 192L64 448C64 483.3 92.7 "
                                            "512 128 512L512 512C547.3 512 576 483.3 576 "
                                            "448L576 192L575.9 192C575.9 191.1 576 190.3 576 "
                                            "189.4C576 155.5 548.5 128 514.6 128L125.4 "
                                            "128zM528 256.3L528 448C528 456.8 520.8 464 512 "
                                            "464L128 464C119.2 464 112 456.8 112 448L112 "
                                            "256.3L266.8 373.7C298.2 397.6 341.7 397.6 373.2 "
                                            "373.7L528 256.3zM112 189.4C112 182 118 176 125.4 "
                                            "176L514.6 176C522 176 528 182 528 189.4C528 "
                                            "193.6 526 197.6 522.7 200.1L344.2 335.5C329.9 "
                                            "346.3 310.1 346.3 295.8 335.5L117.3 200.1C114 "
                                            "197.6 112 193.6 112 189.4z"
                                        ),
                                        class_="w-element",
                                    )
                                ]
                            ]
                        ],
                    ]
                ],
                h.div(class_="w-element c1fjw25m c15vmzu4 c1mdww5 c171p6yf c1wb1hc0")[
                    h.a(
                        href="https://carrd.co/build?ref=auto",
                        class_=(
                            "w-element cghpq0g c1mo9yj1 c16woyi7 ccj2oyi ca4u039 c125plc1 "
                            "c14wber8 c1kkyd5p c1psmwq9 c1lkbx5o c1pmyxpu c1ygep9y c6tgne0 "
                            "crg0onb ckr079c c3g1jgn c15vmzu4 c1idw5j2 cu52st3 czx97jj "
                            "cl7gb7e cv10vxf c1ig1kb1 c1cghu3j cbaqv2z czrsdit cckfc4f "
                            "c1ecdpdd cpy0x0n c1rh1r8b"
                        ),
                    )["Designed by Carrd"]
                ],
            ],
            h.script(id="vike_pageContext", type="application/json")[
                '{"_urlRewrite":null,"pageId":"/pages/index","routeParams":{},"data":{'
                f'"url":"https://url/","system":{{"resources":{{}},"pageMeta":{{"title":"{
                    _site_title.strip('\n\r\t ",')
                }","description":"{
                    _site_description.strip('\n\r\t ",')
                }","excludePageFromSearch":"!undefined","language":"en-GB",'
                f'"socialImageAssetName":"!undefined","socialImageUrl":"{_site_url}{
                    _logo_location
                }","status":"!undefined","redirect":"!undefined","custom":[]}}}}}}'
            ],
            h.script(id="vike_globalContext", type="application/json")[" {}"],
            h.script(src="/static/js/entry-server-routing.js", type="module", async_=True),
            h.link(
                rel="modulepreload",
                href="/static/js/pages_index.js",
                as_="script",
                type="text/javascript",
            ),
        ],
        page_title=_site_title,
        page_description=_site_description,
        page_meta_image=f"{_site_url}{_logo_location}",
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
        theme_colour_primary="#b4d7d3",
        theme_colour_secondary="#99d1d3",
        site_url=_site_url,
        favicon_png_sizes={96},
        stylesheets_extend=(
            h.link(
                rel="preload",
                href="/static/fonts/Jost-VariableFont.woff2",
                as_="font",
                crossorigin="anonymous",
            ),
            h.link(rel="preload", href="/static/images/bg.png", as_="image"),
        ),
        extra_head=(
            h.script(type="application/ld+json")[
                f'{{"@context":"https://schema.org","@type":"WebSite","name":"{_site_title}"}}'
            ],
        ),
    )
}
