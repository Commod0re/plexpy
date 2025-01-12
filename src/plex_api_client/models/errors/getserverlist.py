"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client import utils
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetServerListServerErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class GetServerListServerErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class GetServerListUnauthorizedData(BaseModel):
    errors: Optional[List[GetServerListServerErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class GetServerListUnauthorized(Exception):
    r"""Unauthorized - Returned if the X-Plex-Token is missing from the header or query."""

    data: GetServerListUnauthorizedData

    def __init__(self, data: GetServerListUnauthorizedData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetServerListUnauthorizedData)


class GetServerListErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class GetServerListErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class GetServerListBadRequestData(BaseModel):
    errors: Optional[List[GetServerListErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class GetServerListBadRequest(Exception):
    r"""Bad Request - A parameter was not specified, or was specified incorrectly."""

    data: GetServerListBadRequestData

    def __init__(self, data: GetServerListBadRequestData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetServerListBadRequestData)
