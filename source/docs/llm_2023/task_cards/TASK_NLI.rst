.. _nli-label:

NLI
===

Models
------

+-------------------------------------------------------------------+------+
| Model                                                             | Lang |
+===================================================================+======+
| `cointegrated/rubert-base-cased-nli-threeway <https://            | RU   |
| huggingface.co/cointegrated/rubert-base-cased-nli-threeway>`__    |      |
+-------------------------------------------------------------------+------+
| `cointegrated/rubert-tiny-bilingual-nli                           | RU   |
| <face.co/cointegrated/rubert-tiny-bilingual-nli>`__               |      |
+-------------------------------------------------------------------+------+
| `cross-encoder/qnli-distilroberta-base                            | EN   |
| <https://huggingface.co/cross-encoder/qnli-distilroberta-base>`__ |      |
+-------------------------------------------------------------------+------+
| `MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli <https:             | EN   |
| //huggingface.co/MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli>`__ |      |
+-------------------------------------------------------------------+------+


Datasets
--------

+--------------------------------------------------------------------+-----+
| Dataset                                                            |Lang |
+====================================================================+=====+
| `cointegrated/nli-rus-translated-v2021 <https://                   | RU  |
| huggingface.co/datasets/cointegrated/nli-rus-translated-v2021>`__  |     |
+--------------------------------------------------------------------+-----+
| `XNLI <https://huggingface.co/datasets/xnli>`__                    | RU  |
+--------------------------------------------------------------------+-----+
| `Russian Super GLUE TERRA                                          | RU  |
| <https://huggingface.co/datasets/RussianNLP/russian_super_glue>`__ |     |
+--------------------------------------------------------------------+-----+
| `GLUE QNLI <https://huggingface.co/datasets/glue>`__               | EN  |
+--------------------------------------------------------------------+-----+
| `GLUE MNLI <https://huggingface.co/datasets/glue>`__               | EN  |
+--------------------------------------------------------------------+-----+


Dataset preprocessing
---------------------

-  Remove duplicated and empty rows.

Metrics
-------

-  Accuracy
