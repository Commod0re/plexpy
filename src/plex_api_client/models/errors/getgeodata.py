"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client import utils
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetGeoDataPlexErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class GetGeoDataPlexErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class GetGeoDataPlexResponseBodyData(BaseModel):
    errors: Optional[List[GetGeoDataPlexErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class GetGeoDataPlexResponseBody(Exception):
    r"""Unauthorized - Returned if the X-Plex-Token is missing from the header or query."""

    data: GetGeoDataPlexResponseBodyData

    def __init__(self, data: GetGeoDataPlexResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetGeoDataPlexResponseBodyData)


class GetGeoDataErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class GetGeoDataErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class GetGeoDataResponseBodyData(BaseModel):
    errors: Optional[List[GetGeoDataErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class GetGeoDataResponseBody(Exception):
    r"""Bad Request - A parameter was not specified, or was specified incorrectly."""

    data: GetGeoDataResponseBodyData

    def __init__(self, data: GetGeoDataResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetGeoDataResponseBodyData)
