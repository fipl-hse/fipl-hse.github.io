.. _faq-label:

Часто задаваемые вопросы
========================

.. contents:: Content:
   :depth: 2


Лабораторные работы
-------------------

1. Ошибка Argument 1 to "get_top_n" has incompatible type "Dict[str, int]"; expected "Dict[str, Union[int, float]]" [arg-type]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Это проблема часто встречается в лабораторной работе ``lab_1_keywords_tfidf`` и легко решаема.

Обычно, за этой ошибкой следуют следующие примечания:

* ``note: "Dict" is invariant -- see [link]``
* ``note: Consider using "Mapping" instead, which is covariant in the value type``

Чтобы решить проблемы, достаточно внимательно изучить описание задачи.
Там написано, что студентам нужно продемонстрировать использование
``get_top_n`` с двумя типами словарей: словарём, содержащим значения ``TF-IDF``,
и словарём, содержащим значения хи-квадрата. Оба эти словаря содежат значения
типа ``float``.

Проблема возникает, если использовать ``get_top_n`` на словаре частот,
что **не** требуется в описании. Частотный словарь содержит целочисленные
значения, которые не сочетаются с типами функции, и это вызывает ошибки
в ``MyPy``.

Чтобы решить проблему, используйте ``get_top_n`` только со словарями с типом
значений ``float``.

Похожие проблемы часто возникают из-за того, как ``MyPy`` интерпретирует типы.
Обычно для их решения достаточно сделать дополнительную проверку значений
перед передачей аргуметов в фунции. 

2. Ошибка импорта Cannot find implementation or library stub for module named "main" [import]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Предположим, что структура Вашег проекта выглядит так:

.. code:: text

   +-- 2025-2-level-labs
       +-- config
       +-- docs
       +-- lab_1_keywords_tfidf
           +-- assets
           +-- tests
           +-- main.py
           +-- start.py
           +-- settings.json
           +-- README.rst
       +-- seminars
   ...

Вы хотите импортировать функции из файла ``main.py`` в файл ``start.py``.
Чтобы сделать это, вспомните, что программа смотрит на Ваш код из корневой
папки. Это значит, что на самом деле Ваш файл ``main.py`` имеет путь
``lab_1_keywords_tfidf/main.py``.

Поэтому Вам нужно импортировать функции из ``main.py`` в ``start.py``
следующим образом:

.. code:: py

   from lab_1_keywords_tfidf.main import <functions you want to import>


3. Ошибка Argument 1 to <function name> Has incompatible type "Optional[<certain type>]"; expected "[<certain type>]"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

В некоторых лабораторных работах существует необходимость проверять
входные значения. В других словах, помимо логики функции, Вы должны
удостовериться, что все передаваемые аргументы действительно являются
правильных типов.

Обычно это происходит когда мы используем несколько функций подрят
из-за того, что ``MyPy`` не хочет, чтобы, например, во вторую по счёту
функцию попало специальное значение ``None``, так как оно часто используется
как индикатор наличия неправильных значений. ``MyPy`` видит, что значение
может быть ``None`` и не хочет потенциально передавать его в следующую
функцию — оно уже неправильное.

Чтобы избежать ошибок в ``MyPy``, следовать сделать дополнительную проверку
на ``None`` перед передачей значения в следующую функцию.

Например, у Вас есть две функции, представленные ниже.
Первая объединяет два списка в один,
а вторая суммирует все элементы одного списка.

.. code:: py

   def function1(arg1: list[int], arg2: list[int]) -> list[int] | None:
       if not arg1 or not arg2:
           return None
       return arg1 + arg2
       
   def function2(arg: list[int]) -> int | None:
       if not arg:
           return None
       return sum(arg)

Мы хотим использовать их по-порядку: сначала объединить два листа,
а затем найти сумму всех элементов. Неудачным вариантом будет сделать
следующее:

.. code:: py

   united_list = function1(list1, list2)
   elements_sum = function2(united_list)

``function1`` может вернуть ``None``, и нам не следует передавать такое
значение в ``function2``. 

Правильнее будет сделать дополнительную проверку:

.. code:: py

   united_list = function1(list1, list2)
   if united_list:
       elements_sum = function2(united_list)


4. Ошибка Incompatible types in assignment (expression has type X, variable has type Y)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python — динамический язык программирования. Это означает, что при
запуске программ переменные могут принимать значения разных типов.
Хотя это не запрещено в языке, это не самая лучшая практика.

Переиспользование переменных таким образом может сделать код более
уязвимым, потому как увеличивается вероятность сделать ошибку, которую
сложно будет потом найти. Поэтому ``MyPy`` подсвечивает такие переменные.

Можно избавиться от противоречия типов через переназначение типов:

Больше о `несовместимых переопределениях здесь
<https://mypy.readthedocs.io/en/stable/common_issues.html#redefinitions-with-incompatible-types>`__.

Больше об `особенностях стиля назначения типов MyPy здесь
<https://mypy.readthedocs.io/en/stable/faq.html#why-have-both-dynamic-and-static-typing>`__.

5. During working in Visual Studio Code, interpreter cannot be found
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In many cases the issue turns out to be wrong opening of the Visual Studio Code.
Make sure that you open the whole ``202X-2-level-labs`` as a project,
not just the folder with a particular lab.

More details on correct Visual Studio Code opening can be found in :ref:`starting-guide-ru-label`.

Running tests
-------------

1. Why is my CI job cancelled?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usually that happens because your CI check runs for too
long. Possible reasons is that you do not control number of articles
that you collect from your seed URL. If you feel that the problem is
with infrastructure, call a mentor in the group chat.

2. Why is my CI job not started?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usually that happens because your fork has conflicts with a
base repository. Resolve them by merging the upstream, or if it all
sounds new for you, call a mentor in the group chat.

3. Why does my CI or mentor not like my seminar files?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Seminar files are used to teach you some basic knowledge about Python,
but they are not part of the laboratory works you submit to the repository.
So if you accidentally push them to your Pull Request, your mentor
will ask you to remove them or there might be CI errors.

To undo changes in seminar files, you must first find the commit where
you changed them. To do so, execute in Visual Studio Code terminal:

.. code:: bash

   git remote -v

You should have two repositories: `origin` and `upstream`, one of which
is your fork and the other one is the main repository.

.. image:: _static/FAQ/git_remote.jpg

If you don't have an upstream repository, execute:

.. code:: bash

   git remote add upstream <link-to-the-main-repository>
   git fetch upstream

Now you need to get the newest state of the main repository via:

.. code:: bash

   git fetch upstream

Once you've done that, you need to replace the current state of
your local seminar folder with what is available in the main repository.

.. code:: bash

    git checkout upstream/main seminars

The changes will be applied to your current state, and you will be able to
add, commit, and push the updated changes as usual.