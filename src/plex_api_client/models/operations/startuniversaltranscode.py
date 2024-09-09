"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class StartUniversalTranscodeRequestTypedDict(TypedDict):
    has_mde: float
    r"""Whether the media item has MDE"""
    path: str
    r"""The path to the media item to transcode"""
    media_index: float
    r"""The index of the media item to transcode"""
    part_index: float
    r"""The index of the part to transcode"""
    protocol: str
    r"""The protocol to use for the transcode session"""
    fast_seek: NotRequired[float]
    r"""Whether to use fast seek or not"""
    direct_play: NotRequired[float]
    r"""Whether to use direct play or not"""
    direct_stream: NotRequired[float]
    r"""Whether to use direct stream or not"""
    subtitle_size: NotRequired[float]
    r"""The size of the subtitles"""
    subtites: NotRequired[str]
    r"""The subtitles"""
    audio_boost: NotRequired[float]
    r"""The audio boost"""
    location: NotRequired[str]
    r"""The location of the transcode session"""
    media_buffer_size: NotRequired[float]
    r"""The size of the media buffer"""
    session: NotRequired[str]
    r"""The session ID"""
    add_debug_overlay: NotRequired[float]
    r"""Whether to add a debug overlay or not"""
    auto_adjust_quality: NotRequired[float]
    r"""Whether to auto adjust quality or not"""


class StartUniversalTranscodeRequest(BaseModel):
    has_mde: Annotated[
        float,
        pydantic.Field(alias="hasMDE"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Whether the media item has MDE"""

    path: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""The path to the media item to transcode"""

    media_index: Annotated[
        float,
        pydantic.Field(alias="mediaIndex"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""The index of the media item to transcode"""

    part_index: Annotated[
        float,
        pydantic.Field(alias="partIndex"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""The index of the part to transcode"""

    protocol: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""The protocol to use for the transcode session"""

    fast_seek: Annotated[
        Optional[float],
        pydantic.Field(alias="fastSeek"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Whether to use fast seek or not"""

    direct_play: Annotated[
        Optional[float],
        pydantic.Field(alias="directPlay"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Whether to use direct play or not"""

    direct_stream: Annotated[
        Optional[float],
        pydantic.Field(alias="directStream"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Whether to use direct stream or not"""

    subtitle_size: Annotated[
        Optional[float],
        pydantic.Field(alias="subtitleSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The size of the subtitles"""

    subtites: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The subtitles"""

    audio_boost: Annotated[
        Optional[float],
        pydantic.Field(alias="audioBoost"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The audio boost"""

    location: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The location of the transcode session"""

    media_buffer_size: Annotated[
        Optional[float],
        pydantic.Field(alias="mediaBufferSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The size of the media buffer"""

    session: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The session ID"""

    add_debug_overlay: Annotated[
        Optional[float],
        pydantic.Field(alias="addDebugOverlay"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Whether to add a debug overlay or not"""

    auto_adjust_quality: Annotated[
        Optional[float],
        pydantic.Field(alias="autoAdjustQuality"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Whether to auto adjust quality or not"""


class StartUniversalTranscodeResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class StartUniversalTranscodeResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
