""""""

from typing import TYPE_CHECKING

import htpy as h

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence
    from typing import Final


__all__: "Sequence[str]" = ("PAGES_MAP",)

PAGES_MAP: "Final[Mapping[str, h.Element]]" = {
    "index.html": h.html,
}
