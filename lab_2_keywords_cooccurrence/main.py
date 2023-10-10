"""Lab 2.

Extract keywords based on co-occurrence frequency
"""
import json
import re
from pathlib import Path
from typing import Optional, Union, Sequence, Mapping

from lab_1_keywords_tfidf.main import clean_and_tokenize, remove_stop_words, calculate_frequencies

KeyPhrase = tuple[str, ...]
KeyPhrases = Sequence[KeyPhrase]


# 4: Phrase splitting and preprocessing, extracting candidate keyword phrases
def extract_phrases(text: str) -> Optional[Sequence[str]]:
    """Split the text into separate phrases using phrase delimiters.

    Args:
        text (str): Original text

    Returns:
        Sequence[str]: A list of phrases

    In case of corrupt input arguments, None is returned
    """
    if not isinstance(text, str) or not text:
        return None
    split_pattern = re.compile(r'[.,;:¡!¿?…⋯‹›«»|\\"“”\[\]()⟨⟩}{&–\-~—]|\s[-–~—]+\s')
    return [phrase.strip() for phrase in re.split(split_pattern, text) if phrase.strip()]


def extract_candidate_keyword_phrases(phrases: Sequence[str],
                                      stop_words: Sequence[str]) -> Optional[KeyPhrases]:
    """Create a list of candidate keyword phrases by splitting the given phrases by the stop words.

    Args:
        phrases (Sequence[str]): A list of the phrases
        stop_words (Sequence[str]): A list of the stop words

    Returns:
        KeyPhrases: The candidate keyword phrases for the text

    In case of corrupt input arguments, None is returned
    """
    if not isinstance(phrases, list) or not isinstance(stop_words, list):
        return None
    if not phrases or not stop_words:
        return None

    stop_words_with_spaces = [rf'\b{stop_word}\b' for stop_word in stop_words]
    pattern = re.compile('|'.join(stop_words_with_spaces))

    candidate_keyword_phrases = []
    for phrase in phrases:
        split_words = map(str.strip, re.split(pattern, phrase.lower().strip()))

        for keywords in split_words:

            keyword_phrase_wo_stop_words = remove_stop_words(keywords.split(' '), stop_words)

            if keyword_phrase_wo_stop_words and keyword_phrase_wo_stop_words != ['']:
                candidate_keyword_phrases.append(tuple(keyword_phrase_wo_stop_words))

    return candidate_keyword_phrases


# 6: Full algorithm
def calculate_frequencies_for_content_words(candidate_keyword_phrases: KeyPhrases) \
        -> Optional[Mapping[str, int]]:
    """Extract the content words from the candidate keyword phrases list and compute their frequencies.

    Args:
        candidate_keyword_phrases (KeyPhrases): A list of the candidate keyword phrases

    Returns:
        Mapping[str, int]: A dictionary with the content words and corresponding frequencies

    In case of corrupt input arguments, None is returned
    """
    if not isinstance(candidate_keyword_phrases, list) or not candidate_keyword_phrases:
        return None

    content_words = []

    for candidate_keyword_phrase in candidate_keyword_phrases:
        content_words.extend(candidate_keyword_phrase)

    return calculate_frequencies(content_words)


def calculate_word_degrees(candidate_keyword_phrases: KeyPhrases,
                           content_words: Sequence[str]) -> Optional[Mapping[str, int]]:
    """Calculate the word degrees based on the candidate keyword phrases list.

    Degree of a word is equal to the total length of all keyword phrases the word is found in

    Args:
        candidate_keyword_phrases (KeyPhrases): The candidate keyword phrases for the text
        content_words (Sequence[str]): The content words from the candidate keywords

    Returns:
        Mapping[str, int]: The words and their degrees

    In case of corrupt input arguments, None is returned
    """
    if not isinstance(candidate_keyword_phrases, list) or not isinstance(content_words, list):
        return None
    if not candidate_keyword_phrases or not content_words:
        return None

    word_degrees = {}

    for content_word in content_words:
        degree_score = 0
        for candidate_keyword_phrase in candidate_keyword_phrases:
            if content_word in candidate_keyword_phrase:
                degree_score += len(candidate_keyword_phrase)

        word_degrees[content_word] = degree_score

    return word_degrees


def calculate_word_scores(word_degrees: Mapping[str, int],
                          word_frequencies: Mapping[str, int]) -> Optional[Mapping[str, float]]:
    """Calculate the word score based on the word degree and word frequency metrics.

    Args:
        word_degrees (Mapping[str, int]): A mapping between the word and the degree
        word_frequencies (Mapping[str, int]): A mapping between the word and the frequency

    Returns:
        Mapping[str, float]: A dictionary with {word: word_score}

    In case of corrupt input arguments, None is returned
    """
    if not isinstance(word_frequencies, dict) or not isinstance(word_degrees, dict):
        return None
    if not word_frequencies or not word_degrees:
        return None
    if sorted(word_degrees.keys()) != sorted(word_frequencies.keys()):
        return None

    word_scores = {}

    for word, frequency in word_frequencies.items():
        word_scores[word] = word_degrees[word] / frequency

    return word_scores


def calculate_cumulative_score_for_candidates(candidate_keyword_phrases: KeyPhrases,
                                              word_scores: Mapping[str, float]) \
        -> Optional[Mapping[KeyPhrase, float]]:
    """Calculate cumulative score for each candidate keyword phrase.

    Cumulative score for a keyword phrase equals to
    the sum of the word scores of each keyword phrase's constituent

    Args:
        candidate_keyword_phrases (KeyPhrases): A list of candidate keyword phrases
        word_scores (Mapping[str, float]): Word scores

    Returns:
        Mapping[KeyPhrase, float]: A dictionary containing the mapping between
        the candidate keyword phrases and respective cumulative scores

    In case of corrupt input arguments, None is returned
    """
    if not isinstance(candidate_keyword_phrases, list) or not isinstance(word_scores, dict):
        return None
    if not candidate_keyword_phrases or not word_scores:
        return None

    cumulative_scores = {}

    for candidate_keyword_phrase in candidate_keyword_phrases:
        if candidate_keyword_phrase in cumulative_scores:
            continue

        cumulative_scores[candidate_keyword_phrase] = 0.0
        for word in candidate_keyword_phrase:
            if word not in word_scores:
                return None
            cumulative_scores[candidate_keyword_phrase] += word_scores[word]

    return cumulative_scores


def get_top_n(keyword_phrases_with_scores: Mapping[KeyPhrase, float],
              top_n: int,
              max_length: int) -> Optional[Sequence[str]]:
    """Extract the top N keyword phrases based on their scores and lengths.

    Args:
        keyword_phrases_with_scores (Mapping[KeyPhrase, float]): A dictionary containing the keyword phrases and their cumulative scores
        top_n (int): The number of the keyword phrases to extract
        max_length (int): Maximal length of a keyword phrase to be considered

    Returns:
        Sequence[str]: A list of keyword phrases sorted by their scores in descending order

    In case of corrupt input arguments, None is returned
    """
    if not isinstance(keyword_phrases_with_scores, dict) or \
            not isinstance(top_n, int) or \
            not isinstance(max_length, int):
        return None
    if not keyword_phrases_with_scores or (top_n <= 0) or (max_length <= 0):
        return None

    keywords_with_desired_lengths = {' '.join(keyword): score for keyword, score
                                     in keyword_phrases_with_scores.items() if len(keyword) <= max_length}

    sorted_keywords = sorted(keywords_with_desired_lengths.keys(),
                             key=lambda x: float(keywords_with_desired_lengths[x]),
                             reverse=True)

    return sorted_keywords[:top_n]


# 8: Adjoining keywords extraction
def extract_adjoining_keyword_phrases(candidate_keyword_phrases: KeyPhrases) \
        -> Optional[Sequence[tuple[KeyPhrase, KeyPhrase]]]:
    """Extract the keyword phrases that are found at least twice together.

    Helper function

    Args:
        candidate_keyword_phrases (KeyPhrases): A list of candidate keyword phrases

    Returns:
        Sequence[tuple[KeyPhrase, KeyPhrase]]: Pairs of keyword phrases that are found together at least twice
    """
    adjoining_keyword_phrases = []
    possible_pairs = []

    for keyword_idx, keyword_phrase in enumerate(candidate_keyword_phrases):
        if keyword_idx == len(candidate_keyword_phrases) - 1:
            break

        possible_pairs.append((keyword_phrase, candidate_keyword_phrases[keyword_idx + 1]))

    for possible_pair in possible_pairs:
        if possible_pairs.count(possible_pair) >= 2 and possible_pair not in adjoining_keyword_phrases:
            adjoining_keyword_phrases.append(possible_pair)

    return adjoining_keyword_phrases


def extract_candidate_keyword_phrases_with_adjoining(candidate_keyword_phrases: KeyPhrases,
                                                     phrases: Sequence[str]) -> Optional[KeyPhrases]:
    """Extract the adjoining keyword phrases from the candidate keywords Sequence and build new candidate keywords containing stop words.

    Adjoining keywords: such pairs that are found at least twice in the candidate keyword phrases list one after another

    To build a new keyword phrase the following is required:
        1. Find the first constituent of the adjoining keyword phrase in the phrases followed by:
            a stop word and the second constituent of the adjoining keyword phrase
        2. Combine these three pieces in the new candidate keyword phrase, i.e.:
            new_candidate_keyword = [first_constituent, stop_word, second_constituent]

    Args:
        candidate_keyword_phrases (KeyPhrases): A list of candidate keyword phrases
        phrases (Sequence[str]): A list of phrases

    Returns:
        KeyPhrases: A list containing the pairs of candidate keyword phrases that are found at least twice together

    In case of corrupt input arguments, None is returned
    """
    if not isinstance(candidate_keyword_phrases, list) or not isinstance(phrases, list):
        return None
    if not candidate_keyword_phrases or not phrases:
        return None

    adjoining_keyword_phrases = extract_adjoining_keyword_phrases(candidate_keyword_phrases)

    tokenized_phrases = [clean_and_tokenize(phrase) for phrase in phrases]

    new_candidates = []

    for adjoining_keyword_phrase in adjoining_keyword_phrases:

        first_constituent, second_constituent = adjoining_keyword_phrase[0], adjoining_keyword_phrase[1]

        for phrase in tokenized_phrases:
            if not phrase:
                continue
            phrase_: tuple = tuple(phrase)
            possible_keyword_phrase = [*first_constituent]

            start_position = 0

            while start_position <= len(phrase_) - 3:
                first_constituent_position = find_subsequence_position(first_constituent,
                                                                       phrase_,
                                                                       start_position)
                if first_constituent_position != -1:

                    following_sequence = phrase_[first_constituent_position + len(first_constituent) + 1:
                                                 first_constituent_position + len(first_constituent) + 1
                                                 + len(second_constituent)]

                    start_position = first_constituent_position + len(first_constituent) + 1

                    if following_sequence == second_constituent:
                        stop_word = phrase_[first_constituent_position + len(first_constituent)]

                        possible_keyword_phrase.append(stop_word)
                        possible_keyword_phrase.extend(second_constituent)
                        new_candidates.append(tuple(possible_keyword_phrase))
                        possible_keyword_phrase = [*first_constituent]

                start_position += 1

    # Filter out those that are found only once
    new_candidates_found_more_than_once = []
    for new_candidate in new_candidates:
        if new_candidate not in new_candidates_found_more_than_once and new_candidates.count(new_candidate) > 1:
            new_candidates_found_more_than_once.append(new_candidate)

    return new_candidates_found_more_than_once


def calculate_cumulative_score_for_candidates_with_stop_words(candidate_keyword_phrases: KeyPhrases,
                                                              word_scores: Mapping[str, float],
                                                              stop_words: Sequence[str]) \
        -> Optional[Mapping[KeyPhrase, float]]:
    """Calculate cumulative score for each candidate keyword phrase.

    Cumulative score for a keyword phrase equals to
    the sum of the word scores of each keyword phrase's constituent except for the stop words

    Args:
        candidate_keyword_phrases (KeyPhrases): A list of candidate keyword phrases
        word_scores (Mapping[str, float]): Word scores
        stop_words (Sequence[str]): A list of stop words

    Returns:
        Mapping[KeyPhrase, float]: A dictionary containing the mapping between the candidate keyword phrases
        and respective cumulative scores

    In case of corrupt input arguments, None is returned
    """
    if not isinstance(candidate_keyword_phrases, list) \
            or not isinstance(word_scores, dict) \
            or not isinstance(stop_words, list):
        return None
    if not candidate_keyword_phrases or not word_scores or not stop_words:
        return None

    cumulative_scores = {}

    for candidate_keyword_phrase in candidate_keyword_phrases:
        if candidate_keyword_phrase in cumulative_scores:
            continue

        cumulative_scores[candidate_keyword_phrase] = sum([word_scores[word] for word in candidate_keyword_phrase
                                                           if word not in stop_words])

    return cumulative_scores


def find_subsequence_position(subsequence: Union[Sequence[str], tuple[str, ...]],
                              sequence: Union[Sequence[str], tuple[str, ...]],
                              start: int) -> int:
    """Find the starting position of a subsequence in a sequence.

    Helper function

    Args:
        subsequence (Union[Sequence[str], tuple[str, ...]]): A subsequence for which the function searches
        sequence (Union[Sequence[str], tuple[str, ...]]): A sequence in which the function searches
        start (int): Starting position of the search

    Returns:
        int: A position from which the subsequence starts; -1 returned if the subsequence is not found
    """
    for idx in range(start, len(sequence) - len(subsequence) + 1):
        if tuple(sequence[idx:idx + len(subsequence)]) == subsequence:
            return idx
    return -1


# 10: Stop words generation
def find_ceil_of_value(value: float) -> int:
    """Find the ceiling value (closes int x that is >= value) of the given value.

    Helper function

    Args:
        value (float): The value for which the ceiling value should be found

    Returns:
        int: The ceiling value
    """
    return int(value) if int(value) == value else int(value + 1)


def find_percentile(data: Union[Sequence[int], tuple[int, ...]], percentage: int) -> int:
    """Find the percentile value.

    Helper function

    Args:
        data (Union[Sequence[int], tuple[int, ...]]): An array of values
        percentage (int): Required percentile

    Returns:
        int: The percentile
    """
    size = len(data)
    return sorted(data)[find_ceil_of_value((size * percentage) / 100) - 1]


def generate_stop_words(text: str,
                        max_length: int) -> Optional[Sequence[str]]:
    """Generate the list of stop words from the given text.

    Args:
        text (str): The text
        max_length (int): Maximum length (in characters) of an individual stop word

    Returns:
        Sequence[str]: A list of stop words
    """
    if not isinstance(text, str) or not isinstance(max_length, int):
        return None
    if max_length <= 0:
        return None

    tokens = clean_and_tokenize(text)
    if not tokens:
        return None

    frequencies = calculate_frequencies(tokens)

    percentile_value = find_percentile(list(frequencies.values()), 80)

    stop_words = []
    for word, word_frequency in frequencies.items():
        if word_frequency >= percentile_value and len(word) <= max_length:
            stop_words.append(word)

    return stop_words


def load_stop_words(path: Path) -> Optional[Mapping[str, Sequence[str]]]:
    """Load stop word lists from the file.

    Args:
        path (Path): A path to the file with stop word lists

    Returns:
        Mapping[str, Sequence[str]]: A dictionary containing the language names and corresponding stop word lists
    """
    if not isinstance(path, Path) or not path:
        return None
    with open(path, 'r', encoding='utf-8') as stop_word_file:
        stop_words: Mapping[str, Sequence[str]] = json.load(stop_word_file)
        return stop_words