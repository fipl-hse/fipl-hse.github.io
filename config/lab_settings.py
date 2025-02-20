"""
Settings manager.
"""

# pylint: disable=no-name-in-module
from pathlib import Path

from pydantic.dataclasses import dataclass


@dataclass
class SFTParams:
    """
    Fine-tuning parameters.
    """

    max_length: int
    batch_size: int
    max_fine_tuning_steps: int
    device: str
    finetuned_model_path: Path
    learning_rate: float
    target_modules: list[str] | None = None
