.. _docs-sync:

Синхронизация документации админа и сайта
=========================================

.. contents:: Содержание
    :depth: 2


Инструмент DOCSYNC переносит файлы из админского репозитория в
`репозиторий сайта <https://github.com/fipl-hse/fipl-hse.github.io>`__
и создаёт там Пулл Реквест. Какие файлы и куда переносить, задаётся
в ``project_config.json`` админского репозитория.

.. important:: Источником правды является админский репозиторий.
               Если файл на сайте был исправлен напрямую, синхронизация
               перезапишет эти правки. Перед запуском перенесите такие
               правки в админский репозиторий.


Настройка списка файлов
-----------------------

Список файлов задаётся в поле ``doc_sync_config`` файла ``project_config.json``.
Пути указываются относительно корня репозитория: ``source`` в админском
репозитории, ``target`` в репозитории сайта.

На примере лабораторной работы ``lab_1_classify_profile``:

.. code:: json

    "doc_sync_config": [
        {
            "source": "README.rst",
            "target": "source/docs/labs_2026/general_info.rst"
        },
        {
            "source": "lab_1_classify_profile/__init__.py",
            "target": "lab_1_classify_profile/__init__.py"
        },
        {
            "source": "lab_1_classify_profile/main_stub.py",
            "target": "lab_1_classify_profile/main.py"
        },
        {
            "source": "lab_1_classify_profile/README.rst",
            "target": "source/docs/labs_2026/labs/lab_1_classify_profile/lab_1.rst"
        },
        {
            "source": "lab_1_classify_profile/lab_1_classify_profile.api.rst",
            "target": "source/docs/labs_2026/labs/lab_1_classify_profile/lab_1_classify_profile.api.rst"
        },
        {
            "source": "lab_1_classify_profile/assets/description.png",
            "target": "source/docs/labs_2026/labs/lab_1_classify_profile/assets/description.png"
        }
    ]

Переносятся только файлы, которые отличаются от ``main`` репозитория сайта.


Создание токена
---------------

Для работы инструмента нужен fine-grained токен GitHub.

1. Откройте `страницу создания токена <https://github.com/settings/personal-access-tokens/new>`__.
   Укажите имя токена и выберите ``fipl-hse`` в поле ``Resource owner``:

   .. image:: ../developer_docs/_static/docs_sync/token_create.jpg

2. В разделе ``Repository access`` выберите ``Only select repositories`` и укажите
   репозиторий сайта и админский репозиторий. В разделе ``Permissions`` выдайте
   права ``Read and write`` для ``Contents`` и ``Pull requests``:

   .. image:: ../developer_docs/_static/docs_sync/token_permissions.jpg

3. Для запуска через CI добавьте токен в секреты админского репозитория
   (``Settings`` -> ``Secrets and variables`` -> ``Actions`` -> ``New repository secret``)
   под именем ``TARGET_REPO_PAT``:

   .. image:: ../developer_docs/_static/docs_sync/repo_secret.jpg


Запуск вручную
--------------

Установите `GitHub CLI <https://cli.github.com/>`__ и ``quality-control``
(устанавливается вместе с зависимостями админского репозитория из ``requirements_qa.txt``).

Передайте токен через переменную окружения ``GH_TOKEN``:

.. code:: bash

    export GH_TOKEN=<токен>

В PowerShell:

.. code:: powershell

    $env:GH_TOKEN = "<токен>"

Запустите синхронизацию, указав админский репозиторий и номер Пулл Реквеста в нём:

.. code:: bash

    fiplconfig.sync_docs --repo-name fipl-hse/2026-2-level-labs-admin --pr-number 100

Если Пулл Реквест открыт, файлы берутся из его ветки, если замёржен — из ``main``.
В репозитории сайта будет создана ветка
``auto-update-from-<админский репозиторий>-pr-<номер>`` и Пулл Реквест.
При повторном запуске ветка обновится, а в Пулл Реквест будет добавлен комментарий.

Дополнительные аргументы:

- ``--dry-run`` — только показать, какие файлы изменятся. Коммит, пуш и
  Пулл Реквест не создаются. Рекомендуется запускать перед настоящей синхронизацией.
- ``--work-dir <папка>`` — папка, в которую клонируется репозиторий сайта.
  По умолчанию используется временная папка. Если в указанной папке уже есть
  клон сайта, он будет удалён и склонирован заново.

После запуска с ``--dry-run`` изменения можно посмотреть в клоне сайта:

.. code:: bash

    git -C <папка>/fipl-hse.github.io diff --cached

После синхронизации проверьте и замёржите автоматически созданный
Пулл Реквест в репозитории сайта.


Запуск через CI
---------------

.. note:: WIP.
