.. _ner-label:

NER
==============

Models
------

+--------------------------------------------------------------------------+------+-----------+
| Model                                                                    | Lang | Task      |
+==========================================================================+======+===========+
| `dslim/distilbert-NER                                                    | EN   | NER       |
| <https://huggingface.co/dslim/distilbert-NER>`__                         |      |           |
+--------------------------------------------------------------------------+------+-----------+
| `Babelscape/wikineural-multilingual-ner                                  | EN   | NER       |
| <https://huggingface.co/Babelscape/wikineural-multilingual-ner>`__       |      |           |
+--------------------------------------------------------------------------+------+-----------+

Datasets
--------

1. `Babelscape/wikineural <https://huggingface.co/Babelscape/wikineural-multilingual-ner>`__

   1. **Lang**: EN
   2. **Rows**: 11590
   3. **Preprocess**:

      1. Select ``val_en`` split.
      2. Rename column ``ner_tags`` to ``target``.
      3. Rename column ``tokens`` to ``source``.
      4. Reset indexes.

2. `eriktks/conll2003 <https://huggingface.co/datasets/eriktks/conll2003>`__

   1. **Lang**: EN
   2. **Rows**: 3250
   3. **Preprocess**:

      1. Select ``validation`` split.
      2. Rename column ``ner_tags`` to ``target``.
      3. Rename column ``tokens`` to ``source``.
      4. Reset indexes.

Inferring batch
---------------

Process of implementing method
:py:meth:`lab_7_llm.main.LLMPipeline._infer_batch`
for named entity recognition task has its specifics:

   1. You need to set the ``is_split_into_words=True`` parameter during the tokenization.
   2. The prediction of the model will contain a tensor with labels for each token
      obtained during tokenization of ``sample_batch``.
   3. The number of labels corresponds to the number of tokens.
   4. To assess the quality of the model, it is necessary that the number of labels
      coincides with the length of the original sequence.
   5. You need to process model prediction result so that the prediction contains only
      the labels of the first tokens of each word. Use the ``word_ids`` method of the
      tokenizer to determine the word boundaries.

.. note:: For example, if the model predicts the following labels ``[0, 0, 0, 1]``
          for a sequence of tokens ``['VI', '##CT', '##OR', '##Y']`` that make up one word ``VICTORY``,
          then only the label of the first token, namely ``0``, is included in the final result.

Metrics
-------

-  Accuracy
