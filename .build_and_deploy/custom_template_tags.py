""""""

from collections.abc import Sequence

__all__: Sequence[str] = ("html5up_copyright_comment",)

from django import template
from django.utils import safestring

register: template.Library = template.Library()


@register.simple_tag
def html5up_copyright_comment() -> str:
    return safestring.mark_safe(
        "<!--\n"
        "    Spectral by HTML5 UP\n"
        "    html5up.net | @ajlkn\n"
        "    Free for personal and commercial use under the CCA 3.0 license "
        "(html5up.net/license)\n"
        "-->"
    )
