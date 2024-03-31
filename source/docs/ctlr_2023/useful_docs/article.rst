.. _ctlr-article-label:

Article package
===============

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :caption: Full API

    article.api.rst

The ``article`` package is responsible for handling the articles you
have collected from your website.

.. hint:: In case you think you have found a mistake in this package,
          contact your assistant. Those who considerably improve this module
          will get additional bonuses.

``article`` module
------------------

``article`` module represents the methods to work with the
:py:class:`stubs.core_utils.ctlr.article.article.Article` abstraction.

:py:class:`stubs.core_utils.ctlr.article.article.Article` class is responsible
for storing article raw, meta and ``conllu`` data and working with it.
During the implementation of Lab 5 and Lab 6, you should use the methods of this class,
so we advise you to study them.

.. note:: Do not forget to create a new instance of the
          :py:class:`stubs.core_utils.ctlr.article.article.Article` class to use its methods.

In addition to the ``Article`` class, the module has:

1. :py:func:`stubs.core_utils.ctlr.article.article.date_from_meta` function which converts
   text date to ``datetime`` object.
2. :py:func:`stubs.core_utils.ctlr.article.article.get_article_id_from_filepath` function which
   extracts the article id from its path.
3. :py:class:`stubs.core_utils.ctlr.article.article.SentenceProtocol` abstraction which you should
   inherit for ``lab_6_pipeline.pipeline.ConlluSentence`` abstraction in Lab 6.
4. :py:class:`stubs.core_utils.ctlr.article.article.ArtifactType` abstraction which provides
   types of artifacts that can be created by text processing pipelines, such as ``CLEANED``,
   ``MORPHOLOGICAL_CONLLU``, ``POS_CONLLU`` and ``FULL_CONLLU``.

   1. The description of each artifact you can find in :ref:`dataset-label`.

.. note:: You should utilize attributes of :py:class:`stubs.core_utils.ctlr.article.article.ArtifactType`
          in order to save processed versions of files. Otherwise, if you pass a string
          itself to some saving function, your code will be much more fragile.

``ud`` module
-------------

``ud`` module contains functions which are responsible for parsing ``CONLL-U``.

:py:class:`stubs.core_utils.ctlr.article.ud.OpencorporaTagProtocol` abstraction represents
the abstraction definition for ``pymorphy2.tagset.OpencorporaTag``.
When you implement Lab 6 for mark 10, you should use ``pymorphy2`` for morphological analyzes.
TBD

:py:func:`stubs.core_utils.ctlr.article.ud.extract_sentences_from_raw_conllu` function
extracts sentences from the ``CONLL-U`` formatted article and stores
them in a preferable way:

.. code:: python

       [
           {
               'position': sentence_position,
               'text': sentence_text,
               'tokens': sentence_tokens
           },
           {
               'position': sentence_position,
               'text': sentence_text,
               'tokens': sentence_tokens
           },
           ...
       ]

..

.. hint:: This function will be useful when implementing the Lab 6.

:py:class:`stubs.core_utils.ctlr.article.ud.TagConverter` abstraction is responsible for
tags conversion between different formats, in your case from Mystem to UD and
from PyMorphy to UD (for mark 10). You need to inherit its interface and implement the
following abstraction inside the ``pipeline.py`` file.

.. note:: To use it, you should have an information about the
          correspondence of one format tags to another format tags.

:py:class:`stubs.core_utils.ctlr.article.ud.TagConverter` class stores information about
POS and morphological tags and contains two methods -
:py:meth:`stubs.core_utils.ctlr.article.ud.TagConverter.convert_morphological_tags` and
:py:meth:`stubs.core_utils.ctlr.article.ud.TagConverter.convert_pos` -
that you need to implement for Lab 6.

``io`` module
-------------

``io`` module provide functions to work with input/output operations for
the :py:class:`stubs.core_utils.ctlr.article.article.Article` abstraction.

It consists of the following functions, which are grouped by usage in the labs:

Lab_5
~~~~~

-  :py:func:`stubs.core_utils.ctlr.article.io.to_raw` - use to save raw texts of each article;
-  :py:func:`stubs.core_utils.ctlr.article.io.to_meta` - use to save meta-information about each article.

Lab_6
~~~~~

-  :py:func:`stubs.core_utils.ctlr.article.io.from_raw` - use to load raw texts and
   create the :py:class:`stubs.core_utils.ctlr.article.article.Article` abstraction;
-  :py:func:`stubs.core_utils.ctlr.article.io.to_cleaned` - use to save cleaned texts
   of each article, i.e. lowercased texts with no punctuation;
-  :py:func:`stubs.core_utils.ctlr.article.io.to_meta` - use to save POS information
   about each article;
-  :py:func:`stubs.core_utils.ctlr.article.io.from_meta` - use to load
   meta-information about each article and create the
   :py:class:`stubs.core_utils.ctlr.article.article.Article` abstraction;
-  :py:func:`stubs.core_utils.ctlr.article.io.to_conllu` - use to save morphological
   and syntactic information from the
   :py:class:`stubs.core_utils.ctlr.article.article.Article` abstraction into the ``conllu`` file.
