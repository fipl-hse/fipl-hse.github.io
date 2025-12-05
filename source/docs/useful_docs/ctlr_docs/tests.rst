.. _ctlr-tests-label:

.. contents:: Contents:
   :depth: 2

Working with tests: locally and in CI
=====================================

.. contents:: Content:
   :depth: 2


Tests configuration in Visual Studio Code
-----------------------------------------
To configure tests locally you need to perform several steps:

1. Install tests dependencies:

   .. code:: bash

      python -m pip install -r requirements_qa.txt

.. important:: Ensure you have activated your environment
               if you have such by running ``.\venv\Scripts\activate``
               (Windows) or ``source venv\bin\activate`` (macOS).

2. Create a new configuration:

   To create a new configuration open the Testing tab on the side
   bar of Visual Studio Code and press the `Configure Python Tests`
   button.

   .. image:: _static/tests/vscode_testing_tab.jpg

   Alternatively, you can open configuration settings via command bar.
   Use `Ctrl + Shift + P` keyboard shortcut to open it and type in
   `Python: Configure Tests`.

   .. image:: _static/tests/vscode_command_bar.jpg

3. Choose ``pytest`` as a target:

   .. image:: _static/tests/vscode_tests_configuration_step_1.jpg

4. Choose the directory to run all tests. You can use root directory to run all
   tests or a specific lab.

   .. image:: _static/tests/vscode_tests_configuration_step_2.jpg

   When you are done, the `settings.json` file for the tests will be opened
   and all the tests will be displayed on the `Testing` tab of the
   Visual Studio Code.

   .. image:: _static/tests/vscode_configured_tests.jpg

Running tests in Visual Studio Code
-----------------------------------
  
To run the test, press the run button, as indicated in the screenshot above.

As you have some tests failing, you want to run them separately. You can press
a run button next to a test you want to run in the tests files specifically
or in the `Testing` tab.

.. image:: _static/tests/vscode_running_tests.jpg

Debugging
---------

When you want to debug a test, execute debugging by clicking a run button
with a bug on it on a test you want to run in the `Testing` tab or make a
right click on the testing button in the test file itself and choose the
`Debug Test` option.

.. image:: _static/tests/vscode_debugging.jpg

To debug you should put a breakpoint in your code or in the test itself.
Breakpoints are red dots that you can put at the potentially vulnerable place of code.
The execution stops at breakpoints and you can debug your code from these lines.

.. image:: _static/tests/breakpoints.jpg

Running tests in terminal
-------------------------

.. important:: Ensure you have activated your environment
               and installed all required dependencies.

To run all tests, execute the following command in the terminal:

.. code:: bash

   python -m pytest

You can also run tests for any of the allowed marks:
``mark4``, ``mark6``, ``mark8`` or ``mark10``.

.. code:: bash

   python -m pytest -m mark8

To run tests for a specific laboratory work you can add the directory name
after `pytest` command. For example, if you want to run tests for
`lab_1_keywords_tfidf` and mark 4, the full command and the full terminal
output should look like this:

.. image:: _static/tests/running_from_command_line.jpg

.. hint:: Note that if you activated virtual environment and installed
          requirements properly, you can use `pytest` without calling
          `python` first.

Running tests in CI
-------------------

Tests will never run until you create a Pull Request.

The very first check happens exactly when you create a pull request.
After that, each time you push changes in your fork, CI check will be
automatically started, normally within a minute or two. To see the
results, navigate to your PR and click either the particular step in the
report at the end of a page, or click **Checks** in the toolbar.

.. image:: _static/tests/ci_report.png

.. image:: _static/tests/ci_tab.png

Inspect each step by clicking through the list to the left.
