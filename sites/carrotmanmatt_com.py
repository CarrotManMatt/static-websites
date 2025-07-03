"""carrotmanmatt.com static site definition."""

from pathlib import PurePosixPath
from typing import TYPE_CHECKING

import htpy as h
from markupsafe import Markup

from components import component_base, component_icons_list, component_site_copyright

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence
    from typing import Final


__all__: "Sequence[str]" = ("PAGES_MAP",)

PAGES_MAP: "Final[Mapping[PurePosixPath, h.HTMLElement]]" = {
    PurePosixPath("index.html"): component_base(
        copyright_comment=h.comment(
            "Spectral by HTML5 UP | "
            "html5up.net - @ajlkn | "
            "Free for personal and commercial use under the CCA 3.0 license "
            "(html5up.net/license)"
        ),
        page_meta_image="https://carrotmanmatt.com/static/carrot_icon.png",
        page_content_type="profile",
        stylesheets_extend=h.noscript[
            h.link(rel="stylesheet", href="/static/css/noscript.css")
        ],
        body=h.body(class_=("landing", "is-preload"))[
            h.div(id="page-wrapper")[
                h.header(id="header", class_=("alt",))[
                    h.h1[h.a(href="")["CarrotManMatt.com"]]
                ],
                h.section(id="banner")[
                    h.div(class_=("inner",))[
                        h.h2(style="text-shadow: 2px 2px #1c1001")["Carrot Man Matt"],
                        h.ul(
                            class_=("icons",),
                            style="font-size: 20px; text-shadow: 2px 2px #1c1001",
                        )[component_icons_list()],
                        h.img(
                            src="/static/images/Avatar.png",
                            alt="Smiling carrot avatar",
                            width="100%",
                            height="auto",
                            style="width: 170px; padding-top: 25px; shadow: 2px 2px #1c1001",
                        ),
                    ],
                    h.a(
                        href="#one",
                        class_=("more", "scrolly"),
                        style="text-shadow: 2px 2px #1c1001",
                    )["Learn More"],
                ],
                h.section(id="one", class_=("wrapper", "style1", "special"))[
                    h.div(class_=("inner",))[
                        h.header(class_=("major",))[
                            h.h2["About Me"],
                            h.p[
                                "I'm CarrotManMatt, it's great to see you.",
                                h.br,
                                (
                                    "Welcome to my small corner of the internet (hosted on an "
                                    "old office PC), so feel free to look around!"
                                ),
                            ],
                        ],
                        h.span(class_=("icon", "solid", "fa-carrot", "major"))[
                            h.span(class_=("label",))["Carrot"]
                        ],
                    ]
                ],
                h.section(id="two", class_=("wrapper", "alt", "style2"))[
                    h.section(class_=("spotlight",))[
                        h.div(class_=("image",))[
                            h.img(
                                src="/static/images/pic01.png",
                                width="100%",
                                height="100%",
                                alt=(
                                    "Woman leaning against a counter, eating a bowl of salad. "
                                    "A plastic bottle of water and a bowl of apples are on "
                                    "the counter."
                                ),
                            )
                        ],
                        h.div(class_=("content",))[
                            h.h2["What is CarrotManMatt?"],
                            h.p[
                                (
                                    "That's me! "
                                    "Veggies are great, and the colour orange is one of the "
                                    "best. "
                                    "So what better brand to choose than the food that makes "
                                    "you see in the dark?"
                                )
                            ],
                        ],
                    ],
                    h.section(class_=("spotlight",))[
                        h.div(class_=("image",))[
                            h.img(
                                src="/static/images/pic02.png",
                                width="100%",
                                height="100%",
                                alt=(
                                    "Three people sat on stools around a table in a cafe, "
                                    "talking and eating cake, sandwiches & pastries."
                                ),
                            )
                        ],
                        h.div(class_=("content",))[
                            h.h2(style="font-size: 18px")[
                                "Communicate | Contemplate | Appreciate"
                            ],
                            h.p[
                                (
                                    "These are the three words I strive to live by. "
                                    "I think it's a simple way for us all to act to the "
                                    "benefit of others"
                                ),
                                h.br,
                                h.br,
                                (
                                    "• Communicate - "
                                    "Talking clearly to others is imperative for "
                                    "understanding and will quickly solve many issues."
                                    "Try to truly listen to others rather than just talking "
                                    "at them"
                                ),
                                h.br,
                                h.br,
                                (
                                    "• Contemplate - "
                                    "Always take time to reflect on yourself, how you are "
                                    "acting and the situation you are in. "
                                    'It\'s certainly a bit "meta", but I think self-awareness '
                                    "is the key to ensuring we all act sensibly and kindly"
                                ),
                                h.br,
                                h.br,
                                (
                                    "• Appreciate - "
                                    "I know it's rather vague, but it involves many things. "
                                    'Try to understand the additional "baggage" others may be '
                                    "carrying, always assume the best in people and show "
                                    "explicit kindness and care to everyone"
                                ),
                            ],
                        ],
                    ],
                    h.section(class_=("spotlight",))[
                        h.div(class_=("image",))[
                            h.img(
                                src="/static/images/pic03.png",
                                width="100%",
                                height="100%",
                                alt=(
                                    "Two people practising a theatre dialogue script in front "
                                    "of a white background, with two rows of theatre lights "
                                    "behind them."
                                ),
                            )
                        ],
                        h.div(class_=("content",))[
                            h.h2["The Little Things"],
                            h.p[
                                (
                                    "I'm quite extroverted and often take a leadership role "
                                    "in group activities, but I am excellent at finding the "
                                    "balance between focusing on the details and seeing the "
                                    "bigger picture. "
                                    "I always strive for perfection in my work (even with the "
                                    "understanding that it can never be met), and hope that "
                                    "my interactions with others help them to also reach for "
                                    "a high standard"
                                )
                            ],
                        ],
                    ],
                ],
                h.section(id="three", class_=("wrapper", "style3", "special"))[
                    h.div(class_=("inner",))[
                        h.header(class_=("major",))[
                            h.h2["Hobbies & Interests"],
                            h.p[
                                (
                                    "I'm grateful to have had the opportunity to try an "
                                    "astonishing range of activities. "
                                    "Below are a few of the key ones that really stuck with "
                                    "me."
                                ),
                                h.br,
                                (
                                    "You can probably tell that there's a theme between them "
                                    "all; "
                                    "I guess these all stem from my love for technology and "
                                    "learning"
                                ),
                            ],
                        ],
                        h.ul(class_=("features",))[
                            h.li(class_=("icon", "solid", "fa-laptop-code"))[
                                h.h3["Coding"],
                                h.p[
                                    (
                                        "As you can see from this website and my hosting of "
                                        "it, I really enjoy improving my productivity and "
                                        "simplifying my life through technology. "
                                        "Programming can help you become a master at anything!"
                                    )
                                ],
                            ],
                            h.li(class_=("icon", "solid", "fa-guitar"))[
                                h.h3["Playing Guitar"],
                                h.p[
                                    (
                                        "I love music and the way it can bring people "
                                        "together; it's when performing for others that I "
                                        "feel at my best. "
                                        "I've been playing since I was six and have even had "
                                        "a bit of a crack at karaoke recently"
                                    )
                                ],
                            ],
                            h.li(class_=("icon", "solid", "fa-lightbulb"))[
                                h.h3["Live Events Technology"],
                                h.p[
                                    (
                                        "Putting on a great show can't be beat. "
                                        "Even from more of a backstage role, the connection "
                                        "between performers and their audience is often "
                                        "palpable. "
                                        "Aiding in that process (whether it be in the wings, "
                                        "at the lighting desk or on the sound board) is "
                                        "always a rewarding experience"
                                    )
                                ],
                            ],
                            h.li(class_=("icon", "solid", "fa-video"))[
                                h.h3["Video Production"],
                                h.p[
                                    (
                                        "Both presenting and editing videos are useful skills "
                                        "for me to take into the workplace, even if my "
                                        "infrequent dabbling with it is for smaller passion "
                                        "projects."
                                        "It's great fun to see a simple idea turn into a "
                                        "piece of quality content, especially when shared "
                                        "with others after completion"
                                    )
                                ],
                            ],
                            h.li(class_=("icon", "solid", "fa-city"))[
                                h.h3["The UK"],
                                h.p[
                                    (
                                        "My home country is something I am both proud and in "
                                        "awe of. "
                                        "I love to explore all it has to offer from the "
                                        "bustling London Underground; to the smallest of "
                                        "picturesque villages, there's nowhere like here on "
                                        "earth. "
                                        "I'm constantly surprised by the people, culture and "
                                        "architecture that can easily be found not too far "
                                        "away"
                                    )
                                ],
                            ],
                            h.li(class_=("icon", "solid", "fa-microscope"))[
                                h.h3["Maths & Science"],
                                h.p[
                                    (
                                        "I have a passion for exploring complex maths and "
                                        "physics at a level of detail that few do. "
                                        "I admit, I fell in love with the logical deduction "
                                        "and problem-solving involved. Mixed with my constant "
                                        "intake of educational YouTube content, I don't think "
                                        "I'll ever want to stop my journey of discovery into "
                                        "the building blocks of our world"
                                    )
                                ],
                            ],
                        ],
                    ]
                ],
                h.footer(id="footer")[
                    h.ul(class_=("icons",))[component_icons_list()],
                    h.ul(class_=("copyright",))[
                        h.li[
                            component_site_copyright(
                                styles="border: none",
                                extra_tags=h.span(
                                    class_=("icon", "solid", "fa-carrot"),
                                    style="margin-left: 7px",
                                ),
                            )
                        ],
                        h.li(id="css-sponsorship")[
                            "Sponsored by: ",
                            h.a(href="https://cssbham.com")[Markup("UoB&nbsp;CSS")],
                        ],
                        h.li[
                            "Design: ",
                            h.a(href="https://html5up.net")[Markup("HTML5&nbsp;UP")],
                        ],
                        h.li["Illustrations: ", h.a(href="https://storyset.com")["Storyset"]],
                    ],
                ],
            ],
            h.script(src="/static/js/jquery.min.js"),
            h.script(src="/static/js/jquery.scrollex.min.js"),
            h.script(src="/static/js/jquery.scrolly.min.js"),
            h.script(src="/static/js/browser.min.js"),
            h.script(src="/static/js/breakpoints.min.js"),
            h.script(src="/static/js/util.js"),
            h.script(src="/static/js/main.js"),
        ],
        after_body=h.style(id="custom-page-zoom-css"),
    ),
}
