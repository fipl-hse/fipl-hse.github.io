.. _run-in-terminal-label:

.. contents:: Contents:
   :depth: 2

Run Python Programs in Terminal
===============================

This is a short tutorial on calling Python programs in terminal (Unix)
or ``cmd`` (Windows).

.. _running-code-en:

Run simple program with no dependencies
---------------------------------------

Let's try to launch a Python program represented as ``script.py`` file in folder
``lab_N_lab_name`` of a project ``2-level-ctlr``.

1. Open terminal (Windows: ``PowerShell``, macOS: ``Terminal``).

2. Go to the project folder via command ``cd C:\<path-to-folder>\2-level-labs``.

3. Create a virtual environment via command ``python -m venv venv``.

4. Activate environment:

   1. For Windows: ``.\venv\Scripts\activate``.
   2. For macOS: ``source venv\bin\activate``.

   As a result, you get ``(venv)`` at the beginning of line.

5. Run your program from the root of the project via ``python lab_N_lab_name/script.py``.


Running programs with custom modules
------------------------------------

Now, try to run your scraper:

1. Complete steps 1-4 of :ref:`the previous instruction <running-code-en>`
   to start working in your CTLR project.

2. Install dependencies via ``python -m pip install -r requirements.txt``.

3. Run scraper ``python lab_5_scraper/scraper.py``.

You get error:

.. code:: shell

   Traceback (most recent call):
      File ...., line 5 in <module>
         from core_utils.constants import ASSETS_PATH
   ModuleNotFoundError: No module named 'core_utils'

Why? When we run the same from our Integrated Development Environment, it works like a charm! What
is wrong with terminal run? ``core_utils`` is exactly here, in our
current directory!

Answer is a bit deep. We need to understand how Python imports modules
and libraries. To be able to import installed libraries, Python needs to
know where they are placed. By default, it knows several locations on
your computer where it can find requested library.

You can see them if you want ``python -c "import sys;print(sys.path)"``.
You will see standard directories where Python will try to find
libraries:

.. code:: text

   [
       '/Users/alexanderdemidovskij/.pyenv/versions/3.10.8/lib/python310.zip',
       '/Users/alexanderdemidovskij/.pyenv/versions/3.10.8/lib/python3.10',
       '/Users/alexanderdemidovskij/.pyenv/versions/3.10.8/lib/python3.10/lib-dynload',
       '/Users/alexanderdemidovskij/Documents/hse/2022-2-level-ctlr/venv/lib/python3.10/site-packages'
   ]

So, if the module you are trying to import is not within these paths,
Python will fail with the aforementioned error.

To resolve this you need to explicitly add path to your custom
dependencies to that standard list.

The recommended way is to append it to a ``PYTHONPATH`` system variable
in terminal:

1. For Windows: ``$env:PYTHONPATH = "$pwd;" + $env:PYTHONPATH``.
2. For macOS: ``export PYTHONPATH=$pwd:$PYTHONPATH``, ``pwd`` allows to
   get current working directory.

Run scraper again ``python lab_5_scraper/scraper.py``.

Does it work? If yes, congratulations, you have a chance to get the
highest possible mark. If not, write in chat for help.


FAQ
===

Python is not recognized as a command
-------------------------------------

If ``python`` is not recognized as a command, you need to install it.
Follow install instructions from :ref:`starting-guide-en-label`.


I get an access error in PowerShell
-----------------------------------

If you have problems with access in ``PowerShell``, you should change
the execution policy in 2 steps:

1. Start Windows ``PowerShell`` with the “Run as Administrator” option.
2. Enable running unsigned scripts by entering:

.. code:: text

   set-executionpolicy remotesigned

If any other problems appear during activation, write in chat to get
help.
