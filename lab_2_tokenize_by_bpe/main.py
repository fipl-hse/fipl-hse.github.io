"""
Lab 2.

BPE and machine translation evaluation
"""

def prepare_word(raw_word: str, start_of_word: str | None, end_of_word: str | None) -> tuple[str, ...] | None:
    """
    Tokenize word into unigrams and append end-of-word token.

    Args:
        raw_word (str): Original word
        start_of_word (str): A token that signifies the start of word
        end_of_word (str): A token that signifies the end of word

    Returns:
        tuple[str, ...]: Preprocessed word

    In case of corrupt input arguments, None is returned
    """

def collect_frequencies(text: str, start_of_word: str | None, end_of_word: str) -> dict[tuple[str, ...], int] | None:
    """
    Count number of occurrences of each word.

    Args:
        text (str): Original text with no preprocessing
        start_of_word (str): A token that signifies the start of word
        end_of_word (str): A token that signifies the end of word

    Returns:
        dict[tuple[str, ...], int]: Dictionary in the form of
            <preprocessed word: number of occurrences>

    In case of corrupt input arguments or functions used return None,
    None is returned
    """

def count_tokens_pairs(word_frequencies: dict[tuple[str, ...], int]) -> dict[tuple[str, str], int] | None:
    """
    Count number of occurrences of each pair of subsequent tokens.

    Args:
        word_frequencies (dict[tuple[str, ...], int]): A dictionary in the form of
            <preprocessed word: number of occurrences>

    Returns:
        dict[tuple[str, str], int]: A dictionary in the form of
            <token pair: number of occurrences>

    In case of corrupt input arguments, None is returned
    """

def merge_tokens(word_frequencies: dict[tuple[str, ...], int], pair: tuple[str, str]) -> dict[tuple[str, ...], int] | None:
    """
    Update word frequency dictionary by replacing a pair of token with a merged one.

    Args:
        word_frequencies (dict[tuple[str, ...], int]): A dictionary in the form of
            <preprocessed word: number of occurrences>
        pair (tuple[str, str]): A pair of tokens to be merged

    Returns:
        dict[tuple[str, ...], int]: A dictionary in the form of
            <preprocessed word: number of occurrences>

    In case of corrupt input arguments, None is returned
    """

def train(word_frequencies: dict[tuple[str, ...], int] | None, num_merges: int) -> dict[tuple[str, ...], int] | None:
    """
    Create required number of new tokens by merging existing ones.

    Args:
        word_frequencies (dict[tuple[str, ...], int]): A dictionary in the form of
            <preprocessed word: number of occurrences>
        num_merges (int): Required number of new tokens

    Returns:
        dict[tuple[str, ...], int]: A dictionary in the form of
            <preprocessed word: number of occurrences>

    In case of corrupt input arguments or functions used return None,
    None is returned
    """

def get_vocabulary(word_frequencies: dict[tuple[str, ...], int], unknown_token: str) -> dict[str, int] | None:
    """
    Establish correspondence between tokens and its integer identifier.

    Args:
        word_frequencies (dict[tuple[str, ...], int]): A dictionary in the form of
            <preprocessed word: number of occurrences>
        unknown_token (str): A token to signify an unknown token

    Returns:
        dict[str, int]: A dictionary in the form of <token: identifier>

    In case of corrupt input arguments, None is returned
    """

def decode(encoded_text: list[int] | None, vocabulary: dict[str, int] | None, end_of_word_token: str | None) -> str | None:
    """
    Translate encoded sequence into decoded one.

    Args:
        encoded_text (list[int]): A sequence of token identifiers
        vocabulary (dict[str, int]): A dictionary in the form of <token: identifier>
        end_of_word_token (str): An end-of-word token

    Returns:
        str: Decoded sequence

    In case of corrupt input arguments, None is returned
    """

def tokenize_word(word: tuple[str, ...], vocabulary: dict[str, int], end_of_word: str | None, unknown_token: str) -> list[int] | None:
    """
    Split word into tokens.

    Args:
        word (tuple[str, ...]): Preprocessed word
        vocabulary (dict[str, int]): A dictionary in the form of <token: identifier>
        end_of_word (str): An end-of-word token
        unknown_token (str): A token that signifies unknown sequence

    Returns:
        list[int]: A list of token identifiers

    In case of corrupt input arguments, None is returned
    """

def load_vocabulary(vocab_path: str) -> dict[str, int] | None:
    """
    Read and retrieve dictionary of type <token: identifier>.

    Args:
        vocab_path (str): A path to the saved vocabulary

    Returns:
        dict[str, int]: A dictionary in the form of <token: identifier>

    In case of corrupt input arguments, None is returned
    """

def encode(original_text: str, vocabulary: dict[str, int] | None, start_of_word_token: str | None, end_of_word_token: str | None, unknown_token: str) -> list[int] | None:
    """
    Translate decoded sequence into encoded one.

    Args:
        original_text (str): Original text
        vocabulary (dict[str, int]): A dictionary in the form of <token: identifier>
        start_of_word_token (str): A start-of-word token
        end_of_word_token (str): An end-of-word token
        unknown_token (str): A token that signifies unknown sequence

    Returns:
        list[int]: A list of token identifiers

    In case of corrupt input arguments or functions used return None,
    None is returned
    """

def collect_ngrams(text: str, order: int) -> list[tuple[str, ...]] | None:
    """
    Extract n-grams from the given sequence.

    Args:
        text (str): Original text
        order (int): Required number of elements in a single n-gram

    Returns:
        list[tuple[str, ...]]: A sequence of n-grams

    In case of corrupt input arguments, None is returned
    """

def calculate_precision(actual: list[tuple[str, ...]], reference: list[tuple[str, ...]]) -> float | None:
    """
    Compare two sequences by virtue of Precision metric.

    Args:
        actual (list[tuple[str, ...]]): Predicted sequence of n-grams
        reference (reference: list[tuple[str, ...]]): Expected sequence of n-grams

    Returns:
        float: Value of Precision metric

    In case of corrupt input arguments, None is returned
    """

def geo_mean(precisions: list[float], max_order: int) -> float | None:
    """
    Compute geometric mean of sequence of values.

    Args:
        precisions (list[float]): A sequence of Precision values
        max_order (int): Maximum length of n-gram considered

    Returns:
        float: A value of geometric mean of Precision metric

    In case of corrupt input arguments, None is returned
    """

def calculate_bleu(actual: str | None, reference: str, max_order: int=3) -> float | None:
    """
    Compare two sequences by virtue of BLEU metric.

    Args:
        actual (str): Predicted sequence
        reference (str): Expected sequence
        max_order (int): Max length of n-gram to consider for comparison

    Returns:
        float: A value of BLEU metric

    In case of corrupt input arguments or functions used return None,
    None is returned
    """