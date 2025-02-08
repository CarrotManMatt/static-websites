""""""

from typing import TYPE_CHECKING

from . import car_points, carrotmanmatt_com

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence
    from pathlib import PurePosixPath
    from typing import Final

    import htpy as h

__all__: "Sequence[str]" = ("SITES_MAP",)

SITES_MAP: "Final[Mapping[str, Mapping[PurePosixPath, h.Element]]]" = {
    "car-points": car_points.PAGES_MAP,
    "carrotmanmatt.com": carrotmanmatt_com.PAGES_MAP,
}
