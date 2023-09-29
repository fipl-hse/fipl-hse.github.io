"""
Lab 1
Extract keywords based on frequency related metrics
"""
from string import punctuation
from typing import Optional


def is_dict_valid(dictionary: dict,
                  key_types: tuple = (str,), value_types: tuple = (int, float),
                  can_be_empty: bool = False) -> bool:
    """Check dictionary.

    Check dictionary for conforming to the specified types.

    Args:
        dictionary (dict): the dictionary to check
        key_types (tuple): allowed key types
        value_types (tuple): allowed value types
        can_be_empty (bool): whether the dictionary could be empty

    Returns:
        bool: is the dictionary conforms to the specified types
    """
    if not isinstance(dictionary, dict):
        return False
    if not dictionary and not can_be_empty:
        return False
    if not all(isinstance(key, key_types) for key in dictionary.keys()):
        return False
    if not all(type(value) in value_types for value in dictionary.values()):
        return False
    return True


# 4: Text Preprocessing
def clean_and_tokenize(text: str) -> Optional[list[str]]:
    """
    Removes punctuation, casts to lowercase, splits into tokens

    Parameters:
    text (str): Original text

    Returns:
    list[str]: A sequence of lowercase tokens with no punctuation

    In case of corrupt input arguments, None is returned
    """
    if not isinstance(text, str):
        return None
    for symbol in punctuation:
        text = text.replace(symbol, "")
    return text.lower().split()
