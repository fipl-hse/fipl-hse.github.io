"""
Co-occurrence-driven keyword extraction starter
"""

import sys
from pathlib import Path

from lab_2_keywords_cooccurrence.main import (
    extract_phrases,
    extract_candidate_keyword_phrases,
    calculate_frequencies_for_content_words,
    calculate_word_scores,
    calculate_word_degrees,
    calculate_cumulative_score_for_candidates,
    get_top_n,
    extract_candidate_keyword_phrases_with_adjoining,
    generate_stop_words,
    calculate_cumulative_score_for_candidates_with_stop_words,
    load_stop_words
)


def read_target_text(file_path: Path) -> str:
    """
    Utility functions that reads the text content from the file
    :param file_path: the path to the file
    :return: the text content of the file
    """
    with open(file_path, 'r', encoding='utf-8') as target_text_file:
        return target_text_file.read()


if __name__ == "__main__":
    # finding paths to the necessary utils
    PROJECT_ROOT = Path(__file__).parent
    ASSETS_PATH = PROJECT_ROOT / 'assets'

    # reading list of stop words
    STOP_WORDS_PATH = ASSETS_PATH / 'stop_words.txt'
    with open(STOP_WORDS_PATH, 'r', encoding='utf-8') as fd:
        stop_words = fd.read().split('\n')

    # reading the text from which keywords are going to be extracted
    TARGET_TEXT_PATH_GENOME = ASSETS_PATH / 'genome_engineering.txt'
    TARGET_TEXT_PATH_ALBATROSS = ASSETS_PATH / 'albatross.txt'
    TARGET_TEXT_PATH_PAIN_DETECTION = ASSETS_PATH / 'pain_detection.txt'
    TARGET_TEXT_PATH_GAGARIN = ASSETS_PATH / 'gagarin.txt'

    corpus = {
        'gagarin': read_target_text(TARGET_TEXT_PATH_GAGARIN),
        'albatross': read_target_text(TARGET_TEXT_PATH_ALBATROSS),
        'genome_engineering': read_target_text(TARGET_TEXT_PATH_GENOME),
        'pain_detection': read_target_text(TARGET_TEXT_PATH_PAIN_DETECTION)
    }

    # 4
    phrases = extract_phrases(corpus['gagarin'])
    print(f'PHRASES: {phrases}')
    print('*' * 20 + '\n')

    if not phrases or not stop_words:
        sys.exit(1)
    candidate_keyword_phrases = extract_candidate_keyword_phrases(
        phrases,
        stop_words)

    print(f'CANDIDATE KEYWORD PHRASES: {candidate_keyword_phrases}')
    print('*' * 20 + '\n')

    # 6
    if not candidate_keyword_phrases:
        sys.exit(1)
    content_words_with_frequencies = calculate_frequencies_for_content_words(candidate_keyword_phrases)
    print(f'CONTENT WORDS WITH FREQUENCIES: {content_words_with_frequencies}')
    print('*' * 20 + '\n')

    if not candidate_keyword_phrases or not content_words_with_frequencies:
        sys.exit(1)
    word_degrees = calculate_word_degrees(candidate_keyword_phrases, list(content_words_with_frequencies.keys()))
    print(word_degrees)
    print('*' * 20 + '\n')

    if not word_degrees or not content_words_with_frequencies:
        sys.exit(1)
    word_scores = calculate_word_scores(word_degrees, content_words_with_frequencies)
    print(word_scores)
    print('*' * 20 + '\n')

    if not candidate_keyword_phrases or not word_scores:
        sys.exit(1)
    cumulative_scores_for_candidates = calculate_cumulative_score_for_candidates(candidate_keyword_phrases, word_scores)
    print(cumulative_scores_for_candidates)
    print('*' * 20 + '\n')

    if not cumulative_scores_for_candidates:
        sys.exit(1)
    top_n = get_top_n(keyword_phrases_with_scores=cumulative_scores_for_candidates, top_n=10, max_length=2)
    print(top_n)
    print('*' * 20 + '\n')

    # 8
    if not candidate_keyword_phrases or not phrases:
        sys.exit(1)
    new_candidates = extract_candidate_keyword_phrases_with_adjoining(candidate_keyword_phrases, phrases)
    print(f'NEW CANDIDATES: {new_candidates}')
    print('*' * 20 + '\n')

    if not new_candidates:
        sys.exit(1)
    candidate_keyword_phrases.extend(new_candidates)

    if not candidate_keyword_phrases or not word_scores or not stop_words:
        sys.exit(1)
    cumulative_scores_for_candidates = calculate_cumulative_score_for_candidates_with_stop_words(
        candidate_keyword_phrases,
        word_scores,
        stop_words)

    if not cumulative_scores_for_candidates:
        sys.exit(1)
    top_n = get_top_n(keyword_phrases_with_scores=cumulative_scores_for_candidates, top_n=10, max_length=4)

    print(f'TOP N WITH KEYWORDS WITH STOP WORDS: {top_n}')
    print('*' * 20 + '\n')

    # 10

    stop_words_collection = load_stop_words(ASSETS_PATH.joinpath('stopwords.json'))

    # Extracting from unknown language
    unknown_text = read_target_text(ASSETS_PATH.joinpath('unknown.txt'))
    generated_stop_words = generate_stop_words(unknown_text, 4)
    print(f'GENERATED STOP WORDS: {generated_stop_words}')
    print('*' * 20 + '\n')

    phrases = extract_phrases(unknown_text)

    if not phrases or not generated_stop_words:
        sys.exit(1)
    candidate_keyword_phrases = extract_candidate_keyword_phrases(phrases, generated_stop_words)

    if not candidate_keyword_phrases:
        sys.exit(1)
    content_words_with_frequencies = calculate_frequencies_for_content_words(candidate_keyword_phrases)

    if not candidate_keyword_phrases or not content_words_with_frequencies:
        sys.exit(1)
    word_degrees = calculate_word_degrees(candidate_keyword_phrases, list(content_words_with_frequencies.keys()))

    if not word_degrees or not content_words_with_frequencies:
        sys.exit(1)
    word_scores = calculate_word_scores(word_degrees, content_words_with_frequencies)

    if not candidate_keyword_phrases or not word_scores:
        sys.exit(1)
    cumulative_scores_for_candidates = calculate_cumulative_score_for_candidates(candidate_keyword_phrases, word_scores)

    if not cumulative_scores_for_candidates:
        sys.exit(1)
    top_n = get_top_n(keyword_phrases_with_scores=cumulative_scores_for_candidates, top_n=10, max_length=2)
    print(f'KEYWORD PHRASES FOR UNKNOWN TEXT: {top_n}')

    RESULT = top_n

    assert RESULT, 'Keywords are not extracted'
