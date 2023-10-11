"""Lab 3.

Extract keywords based on TextRank algorithm
"""
from itertools import combinations
from pathlib import Path
from time import ctime
from typing import Optional, Union

from lab_1_keywords_tfidf.main import (
    calculate_frequencies,
    calculate_tf,
    calculate_tfidf,
)
from lab_2_keywords_cooccurrence.main import (
    extract_phrases,
    extract_candidate_keyword_phrases,
    calculate_frequencies_for_content_words,
    calculate_word_scores,
    calculate_word_degrees,
)

PROJECT_ROOT = Path(__file__).parent
ASSETS_PATH = PROJECT_ROOT / 'assets'


class TextPreprocessor:
    """A class to preprocess raw text.

    Attributes:
        _stop_words (tuple[str, ...]): Insignificant words to remove from tokens
        _punctuation (tuple[str, ...]): Punctuation symbols to remove during text cleaning
    """

    # 4
    def __init__(self, stop_words: tuple[str, ...], punctuation: tuple[str, ...]) -> None:
        """Construct all the necessary attributes for the text preprocessor object.

        Args:
            stop_words (tuple[str, ...]): Insignificant words to remove from tokens
            punctuation (tuple[str, ...]): Punctuation symbols to remove during text cleaning
        """
        self._stop_words = stop_words
        self._punctuation = punctuation

    # 4
    def _clean_and_tokenize(self, text: str) -> tuple[str, ...]:
        """Remove punctuation, cast to lowercase, split into tokens.

        Args:
            text (str): Raw text

        Returns:
            tuple[str, ...]: Clean lowercase tokens
        """
        for symbol in self._punctuation:
            text = text.replace(symbol, "")
        return tuple(text.lower().split())

    # 4
    def _remove_stop_words(self, tokens: tuple[str, ...]) -> tuple[str, ...]:
        """Filter tokens, removing stop words.

        Args:
            tokens (tuple[str, ...]): Tokens containing stop-words

        Returns:
            tuple[str, ...]: Tokens without stop-words
        """
        return tuple(token for token in tokens if token not in self._stop_words)

    # 4
    def preprocess_text(self, text: str) -> tuple[str, ...]:
        """Produce filtered clean lowercase tokens from raw text.

        Args:
            text (str): Raw text

        Returns:
            tuple[str, ...]: Clean lowercase tokens with no stop-words
        """
        tokens = self._clean_and_tokenize(text)
        return self._remove_stop_words(tokens)


# 4
class TextEncoder:
    """A class to encode string sequence into matching integer sequence.

    Attributes:
        _word2id (dict[str, int]): Maps words to integers
        _id2word (dict[int, str]): Maps integers to words
    """

    def __init__(self) -> None:
        """Construct all the necessary attributes for the text encoder object."""
        self._word2id = {}
        self._id2word = {}

    def _learn_indices(self, tokens: tuple[str, ...]) -> None:
        """Fill attributes mapping words and integer equivalents to each other.

        Args:
            tokens (tuple[str, ...]): Sequence of string tokens
        """
        self._word2id = {token: id + 1000 for id, token in enumerate(set(tokens))}
        self._id2word = {id: token for token, id in self._word2id.items()}

    def encode(self, tokens: tuple[str, ...]) -> Optional[tuple[int, ...]]:
        """Encode input sequence of string tokens to sequence of integer tokens.

        Args:
            tokens (tuple[str, ...]): Sequence of string tokens

        Returns:
            tuple[int, ...]: Sequence of integer tokens

        In case of empty tokens input data, None is returned
        """
        if not tokens:
            return None
        self._learn_indices(tokens)
        return tuple(self._word2id[token] for token in tokens)

    def decode(self, encoded_tokens: tuple[int, ...]) -> Optional[tuple[str, ...]]:
        """Decode input sequence of integer tokens to sequence of string tokens.

        Args:
            encoded_tokens (tuple[int, ...]): Sequence of integer tokens

        Returns:
            tuple[str, ...]: Sequence of string tokens

        In case of out-of-dictionary input data, None is returned
        """
        if not all(token in self._id2word.keys() for token in encoded_tokens):
            return None
        return tuple(self._id2word[token] for token in encoded_tokens)


# 4
def extract_pairs(tokens: tuple[int, ...], window_length: int) -> Optional[tuple[tuple[int, ...], ...]]:
    """Retrieve all pairs of co-occurring words in the token sequence.

    Args:
        tokens (tuple[int, ...]): Sequence of tokens
        window_length (int): Maximum distance between co-occurring tokens: tokens are considered co-occurring if they appear in the same window of this length

    Returns:
        tuple[tuple[int, ...], ...]: Pairs of co-occurring tokens

    In case of corrupt input data, None is returned:
    tokens must not be empty, window lengths must be integer, window lengths cannot be less than 2.
    """
    if not tokens or not isinstance(window_length, int):
        return None
    if window_length < 2:
        return None
    pairs = []
    for window_start in range(0, (len(tokens) - window_length)):
        window_end = window_start + window_length
        window = tokens[window_start:window_end]
        cooccurrences = set(combinations(window, 2))
        for pair in cooccurrences:
            if not pair[0] == pair[1]:
                pairs.append(pair)
    return tuple(set(pairs))


# 6
class AdjacencyMatrixGraph:
    """A class to represent graph as matrix of adjacency.

    Attributes:
        _matrix (list[list[int]]): Stores information about vertices interrelation
        _positions (dict[int, list[int]]): Stores information about positions in text
    """

    _matrix: list[list[int]]
    _vertices: dict[int, int]
    _positions: dict[int, list[int]]
    _position_weights: dict[int, float]

    def __init__(self) -> None:
        """Construct all the necessary attributes for the adjacency matrix graph object."""
        self._matrix = []
        self._vertices = {}
        self._positions = {}
        self._position_weights = {}

    def get_vertices(self) -> tuple[int, ...]:
        """Return a sequence of all vertices present in the graph.

        Returns:
            tuple[int, ...]: A sequence of vertices present in the graph
        """
        return tuple(self._vertices.keys())

    def _extend_matrix_by_one(self) -> None:
        """Add one dimension to the matrix, increasing number of rows and number of columns by one."""
        for index in range(len(self._vertices)):
            self._matrix[index].append(0)
        self._matrix.append([0 for _ in range(len(self._vertices) + 1)])

    def _add_vertex(self, vertex: int) -> None:
        """Record information about a new vertex and assigns a sequence number to it.

        Args:
            vertex (int): Vertex to add
        """
        if vertex not in self._vertices:
            self._vertices[vertex] = len(self._vertices)

    def _get_vertex_index(self, vertex: int) -> int:
        """Retrieve a sequence number of the specified vertex.

        Args:
            vertex (int): A vertex for which to retrieve a sequence number

        Returns:
            int: Sequence number of the specified vertex

        In case of corrupt input data, None is returned
        """
        if vertex not in self.get_vertices():
            return -1
        return self._vertices[vertex]

    def add_edge(self, vertex1: int, vertex2: int) -> int:
        """Add or overwrite an edge in the graph between the specified vertices.

        Args:
            vertex1 (int): The first vertex incidental to the added edge
            vertex2 (int): The second vertex incidental to the added edge

        Returns:
            int: 0 if edge was added successfully, otherwise -1

        In case of vertex1 being equal to vertex2, -1 is returned as loops are prohibited
        """
        if vertex1 == vertex2:
            return -1
        if not self._vertices:
            self._matrix = [[0, 0], [0, 0]]
            self._add_vertex(vertex1)
            self._add_vertex(vertex2)
        else:
            if vertex1 not in self._vertices:
                self._extend_matrix_by_one()
                self._add_vertex(vertex1)
            if vertex2 not in self._vertices:
                self._extend_matrix_by_one()
                self._add_vertex(vertex2)

        index_vertex1 = self._get_vertex_index(vertex1)
        index_vertex2 = self._get_vertex_index(vertex2)
        if index_vertex1 != -1 or index_vertex2 != -1:
            self._matrix[index_vertex1][index_vertex2] = 1
            self._matrix[index_vertex2][index_vertex1] = 1
        return 0

    def is_incidental(self, vertex1: int, vertex2: int) -> int:
        """Retrieve information about whether the two vertices are incidental.

        Args:
            vertex1 (int): The first vertex incidental to the edge sought
            vertex2 (int): The second vertex incidental to the edge sought

        Returns:
            int: 1 if vertices are incidental, otherwise 0

        If either of vertices is not present in the graph, -1 is returned
        """
        index_vertex1 = self._get_vertex_index(vertex1)
        index_vertex2 = self._get_vertex_index(vertex2)
        if index_vertex1 == -1 or index_vertex2 == -1:
            return -1
        return self._matrix[index_vertex1][index_vertex2]

    def calculate_inout_score(self, vertex: int) -> int:
        """Retrieve a number of incidental vertices to a specified vertex.

        Args:
            vertex (int): A vertex to calculate inout score for

        Returns:
            int: Number of incidental vertices

        If vertex is not present in the graph, -1 is returned
        """
        vertex_index = self._get_vertex_index(vertex)
        if vertex_index == -1:
            return -1
        return sum(self._matrix[vertex_index])

    def fill_from_tokens(self, tokens: tuple[int, ...], window_length: int) -> None:
        """Update graph instance with vertices and edge extracted from tokenized text.

        Args:
            tokens (tuple[int, ...]): Sequence of tokens
            window_length (int): Maximum distance between co-occurring tokens: tokens are considered co-occurring if they appear in the same window of this length
        """
        edges = extract_pairs(tokens, window_length)
        for vertex1, vertex2 in edges:
            self.add_edge(vertex1, vertex2)

    def fill_positions(self, tokens: tuple[int, ...]) -> None:
        """Save information about all positions of each vertex in the token sequence.

        Args:
            tokens (tuple[int, ...]): Sequence of tokens
        """
        positions = {token: [] for token in tokens}
        for position, token in enumerate(tokens):
            positions[token].append(position + 1)
        self._positions = positions

    def calculate_position_weights(self) -> None:
        """Compute position weights for all tokens in text."""
        position_weights = {}
        for vertex, positions in self._positions.items():
            position_weights[vertex] = sum([1 / position for position in positions])
        position_weights_sum = sum(position_weights.values())
        position_weights_norm = {vertex: position_weight / position_weights_sum
                                 for vertex, position_weight in position_weights.items()}
        self._position_weights = position_weights_norm

    def get_position_weights(self) -> dict[int, float]:
        """Retrieve position weights for all vertices in the graph.

        Returns:
            dict[int, float]: Position weights for all vertices in the graph
        """
        return self._position_weights


# 8
class EdgeListGraph:
    """A class to represent graph as a list of edges.

    Attributes:
        _edges (dict[int, list[int]]): Stores information about vertices interrelation
    """

    def __init__(self) -> None:
        """Construct all the necessary attributes for the edge list graph object."""
        self._edges = {}
        self._positions = {}
        self._position_weights = {}

    def get_vertices(self) -> tuple[int, ...]:
        """Return a sequence of all vertices present in the graph.

        Returns:
            tuple[int, ...]: A sequence of vertices present in the graph
        """
        return tuple(list(self._edges.keys()))

    def add_edge(self, vertex1: int, vertex2: int) -> int:
        """Add or overwrite an edge in the graph between the specified vertices.

        Args:
            vertex1 (int): The first vertex incidental to the added edge
            vertex2 (int): The second vertex incidental to the added edge

        Returns:
            int: 0 if edge was added successfully, otherwise -1

        In case of vertex1 being equal to vertex2, -1 is returned as loops are prohibited
        """
        if vertex1 == vertex2:
            return -1
        if vertex1 not in self._edges:
            self._edges[vertex1] = []
        if vertex2 not in self._edges:
            self._edges[vertex2] = []
        if not self.is_incidental(vertex1, vertex2) == 1:
            self._edges[vertex1].append(vertex2)
            self._edges[vertex2].append(vertex1)
        return 0

    def is_incidental(self, vertex1: int, vertex2: int) -> int:
        """Retrieve information about whether the two vertices are incidental.

        Args:
            vertex1 (int): The first vertex incidental to the edge sought
            vertex2 (int): The second vertex incidental to the edge sought

        Returns:
            int: 1 if vertices are incidental, otherwise 0

        If either of vertices is not present in the graph, -1 is returned
        """
        if vertex1 not in self.get_vertices() or vertex2 not in self.get_vertices():
            return -1
        return 1 if vertex1 in self._edges.get(vertex2, []) else 0

    def calculate_inout_score(self, vertex: int) -> int:
        """Retrieve a number of incidental vertices to a specified vertex.

        Args:
            vertex (int): A vertex to calculate inout score for

        Returns:
            int: Number of incidental vertices

        If vertex is not present in the graph, -1 is returned
        """
        if vertex not in self.get_vertices():
            return -1
        inout = len(self._edges[vertex])
        return inout

    def fill_from_tokens(self, tokens: tuple[int, ...], window_length: int) -> None:
        """Update graph instance with vertices and edge extracted from tokenized text.

        Args:
            tokens (tuple[int, ...]): Sequence of tokens
            window_length (int): Maximum distance between co-occurring tokens: tokens are considered co-occurring if they appear in the same window of this length
        """
        edges = extract_pairs(tokens, window_length)
        for vertex1, vertex2 in edges:
            self.add_edge(vertex1, vertex2)

    def fill_positions(self, tokens: tuple[int, ...]) -> None:
        """Save information on all positions of each vertex in the token sequence.

        Args:
            tokens (tuple[int, ...]): Sequence of tokens
        """
        positions = {token: [] for token in tokens}
        for position, token in enumerate(tokens):
            positions[token].append(position + 1)
        self._positions = positions

    def calculate_position_weights(self) -> None:
        """Compute position weights for all tokens in text."""
        position_weights = {}
        for vertex, positions in self._positions.items():
            position_weights[vertex] = sum([1 / position for position in positions])
        position_weights_sum = sum(position_weights.values())
        position_weights_norm = {vertex: position_weight / position_weights_sum
                                 for vertex, position_weight in position_weights.items()}
        self._position_weights = position_weights_norm

    def get_position_weights(self) -> dict[int, float]:
        """Retrieve position weights for all vertices in the graph.

        Returns:
            dict[int, float]: Position weights for all vertices in the graph
        """
        return self._position_weights


# 6
class VanillaTextRank:
    """Basic TextRank implementation.

    Attributes:
        _graph (Union[AdjacencyMatrixGraph, EdgeListGraph]): A graph representing the text
        _damping_factor (float): Probability of jumping from a given vertex to another random vertex in the graph during vertices scores calculation
        _convergence_threshold (float): Maximal acceptable difference between the vertices scores in two consequent iteration
        _max_iter (int): Maximal number of iterations to perform
        _scores (dict[int, float]): Scores of significance for all vertices present in the graph
    """

    _scores: dict[int, float]

    def __init__(self, graph: Union[AdjacencyMatrixGraph, EdgeListGraph]) -> None:
        """Construct all the necessary attributes for the text rank algorithm implementation.

        Args:
            graph (Union[AdjacencyMatrixGraph, EdgeListGraph]): A graph representing the text
        """
        self._graph = graph

        self._damping_factor = 0.85
        self._convergence_threshold = 0.0001
        self._max_iter = 50

        self._scores = {}

    def update_vertex_score(self, vertex: int, incidental_vertices: list[int], scores: dict[int, float]) -> None:
        """Change vertex significance score using algorithm-specific formula.

        Args:
            vertex (int): A vertex which significance score is updated
            incidental_vertices (list[int]): Vertices incidental to the scored one
            scores (dict[int, float]): Scores of all vertices in the graph
        """
        summation = 0.0
        for incidental_vertex in incidental_vertices:
            incidental_vertex_score = scores[incidental_vertex]
            incidental_vertex_inout = self._graph.calculate_inout_score(incidental_vertex)
            if not incidental_vertex_inout == -1:
                summation += ((1 / incidental_vertex_inout) * incidental_vertex_score)
        self._scores[vertex] = (1 - self._damping_factor) + self._damping_factor * summation

    def train(self) -> None:
        """Compute iteratively significance scores for vertices."""
        vertices = self._graph.get_vertices()
        for vertex in vertices:
            self._scores[vertex] = 1.0

        for iteration in range(0, self._max_iter):
            prev_score = self._scores.copy()
            for scored_vertex in vertices:
                incidental_vertices = [vertex for vertex in vertices
                                       if self._graph.is_incidental(scored_vertex, vertex) == 1]
                self.update_vertex_score(scored_vertex, incidental_vertices, prev_score)
            abs_score_diff = [abs(i - j) for i, j in zip(prev_score.values(), self._scores.values())]
            if not iteration % 10:
                print("Iteration", iteration, ctime())
            if sum(abs_score_diff) <= self._convergence_threshold:  # convergence condition
                print("Converging at iteration " + str(iteration) + "...")
                break

    def get_scores(self) -> dict[int, float]:
        """Retrieve importance scores of all tokens in the encoded text.

        Returns:
            dict[int, float]: Importance scores of all tokens in the encoded text
        """
        return self._scores

    def get_top_keywords(self, n_keywords: int) -> tuple[int, ...]:
        """Retrieve top n most important tokens in the encoded text.

        Args:
            n_keywords (int): Requested number of keywords to extract

        Returns:
            tuple[int, ...]: Top n most important tokens in the encoded text
        """
        return tuple(sorted(self.get_scores().keys(), key=lambda x: (self._scores[x], -x), reverse=True)[:n_keywords])


# 8
class PositionBiasedTextRank(VanillaTextRank):
    """Advanced TextRank implementation: positions of tokens in text are taken into consideration.

    Attributes:
        _graph (Union[AdjacencyMatrixGraph, EdgeListGraph]): A graph representing the text
        _damping_factor (float): Probability of jumping from a given vertex to another random vertex in the graph during vertices scores calculation
        _convergence_threshold (float): Maximal acceptable difference between the vertices scores in two consequent iteration
        _max_iter (int): Maximal number of iterations to perform
        _scores (dict[int, float]): Scores of significance for all vertices present in the graph
        _position_weights (dict[int, float]): Position weights for all tokens in the text
    """

    def __init__(self, graph: Union[AdjacencyMatrixGraph, EdgeListGraph]) -> None:
        """Construct all the necessary attributes for the position-aware text rank algorithm implementation.

        Args:
            graph (Union[AdjacencyMatrixGraph, EdgeListGraph]): A graph representing the text
        """
        super().__init__(graph)
        self._position_weights = self._graph.get_position_weights()

    def update_vertex_score(self, vertex: int, incidental_vertices: list[int], scores: dict[int, float]) -> None:
        """Change vertex significance score using algorithm-specific formula.

        Args:
            vertex (int): A vertex which significance score is updated
            incidental_vertices (list[int]): Vertices incidental to the scored one
            scores (dict[int, float]): Scores of all vertices in the graph
        """
        summation = 0.0
        for incidental_vertex in incidental_vertices:
            incidental_vertex_score = scores[incidental_vertex]
            incidental_vertex_inout = self._graph.calculate_inout_score(incidental_vertex)
            if not incidental_vertex_inout == -1:
                summation += (1 / incidental_vertex_inout * incidental_vertex_score)
        self._scores[vertex] = (1 - self._damping_factor) * self._position_weights[vertex]\
                                + self._damping_factor * summation


# 10
BENCHMARK_MATERIAL_PATH = ASSETS_PATH / 'benchmark_materials'
IDF_PATH = BENCHMARK_MATERIAL_PATH / 'IDF.json'
ENG_STOP_WORDS_PATH = BENCHMARK_MATERIAL_PATH / 'eng_stop_words.txt'


class TFIDFAdapter:
    """A class to unify the interface of TF-IDF keywords extractor with TextRank algorithms.

    Attributes:
        _tokens (tuple[str, ...]): Sequence of tokens from which to extract keywords
        _idf (dict[str, float]): Inverse Document Frequency scores for tokens
        _scores (dict[str, float]): TF-IDF scores reflecting how important each token is
    """

    _scores: dict[str, float]

    def __init__(self, tokens: tuple[str, ...], idf: dict[str, float]) -> None:
        """Construct all the necessary attributes for the TF-IDF keywords extractor.

        Args:
            tokens (tuple[str, ...]): Sequence of tokens from which to extract keywords
            idf (dict[str, float]): Inverse Document Frequency scores for tokens
        """
        self._tokens = tokens
        self._idf = idf
        self._scores = {}

    def train(self) -> int:
        """Compute importance scores for all tokens.

        Returns:
            int: 0 if importance scores were calculated successfully, otherwise -1
        """
        frequencies = calculate_frequencies(list(self._tokens))
        if not frequencies:
            return -1
        tf_scores = calculate_tf(frequencies)
        if not tf_scores:
            return -1
        tfidf_scores = calculate_tfidf(tf_scores, self._idf)
        if not tfidf_scores:
            return -1
        self._scores = tfidf_scores
        return 0

    def get_scores(self) -> dict[str, float]:
        """Retrieve importance scores for each of the tokens.

        Returns:
            dict[str, float]: Dictionary with importance scores calculated
        """
        return self._scores

    def get_top_keywords(self, n_keywords: int) -> tuple[str, ...]:
        """Retrieve a requested number of the most important tokens.

        Args:
            n_keywords (int): Requested number of keywords to extract

        Returns:
            tuple[str, ...]: A requested number tokens with the highest importance scores
        """
        return tuple(sorted(self.get_scores().keys(), key=lambda x: (-self.get_scores()[x], x))[:n_keywords])


class RAKEAdapter:
    """A class to unify the interface of RAKE keywords extractor with TextRank algorithms.

    Attributes:
        _text (str): A text from which to extract keywords
        _stop_words (tuple[str, ...]): A sequence of stop-words
        _scores (dict[str, float]): Word scores reflecting how important each token is
    """

    _scores: dict[str, float]

    def __init__(self, text: str, stop_words: tuple[str, ...]) -> None:
        """Construct all the necessary attributes for the RAKE keywords extractor.

        Args:
            text (str): A text from which to extract keywords
            stop_words (tuple[str, ...]): A sequence of stop-words
        """
        self._text = text
        self._stop_words = stop_words
        self._scores = {}

    def train(self) -> int:
        """Compute importance scores for all tokens.

        Returns:
            int: 0 if importance scores were calculated successfully, otherwise -1
        """
        phrases = extract_phrases(self._text)
        if not phrases:
            return -1
        candidate_keywords_phrases = extract_candidate_keyword_phrases(phrases, list(self._stop_words))
        if not candidate_keywords_phrases:
            return -1
        frequencies = calculate_frequencies_for_content_words(candidate_keywords_phrases)
        if not frequencies:
            return -1
        content_words = list(frequencies.keys())
        word_degrees = calculate_word_degrees(candidate_keywords_phrases, content_words)
        if not word_degrees:
            return -1
        word_scores = calculate_word_scores(word_degrees, frequencies)
        if not word_scores:
            return -1
        self._scores = dict(word_scores)
        return 0

    def get_scores(self) -> dict[str, float]:
        """Retrieve importance scores for each of the tokens.

        Returns:
            dict[str, float]: Dictionary with importance scores calculated
        """
        return self._scores

    def get_top_keywords(self, n_keywords: int) -> tuple[str, ...]:
        """Retrieve a requested number of the most important tokens.

        Args:
            n_keywords (int): Requested number of keywords to extract

        Returns:
            tuple[str, ...]: A requested number tokens with the highest importance scores
        """
        return tuple(sorted(self.get_scores().keys(), key=lambda x: (-self.get_scores()[x], x))[:n_keywords])


def calculate_recall(predicted: tuple[str, ...], target: tuple[str, ...]) -> float:
    """Compute recall metric.

    Args:
        predicted (tuple[str, ...]): Keywords predictions of an algorithm to estimate
        target (tuple[str, ...]): Ground truth keywords

    Returns:
        float: Recall value
    """
    tp_rate = len([pred_kw for pred_kw in predicted if pred_kw in target])
    fn_rate = len([true_kw for true_kw in target if true_kw not in predicted])
    recall = tp_rate / (tp_rate + fn_rate)
    return recall


class KeywordExtractionBenchmark:
    """A class to compare 4 different algorithms of keywords extraction.

    Attributes:
        _stop_words (tuple[str, ...]): A sequence of stop-words
        _punctuation (tuple[str, ...]): Symbols of punctuation
        _idf (dict[str, float]): Inverse Document Frequency scores for the words in materials
        _materials_path (Path): A path to materials to use for comparison
        themes (tuple[str, ...]): A sequence of topics to which comparison materials relate
        report (dict[str, dict[str, float]]): Comparison report reflecting how successfully each model extracts keywords
    """

    def __init__(self, stop_words: tuple[str, ...], punctuation: tuple[str, ...],
                 idf: dict[str, float], materials_path: Path) -> None:
        """Construct all the necessary attributes for the Benchmark instance.

        Args:
            stop_words (tuple[str, ...]): A sequence of stop-words
            punctuation (tuple[str, ...]): Symbols of punctuation
            idf (dict[str, float]): Inverse Document Frequency scores for the words in materials
            materials_path (Path): A path to materials to use for comparison
        """
        self._stop_words = stop_words
        self._punctuation = punctuation
        self._idf = idf

        self._materials_path = materials_path
        self.themes = ('culture', 'business', 'crime',
                       'fashion', 'health', 'politics',
                       'science', 'sports', 'tech')

        self.report = {}

    def retrieve_text(self, theme: str) -> str:
        """Retrieve the text from which to extract keywords by the theme requested.

        Args:
            theme (str): Requested theme

        Returns:
            str: The text from which to extract keywords
        """
        theme_index = self.themes.index(theme)
        path = self._materials_path / f"{theme_index}_text.txt"
        with open(path, 'r', encoding='utf-8') as text_file:
            text = text_file.read()
        return text

    def retrieve_keywords(self, theme: str) -> tuple[str, ...]:
        """Retrieve the ground truth keywords by the theme requested.

        Args:
            theme (str): Requested theme

        Returns:
            tuple[str, ...]: A sequence of ground truth keywords
        """
        theme_index = self.themes.index(theme)
        path = self._materials_path / f"{theme_index}_keywords.txt"
        with open(path, 'r', encoding='utf-8') as kw_file:
            keywords = tuple(keyword.strip() for keyword in kw_file.readlines())
        return keywords

    def run(self) -> Optional[dict[str, dict[str, float]]]:
        """Create comparison report.

        Returns:
            Optional[dict[str, dict[str, float]]]: comparison report

        In case it is impossible to extract keywords due to corrupt inputs, None is returned
        """
        report = {name: {} for name in ['TF-IDF', 'RAKE', 'VanillaTextRank', 'PositionBiasedTextRank']}
        for theme in self.themes:
            text = self.retrieve_text(theme)
            target_keywords = self.retrieve_keywords(theme)

            text_preprocessor = TextPreprocessor(self._stop_words, self._punctuation)
            preprocessed_text = text_preprocessor.preprocess_text(text)

            text_encoder = TextEncoder()
            encoded_tokens = text_encoder.encode(preprocessed_text)
            if not encoded_tokens:
                return None

            graph = EdgeListGraph()
            graph.fill_from_tokens(encoded_tokens, 3)
            graph.fill_positions(encoded_tokens)
            graph.calculate_position_weights()

            tfidf = TFIDFAdapter(preprocessed_text, self._idf)
            rake = RAKEAdapter(text, self._stop_words)
            basic_text_rank = VanillaTextRank(graph)
            advanced_text_rank = PositionBiasedTextRank(graph)

            for algorithm, name in zip([tfidf, rake, basic_text_rank, advanced_text_rank],
                                       ['TF-IDF', 'RAKE', 'VanillaTextRank', 'PositionBiasedTextRank']):
                algorithm.train()
                predicted_keywords = algorithm.get_top_keywords(50)
                if 'TextRank' in name:
                    predicted_keywords = text_encoder.decode(predicted_keywords)
                recall = calculate_recall(predicted_keywords, target_keywords)
                report[name][theme] = recall
        self.report = report
        return report

    def save_to_csv(self, path: Path) -> None:
        """Save comparison report to csv.

        Args:
            path (Path): A path where to save the report file
        """
        title_row = ['name'] + list(self.themes)
        rows = []
        for key in self.report:
            row = [key]
            for theme in self.report[key]:
                row.append(str(self.report[key][theme]))
            rows.append(row)
        all_rows = [title_row] + rows
        report = '\n'.join([','.join(row) for row in all_rows])

        with open(path, 'w', encoding='utf-8') as report_file:
            report_file.write(report)
