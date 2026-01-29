"""
Web service for model inference.
"""

# pylint: disable=too-few-public-methods


def init_application() -> tuple:
    """
    Initialize core application.

    Run: uvicorn lab_7_llm.service:app --reload

    Returns:
        tuple: tuple of two objects, instance of FastAPI server and LLMPipeline pipeline.
    """


app, pipeline = (None, None)
