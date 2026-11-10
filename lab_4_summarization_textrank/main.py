"""
Lab 4
Summarize text using TextRank algorithm

.. py:type:: EncodedSentence

   Type alias representing an encoded sentence as a tuple of integers.

.. py:type:: PreprocessedSentence

   Type alias representing a preprocessed sentence as a tuple of strings.
"""

# pylint:disable=too-few-public-methods, unused-argument
from typing import Any, Sequence

PreprocessedSentence = tuple[str, ...]
EncodedSentence = tuple[int, ...]


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


def calculate_frequencies(tokens: Sequence[str]) -> dict[str, int]:
    """
    Calculates the frequency of each token in a token sequence.

    Args:
        tokens (Sequence[str]): Token sequence to count frequencies for.

    Returns:
        dict[str, int]: Dictionary containing each token and its
        number of occurrences.
    """


def load_idf(idf_path: str) -> dict[str, float]:
    """
    Read and retrieve dictionary of type <token: idf>.

    Args:
        idf_path (str): A path to the saved idfs

    Returns:
        dict[str, float]: A dictionary where key - token, value - idf.
    """


def calculate_tf(frequencies: dict[str, int]) -> dict[str, float]:
    """
    Calculates Term Frequency scores for each token based on raw frequency.

    Args:
        frequencies (dict[str, int]): Raw number of occurrences for each token.

    Returns:
        dict[str, float]: Dictionary containing tokens and their
        corresponding Term Frequency scores.
    """


def calculate_tfidf(term_freq: dict[str, float], idf: dict[str, float]) -> dict[str, float]:
    """
    Calculates TF-IDF scores for tokens using their TF and IDF scores.

    Args:
        term_freq (dict[str, float]): Dictionary containing tokens and their
            Term Frequency scores.
        idf (dict[str, float]): Dictionary containing tokens and their
            inverse document frequency scores.

    Returns:
        dict[str, float]: Dictionary containing tokens and their
        corresponding TF-IDF values.
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


class TFIDFAdapter:
    """
    A class to unify the interface of a TF-IDF keyword extractor with TextRank algorithms.

    Attributes:
        _tokens (Sequence[str]): Sequence of tokens from which to extract keywords.
        _idf (dict[str, float]): Inverse Document Frequency scores for tokens.
        _scores (dict[str, float]): TF-IDF scores reflecting token importance.
    """

    def __init__(self, tokens: Sequence[str], idf: dict[str, float]) -> None:
        """
        Initializes the TF-IDF keyword extractor.

        Args:
            tokens (Sequence[str]): Sequence of tokens from which to extract keywords.
            idf (dict[str, float]): Inverse Document Frequency scores for tokens.
        """

    def train(self) -> int:
        """
        Calculates TF-IDF importance scores for all tokens.

        Returns:
            int: 0 if importance scores were calculated successfully,
            otherwise -1.
        """

    def get_top_keywords(self, n_keywords: int) -> tuple[str, ...]:
        """
        Retrieves the requested number of the most important tokens.

        Args:
            n_keywords (int): Number of keywords to extract.

        Returns:
            tuple[str, ...]: Tokens with the highest importance scores.
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

    def __init__(self, stop_words: Sequence[str], punctuation: Sequence[str]) -> None:
        """
        Initializes a sentence preprocessor.

        Args:
            stop_words (Sequence[str]): Words to remove during preprocessing.
            punctuation (Sequence[str]): Punctuation symbols to remove.
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


class TextRankSummarizer:
    """
    TextRank algorithm for text summarization.
    """

    _scores: dict[Sentence, float]
    _graph: SimilarityGraph

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


class Buddy:
    """
    (Almost) All-knowing entity.
    """

    def __init__(
        self,
        paths_to_texts: Sequence[str],
        stop_words: Sequence[str],
        punctuation: Sequence[str],
        idf_values: dict[str, float],
    ) -> None:
        """
        Initializes the knowledge database and text-processing components.

        Args:
            paths_to_texts (Sequence[str]): Paths to the texts from which to learn.
            stop_words (Sequence[str]): Sequence of stop words.
            punctuation (Sequence[str]): Sequence of punctuation symbols.
            idf_values (dict[str, float]): Pre-computed IDF values.
        """

    def add_text_to_database(self, path_to_text: str) -> None:
        """
        Adds a text to the existing knowledge database.

        Args:
            path_to_text (str): Path to the text file.
        """

    def _find_texts_close_to_keywords(
        self, keywords: Sequence[str], n_texts: int
    ) -> tuple[str, ...]:
        """
        Finds texts containing keywords similar to the provided keywords.

        Args:
            keywords (Sequence[str]): Sequence of keywords to compare.
            n_texts (int): Number of texts to find.

        Returns:
            tuple[str, ...]: Paths of the most relevant texts.
        """

    def reply(self, query: str, n_summaries: int) -> str:
        """
        Generates a response to a query using relevant text summaries.

        Args:
            query (str): Query used to search the knowledge database.
            n_summaries (int): Number of summaries to include in the response.

        Returns:
            str: Response containing summaries of relevant texts.
        """
