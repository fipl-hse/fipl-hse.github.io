"""
Lab #1
"""


def multiply(num: int, other: int) -> int:
    """
    Multiply two numbers

    :param int num: the first number
    :param other: the second number
    :type other: int
    :return: the first number multiplied by the second number
    :rtype: int
    """

    return num * other


class Converter:
    """
    Language converter
    """

    def __init__(self, language: str):
        """
        Initializer

        :param language: input language
        """
        self.language = language

    def convert(self, text: str) -> str:
        """
        Converts text

        :param text: the text to convert
        :return: converted text
        """
        return text.upper()
