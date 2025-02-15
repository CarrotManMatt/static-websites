"""Build and render functions for whole sites and single HTML pages."""

import logging
import re
import shutil
import traceback
from logging import LoggerAdapter
from subprocess import CalledProcessError
from typing import TYPE_CHECKING

from sites import SITES_MAP
from utils import PROJECT_ROOT

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence
    from collections.abc import Set as AbstractSet
    from logging import Logger
    from pathlib import Path, PurePosixPath
    from typing import Final

    import htpy as h

    from utils import CaughtException

__all__: "Sequence[str]" = ("build_all_sites", "build_single_page", "build_single_site")

logger: "Final[Logger]" = logging.getLogger("static-websites-builder")
extra_context_logger: "Final[Logger]" = logging.getLogger(
    "static-websites-builder-extra-context"
)


def minify_single_page(rendered_page: str, PAGE_LOGGER: "Logger") -> str:  # noqa: N803
    import minify_html

    rendered_page = minify_html.minify(
        rendered_page,
        do_not_minify_doctype=True,
        keep_html_and_head_opening_tags=True,
        ensure_spec_compliant_unquoted_attribute_values=True,
        keep_spaces_between_attributes=True,
        minify_js=True,
        minify_css=True,
        keep_comments=False,
    )
    PAGE_LOGGER.debug("HTML file successfully minified.")

    if re.search(r">\s+", rendered_page):
        PAGE_LOGGER.warning(
            "Found whitespace after HTML tag. Make sure to check validity of rendered output."
        )
        rendered_page = re.sub(r">\s+", ">", rendered_page)

    if re.search(r"\s+<", rendered_page):
        PAGE_LOGGER.warning(
            "Found whitespace before HTML tag. Make sure to check validity of rendered output."
        )
        rendered_page = re.sub(r"\s+<", "<", rendered_page)

    rendered_page = re.sub(r"(?<=[A-Za-z]):<(?=a|span)", r": <", rendered_page)


def build_single_page(
    *,
    page_path: "PurePosixPath",
    page_content: "h.Element",
    site_name: str,
    site_deploy_directory: "Path",
    minify: bool = False,
) -> None:
    """Render a single HTML page into a string output."""
    if page_path.is_absolute():
        INVALID_PAGE_PATH_MESSAGE: str = (
            "Page path must be relative to site name (cannot be an absolute `PurePosixPath`)."
        )
        raise ValueError(INVALID_PAGE_PATH_MESSAGE)

    PAGE_LOGGER: LoggerAdapter[Logger] = LoggerAdapter(
        extra_context_logger, {"extra_context": f"{site_name}/{page_path.as_posix()}"}
    )

    DEPLOY_PAGE_PATH: Path = site_deploy_directory / page_path

    DEPLOY_PAGE_PATH.parent.mkdir(parents=True, exist_ok=True)

    rendered_page: str = str(page_content)

    PAGE_LOGGER.debug("HTML successfully rendered.")

    if minify:
        minify_single_page(rendered_page, PAGE_LOGGER)

    DEPLOY_PAGE_PATH.write_text(f"{rendered_page.strip()}\n", encoding="utf-8")

    PAGE_LOGGER.debug("Rendered HTML file successfully saved to `deploy/` directory.")


def build_single_site(
    *,
    site_name: str,
    site_pages: "Mapping[PurePosixPath, h.Element]",
    site_deploy_directory: "Path",
    minify: bool = False,
) -> None:
    """Render a single site's HTML pages into string outputs."""
    SITE_LOGGER: Final[LoggerAdapter[Logger]] = LoggerAdapter(
        extra_context_logger, {"extra_context": site_name}
    )

    SITE_LOGGER.debug("Begin building single site.")

    SITE_LOGGER.debug("Creating `deploy/` directory.")

    if site_deploy_directory.exists():
        shutil.rmtree(site_deploy_directory)
    site_deploy_directory.mkdir(parents=True)

    SITE_LOGGER.debug(
        "Creating symlink to original static directory from inside `deploy/` directory."
    )

    static_dir: Path = PROJECT_ROOT / f"static/{site_name}"
    if static_dir.is_dir():
        (site_deploy_directory / "static").symlink_to(static_dir, target_is_directory=True)

    page_path: PurePosixPath
    page_content: h.Element
    for page_path, page_content in site_pages.items():
        build_single_page(
            page_path=page_path,
            page_content=page_content,
            site_name=site_name,
            site_deploy_directory=site_deploy_directory,
            minify=minify,
        )

    SITE_LOGGER.debug("Completed building single site successfully.")


def build_all_sites(*, minify: bool = False) -> "AbstractSet[Path]":
    """Render all sites HTML pages into string outputs."""
    logger.info("Begin building all sites.")

    built_sites: dict[Path, CaughtException | None] = {}

    site_name: str
    site_pages: Mapping[PurePosixPath, h.Element]
    for site_name, site_pages in SITES_MAP.items():
        site_deploy_directory: Path = PROJECT_ROOT / f"deploy/{site_name}"

        try:
            build_single_site(
                site_name=site_name,
                site_pages=site_pages,
                site_deploy_directory=site_deploy_directory,
                minify=minify,
            )
        except (
            ValueError,
            RuntimeError,
            AttributeError,
            TypeError,
            OSError,
            CalledProcessError,
        ) as caught_exception:
            built_sites[site_deploy_directory] = caught_exception
            continue
        else:
            built_sites[site_deploy_directory] = None

    site_path: Path
    build_outcome: CaughtException | None
    for site_path, build_outcome in built_sites.items():
        FORMATTED_SITE_NAME: str = (
            site_path.parent.name if site_path.name == "deploy" else site_path.name
        )
        site_name_logger: LoggerAdapter[Logger] = LoggerAdapter(
            extra_context_logger, {"extra_context": FORMATTED_SITE_NAME}
        )
        build_failed_logger: LoggerAdapter[Logger] = LoggerAdapter(
            extra_context_logger, {"extra_context": f"{FORMATTED_SITE_NAME} | Build Failed"}
        )

        if build_outcome is None:
            continue

        traceback_messages: Sequence[str] = traceback.format_exception(build_outcome)

        build_failed_logger.error(traceback_messages[-1].strip())
        site_name_logger.debug("%s\n", "".join(traceback_messages[:-1]).strip())

    built_site_paths: AbstractSet[Path] = {
        site_path for site_path, build_outcome in built_sites.items() if build_outcome is None
    }

    if built_site_paths:
        logger.info("Building all sites completed successfully.")

    return built_site_paths
