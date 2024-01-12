Laboratory work №7. Name
========================


.. toctree::
    :maxdepth: 1
    :titlesonly:
    :caption: Full API

    lab_7.api.rst
    core_utils.api.rst


Python competencies required to complete this tutorial:
    * working with Transformers models;
    * working with HuggingFace datasets;
    * estimating result using metric;
    * making server for the chosen task using FastAPI.

Model pipeline contains the following steps:

    1. Downloading the chosen dataset from HuggingFace.
    2. Retrieving dataset's properties.
    3. Preprocessing dataset.
    4. Retrieving model properties.
    5. Get prediction for one sample from dataset.
    6. Get predictions for the whole dataset.
    7. Saving predictions.
    8. Estimating results with metric.
    9. Implementing server.

Configuring model
-----------------
Model behavior is fully defined by a configuration file that is called ``settings.json``
and it is placed on the same level as ``main.py``.

+----------------------------+------------------------------------------------+---------+
| Config parameter           | Description                                    | Type    |
+============================+================================================+=========+
| ``parameters``             |Set up parameters for laboratory work           |``dict`` |
+----------------------------+------------------------------------------------+---------+
| ``model``                  |Name of the the chosen model                    | ``str`` |
+----------------------------+------------------------------------------------+---------+
| ``dataset``                |Name of the dataset                             | ``str`` |
+----------------------------+------------------------------------------------+---------+
| ``metrics``                |Name of the metrics used for the chosen task    | ``str`` |
+----------------------------+------------------------------------------------+---------+
|``target_score``            |Desired mark for laboratory work                | ``int`` |
+----------------------------+------------------------------------------------+---------+

Assessment criteria
----------------------
1. Desired mark **4**:
    1. ``pylint`` level: **5/10**.
    2. The script downloads dataset and retrieves its properties.
2. Desired mark **6**:
    1. ``pylint`` level: **7/10**.
    2. All requirements for the mark **4**.
    3. The script preprocesses dataset, retrieves model properties
       and infers one sample from dataset.
3. Desired mark **8**:
    1. ``pylint`` level: **10/10**.
    2. All requirements for the mark **6**.
    3. The script infers the whole dataset and evaluates the model performance.
4. Desired mark **10**:
    1. ``pylint`` level: **10/10**;
    2. All requirements for the mark **8**.
    3. Implement model as a service.

Implementation tactics
----------------------

Stage 0. Start working on the laboratory work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start your implementation by selecting a model and dataset you are going to use.
You can find all available combinations
in the `table <https://docs.google.com/spreadsheets/d/1_GTEa3RUkOqdZ82q1SrD7YkOeV3fr8APNcUAC6o0K4M/edit?usp=sharing>`__.

.. important:: All logic for instantiating and using needed abstractions
               should be implemented in a ``main`` function of the module ``start.py``

To do this, implement the functions in the ``main.py`` module
and import them into ``start.py``.

.. code:: py

   if __name__ == '__main__':
       main()

.. note:: You need to set the desired score: 4, 6, 8 or 10 in ``target_score`` field
          in the file `settings.json <reference_lab_nmt/settings.json>`__.
          The higher the desired score, the more
          number of tests run when checking your Pull Request.

Stage 1. Introduce importer abstraction: ``RawDataImporter``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To work with the model first of all you need to import the chosen HuggingFace dataset.

To be able to download dataset inside your program you need to implement special
:py:class:`stubs.llm_2023.lab_7.main.RawDataImporter` abstraction.

This class inherits from
:py:class:`stubs.llm_2023.core_utils.raw_data_importer.AbstractRawDataImporter` abstraction.

It has the following internal attributes:
    * ``self._hf_name`` - string with the name of the HuggingFace dataset.
    * ``self._raw_data`` - fills with the downloaded pd.DataFrame.

Stage 1.1. Download dataset
"""""""""""""""""""""""""""""""""""""""""""""""""""""
Implement a method
:py:meth:`stubs.llm_2023.lab_7.main.RawDataImporter.obtain`,
which allows to download dataset and filling ``_raw_data`` attribute.

You have to use
`load_dataset() <https://huggingface.co/docs/datasets/v2.15.0/en
/package_reference/loading_methods#datasets.load_dataset>`__ function.

.. note:: In our laboratory work we are going to get predictions of the model,
          so you have to download ``validation`` or ``test`` split of the
          chosen dataset by filling the parameter ``split`` of
          the ``load_dataset`` function.

.. note:: If downloaded dataset is not ``pd.DataFrame``, method raises ``TypeError``.

.. important:: ``obtain`` method has ``@report_time`` decorator
               which you will also find in many other methods
               in this laboratory work. The purpose of this
               decorator is to log time spent on method execution.

Stage 2. Introduce preprocessor abstraction: ``RawDataPreprocessor``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Before putting dataset into model we have to preprocess it.

To be able to perform all needed preprocessing and analyze the chosen dataset
inside your program you need to implement
:py:class:`stubs.llm_2023.lab_7.main.RawDataPreprocessor` abstraction.

This class inherits from
:py:class:`stubs.llm_2023.core_utils.raw_data_preprocessor.AbstractRawDataPreprocessor` abstraction.

It has the following internal attributes:
    * ``self._raw_data`` - downloaded pd.DataFrame.
    * ``self._data`` - preprocessed pd.DataFrame.

Stage 2.1. Analyze dataset properties
""""""""""""""""""""""""""""""""""""""""""""""""""
Implement method
:py:meth:`stubs.llm_2023.lab_7.main.RawDataPreprocessor.analyze`
which allows to analyze dataset.

You have to get the following dataset properties:
    1. Number of samples in dataset.
    2. Dataset columns.
    3. Dataset duplicates.
    4. Dataset empty rows.
    5. Length of the dataset minimal sample.
    6. Length of the dataset maximal sample.

Method should return a dictionary with dataset properties.

Stage 2.2. Preprocess dataset
"""""""""""""""""""""""""""""""""""""""""""""""""""""""
Implement method
:py:meth:`stubs.llm_2023.lab_7.main.RawDataPreprocessor.transform`
which allows to preprocess dataset.

.. important:: You can find all needed preprocessing for your
              combination of model and dataset
              choosing appropriate task:

               * :ref:`classification-label`
               * :ref:`generation-label`
               * :ref:`nli-label`
               * :ref:`nmt-label`
               * :ref:`summarization-label`

.. note:: To change column names
          according to the preprocessing instruction, use fields of the
          :py:class:`stubs.llm_2023.core_utils.raw_data_preprocessor.ColumnNames` abstraction.

Stage 2.3. Demonstrate the result in ``start.py``
"""""""""""""""""""""""""""""""""""""""""""""""""
.. important:: Stages 1 - 2 are required to get the mark **4**.

Demonstrate your dataset analysis
in the ``main()`` function of the ``start.py`` module.

Stage 3. Introduce dataset abstraction: ``TaskDataset``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To work with the model we will use
`Dataset <https://pytorch.org/docs/stable/data.html#torch.utils.data.Dataset>`__ abstraction.

To be able to convert ``pd.DataFrame`` to ``Dataset``,
get the number of samples in the dataset,
retrieve an item from the dataset by index
and override ``iter`` method for static checks
you need to implement
:py:class:`stubs.llm_2023.lab_7.main.TaskDataset` abstraction.

This class inherits from ``torch.utils.data.Dataset`` abstraction.

It has one internal attribute:
    * ``self._data`` - pd.DataFrame with preprocessed data.

Stage 3.1. Implement magic methods
""""""""""""""""""""""""""""""""""
    * Implement method :py:meth:`stubs.llm_2023.lab_7.main.TaskDataset.__len__`
      which allows to get the number of items in dataset.
    * Implement method :py:meth:`stubs.llm_2023.lab_7.main.TaskDataset.__getitem__`
      which allows to retrieve an item from the dataset by index.
    * Implement method :py:meth:`stubs.llm_2023.lab_7.main.TaskDataset.__iter__`
      which allows to override iter method for static checks.

Stage 3.2. Retrieve data
""""""""""""""""""""""""
Implement method
:py:meth:`stubs.llm_2023.lab_7.main.TaskDataset.data`
which allows to access to preprocessed pd.Dataframe.

Stage 4. Introduce model pipeline abstraction: ``LLMPipeline``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now we are ready to run our model.

To be able to initialize our model, analyze its properties,
infer the whole dataset and one sample from it you need to implement
:py:class:`stubs.llm_2023.lab_7.main.LLMPipeline` abstraction.

This class inherits from
:py:class:`stubs.llm_2023.core_utils.llm_pipeline.AbstractLLMPipeline` abstraction.

It has the following internal attributes:
    * ``self._model_name`` - a string with the model name.
    * ``self._model`` - fills with the model instance.
    * ``self._dataset`` - ``Dataset`` instance.
    * ``self._device`` - a string with a device type (``cpu``, ``cuda`` or ``mps``).
    * ``self._tokenizer`` - fills with tokenizer instance suitable for your model.
    * ``self._batch_size`` - fill with the batch size.

Stage 4.1. Analyze model properties
""""""""""""""""""""""""""""""""""""""""""""""""
Implement method
:py:meth:`stubs.llm_2023.lab_7.main.LLMPipeline.analyze_model`
which allows to analyze model properties.

You have to get the following model properties:
    1. Vocabulary size.
    2. Embedding size.
    3. Number of parameters.
    4. Maximum context length.
    5. Number of trainable parameters.
    6. Input shape.
    7. Output shape.

Method should return a dictionary with model properties.

.. note:: If the model does not have one of these properties, return **None**.

Stage 4.2. Infer one sample from dataset
""""""""""""""""""""""""""""""""""""""""""""""""
Implement method
:py:meth:`stubs.llm_2023.lab_7.main.LLMPipeline.infer_sample`,
which allows to infer one sample from dataset.

Stage 4.3. Demonstrate the result in ``start.py``
"""""""""""""""""""""""""""""""""""""""""""""""""
.. important:: Stages 3 - 4.2 are required to get the mark **6**.

Demonstrate model properties analysis and dataset sample inference
in the ``main()`` function of the ``start.py`` module.

Stage 4.4. Infer dataset
"""""""""""""""""""""""""""""""""""""""""""""""""
Implement method
:py:meth:`stubs.llm_2023.lab_7.main.LLMPipeline.infer_dataset`,
which allows to infer the dataset.

.. note:: While iterating through dataset samples,
          use `Dataloader <https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader>`__.

.. note:: When using tokenizer, set parameters
          ``padding=True``, ``truncation=True`` to handle varying sequence lengths.

Method returns pd.DataFrame with ``target`` and ``predictions`` columns.

Stage 5. Introduce evaluation abstraction: ``TaskEvaluator``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now we have our predictions and can evaluate obtained result.

To be able to evaluate the performance of the model
with an appropriate metric you need to implement
:py:class:`stubs.llm_2023.lab_7.main.TaskEvaluator` abstraction.

This class inherits from
:py:class:`stubs.llm_2023.core_utils.task_evaluator.AbstractTaskEvaluator` abstraction.

It has the following internal attributes:
    * ``self._metrics`` - a field of
      :py:class:`stubs.llm_2023.core_utils.metrics.Metrics` abstraction
      with suitable metric.
    * ``self._data_path`` - a string with the path to the `predictions.csv`.

Stage 5.1. Evaluate model performance
"""""""""""""""""""""""""""""""""""""""""""""""""
Implement method
:py:meth:`stubs.llm_2023.lab_7.main.TaskEvaluator.run`,
which allows to evaluate the predictions against the
references using the specified metric.

.. note:: To load evaluation module for your metric you have to use
         `load <https://huggingface.co/docs/evaluate/main/
         en/package_reference/loading_methods#evaluate.load>`__ method.

.. note:: To compute the metrics you have to use
          `compute <https://huggingface.co/docs/datasets/v2.15.0/
          en/package_reference/main_classes#datasets.Metric.compute>`__ method.

Method returns a dictionary with metric result.

Stage 5.2. Demonstrate the result in ``start.py``
"""""""""""""""""""""""""""""""""""""""""""""""""
.. important:: Stages 4.4 - 5.1 are required to get the mark **8**.

Demonstrate dataset inference and model performance evaluation
in the ``main()`` function of the ``start.py`` module.

.. note:: After dataset inference you have to save
          you predictions to ``predictions.csv`` in ``start.py``.

Stage 6. Implement Model as a Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The next step after making an LLM pipeline is the implementation
of a **FastAPI** service utilizing Transformers
for the chosen task.

.. note:: For example, if you have chosen the NMT task,
          your service should accept sentence in one language
          and return translated sentence.

.. important:: All logic should be implemented in the module ``service.py``

Stage 6.1. Initialize core application
"""""""""""""""""""""""""""""""""""""""""""""""""
Implement method,
which allows to initialize all needed
instances for pipeline and web-service.

.. important:: Remember, you have to implement your service using
              `FastAPI <https://fastapi.tiangolo.com/>`__ web framework.

Stage 6.2. Make root endpoint
"""""""""""""""""""""""""""""""""""""""""""""""""
Implement method,
which allows to create a root endpoint of the service.

Root endpoint is the base URL of your service,
where start web page with user interface for the service will be located.

Your start page should be made using
`Jinja <https://jinja.palletsprojects.com/en/3.1.x/>`__ templating engine.

.. note:: Put file with your CSS markup into ``assets/main.css`` module.

User interface should contain:
    * ``Entry field`` to write your data for request.
    * ``Button`` to send data to the server.
    * ``Output`` field to display the results received from the server.

Method returns a dictionary with your page content.

.. note:: Use ``@app.get("/")`` decorator to create a route for the root URL.

Stage 6.2. Make main endpoint
"""""""""""""""""""""""""""""""""""""""""""""""""
When a user clicks the button on the start page,
a POST request must be initiated to the main endpoint,
which is responsible for processing the data using LLM pipeline.

Implement method,
which allows to create a main endpoint for model call.

To be able to make a query in an ``entry field``
you need to implement a class abstraction
with the field ``question``
which contains text of the query.

Method returns response obtained as a result of the pipeline,
which will be displayed in the ``output field``.
Response should be in the form of the **dictionary**
with the key ``infer`` and
the value containing response.

.. note:: Use ``@app.post("/infer")`` decorator to create a route for the
          main endpoint URL.

Stage 6.3. Demonstrate the result
"""""""""""""""""""""""""""""""""""""""""""""""""
.. important:: Stage 6 is required to get the mark **10**.

Demonstrate work of your service by running server
implemented in ``service.py`` module
and obtaining one sample inference result.

.. note:: You can run you server using command:
          ``uvicorn PATH:app --reload``.
