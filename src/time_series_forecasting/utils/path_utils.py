import sys
from pathlib import Path


def get_project_root(levels_up: int = 1) -> Path:
    """
    Return the project root directory as a pathlib.Path.

    By default this assumes the project root is one level above the directory
    containing this file, i.e.:

        <project_root>/
            utils/
                path_utils.py

    If your structure is different, adjust `levels_up` accordingly.
    This is more robust than relying on `Path.cwd()`, which changes
    depending on where you run Python (e.g. from a notebook folder).
    """
    return Path(__file__).resolve().parents[levels_up]


def append_to_syspath(levels_up: int = 1) -> None:
    """
    Add the project root (or a parent) to sys.path, if not already present.

    Parameters
    ----------
    levels_up : int, optional
        How many levels above this file to treat as the root.
        Default is 1 (see `get_project_root` for details).
    """
    project_root = str(get_project_root(levels_up))

    if project_root not in sys.path:
        # Prepend so project imports take precedence over site-packages duplicates
        sys.path.insert(0, project_root)


if __name__ == '__main__':
    append_to_syspath()