.. _lectures-content-llm-label-2026:

History of Lectures
===================

+-------------+----------------------------+---------------------------------------------------+
| Date        | Lecture Topic              | Practice Materials.                               |
+=============+============================+===================================================+
| 07.11.2026  | Modern NLP Tasks           | Creating a fork.                                  |
|             | Lifecycle of a neural      |                                                   |
|             | network model.             |                                                   |
+-------------+----------------------------+---------------------------------------------------+
| 13.11.2026  | Inference                  |                                                   |
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
