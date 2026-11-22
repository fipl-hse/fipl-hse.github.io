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
| 13.11.2026  | Inference                  | Datasets.                                         |
|             |                            | `Listing <https://github.com/fipl-hse/            |
|             |                            | 2026-hello-llm/blob/main/seminars/                |
|             |                            | listing_1_datasets.py>`__.                        |
|             |                            | Pandas.                                           |
|             |                            | `Listing <https://github.com/fipl-hse/            |
|             |                            | 2026-hello-llm/blob/main/seminars/                |
|             |                            | listing_2_pandas.py>`__.                          |
|             |                            | Inference.                                        |
|             |                            | `Listing <https://github.com/fipl-hse/            |
|             |                            | 2026-hello-llm/blob/main/seminars/                |
|             |                            | listing_3_model.py>`__.                           |
+-------------+----------------------------+---------------------------------------------------+
| 20.11.2026  | Batch Inference            | Python protocols.                                 |
|             |                            | `Listing <https://github.com/fipl-hse/            |
|             |                            | 2026-hello-llm/blob/main/seminars/                |
|             |                            | listing_4_iter_data.py>`__.                       |
|             |                            | DataLoader.                                       |
|             |                            | `Listing <https://github.com/fipl-hse/            |
|             |                            | 2026-hello-llm/blob/main/seminars/                |
|             |                            | listing_5_dataloader.py>`__.                      |
|             |                            | Evaluate.                                         |
|             |                            | `Listing <https://github.com/fipl-hse/            |
|             |                            | 2026-hello-llm/blob/main/seminars/                |
|             |                            | listing_6_evaluate.py>`__.                        |
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


Lecture 3. Batch Inference
------------------------------------------

Typical control-test errors: batch size ``1``, batch size versus number of batches, independent predictions.
Batch inference as data organization: one sample and one batch; sample = batch of size ``1``.
Batch size and number of model calls; independent outputs; throughput versus latency.
Variable-length samples: padding and truncation; one input tensor; logits; row-wise softmax and argmax.
Generation as iterative classification over the vocabulary; greedy, top-k and top-p; renormalization.
Dataset schemas and splits; task-specific dataset and metric.
Classification metrics: Accuracy, F1. Generation metrics: BLEU, ROUGE-L; token Accuracy is not a generation metric.
