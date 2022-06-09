import typing

from pathlib import Path


def get_plugins(path: str | Path) -> typing.Generator[Path, None, None]:
    """Get the modules from a specified path

    Parameters
    ----------
    path : str | Path
        The module to get the path of

    Returns
    -------
    typing.Generator[Path, None, None]
        The paths of the plugins
    """
    if isinstance(path, str):
        path = Path(path)

    return path.rglob("[!_]*.py")
