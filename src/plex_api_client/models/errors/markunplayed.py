"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client import utils
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class MarkUnplayedMediaErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class MarkUnplayedMediaErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class MarkUnplayedMediaResponseBodyData(BaseModel):
    errors: Optional[List[MarkUnplayedMediaErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class MarkUnplayedMediaResponseBody(Exception):
    r"""Unauthorized - Returned if the X-Plex-Token is missing from the header or query."""

    data: MarkUnplayedMediaResponseBodyData

    def __init__(self, data: MarkUnplayedMediaResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, MarkUnplayedMediaResponseBodyData)


class MarkUnplayedErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class MarkUnplayedErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class MarkUnplayedResponseBodyData(BaseModel):
    errors: Optional[List[MarkUnplayedErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class MarkUnplayedResponseBody(Exception):
    r"""Bad Request - A parameter was not specified, or was specified incorrectly."""

    data: MarkUnplayedResponseBodyData

    def __init__(self, data: MarkUnplayedResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, MarkUnplayedResponseBodyData)
