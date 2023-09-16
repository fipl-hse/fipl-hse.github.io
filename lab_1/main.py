"""
Lab 1

Language detection
"""

import json
import re


def tokenize(text: str) -> list[str] | None:
    """
    Splits a text into tokens, converts the tokens into lowercase,
    removes punctuation, digits and other symbols

    :param text: a text
    :type text: str
    :return: a list of lower-cased tokens without punctuation
    """
    if not isinstance(text, str):
        return None
    text_output = list(re.sub(r'[\W\d_]+', '', text.lower()))
    return text_output


def calculate_frequencies(tokens: list[str] | None) -> dict[str, float] | None:
    """
    Calculates frequencies of given tokens

    :param tokens: a list of tokens
    :return: a dictionary with frequencies
    """
    if not isinstance(tokens, list):
        return None
    if len(tokens) > 0 and not isinstance(tokens[0], str):
        return None
    set_symbols = set(tokens)
    return {symbol: tokens.count(symbol) / len(tokens) for symbol in set_symbols}


def create_language_profile(language: str, text: str) -> dict[str, str | dict[str, float]] | None:
    """
    Creates a language profile

    :param language: a language
    :param text: a text
    :return: a dictionary with two keys – name, freq
    """
    if not isinstance(language, str) or not isinstance(text, str):
        return None

    frequencies = calculate_frequencies(tokenize(text))

    if frequencies is None:
        return None

    return {'name': language, 'freq': frequencies}
