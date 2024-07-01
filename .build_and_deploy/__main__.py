"""Command-line execution of the static websites builder & deployment script."""

from collections.abc import Sequence

__all__: Sequence[str] = ()


import console

if __name__ == "__main__":
    raise SystemExit(console.run())
