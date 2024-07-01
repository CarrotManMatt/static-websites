""""""

from collections.abc import Sequence

__all__: Sequence[str] = (
    "build_single_page",
    "build_single_site",
    "build_all_sites",
)

from pathlib import Path
from typing import Final

from django.conf import settings

from ..utils import PROJECT_ROOT

settings.configure(
    TEMPLATES={
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [PROJECT_ROOT],
        "APP_DIRS": False,
        "OPTIONS": {
            "libraries": {
                "copyright_comments": ".custom_template_tags",
            }
        },
    }
)

import django
django.setup()

from django.template.loader import render_to_string


def build_single_page(*, html_file_path: Path) -> None:
    """Render a single HTML page into a string output."""
    if not html_file_path.is_file() or html_file_path.suffix != ".html":
        INVALID_FILE_PATH_MESSAGE: Final[str] = (
            "Provided file path does not refer to a valid HTML file."
        )
        raise ValueError(INVALID_FILE_PATH_MESSAGE)

    print(render_to_string(html_file_path))


def build_single_site(*, site_root_directory: Path) -> None:
    """Render a single site's HTML pages into string outputs."""
    html_file_path: Path
    for html_file_path in site_root_directory.rglob("*.html"):
        if (site_root_directory / "static") in html_file_path.parents:
            continue

        build_single_page(html_file_path=html_file_path)


def build_all_sites() -> None:
    """Render all sites HTML pages into string outputs."""
    site_subdirectory: Path
    for site_subdirectory in PROJECT_ROOT.iterdir():
        if not site_subdirectory.is_dir() or site_subdirectory.stem.startswith("."):
            continue

        build_single_site(site_root_directory=site_subdirectory)

    # 1. Glob through all files
    # 2. Check if contains HTML5up Copyright
    # 3. Django render
    # 4. Minify
    # 5. Add copyright if needed
    # 6. output to stdout


if __name__ == "__main__":
    build_all_sites()
