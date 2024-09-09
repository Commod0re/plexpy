"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdatePlaylistRequestTypedDict(TypedDict):
    playlist_id: float
    r"""the ID of the playlist"""
    title: NotRequired[str]
    r"""name of the playlist"""
    summary: NotRequired[str]
    r"""summary description of the playlist"""


class UpdatePlaylistRequest(BaseModel):
    playlist_id: Annotated[
        float,
        pydantic.Field(alias="playlistID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""the ID of the playlist"""

    title: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""name of the playlist"""

    summary: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""summary description of the playlist"""


class UpdatePlaylistResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class UpdatePlaylistResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
