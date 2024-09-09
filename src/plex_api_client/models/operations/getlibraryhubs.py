"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import date
from enum import Enum
import httpx
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class QueryParamOnlyTransient(int, Enum):
    r"""Only return hubs which are \"transient\", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added)."""

    ZERO = 0
    ONE = 1


class GetLibraryHubsRequestTypedDict(TypedDict):
    section_id: float
    r"""the Id of the library to query"""
    count: NotRequired[float]
    r"""The number of items to return with each hub."""
    only_transient: NotRequired[QueryParamOnlyTransient]
    r"""Only return hubs which are \"transient\", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added)."""


class GetLibraryHubsRequest(BaseModel):
    section_id: Annotated[
        float,
        pydantic.Field(alias="sectionId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""the Id of the library to query"""

    count: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The number of items to return with each hub."""

    only_transient: Annotated[
        Optional[QueryParamOnlyTransient],
        pydantic.Field(alias="onlyTransient"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Only return hubs which are \"transient\", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added)."""


class GetLibraryHubsPartTypedDict(TypedDict):
    id: NotRequired[int]
    key: NotRequired[str]
    duration: NotRequired[int]
    file: NotRequired[str]
    size: NotRequired[int]
    audio_profile: NotRequired[str]
    container: NotRequired[str]
    has64bit_offsets: NotRequired[bool]
    optimized_for_streaming: NotRequired[bool]
    video_profile: NotRequired[str]


class GetLibraryHubsPart(BaseModel):
    id: Optional[int] = None

    key: Optional[str] = None

    duration: Optional[int] = None

    file: Optional[str] = None

    size: Optional[int] = None

    audio_profile: Annotated[Optional[str], pydantic.Field(alias="audioProfile")] = None

    container: Optional[str] = None

    has64bit_offsets: Annotated[
        Optional[bool], pydantic.Field(alias="has64bitOffsets")
    ] = None

    optimized_for_streaming: Annotated[
        Optional[bool], pydantic.Field(alias="optimizedForStreaming")
    ] = None

    video_profile: Annotated[Optional[str], pydantic.Field(alias="videoProfile")] = None


class GetLibraryHubsMediaTypedDict(TypedDict):
    id: NotRequired[int]
    duration: NotRequired[int]
    bitrate: NotRequired[int]
    width: NotRequired[int]
    height: NotRequired[int]
    aspect_ratio: NotRequired[float]
    audio_channels: NotRequired[int]
    audio_codec: NotRequired[str]
    video_codec: NotRequired[str]
    video_resolution: NotRequired[str]
    container: NotRequired[str]
    video_frame_rate: NotRequired[str]
    optimized_for_streaming: NotRequired[int]
    audio_profile: NotRequired[str]
    has64bit_offsets: NotRequired[bool]
    video_profile: NotRequired[str]
    part: NotRequired[List[GetLibraryHubsPartTypedDict]]


class GetLibraryHubsMedia(BaseModel):
    id: Optional[int] = None

    duration: Optional[int] = None

    bitrate: Optional[int] = None

    width: Optional[int] = None

    height: Optional[int] = None

    aspect_ratio: Annotated[Optional[float], pydantic.Field(alias="aspectRatio")] = None

    audio_channels: Annotated[Optional[int], pydantic.Field(alias="audioChannels")] = (
        None
    )

    audio_codec: Annotated[Optional[str], pydantic.Field(alias="audioCodec")] = None

    video_codec: Annotated[Optional[str], pydantic.Field(alias="videoCodec")] = None

    video_resolution: Annotated[
        Optional[str], pydantic.Field(alias="videoResolution")
    ] = None

    container: Optional[str] = None

    video_frame_rate: Annotated[
        Optional[str], pydantic.Field(alias="videoFrameRate")
    ] = None

    optimized_for_streaming: Annotated[
        Optional[int], pydantic.Field(alias="optimizedForStreaming")
    ] = None

    audio_profile: Annotated[Optional[str], pydantic.Field(alias="audioProfile")] = None

    has64bit_offsets: Annotated[
        Optional[bool], pydantic.Field(alias="has64bitOffsets")
    ] = None

    video_profile: Annotated[Optional[str], pydantic.Field(alias="videoProfile")] = None

    part: Annotated[
        Optional[List[GetLibraryHubsPart]], pydantic.Field(alias="Part")
    ] = None


class GetLibraryHubsGenreTypedDict(TypedDict):
    tag: NotRequired[str]


class GetLibraryHubsGenre(BaseModel):
    tag: Optional[str] = None


class GetLibraryHubsCountryTypedDict(TypedDict):
    tag: NotRequired[str]


class GetLibraryHubsCountry(BaseModel):
    tag: Optional[str] = None


class GetLibraryHubsDirectorTypedDict(TypedDict):
    tag: NotRequired[str]


class GetLibraryHubsDirector(BaseModel):
    tag: Optional[str] = None


class GetLibraryHubsRoleTypedDict(TypedDict):
    tag: NotRequired[str]


class GetLibraryHubsRole(BaseModel):
    tag: Optional[str] = None


class GetLibraryHubsWriterTypedDict(TypedDict):
    tag: NotRequired[str]


class GetLibraryHubsWriter(BaseModel):
    tag: Optional[str] = None


class GetLibraryHubsMetadataTypedDict(TypedDict):
    rating_key: NotRequired[str]
    key: NotRequired[str]
    guid: NotRequired[str]
    studio: NotRequired[str]
    type: NotRequired[str]
    title: NotRequired[str]
    library_section_title: NotRequired[str]
    library_section_id: NotRequired[int]
    library_section_key: NotRequired[str]
    content_rating: NotRequired[str]
    summary: NotRequired[str]
    rating: NotRequired[float]
    audience_rating: NotRequired[float]
    view_count: NotRequired[int]
    last_viewed_at: NotRequired[int]
    year: NotRequired[int]
    tagline: NotRequired[str]
    thumb: NotRequired[str]
    art: NotRequired[str]
    duration: NotRequired[int]
    originally_available_at: NotRequired[date]
    added_at: NotRequired[int]
    updated_at: NotRequired[int]
    audience_rating_image: NotRequired[str]
    primary_extra_key: NotRequired[str]
    rating_image: NotRequired[str]
    media: NotRequired[List[GetLibraryHubsMediaTypedDict]]
    genre: NotRequired[List[GetLibraryHubsGenreTypedDict]]
    country: NotRequired[List[GetLibraryHubsCountryTypedDict]]
    director: NotRequired[List[GetLibraryHubsDirectorTypedDict]]
    role: NotRequired[List[GetLibraryHubsRoleTypedDict]]
    writer: NotRequired[List[GetLibraryHubsWriterTypedDict]]
    skip_count: NotRequired[int]
    chapter_source: NotRequired[str]


class GetLibraryHubsMetadata(BaseModel):
    rating_key: Annotated[Optional[str], pydantic.Field(alias="ratingKey")] = None

    key: Optional[str] = None

    guid: Optional[str] = None

    studio: Optional[str] = None

    type: Optional[str] = None

    title: Optional[str] = None

    library_section_title: Annotated[
        Optional[str], pydantic.Field(alias="librarySectionTitle")
    ] = None

    library_section_id: Annotated[
        Optional[int], pydantic.Field(alias="librarySectionID")
    ] = None

    library_section_key: Annotated[
        Optional[str], pydantic.Field(alias="librarySectionKey")
    ] = None

    content_rating: Annotated[Optional[str], pydantic.Field(alias="contentRating")] = (
        None
    )

    summary: Optional[str] = None

    rating: Optional[float] = None

    audience_rating: Annotated[
        Optional[float], pydantic.Field(alias="audienceRating")
    ] = None

    view_count: Annotated[Optional[int], pydantic.Field(alias="viewCount")] = None

    last_viewed_at: Annotated[Optional[int], pydantic.Field(alias="lastViewedAt")] = (
        None
    )

    year: Optional[int] = None

    tagline: Optional[str] = None

    thumb: Optional[str] = None

    art: Optional[str] = None

    duration: Optional[int] = None

    originally_available_at: Annotated[
        Optional[date], pydantic.Field(alias="originallyAvailableAt")
    ] = None

    added_at: Annotated[Optional[int], pydantic.Field(alias="addedAt")] = None

    updated_at: Annotated[Optional[int], pydantic.Field(alias="updatedAt")] = None

    audience_rating_image: Annotated[
        Optional[str], pydantic.Field(alias="audienceRatingImage")
    ] = None

    primary_extra_key: Annotated[
        Optional[str], pydantic.Field(alias="primaryExtraKey")
    ] = None

    rating_image: Annotated[Optional[str], pydantic.Field(alias="ratingImage")] = None

    media: Annotated[
        Optional[List[GetLibraryHubsMedia]], pydantic.Field(alias="Media")
    ] = None

    genre: Annotated[
        Optional[List[GetLibraryHubsGenre]], pydantic.Field(alias="Genre")
    ] = None

    country: Annotated[
        Optional[List[GetLibraryHubsCountry]], pydantic.Field(alias="Country")
    ] = None

    director: Annotated[
        Optional[List[GetLibraryHubsDirector]], pydantic.Field(alias="Director")
    ] = None

    role: Annotated[
        Optional[List[GetLibraryHubsRole]], pydantic.Field(alias="Role")
    ] = None

    writer: Annotated[
        Optional[List[GetLibraryHubsWriter]], pydantic.Field(alias="Writer")
    ] = None

    skip_count: Annotated[Optional[int], pydantic.Field(alias="skipCount")] = None

    chapter_source: Annotated[Optional[str], pydantic.Field(alias="chapterSource")] = (
        None
    )


class GetLibraryHubsHubTypedDict(TypedDict):
    key: NotRequired[str]
    title: NotRequired[str]
    type: NotRequired[str]
    hub_identifier: NotRequired[str]
    context: NotRequired[str]
    size: NotRequired[int]
    more: NotRequired[bool]
    style: NotRequired[str]
    hub_key: NotRequired[str]
    metadata: NotRequired[List[GetLibraryHubsMetadataTypedDict]]
    promoted: NotRequired[bool]
    random: NotRequired[bool]


class GetLibraryHubsHub(BaseModel):
    key: Optional[str] = None

    title: Optional[str] = None

    type: Optional[str] = None

    hub_identifier: Annotated[Optional[str], pydantic.Field(alias="hubIdentifier")] = (
        None
    )

    context: Optional[str] = None

    size: Optional[int] = None

    more: Optional[bool] = None

    style: Optional[str] = None

    hub_key: Annotated[Optional[str], pydantic.Field(alias="hubKey")] = None

    metadata: Annotated[
        Optional[List[GetLibraryHubsMetadata]], pydantic.Field(alias="Metadata")
    ] = None

    promoted: Optional[bool] = None

    random: Optional[bool] = None


class GetLibraryHubsMediaContainerTypedDict(TypedDict):
    size: NotRequired[int]
    allow_sync: NotRequired[bool]
    identifier: NotRequired[str]
    library_section_id: NotRequired[int]
    library_section_title: NotRequired[str]
    library_section_uuid: NotRequired[str]
    hub: NotRequired[List[GetLibraryHubsHubTypedDict]]


class GetLibraryHubsMediaContainer(BaseModel):
    size: Optional[int] = None

    allow_sync: Annotated[Optional[bool], pydantic.Field(alias="allowSync")] = None

    identifier: Optional[str] = None

    library_section_id: Annotated[
        Optional[int], pydantic.Field(alias="librarySectionID")
    ] = None

    library_section_title: Annotated[
        Optional[str], pydantic.Field(alias="librarySectionTitle")
    ] = None

    library_section_uuid: Annotated[
        Optional[str], pydantic.Field(alias="librarySectionUUID")
    ] = None

    hub: Annotated[Optional[List[GetLibraryHubsHub]], pydantic.Field(alias="Hub")] = (
        None
    )


class GetLibraryHubsResponseBodyTypedDict(TypedDict):
    r"""The hubs specific to the library"""

    media_container: NotRequired[GetLibraryHubsMediaContainerTypedDict]


class GetLibraryHubsResponseBody(BaseModel):
    r"""The hubs specific to the library"""

    media_container: Annotated[
        Optional[GetLibraryHubsMediaContainer], pydantic.Field(alias="MediaContainer")
    ] = None


class GetLibraryHubsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetLibraryHubsResponseBodyTypedDict]
    r"""The hubs specific to the library"""


class GetLibraryHubsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetLibraryHubsResponseBody] = None
    r"""The hubs specific to the library"""
