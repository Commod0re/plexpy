"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client import utils
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetTranscodeSessionsSessionsErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class GetTranscodeSessionsSessionsErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class GetTranscodeSessionsUnauthorizedData(BaseModel):
    errors: Optional[List[GetTranscodeSessionsSessionsErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class GetTranscodeSessionsUnauthorized(Exception):
    r"""Unauthorized - Returned if the X-Plex-Token is missing from the header or query."""

    data: GetTranscodeSessionsUnauthorizedData

    def __init__(self, data: GetTranscodeSessionsUnauthorizedData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetTranscodeSessionsUnauthorizedData)


class GetTranscodeSessionsErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class GetTranscodeSessionsErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class GetTranscodeSessionsBadRequestData(BaseModel):
    errors: Optional[List[GetTranscodeSessionsErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class GetTranscodeSessionsBadRequest(Exception):
    r"""Bad Request - A parameter was not specified, or was specified incorrectly."""

    data: GetTranscodeSessionsBadRequestData

    def __init__(self, data: GetTranscodeSessionsBadRequestData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetTranscodeSessionsBadRequestData)