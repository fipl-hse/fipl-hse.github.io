"""

"""
from pathlib import Path
from typing import Union


def prepare_args_for_shell(args: list[Union[str, Path]]) -> str:
    return " ".join(map(str, args))
