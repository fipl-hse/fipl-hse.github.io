"""
Frequency-driven keyword extraction starter
"""
import json
import sys
from pathlib import Path

from lab_1_keywords_tfidf.main import (
    clean_and_tokenize,
    remove_stop_words,
    get_top_n,
    calculate_frequencies,
    calculate_tf,
    calculate_tfidf,
    calculate_expected_frequency,
    calculate_chi_values,
    extract_significant_words
)


if __name__ == "__main__":

    # finding paths to the necessary utils
    PROJECT_ROOT = Path(__file__).parent
    ASSETS_PATH = PROJECT_ROOT / 'assets'

    # reading the text from which keywords are going to be extracted
    TARGET_TEXT_PATH = ASSETS_PATH / 'Дюймовочка.txt'
    with open(TARGET_TEXT_PATH, 'r', encoding='utf-8') as file:
        target_text = file.read()

    # reading list of stop words
    STOP_WORDS_PATH = ASSETS_PATH / 'stop_words.txt'
    with open(STOP_WORDS_PATH, 'r', encoding='utf-8') as file:
        stop_words = file.read().split('\n')

    # reading IDF scores for all tokens in the corpus of H.C. Andersen tales
    IDF_PATH = ASSETS_PATH / 'IDF.json'
    with open(IDF_PATH, 'r', encoding='utf-8') as file:
        idf = json.load(file)

    # reading frequencies for all tokens in the corpus of H.C. Andersen tales
    CORPUS_FREQ_PATH = ASSETS_PATH / 'corpus_frequencies.json'
    with open(CORPUS_FREQ_PATH, 'r', encoding='utf-8') as file:
        corpus_freqs = json.load(file)

    # preprocessing
    tokenized_text = clean_and_tokenize(target_text)
    if tokenized_text is None:
        sys.exit(1)
    tokenized_text = remove_stop_words(tokenized_text, stop_words)

    # TF-IDF calculation
    if tokenized_text is None:
        sys.exit(1)
    frequencies = calculate_frequencies(tokenized_text)
    if frequencies is None:
        sys.exit(1)
    tf = calculate_tf(frequencies)
    if tf is None:
        sys.exit(1)
    tf_idf = calculate_tfidf(tf, idf)

    if tf_idf is None:
        sys.exit(1)
    RESULT = get_top_n(tf_idf, 10)
    if RESULT is None:
        sys.exit(1)
    print("Keywords according to TF-IDF:", ", ".join(RESULT))

    # chi-squared calculation
    expected = calculate_expected_frequency(frequencies, corpus_freqs)
    if expected is None:
        sys.exit(1)
    chi_values = calculate_chi_values(expected, frequencies)

    if chi_values is None:
        sys.exit(1)
    keywords = extract_significant_words(chi_values, 0.001)
    if keywords is None:
        sys.exit(1)

    RESULT = get_top_n(keywords, 10)
    if RESULT is None:
        sys.exit(1)
    print("Keywords according to chi-squared:", ", ".join(RESULT))
    print(len(keywords), "keywords in total")

    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT, 'Keywords are not extracted'
