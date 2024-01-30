"""
Web service for model inference.
"""
# pylint: disable=too-few-public-methods, undefined-variable, unused-import, assignment-from-no-return, duplicate-code
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic.dataclasses import dataclass

from stubs.labs.lab_7_llm.main import LLMPipeline


def init_application() -> tuple[FastAPI, LLMPipeline]:
    """
    Initialize core application.

    Run: uvicorn reference_service.server:app --reload

    Returns:
        tuple[fastapi.FastAPI, LLMPipeline]: Instance of server and pipeline
    """


@dataclass
class Query:
    """
    Model, defining incoming model request.
    """

    question: str


# @app.get("/", response_class=HTMLResponse)
async def root(request: Request) -> Jinja2Templates.TemplateResponse:
    """
    Root endpoint with server-side rendering.

    Args:
        request (Request): Request

    Returns:
        TemplateResponse: Template with index.html
    """


# @app.post("/infer")
async def infer(query: Query) -> dict:
    """
    Main endpoint for model call.

    Args:
        query (Query): Query from client

    Returns:
        dict: Content with predictions.
    """
