"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client import utils
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PostUsersSignInDataAuthenticationErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class PostUsersSignInDataAuthenticationErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class PostUsersSignInDataUnauthorizedData(BaseModel):
    errors: Optional[List[PostUsersSignInDataAuthenticationErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class PostUsersSignInDataUnauthorized(Exception):
    r"""Unauthorized - Returned if the X-Plex-Token is missing from the header or query."""

    data: PostUsersSignInDataUnauthorizedData

    def __init__(self, data: PostUsersSignInDataUnauthorizedData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, PostUsersSignInDataUnauthorizedData)


class PostUsersSignInDataErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class PostUsersSignInDataErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class PostUsersSignInDataBadRequestData(BaseModel):
    errors: Optional[List[PostUsersSignInDataErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class PostUsersSignInDataBadRequest(Exception):
    r"""Bad Request - A parameter was not specified, or was specified incorrectly."""

    data: PostUsersSignInDataBadRequestData

    def __init__(self, data: PostUsersSignInDataBadRequestData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, PostUsersSignInDataBadRequestData)
