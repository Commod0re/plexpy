"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ReleaseTypedDict(TypedDict):
    key: NotRequired[str]
    version: NotRequired[str]
    added: NotRequired[str]
    fixed: NotRequired[str]
    download_url: NotRequired[str]
    state: NotRequired[str]


class Release(BaseModel):
    key: Optional[str] = None

    version: Optional[str] = None

    added: Optional[str] = None

    fixed: Optional[str] = None

    download_url: Annotated[Optional[str], pydantic.Field(alias="downloadURL")] = None

    state: Optional[str] = None


class GetUpdateStatusMediaContainerTypedDict(TypedDict):
    size: NotRequired[int]
    can_install: NotRequired[bool]
    checked_at: NotRequired[int]
    download_url: NotRequired[str]
    status: NotRequired[int]
    release: NotRequired[List[ReleaseTypedDict]]


class GetUpdateStatusMediaContainer(BaseModel):
    size: Optional[int] = None

    can_install: Annotated[Optional[bool], pydantic.Field(alias="canInstall")] = None

    checked_at: Annotated[Optional[int], pydantic.Field(alias="checkedAt")] = None

    download_url: Annotated[Optional[str], pydantic.Field(alias="downloadURL")] = None

    status: Optional[int] = None

    release: Annotated[Optional[List[Release]], pydantic.Field(alias="Release")] = None


class GetUpdateStatusResponseBodyTypedDict(TypedDict):
    r"""The Server Updates"""

    media_container: NotRequired[GetUpdateStatusMediaContainerTypedDict]


class GetUpdateStatusResponseBody(BaseModel):
    r"""The Server Updates"""

    media_container: Annotated[
        Optional[GetUpdateStatusMediaContainer], pydantic.Field(alias="MediaContainer")
    ] = None


class GetUpdateStatusResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetUpdateStatusResponseBodyTypedDict]
    r"""The Server Updates"""


class GetUpdateStatusResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetUpdateStatusResponseBody] = None
    r"""The Server Updates"""
