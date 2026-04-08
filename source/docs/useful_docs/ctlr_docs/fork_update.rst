Fork update
===========

During the course changes will be added to the main repository (changes
in tests, bug fixes, etc.) - these changes will not automatically appear
in your forks.

To add changes to your fork from the main repository, follow these steps:

1. Open the repository site sent to you by your lecturer.

2. Click ``Code``, select ``HTTPS`` and click the copy button.

   .. figure:: _static/fork_update/copy_original_repo_url.png
      :alt: copy repo url

3. Open terminal in Visual Studio Code development environment.

   You can do that by clicking Terminal -> New Terminal
   at the top bar of the IDE or with a keyboard shortcut
   ``Ctrl + ```.

4. Run ``git remote add upstream <link-to-main-repository>``.

   .. image:: _static/fork_update/add_upstream.png

5. Run ``git fetch upstream``.

   .. image:: _static/fork_update/fetch_upstream.png

.. important:: Please note that the link in the screenshot
               above points to the parent repository.

6. Run ``git merge upstream/main --no-edit``.

   .. image:: _static/fork_update/merge_upstream.png

.. note:: Depending on the number of changes, the output of the
          command will be different.

This command will result in the latest changes from
the main repository appearing in your local fork.

More information about the commands described above can be found
in the `official Git documentation <https://git-scm.com/docs>`__.
