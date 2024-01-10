"""
Web service for model inference.
"""
# pylint: disable=too-few-public-methods, undefined-variable, unused-import, assignment-from-no-return
from pathlib import Path

from fastapi import FastAPI
from pydantic.dataclasses import dataclass

from stubs.llm_2023.lab_7.main import LLMPipeline


def init_application() -> tuple[FastAPI, LLMPipeline]:
    """
    #doctest: +SKIP
    Initialize core application.

    Run: uvicorn reference_service.server:app --reload

    Returns:
        tuple[fastapi.FastAPI, LLMPipeline]: instance of server and pipeline
    """


@dataclass
class Query:
    """
    Model, defining incoming model request.
    """

    question: str


(app, pipeline) = init_application()


@app.get("/")
async def root() -> dict:
    """
    Root endpoint with server-side rendering.

    Returns:
        dict: temporary dict with content
    """
    return {"message": "Hello, Egor!"}


@app.post("/infer")
async def infer(query: Query) -> dict:
    """
    Main endpoint for model call.

    Args:
        query (Query): query from client

    Returns:
        dict: content with predictions.
    """
    result = pipeline.infer_sample(query.question)
    return {"infer": result}
