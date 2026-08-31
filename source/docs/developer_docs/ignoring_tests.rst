Ignoring Lab Tests Optionally
=============================

The configuration file allows now to specify which lab tests should be ignored.
This is useful when you need to temporarily disable checks for specific labs.

Configuration
-------------

Test ignoring is configured in the ``settings`` section of each lab using the ``ignore`` parameter.
This parameter accepts a list of lab names which tests should be skipped.

.. code-block:: json

    {
        "labs": [
            {
                "name": "lab_5_scraper",
                "coverage": 98,
                "settings": {
                    "ignore": ["lab_6_pipeline"]
                }
            },
            {
                "name": "lab_6_pipeline",
                "coverage": 76
            },
            {
                "name": "final_project",
                "coverage": 0
            }
        ],
    ...
    }

In this example:

    - When testing ``lab_5_scraper``, checks related to ``lab_6_pipeline`` will be skipped
    - When testing ``lab_6_pipeline`` or ``final_project``, no tests will be ignored
