"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import httpx
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, QueryParamMetadata
from typing import TypedDict
from typing_extensions import Annotated


class Level(int, Enum):
    r"""An integer log level to write to the PMS log with.
    0: Error
    1: Warning
    2: Info
    3: Debug
    4: Verbose

    """

    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4


class LogLineRequestTypedDict(TypedDict):
    level: Level
    r"""An integer log level to write to the PMS log with.
    0: Error
    1: Warning
    2: Info
    3: Debug
    4: Verbose

    """
    message: str
    r"""The text of the message to write to the log."""
    source: str
    r"""a string indicating the source of the message."""


class LogLineRequest(BaseModel):
    level: Annotated[
        Level, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""An integer log level to write to the PMS log with.
    0: Error
    1: Warning
    2: Info
    3: Debug
    4: Verbose

    """

    message: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""The text of the message to write to the log."""

    source: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""a string indicating the source of the message."""


class LogLineResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class LogLineResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
