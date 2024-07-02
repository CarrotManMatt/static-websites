"""Build and render functions for whole sites and single HTML pages."""

from collections.abc import Sequence

__all__: Sequence[str] = (
    "build_single_page",
    "build_single_site",
    "build_all_sites",
)


import re
import shutil
from pathlib import Path
from typing import Final

import minify_html
from django.template import Context as TemplateContext
from django.template import Template
from django.template.engine import Engine as TemplateEngine

from utils import PROJECT_ROOT

TEMPLATE_ENGINE: Final[TemplateEngine] = TemplateEngine(
    dirs=[str(PROJECT_ROOT)],
    app_dirs=False,
    libraries={
        "simple_dates": "custom_template_tags.simple_dates",
        "icons_list": "custom_template_tags.icons_list",
    },
)


def build_single_page(*, html_file_path: Path) -> str:
    """Render a single HTML page into a string output."""
    if not html_file_path.is_file() or html_file_path.suffix != ".html":
        INVALID_FILE_PATH_MESSAGE: Final[str] = (
            "Provided file path does not refer to a valid HTML file."
        )
        raise ValueError(INVALID_FILE_PATH_MESSAGE)

    template: Template = TEMPLATE_ENGINE.get_template(str(html_file_path))

    copyright_comment_match: re.Match[str] | None = re.search(
        r"{# ?COPYRIGHT_COMMENT \"(?P<copyright_type>[A-Za-z0-9 +!?'£$^&*\-_=@;:~.,¬]+)\" ?#}",
        template.source,
    )

    minified_html: str = minify_html.minify(
        template.render(TemplateContext()),
        do_not_minify_doctype=True,
        keep_html_and_head_opening_tags=True,
        ensure_spec_compliant_unquoted_attribute_values=True,
        keep_spaces_between_attributes=True,
        minify_js=True,
        minify_css=True,
        keep_comments=False,
    ).replace("<!doctype html>", "<!DOCTYPE HTML>")

    if copyright_comment_match:
        copyright_comment_type: str = copyright_comment_match.group("copyright_type")

        if copyright_comment_type == "HTML5 UP":
            minified_html = minified_html.replace(
                "<!DOCTYPE HTML>",
                (
                    "<!DOCTYPE HTML>\n"
                    "<!--\n"
                    "    Spectral by HTML5 UP\n"
                    "    html5up.net | @ajlkn\n"
                    "    Free for personal and commercial use under the CCA 3.0 license "
                    "(html5up.net/license)\n"
                    "-->\n"
                ),
            )
        else:
            UNKNOWN_COPYRIGHT_COMMENT_TYPE_MESSAGE: Final[str] = (
                f"Unknown copyright comment type: {copyright_comment_type}"
            )
            raise NotImplementedError(UNKNOWN_COPYRIGHT_COMMENT_TYPE_MESSAGE)

    return minified_html


def build_single_site(*, site_root_directory: Path) -> None:
    """Render a single site's HTML pages into string outputs."""
    deploy_dir: Path = site_root_directory / "deploy"
    if deploy_dir.exists():
        shutil.rmtree(deploy_dir)
    deploy_dir.mkdir()

    static_dir: Path = site_root_directory / "static"
    if static_dir.is_dir():
        (deploy_dir / "static").symlink_to(static_dir, target_is_directory=True)

    html_file_path: Path
    for html_file_path in site_root_directory.rglob("*.html"):
        if (site_root_directory / "static") in html_file_path.parents:
            continue

        if (site_root_directory / "deploy") in html_file_path.parents:
            continue

        new_html_file_location: Path = (
            deploy_dir / html_file_path.relative_to(site_root_directory)
        )

        new_html_file_location.parent.mkdir(parents=True, exist_ok=True)

        new_html_file_location.write_text(
            build_single_page(html_file_path=html_file_path),
            encoding="utf-8",
        )


def build_all_sites() -> None:
    """Render all sites HTML pages into string outputs."""
    site_subdirectory: Path
    for site_subdirectory in PROJECT_ROOT.iterdir():
        if not site_subdirectory.is_dir() or site_subdirectory.stem.startswith("."):
            continue

        build_single_site(site_root_directory=site_subdirectory)


if __name__ == "__main__":
    build_all_sites()
