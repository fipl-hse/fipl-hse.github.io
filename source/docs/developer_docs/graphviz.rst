Graphviz для работы с автоматическим построением UML диаграмм
============================================================================

**Graphviz** — это инструмент для автоматического построения структурных диаграмм
из текстового описания на языке DOT

Как установить Graphviz
-----------------------

1. Перейти на `официальный сайт <https://graphviz.org/download/>`__

2. Выбрать опцию для нужной операционной системы

    2.1. Linux
        - для Ubuntu или Debian:

        .. code-block:: python

            sudo apt install graphviz

        - для Fedora project, Rocky Linux, Redhat Enterprise Linux, или CentOS:

        .. code-block:: python

            sudo dnf install graphviz

    2.2. Windows
        - выбрать graphviz-14.0.0 EXE installer для

        `32 <https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/14.0.0/windows_10_cmake_Release_graphviz-install-14.0.0-win32.exe>`__
        или `64-битной <https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/14.0.0/windows_10_cmake_Release_graphviz-install-14.0.0-win64.exe>`__ системы

        - после окончания загрузки нажать на файл и следовать инструкции

    2.3. Mac
        - для MacPorts:

        .. code-block:: python

            sudo port install graphviz

        - для Homebrew:

        .. code-block:: python

            brew install graphviz
