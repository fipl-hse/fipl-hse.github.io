Docker usage guide
==================

..  contents:: Contents
   :depth: 2


Docker Setup Guide
------------------
This guide helps you set up Docker and VSCode for development in this repository.

1. Install Docker Desktop
2. Download Docker Desktop from `official site <https://www.docker.com/products/docker-desktop>`_;
3. Run installer and follow prompts;
4. After installation:

   - Launch Docker Desktop
   - Enable WSL2 backend (Windows) or VirtioFS (macOS) for better performance.

5. Install all required extensions:

   - Docker (ms-azuretools.vscode-docker);
   - Docker containers (ms-vscode-remote.remote-containers).


Basic usage
-----------
If you want to check your files with `precommit.sh`, launch this commandline:

.. code:: bash

   docker run --rm -v ${PWD}:/app -w /app python:3.13-slim bash -c "bash ./admin_utils/docker/docker.sh && bash ./admin_utils/precommit.sh"

If you want to check your files with spellcheck, launch this commandline:

.. code:: bash

   docker run --rm -v ${PWD}:/app -w /app python:3.13-slim bash -c "bash ./admin_utils/docker/docker.sh && source venv/bin/activate && fiplconfig.check_spelling"


If you encounter the ``script.sh: line N: $'\r': command not found`` error
with any bash script, make sure that the file in your VSCode has end-of-line sequence set to LF
instead of CRLF. You can check at the bottom right of the screen or find
``Change End of Line Sequence`` via Comand Palette (``Ctrl+Shift+P``) with the bash script open.


Advanced usage
--------------
After several launches of basic script,
you noticed that the dependencies are downloading every time.
To download dependencies once and check your code many times, you should create image and use it.

Follow the instructions:

.. code:: bash

   docker build -t advanced-ctlr-admin -f admin_utils/docker/Dockerfile .

After creating own image you can check your code with next docker command:

.. code:: bash

   docker run --rm -v ${PWD}:/app -w /app advanced-ctlr-admin bash -c "bash ./admin_utils/docker/docker.sh && ./admin_utils/precommit.sh"


If any dependencies (especially from Quality Control) are not installed properly,
delete created container and virtual environment and rebuild them via the abovementioned commands.

Interactive Development Mode
----------------------------
If you want to develop yourself in interactive mode
to fix some problems which are not reproducable on Windows,
you can create own image, create container and start it:

.. code:: bash

   docker build -t advanced-ctlr-admin -f admin_utils/docker/Dockerfile .

   docker run --name advanced_ctlr -d -v ${PWD}:/app -w /app advanced-ctlr-admin tail -f /dev/null bash

After creating own image for interactive development mode, follow the instructions:

1. Make sure that you have the `Dev Containers` extension downloaded;
2. Open Command Palette (Ctrl+Shift+P);
3. Select "Remote-Containers: Attach to Running Container";
4. Select `advanced_ctlr`;
5. Open the folder on the path `/app`;
6. Activate your environment and install dependencies

.. code:: bash

   source venv/bin/activate
   pip install -r requirements.txt -r requirements_qa.txt 

Now you are ready to develop. Good luck!

If you already have a container and you want to enter it, then first you need to launch it:

.. code:: bash

   docker start advanced_ctlr
