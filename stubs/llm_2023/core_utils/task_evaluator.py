"""
Module with description of abstract task evaluator.
"""
# pylint: disable=too-few-public-methods, duplicate-code
from abc import ABC, abstractmethod
from typing import Iterable

try:
    from pandas import DataFrame
except ImportError:
    print('Library "pandas" not installed. Failed to import.')
    DataFrame = dict  # type: ignore

from stubs.llm_2023.core_utils.metrics import Metrics


class AbstractTaskEvaluator(ABC):
    """
    Abstract Task Evaluator.
    """
    def __init__(self, metrics: Iterable[Metrics]):
        self._metrics = metrics

    @abstractmethod
    def run(self) -> DataFrame:
        """
        Entrypoint for task evaluation versus a number of specified metrics.
        """
