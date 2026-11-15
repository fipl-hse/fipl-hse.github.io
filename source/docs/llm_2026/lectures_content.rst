.. _lectures-content-llm-label-2026:

History of Lectures
===================

+-------------+----------------------------+---------------------------------------------------+
| Date        | Lecture Topic              | Practice Materials.                               |
+=============+============================+===================================================+
| 06.11.2026  | Modern NLP Tasks           | Creating a fork.                                  |
|             | Lifecycle of a neural      |                                                   |
|             | network model.             |                                                   |
+-------------+----------------------------+---------------------------------------------------+
| 13.11.2026  | Inference                  | Loading a dataset from HuggingFace.               |
|             |                            | `Listing <https://github.com/fipl-hse/            |
|             |                            | 2026-hello-llm/blob/main/seminars/                |
|             |                            | seminar_2026_11_13/try_datasets.py>`__.           |
|             |                            | Analysing and preprocessing a dataset.            |
|             |                            | `Listing <https://github.com/fipl-hse/            |
|             |                            | 2026-hello-llm/blob/main/seminars/                |
|             |                            | seminar_2026_11_13/try_pandas.py>`__.             |
|             |                            | Infering an LLM. `Listing <https://github.com/    |
|             |                            | fipl-hse/2026-hello-llm/blob/main/seminars/       |
|             |                            | seminar_2026_11_13/try_model.py>`__.              |
+-------------+----------------------------+---------------------------------------------------+

Lecture 1. Modern NLP Tasks
------------------------------------------

Introduction of the instructor. General course structure. Formation of the final grade. Core ideas
behind the course. The place of the course in the degree programme. Structure of the laboratory work.
``LLM``. Typical ``NLP`` tasks solved with neural network models. Model lifecycle: ``pre-training``,
inference, ``fine-tuning``, inference. Tokenization as a way to move from text to numeric form and back.
Fundamental relationship between the tokenizer and the model. Model vocabulary. Main criteria when
choosing a model: quality of solving the task and the amount of computational resources required.

Lecture 2. Inference
------------------------------------------

Inference as a forward pass with fixed weights. Difference between inference and training: loss,
backward pass, and weight update. Inference pipeline: text, tokens, IDs, forward pass, logits,
probabilities, one class or one token. Tokenization in practice: vocabulary, token versus word,
byte-pair encoding (``BPE``), encoding and decoding, padding, truncation, max length, and special
tokens. Logits and softmax. Generation as repeated classification over tokens. Greedy decoding and
sampling with temperature. Prefill and decode phases, ``TTFT`` and tokens/s.
