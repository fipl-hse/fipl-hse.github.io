"""
TextRank keyword extraction starter
"""
import json
from pathlib import Path
from string import punctuation
# import sys
# from time import time

from lab_3_keywords_textrank.main import (
    # TextPreprocessor,
    # TextEncoder,
    # VanillaTextRank,
    # PositionBiasedTextRank,
    # AdjacencyMatrixGraph,
    # EdgeListGraph,
    KeywordExtractionBenchmark,
    BENCHMARK_MATERIAL_PATH,
    ENG_STOP_WORDS_PATH,
    IDF_PATH
)


if __name__ == "__main__":

    # finding paths to the necessary utils
    PROJECT_ROOT = Path(__file__).parent
    ASSETS_PATH = PROJECT_ROOT / 'assets'

    # # reading the text from which keywords are going to be extracted
    # TARGET_TEXT_PATH = ASSETS_PATH / 'article.txt'
    # with open(TARGET_TEXT_PATH, 'r', encoding='utf-8') as file:
    #     text = file.read()
    #
    # # reading list of stop words
    # STOP_WORDS_PATH = ASSETS_PATH / 'stop_words.txt'
    # with open(STOP_WORDS_PATH, 'r', encoding='utf-8') as file:
    #     stop_words = tuple(file.read().split('\n'))
    #
    # # text preprocessing
    # text_preprocessor = TextPreprocessor(stop_words, tuple(punctuation))
    # preprocessed_text = text_preprocessor.preprocess_text(text)
    #
    # # text encoding
    # text_encoder = TextEncoder()
    # encoded_tokens = text_encoder.encode(preprocessed_text)
    # if not encoded_tokens:
    #     sys.exit()
    #
    # # basic TR with matrix graph
    # start = time()
    #
    # matrix_graph = AdjacencyMatrixGraph()
    # matrix_graph.fill_from_tokens(encoded_tokens, 3)
    # matrix_graph.fill_positions(encoded_tokens)
    # matrix_graph.calculate_position_weights()
    #
    # text_rank_basic = VanillaTextRank(matrix_graph)
    # text_rank_basic.train()
    # encoded_keywords = text_rank_basic.get_top_keywords(10)
    #
    # if not encoded_keywords:
    #     sys.exit()
    # decoded_keywords = text_encoder.decode(encoded_keywords)
    #
    # print('Basic TR with Matrix graph:', decoded_keywords)
    # print('it took', round(time() - start, 2), 'seconds\n')
    # scores_basic_matrix = text_rank_basic.get_scores()
    #
    # # basic TR with list graph
    # start = time()
    #
    # edge_list_graph = EdgeListGraph()
    # edge_list_graph.fill_from_tokens(encoded_tokens, 3)
    # edge_list_graph.fill_positions(encoded_tokens)
    # edge_list_graph.calculate_position_weights()
    #
    # text_rank_basic = VanillaTextRank(edge_list_graph)
    # text_rank_basic.train()
    # encoded_keywords = text_rank_basic.get_top_keywords(10)
    # if not encoded_keywords:
    #     sys.exit()
    # decoded_keywords = text_encoder.decode(encoded_keywords)
    #
    # print('Basic TR with Edge graph:', decoded_keywords)
    # print('it took', round(time() - start, 2), 'seconds\n')
    # scores_basic_edge = text_rank_basic.get_scores()
    #
    # assert scores_basic_edge == scores_basic_matrix
    #
    # # advanced TR with matrix graph
    # start = time()
    #
    # text_rank_advanced = PositionBiasedTextRank(matrix_graph)
    # text_rank_advanced.train()
    # encoded_keywords = text_rank_advanced.get_top_keywords(10)
    # if not encoded_keywords:
    #     sys.exit()
    # decoded_keywords = text_encoder.decode(encoded_keywords)
    #
    # print('Advanced TR with Matrix graph:', decoded_keywords)
    # print('it took', round(time() - start, 2), 'seconds\n')
    # scores_advanced_matrix = text_rank_advanced.get_scores()
    #
    # # advanced TR with edge graph
    # start = time()
    #
    # text_rank_advanced = PositionBiasedTextRank(edge_list_graph)
    # text_rank_advanced.train()
    # encoded_keywords = text_rank_advanced.get_top_keywords(10)
    # if not encoded_keywords:
    #     sys.exit()
    # decoded_keywords = text_encoder.decode(encoded_keywords)
    #
    # print('Advanced TR with Edge graph:', decoded_keywords)
    # print('it took', round(time() - start, 2), 'seconds\n')
    # scores_advanced_edge = text_rank_advanced.get_scores()
    #
    # assert scores_advanced_edge == scores_advanced_matrix

    # 10
    with open(IDF_PATH, 'r', encoding='utf-8') as file:
        idf = json.load(file)

    with open(ENG_STOP_WORDS_PATH, 'r', encoding='utf-8') as sw_file:
        eng_stop_words = tuple(sw_file.read().split('\n'))

    benchmark = KeywordExtractionBenchmark(eng_stop_words, tuple(punctuation), idf, BENCHMARK_MATERIAL_PATH)
    report = benchmark.run()
    report_path = Path(PROJECT_ROOT / 'report.csv')
    benchmark.save_to_csv(report_path)

    RESULT = report
    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT, 'Keywords are not extracted'
