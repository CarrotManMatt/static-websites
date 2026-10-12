"""Overall static site pages definition map."""

__all__: Sequence[str] = ("SITES_MAP",)

lazy from collections.abc import Mapping, Sequence
lazy from pathlib import PurePosixPath
lazy from typing import Final

lazy import htpy as h

from . import car_points, carrotmanmatt_com, infratek, olympic_show_uk

SITES_MAP: Final[Mapping[str, Mapping[PurePosixPath, h.HTMLElement]]] = frozendict(
    {
        "car-points": car_points.PAGES_MAP,
        "carrotmanmatt.com": carrotmanmatt_com.PAGES_MAP,
        "olympic-show": olympic_show_uk.PAGES_MAP,
        "infratek": infratek.PAGES_MAP,
    }
)
