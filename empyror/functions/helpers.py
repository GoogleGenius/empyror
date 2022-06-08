import typing

from pathlib import Path


def get_modules(path: str | Path) -> typing.Generator[Path, None, None]:
    """Get the modules from a specified path

    Parameters
    ----------
    path : str | Path
        The module to get the path of

    Returns
    -------
    modules : typing.Generator[Path, None, None]
        The paths of the modules
    """
    if isinstance(path, str):
        path = Path(path)

    modules = path.rglob("[!_]*.py")

    return modules
