"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import httpx
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetSearchResultsRequestTypedDict(TypedDict):
    query: str
    r"""The search query string to use"""


class GetSearchResultsRequest(BaseModel):
    query: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""The search query string to use"""


class GetSearchResultsPartTypedDict(TypedDict):
    id: NotRequired[float]
    key: NotRequired[str]
    duration: NotRequired[float]
    file: NotRequired[str]
    size: NotRequired[float]
    audio_profile: NotRequired[str]
    container: NotRequired[str]
    video_profile: NotRequired[str]


class GetSearchResultsPart(BaseModel):
    id: Optional[float] = None

    key: Optional[str] = None

    duration: Optional[float] = None

    file: Optional[str] = None

    size: Optional[float] = None

    audio_profile: Annotated[Optional[str], pydantic.Field(alias="audioProfile")] = None

    container: Optional[str] = None

    video_profile: Annotated[Optional[str], pydantic.Field(alias="videoProfile")] = None


class GetSearchResultsMediaTypedDict(TypedDict):
    id: NotRequired[float]
    duration: NotRequired[float]
    bitrate: NotRequired[float]
    width: NotRequired[float]
    height: NotRequired[float]
    aspect_ratio: NotRequired[float]
    audio_channels: NotRequired[float]
    audio_codec: NotRequired[str]
    video_codec: NotRequired[str]
    video_resolution: NotRequired[float]
    container: NotRequired[str]
    video_frame_rate: NotRequired[str]
    audio_profile: NotRequired[str]
    video_profile: NotRequired[str]
    part: NotRequired[List[GetSearchResultsPartTypedDict]]


class GetSearchResultsMedia(BaseModel):
    id: Optional[float] = None

    duration: Optional[float] = None

    bitrate: Optional[float] = None

    width: Optional[float] = None

    height: Optional[float] = None

    aspect_ratio: Annotated[Optional[float], pydantic.Field(alias="aspectRatio")] = None

    audio_channels: Annotated[
        Optional[float], pydantic.Field(alias="audioChannels")
    ] = None

    audio_codec: Annotated[Optional[str], pydantic.Field(alias="audioCodec")] = None

    video_codec: Annotated[Optional[str], pydantic.Field(alias="videoCodec")] = None

    video_resolution: Annotated[
        Optional[float], pydantic.Field(alias="videoResolution")
    ] = None

    container: Optional[str] = None

    video_frame_rate: Annotated[
        Optional[str], pydantic.Field(alias="videoFrameRate")
    ] = None

    audio_profile: Annotated[Optional[str], pydantic.Field(alias="audioProfile")] = None

    video_profile: Annotated[Optional[str], pydantic.Field(alias="videoProfile")] = None

    part: Annotated[
        Optional[List[GetSearchResultsPart]], pydantic.Field(alias="Part")
    ] = None


class GetSearchResultsGenreTypedDict(TypedDict):
    tag: NotRequired[str]


class GetSearchResultsGenre(BaseModel):
    tag: Optional[str] = None


class GetSearchResultsDirectorTypedDict(TypedDict):
    tag: NotRequired[str]


class GetSearchResultsDirector(BaseModel):
    tag: Optional[str] = None


class GetSearchResultsWriterTypedDict(TypedDict):
    tag: NotRequired[str]


class GetSearchResultsWriter(BaseModel):
    tag: Optional[str] = None


class GetSearchResultsCountryTypedDict(TypedDict):
    tag: NotRequired[str]


class GetSearchResultsCountry(BaseModel):
    tag: Optional[str] = None


class GetSearchResultsRoleTypedDict(TypedDict):
    tag: NotRequired[str]


class GetSearchResultsRole(BaseModel):
    tag: Optional[str] = None


class GetSearchResultsMetadataTypedDict(TypedDict):
    allow_sync: NotRequired[bool]
    library_section_id: NotRequired[float]
    library_section_title: NotRequired[str]
    library_section_uuid: NotRequired[str]
    personal: NotRequired[bool]
    source_title: NotRequired[str]
    rating_key: NotRequired[float]
    key: NotRequired[str]
    guid: NotRequired[str]
    studio: NotRequired[str]
    type: NotRequired[str]
    title: NotRequired[str]
    content_rating: NotRequired[str]
    summary: NotRequired[str]
    rating: NotRequired[float]
    audience_rating: NotRequired[float]
    year: NotRequired[float]
    tagline: NotRequired[str]
    thumb: NotRequired[str]
    art: NotRequired[str]
    duration: NotRequired[float]
    originally_available_at: NotRequired[datetime]
    added_at: NotRequired[float]
    updated_at: NotRequired[float]
    audience_rating_image: NotRequired[str]
    chapter_source: NotRequired[str]
    primary_extra_key: NotRequired[str]
    rating_image: NotRequired[str]
    media: NotRequired[List[GetSearchResultsMediaTypedDict]]
    genre: NotRequired[List[GetSearchResultsGenreTypedDict]]
    director: NotRequired[List[GetSearchResultsDirectorTypedDict]]
    writer: NotRequired[List[GetSearchResultsWriterTypedDict]]
    country: NotRequired[List[GetSearchResultsCountryTypedDict]]
    role: NotRequired[List[GetSearchResultsRoleTypedDict]]


class GetSearchResultsMetadata(BaseModel):
    allow_sync: Annotated[Optional[bool], pydantic.Field(alias="allowSync")] = None

    library_section_id: Annotated[
        Optional[float], pydantic.Field(alias="librarySectionID")
    ] = None

    library_section_title: Annotated[
        Optional[str], pydantic.Field(alias="librarySectionTitle")
    ] = None

    library_section_uuid: Annotated[
        Optional[str], pydantic.Field(alias="librarySectionUUID")
    ] = None

    personal: Optional[bool] = None

    source_title: Annotated[Optional[str], pydantic.Field(alias="sourceTitle")] = None

    rating_key: Annotated[Optional[float], pydantic.Field(alias="ratingKey")] = None

    key: Optional[str] = None

    guid: Optional[str] = None

    studio: Optional[str] = None

    type: Optional[str] = None

    title: Optional[str] = None

    content_rating: Annotated[Optional[str], pydantic.Field(alias="contentRating")] = (
        None
    )

    summary: Optional[str] = None

    rating: Optional[float] = None

    audience_rating: Annotated[
        Optional[float], pydantic.Field(alias="audienceRating")
    ] = None

    year: Optional[float] = None

    tagline: Optional[str] = None

    thumb: Optional[str] = None

    art: Optional[str] = None

    duration: Optional[float] = None

    originally_available_at: Annotated[
        Optional[datetime], pydantic.Field(alias="originallyAvailableAt")
    ] = None

    added_at: Annotated[Optional[float], pydantic.Field(alias="addedAt")] = None

    updated_at: Annotated[Optional[float], pydantic.Field(alias="updatedAt")] = None

    audience_rating_image: Annotated[
        Optional[str], pydantic.Field(alias="audienceRatingImage")
    ] = None

    chapter_source: Annotated[Optional[str], pydantic.Field(alias="chapterSource")] = (
        None
    )

    primary_extra_key: Annotated[
        Optional[str], pydantic.Field(alias="primaryExtraKey")
    ] = None

    rating_image: Annotated[Optional[str], pydantic.Field(alias="ratingImage")] = None

    media: Annotated[
        Optional[List[GetSearchResultsMedia]], pydantic.Field(alias="Media")
    ] = None

    genre: Annotated[
        Optional[List[GetSearchResultsGenre]], pydantic.Field(alias="Genre")
    ] = None

    director: Annotated[
        Optional[List[GetSearchResultsDirector]], pydantic.Field(alias="Director")
    ] = None

    writer: Annotated[
        Optional[List[GetSearchResultsWriter]], pydantic.Field(alias="Writer")
    ] = None

    country: Annotated[
        Optional[List[GetSearchResultsCountry]], pydantic.Field(alias="Country")
    ] = None

    role: Annotated[
        Optional[List[GetSearchResultsRole]], pydantic.Field(alias="Role")
    ] = None


class ProviderTypedDict(TypedDict):
    key: NotRequired[str]
    title: NotRequired[str]
    type: NotRequired[str]


class Provider(BaseModel):
    key: Optional[str] = None

    title: Optional[str] = None

    type: Optional[str] = None


class GetSearchResultsMediaContainerTypedDict(TypedDict):
    size: NotRequired[float]
    identifier: NotRequired[str]
    media_tag_prefix: NotRequired[str]
    media_tag_version: NotRequired[float]
    metadata: NotRequired[List[GetSearchResultsMetadataTypedDict]]
    provider: NotRequired[List[ProviderTypedDict]]


class GetSearchResultsMediaContainer(BaseModel):
    size: Optional[float] = None

    identifier: Optional[str] = None

    media_tag_prefix: Annotated[
        Optional[str], pydantic.Field(alias="mediaTagPrefix")
    ] = None

    media_tag_version: Annotated[
        Optional[float], pydantic.Field(alias="mediaTagVersion")
    ] = None

    metadata: Annotated[
        Optional[List[GetSearchResultsMetadata]], pydantic.Field(alias="Metadata")
    ] = None

    provider: Annotated[Optional[List[Provider]], pydantic.Field(alias="Provider")] = (
        None
    )


class GetSearchResultsResponseBodyTypedDict(TypedDict):
    r"""Search Results"""

    media_container: NotRequired[GetSearchResultsMediaContainerTypedDict]


class GetSearchResultsResponseBody(BaseModel):
    r"""Search Results"""

    media_container: Annotated[
        Optional[GetSearchResultsMediaContainer], pydantic.Field(alias="MediaContainer")
    ] = None


class GetSearchResultsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetSearchResultsResponseBodyTypedDict]
    r"""Search Results"""


class GetSearchResultsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetSearchResultsResponseBody] = None
    r"""Search Results"""
