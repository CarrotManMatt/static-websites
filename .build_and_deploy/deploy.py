""""""

from collections.abc import Sequence

__all__: Sequence[str] = ("deploy_all_sites",)


from collections.abc import Iterable
from pathlib import Path


def deploy_all_sites(site_paths: Iterable[Path], *, remote_ip: str | None = None, remote_ssh_key: str | None = None, remote_user_name: str | None = None, remote_directory: str | None = None, dry_run: bool = False) -> None:  # noqa: E501    raise NotImplementedError
    raise NotImplementedError
