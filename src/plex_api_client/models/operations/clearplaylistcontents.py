"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import TypedDict
from typing_extensions import Annotated


class ClearPlaylistContentsRequestTypedDict(TypedDict):
    playlist_id: float
    r"""the ID of the playlist"""


class ClearPlaylistContentsRequest(BaseModel):
    playlist_id: Annotated[
        float,
        pydantic.Field(alias="playlistID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""the ID of the playlist"""


class ClearPlaylistContentsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class ClearPlaylistContentsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
