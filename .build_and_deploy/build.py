"""Build and render functions for whole sites and single HTML pages."""

from collections.abc import Sequence

__all__: Sequence[str] = (
    "build_single_page",
    "build_single_site",
    "build_all_sites",
)


import logging
import re
import shutil
import traceback
from collections.abc import Set
from logging import Logger
from pathlib import Path
from subprocess import CalledProcessError
from typing import Final

import minify_html
from django.template import Context as TemplateContext
from django.template import Template
from django.template.engine import Engine as TemplateEngine

from utils import PROJECT_ROOT, CaughtException

logger: Final[Logger] = logging.getLogger("static-website-builder")

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
    FORMATTED_HTML_FILE_PATH: Final[str] = html_file_path.relative_to(PROJECT_ROOT).as_posix()

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

    if copyright_comment_match:
        logger.debug(
            (
                f"({FORMATTED_HTML_FILE_PATH}) "
                "Found copyright-comment that will later be re-added: "
                f"{copyright_comment_match.group("copyright_type")}"
            ),
        )

    rendered_template: str = template.render(TemplateContext())

    logger.debug(f"({FORMATTED_HTML_FILE_PATH}) Django template successfully rendered.")

    minified_html: str = minify_html.minify(
        rendered_template,
        do_not_minify_doctype=True,
        keep_html_and_head_opening_tags=True,
        ensure_spec_compliant_unquoted_attribute_values=True,
        keep_spaces_between_attributes=True,
        minify_js=True,
        minify_css=True,
        keep_comments=False,
    )

    minified_html = minified_html.replace("<!doctype html>", "<!DOCTYPE HTML>")

    logger.debug(f"({FORMATTED_HTML_FILE_PATH}) HTML file successfully minified.")

    if re.search(r">\s+", minified_html):
        logger.warning(
            (
                f"({FORMATTED_HTML_FILE_PATH}) Found whitespace after HTML tag. "
                "Make sure to check validity of rendered output."
            ),
        )
        minified_html = re.sub(r">\s+", ">", minified_html)

    if re.search(r"\s+<", minified_html):
        logger.warning(
            (
                f"({FORMATTED_HTML_FILE_PATH}) Found whitespace before HTML tag. "
                "Make sure to check validity of rendered output."
            ),
        )
        minified_html = re.sub(r"\s+<", "<", minified_html)

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

        logger.debug(
            (
                f"({FORMATTED_HTML_FILE_PATH}) "
                f"Copyright-comment successfully re-added: {copyright_comment_type}"
            ),
        )

    return minified_html


def build_single_site(*, site_root_directory: Path) -> None:
    """Render a single site's HTML pages into string outputs."""
    FORMATTED_SITE_NAME: Final[str] = (
        site_root_directory.parent.name
        if site_root_directory.name == "deploy"
        else site_root_directory.name
    )

    logger.debug(f"({FORMATTED_SITE_NAME}) Begin building single site.")

    if not site_root_directory.is_dir():
        PATH_IS_NOT_DIRECTORY_MESSAGE: Final[str] = (
            f"Path to site's root directory is not a directory: {site_root_directory}"
        )
        raise ValueError(PATH_IS_NOT_DIRECTORY_MESSAGE)

    logger.debug(f"({FORMATTED_SITE_NAME}) Creating `deploy/` directory.")

    deploy_dir: Path = site_root_directory / "deploy"
    if deploy_dir.exists():
        shutil.rmtree(deploy_dir)
    deploy_dir.mkdir()

    logger.debug(
        (
            f"({FORMATTED_SITE_NAME}) "
            "Creating symlink to original static directory from inside `deploy/` directory."
        ),
    )

    static_dir: Path = site_root_directory / "static"
    if static_dir.is_dir():
        (deploy_dir / "static").symlink_to(static_dir, target_is_directory=True)

    html_file_path: Path
    for html_file_path in site_root_directory.rglob("*.html"):
        FORMATTED_HTML_FILE_PATH: str = html_file_path.relative_to(PROJECT_ROOT).as_posix()

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

        logger.debug(
            (
                f"({FORMATTED_HTML_FILE_PATH}) "
                "Rendered HTML file successfully saved to `deploy/` directory."
            ),
        )

    logger.debug(f"({FORMATTED_SITE_NAME}) Completed building single site successfully.")


def build_all_sites() -> Set[Path]:
    """Render all sites HTML pages into string outputs."""
    logger.debug("Begin building all sites.")

    built_sites: dict[Path, CaughtException | None] = {}

    site_subdirectory: Path
    for site_subdirectory in PROJECT_ROOT.iterdir():
        if not site_subdirectory.is_dir() or site_subdirectory.stem.startswith("."):
            continue

        caught_exception: CaughtException
        try:
            build_single_site(site_root_directory=site_subdirectory)
        except (ValueError, RuntimeError, AttributeError, TypeError, OSError, CalledProcessError) as caught_exception:  # noqa: E501
            built_sites[site_subdirectory / "deploy"] = caught_exception
            continue
        else:
            built_sites[site_subdirectory / "deploy"] = None

    site_path: Path
    build_outcome: CaughtException | None
    for site_path, build_outcome in built_sites.items():
        FORMATTED_SITE_NAME: str = (
            site_path.parent.name if site_path.name == "deploy" else site_path.name
        )

        if build_outcome is None:
            continue

        traceback_messages: Sequence[str] = traceback.format_exception(build_outcome)

        logger.error(
            f"(Build Failed | {FORMATTED_SITE_NAME}) {traceback_messages[-1].strip()}",
        )
        logger.debug(f"({FORMATTED_SITE_NAME}) {"".join(traceback_messages[:-1]).strip()}\n")

    built_site_paths: Set[Path] = {
        site_path
        for site_path, build_outcome
        in built_sites.items()
        if build_outcome is None
    }

    if built_site_paths:
        logger.info("Building all sites completed successfully.")

    return built_site_paths
