"""
Lab 4
Summarize text using TextRank algorithm

.. py:class:: EncodedSentence

   Type alias representing an encoded sentence as a tuple of integers.

.. py:class:: PreprocessedSentence

   Type alias representing a preprocessed sentence as a tuple of strings.
"""

# pylint:disable=too-few-public-methods, unused-argument
from typing import Any, Sequence

PreprocessedSentence = tuple[str, ...]
EncodedSentence = tuple[int, ...]


class IncorrectQueryError(ValueError):
    """Raised when a provided input has an invalid type or value."""


def check_sequence(user_input: Any, elements_type: type, can_be_empty: bool) -> bool:
    """
    Checks the type of an object and its elements.

    Args:
        user_input (Any): Object to check.
        elements_type (type): Required type of its elements.
        can_be_empty (bool): Whether the sequence can be empty.

    Returns:
        bool: True if the object is a valid sequence, otherwise False.
    """


def check_dict(user_input: dict, key_type: type, value_type: type, can_be_empty: bool) -> bool:
    """
    Checks whether an object is a dictionary with keys and values of specified types.

    Args:
        user_input (dict): Object to check.
        key_type (type): Required type of dictionary keys.
        value_type (type): Required type of dictionary values.
        can_be_empty (bool): Whether the dictionary can be empty.

    Returns:
        bool: True if the object is a valid dictionary, otherwise False.
    """


class TextPreprocessor:
    """
    A class to preprocess raw text.

    Attributes:
        _stop_words (Sequence[str]): Insignificant words to remove from tokens.
        _punctuation (Sequence[str]): Punctuation symbols to remove during text cleaning.
    """

    def __init__(self, stop_words: Sequence[str], punctuation: Sequence[str]) -> None:
        """
        Initializes the text preprocessor.

        Args:
            stop_words (Sequence[str]): Insignificant words to remove from tokens.
            punctuation (Sequence[str]): Punctuation symbols to remove during text cleaning.
        """

    def _clean_and_tokenize(self, text: str) -> tuple[str, ...]:
        """
        Removes punctuation, converts text to lowercase, and splits it into tokens.

        Args:
            text (str): Raw text.

        Returns:
            tuple[str, ...]: Clean lowercase tokens.
        """

    def _remove_stop_words(self, tokens: Sequence[str]) -> tuple[str, ...]:
        """
        Removes stop words from a sequence of tokens.

        Args:
            tokens (Sequence[str]): Sequence of tokens containing stop words.

        Returns:
            tuple[str, ...]: Sequence of tokens without stop words.
        """

    def preprocess_text(self, text: str) -> tuple[str, ...]:
        """
        Produces filtered, clean, lowercase tokens from raw text.

        Args:
            text (str): Raw text.

        Returns:
            tuple[str, ...]: Clean lowercase tokens without stop words.
        """


class TextEncoder:
    """
    A class to encode a string sequence into a matching integer sequence.

    Attributes:
        _word2id (dict[str, int]): Maps words to integers.
        _id2word (dict[int, str]): Maps integers to words.
    """

    def __init__(self) -> None:
        """
        Initializes empty word-to-ID and ID-to-word mappings.
        """

    def _learn_indices(self, tokens: Sequence[str]) -> None:
        """
        Creates mappings between words and their integer equivalents.

        Args:
            tokens (Sequence[str]): Sequence of string tokens.
        """

    def encode(self, tokens: Sequence[str]) -> tuple[int, ...]:
        """
        Encodes a sequence of string tokens into integer tokens.

        Args:
            tokens (Sequence[str]): Sequence of string tokens.

        Returns:
            tuple[int, ...]: Sequence of integer tokens.
        """

    def decode(self, encoded_tokens: Sequence[int]) -> tuple[str, ...]:
        """
        Decodes a sequence of integer tokens into string tokens.

        Args:
            encoded_tokens (Sequence[int]): Sequence of integer tokens.

        Returns:
            tuple[str, ...]: Sequence of string tokens.
        """


class Sentence:
    """
    An abstraction over a real-world sentence.
    """

    def __init__(self, text: str, position: int) -> None:
        """
        Initializes a sentence with its text and position.

        Args:
            text (str): Text of the sentence.
            position (int): Position of the sentence in the text.
        """

    def get_position(self) -> int:
        """
        Returns the position of the sentence in the text.

        Returns:
            int: Position of the sentence.
        """

    def set_text(self, text: str) -> None:
        """
        Sets the text of the sentence.

        Args:
            text (str): New text of the sentence.
        """

    def get_text(self) -> str:
        """
        Returns the text of the sentence.

        Returns:
            str: Text of the sentence.
        """

    def set_preprocessed(self, preprocessed_sentence: PreprocessedSentence) -> None:
        """
        Sets the preprocessed representation of the sentence.

        Args:
            preprocessed_sentence (PreprocessedSentence): Preprocessed sequence of tokens.
        """

    def get_preprocessed(self) -> PreprocessedSentence:
        """
        Returns the preprocessed representation of the sentence.

        Returns:
            PreprocessedSentence: Preprocessed sequence of tokens.
        """

    def set_encoded(self, encoded_sentence: EncodedSentence) -> None:
        """
        Sets the encoded representation of the sentence.

        Args:
            encoded_sentence (EncodedSentence): Encoded sequence of integers.
        """

    def get_encoded(self) -> EncodedSentence:
        """
        Returns the encoded representation of the sentence.

        Returns:
            EncodedSentence: Encoded sequence of integers.
        """


class SentencePreprocessor(TextPreprocessor):
    """
    Class for sentence preprocessing.
    """

    def _split_by_sentence(self, text: str) -> tuple[Sentence, ...]:
        """
        Splits the provided text into sentences.

        Args:
            text (str): Raw text to split.

        Returns:
            tuple[Sentence, ...]: Sequence of sentences extracted from the text.
        """

    def _preprocess_sentences(self, sentences: Sequence[Sentence]) -> None:
        """
        Preprocesses a sequence of sentences and stores their token representations.

        Args:
            sentences (Sequence[Sentence]): Sequence of sentences to preprocess.
        """

    def get_sentences(self, text: str) -> tuple[Sentence, ...]:
        """
        Extracts and preprocesses sentences from raw text.

        Args:
            text (str): Raw text to process.

        Returns:
            tuple[Sentence, ...]: Sequence of preprocessed sentences.
        """


class SentenceEncoder(TextEncoder):
    """
    A class to encode string sequences into matching integer sequences.
    """

    def __init__(self) -> None:
        """
        Initializes the sentence encoder.
        """

    def _learn_indices(self, tokens: Sequence[str]) -> None:
        """
        Assigns integer IDs to previously unseen tokens.

        Args:
            tokens (Sequence[str]): Sequence of string tokens.
        """

    def encode_sentences(self, sentences: Sequence[Sentence]) -> None:
        """
        Encodes the preprocessed tokens of each sentence.

        Args:
            sentences (Sequence[Sentence]): Sequence of sentences to encode.
        """


def calculate_similarity(sequence: Sequence, other_sequence: Sequence) -> float:
    """
    Calculates the similarity between two sequences using the Jaccard index.

    Args:
        sequence (Sequence): First sequence of items.
        other_sequence (Sequence): Second sequence of items.

    Returns:
        float: Jaccard similarity score between the two sequences.
    """


class SimilarityGraph:
    """
    A class to represent relations between sentences.
    """

    _matrix: list[list[float]]

    def __init__(self) -> None:
        """
        Initializes an empty similarity graph.
        """

    def get_vertices(self) -> tuple[Sentence, ...]:
        """
        Returns all vertices present in the graph.

        Returns:
            tuple[Sentence, ...]: Sequence of vertices in the graph.
        """

    def calculate_inout_score(self, vertex: Sentence) -> int:
        """
        Calculates the number of vertices similar to the specified vertex.

        Args:
            vertex (Sentence): Vertex whose similar vertices should be counted.

        Returns:
            int: Number of similar vertices.
        """

    def _add_vertex(self, vertex: Sentence) -> None:
        """Adds a vertex and updates the similarity matrix for it.

        Args:
            vertex (Sentence): Vertex to add to the graph.
        """

    def add_edge(self, vertex1: Sentence, vertex2: Sentence) -> None:
        """
        Adds or overwrites an edge between two vertices in the graph.

        Args:
            vertex1 (Sentence): First vertex.
            vertex2 (Sentence): Second vertex.
        """

    def get_similarity_score(self, vertex1: Sentence, vertex2: Sentence) -> float:
        """
        Returns the similarity score between two vertices.

        Args:
            vertex1 (Sentence): First vertex.
            vertex2 (Sentence): Second vertex.

        Returns:
            float: Similarity score between the two vertices.
        """

    def fill_from_sentences(self, sentences: Sequence[Sentence]) -> None:
        """
        Updates the graph with vertices and edges extracted from sentences.

        Args:
            sentences (Sequence[Sentence]): Sequence of sentences to add.
        """


class GraphSummarizer:
    """
    Graph based algorithm for text summarization.
    """

    _scores: dict[Sentence, float]
    _graph: SimilarityGraph

    def __init__(self, graph: SimilarityGraph) -> None:
        """
        Initializes a graph summarizer with a similarity graph.

        Args:
            graph (SimilarityGraph): Filled similarity graph.
        """

    def train(self) -> None:
        """
        Computes sentence importance scores in a single pass.
        """

    def get_top_sentences(self, n_sentences: int) -> tuple[Sentence, ...]:
        """
        Retrieves the most important sentences according to their scores.

        Args:
            n_sentences (int): Number of sentences to retrieve.

        Returns:
            tuple[Sentence, ...]: Sequence of the highest-scoring sentences.
        """

    def make_summary(self, n_sentences: int) -> str:
        """
        Constructs a summary from the most important sentences.

        Args:
            n_sentences (int): Number of sentences to include in the summary.

        Returns:
            str: Summary containing the selected sentences in their original order.
        """


class TextRankSummarizer(GraphSummarizer):
    """
    TextRank algorithm for text summarization.
    """

    def __init__(self, graph: SimilarityGraph) -> None:
        """
        Initializes a TextRank summarizer with a similarity graph.

        Args:
            graph (SimilarityGraph): Filled similarity graph.
        """

    def update_vertex_score(
        self,
        vertex: Sentence,
        incidental_vertices: Sequence[Sentence],
        scores: dict[Sentence, float],
    ) -> None:
        """
        Updates a vertex significance score using the TextRank formula.

        Args:
            vertex (Sentence): Sentence whose score should be updated.
            incidental_vertices (Sequence[Sentence]): Vertices related to the sentence.
            scores (dict[Sentence, float]): Current scores of all vertices.
        """

    def train(self) -> None:
        """
        Iteratively calculates significance scores for all vertices until convergence.
        """
