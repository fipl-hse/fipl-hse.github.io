"""
Lab 1
Extract keywords based on frequency related metrics
"""
from math import log
from string import punctuation
from typing import Optional, Union


def is_dict_valid(dictionary: dict,
                  key_types: tuple = (str,), value_types: tuple = (int, float),
                  can_be_empty: bool = False) -> bool:
    """
    Verifies that dictionary meets expectations

    Parameters:
    dictionary (dict): Object to test
    key_types (tuple): Acceptable types for keys
    value_types (tuple): Acceptable types for values
    can_be_empty (bool): Indicator whether it is acceptable that the dictionary has no content

    Returns:
    bool: Indicator whether the dictionary satisfies all the requirements presented
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


def remove_stop_words(tokens: list[str], stop_words: list[str]) -> Optional[list[str]]:
    """
    Excludes stop words from the token sequence

    Parameters:
    tokens (List[str]): Original token sequence
    stop_words (List[str]: Tokens to exclude

    Returns:
    List[str]: Token sequence that does not include stop words

    In case of corrupt input arguments, None is returned
    """
    if tokens and isinstance(tokens, list) and isinstance(stop_words, list):
        if all(isinstance(token, str) for token in tokens):
            return [token for token in tokens if token not in stop_words]
    return None


# 6: Frequencies dictionary and sorting
def calculate_frequencies(tokens: list[str]) -> Optional[dict[str, int]]:
    """
    Composes a frequency dictionary from the token sequence

    Parameters:
    tokens (List[str]): Token sequence to count frequencies for

    Returns:
    Dict: {token: number of occurrences in the token sequence} dictionary

    In case of corrupt input arguments, None is returned
    """
    if isinstance(tokens, list) and all(isinstance(token, str) for token in tokens):
        return {token: tokens.count(token) for token in tokens}
    return None


def get_top_n(frequencies: dict[str, Union[int, float]], top: int) -> Optional[list[str]]:
    """
    Extracts a certain number of most frequent tokens

    Parameters:
    frequencies (Dict): A dictionary with tokens and
    its corresponding frequency values
    top (int): Number of token to extract

    Returns:
    List[str]: Sequence of specified length
    consisting of tokens with the largest frequency

    In case of corrupt input arguments, None is returned
    """
    if is_dict_valid(frequencies) and isinstance(top, int) and not isinstance(top, bool) and top > 0:
        return sorted(frequencies.keys(),
                      key=lambda x: frequencies[x],
                      reverse=True)[:top]
    return None


# 8: TF-IDF calculations
def calculate_tf(frequencies: dict[str, int]) -> Optional[dict[str, float]]:
    """
    Calculates Term Frequency score for each word in a token sequence
    based on the raw frequency

    Parameters:
    frequencies (Dict): Raw number of occurrences for each of the tokens

    Returns:
    dict: A dictionary with tokens and corresponding term frequency score

    In case of corrupt input arguments, None is returned
    """
    if not is_dict_valid(frequencies, value_types=(int,)):
        return None
    total_tokens = sum(frequencies.values())
    term_frequency = {key: (value / total_tokens) for key, value in frequencies.items()}
    return term_frequency


def calculate_tfidf(term_freq: dict[str, float], idf: dict[str, float]) -> Optional[dict[str, float]]:
    """
    Calculates TF-IDF score for each of the tokens
    based on its TF and IDF scores

    Parameters:
    term_freq (Dict): A dictionary with tokens and its corresponding TF values
    idf (Dict): A dictionary with tokens and its corresponding IDF values

    Returns:
    Dict: A dictionary with tokens and its corresponding TF-IDF values

    In case of corrupt input arguments, None is returned
    """
    if not is_dict_valid(term_freq, value_types=(float, )) or not is_dict_valid(idf, can_be_empty=True):
        return None
    max_idf = log(47 / 1)
    tfidf = {key: value * idf.get(key, max_idf) for key, value in term_freq.items()}
    return tfidf


# 10: Chi-squared based keywords extraction
def calculate_expected_frequency(doc_freqs: dict[str, int],
                                 corpus_freqs: dict[str, int]) -> Optional[dict[str, float]]:
    """
    Calculates expected frequency for each of the tokens based on its
    Term Frequency score for both target document and general corpus

    Parameters:
    doc_freqs (Dict): A dictionary with tokens and its corresponding number of occurrences in document
    corpus_freqs (Dict): A dictionary with tokens and its corresponding number of occurrences in corpus

    Returns:
    Dict: A dictionary with tokens and its corresponding expected frequency

    In case of corrupt input arguments, None is returned
    """
    if not is_dict_valid(doc_freqs, value_types=(int,)) or \
            not is_dict_valid(corpus_freqs, value_types=(int,), can_be_empty=True):
        return None
    expected = {}
    for token in doc_freqs.keys():
        total_doc, total_corpus = sum(doc_freqs.values()), sum(corpus_freqs.values())

        token_freq_doc = doc_freqs[token]
        token_freq_corpus = corpus_freqs.get(token, 0)
        other_tokens_freq_doc = total_doc - token_freq_doc
        other_tokens_freq_corpus = total_corpus - token_freq_corpus

        expected[token] = ((token_freq_doc + token_freq_corpus) *
                           (token_freq_doc + other_tokens_freq_doc)) / \
                          (token_freq_doc + token_freq_corpus +
                           other_tokens_freq_doc + other_tokens_freq_corpus)
        expected[token] = expected[token]
    return expected


def calculate_chi_values(expected: dict[str, float], observed: dict[str, int]) -> Optional[dict[str, float]]:
    """
    Calculates chi-squared value for the tokens
    based on their expected and observed frequency rates

    Parameters:
    expected (Dict): A dictionary with tokens and
    its corresponding expected frequency
    observed (Dict): A dictionary with tokens and
    its corresponding observed frequency

    Returns:
    Dict: A dictionary with tokens and its corresponding chi-squared value

    In case of corrupt input arguments, None is returned
    """
    if not is_dict_valid(expected) or not is_dict_valid(observed):
        return None
    chi_values = {}
    for token in observed.keys():
        obs = observed[token]
        exp = expected[token]
        chi_values[token] = ((obs - exp) ** 2) / exp
    return chi_values


def extract_significant_words(chi_values: dict[str, float], alpha: float) -> Optional[dict[str, float]]:
    """
    Select those tokens from the token sequence that
    have a chi-squared value smaller than the criterion

    Parameters:
    chi_values (Dict): A dictionary with tokens and
    its corresponding chi-squared value
    alpha (float): Level of significance that controls critical value of chi-squared metric

    Returns:
    Dict: A dictionary with significant tokens
    and its corresponding chi-squared value

    In case of corrupt input arguments, None is returned
    """
    critical_values = {0.05: 3.842, 0.01: 6.635, 0.001: 10.828}
    if not is_dict_valid(chi_values) or not isinstance(alpha, float) or alpha not in critical_values:
        return None
    criterion = critical_values[alpha]
    significant_words = {key: item for key, item in chi_values.items() if item > criterion}
    return significant_words
