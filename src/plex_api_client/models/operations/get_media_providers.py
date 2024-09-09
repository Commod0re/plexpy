"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetMediaProvidersRequestTypedDict(TypedDict):
    x_plex_token: str
    r"""Plex Authentication Token"""


class GetMediaProvidersRequest(BaseModel):
    x_plex_token: Annotated[
        str,
        pydantic.Field(alias="X-Plex-Token"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Plex Authentication Token"""


class PivotTypedDict(TypedDict):
    id: NotRequired[str]
    key: NotRequired[str]
    type: NotRequired[str]
    title: NotRequired[str]
    context: NotRequired[str]
    symbol: NotRequired[str]


class Pivot(BaseModel):
    id: Optional[str] = None

    key: Optional[str] = None

    type: Optional[str] = None

    title: Optional[str] = None

    context: Optional[str] = None

    symbol: Optional[str] = None


class GetMediaProvidersDirectoryTypedDict(TypedDict):
    hub_key: NotRequired[str]
    title: NotRequired[str]
    agent: NotRequired[str]
    language: NotRequired[str]
    refreshing: NotRequired[bool]
    scanner: NotRequired[str]
    uuid: NotRequired[str]
    id: NotRequired[str]
    key: NotRequired[str]
    type: NotRequired[str]
    subtype: NotRequired[str]
    updated_at: NotRequired[int]
    scanned_at: NotRequired[int]
    pivot: NotRequired[List[PivotTypedDict]]


class GetMediaProvidersDirectory(BaseModel):
    hub_key: Annotated[Optional[str], pydantic.Field(alias="hubKey")] = None

    title: Optional[str] = None

    agent: Optional[str] = None

    language: Optional[str] = None

    refreshing: Optional[bool] = None

    scanner: Optional[str] = None

    uuid: Optional[str] = None

    id: Optional[str] = None

    key: Optional[str] = None

    type: Optional[str] = None

    subtype: Optional[str] = None

    updated_at: Annotated[Optional[int], pydantic.Field(alias="updatedAt")] = None

    scanned_at: Annotated[Optional[int], pydantic.Field(alias="scannedAt")] = None

    pivot: Annotated[Optional[List[Pivot]], pydantic.Field(alias="Pivot")] = None


class FeatureTypedDict(TypedDict):
    key: NotRequired[str]
    type: NotRequired[str]
    directory: NotRequired[List[GetMediaProvidersDirectoryTypedDict]]


class Feature(BaseModel):
    key: Optional[str] = None

    type: Optional[str] = None

    directory: Annotated[
        Optional[List[GetMediaProvidersDirectory]], pydantic.Field(alias="Directory")
    ] = None


class MediaProviderTypedDict(TypedDict):
    identifier: NotRequired[str]
    title: NotRequired[str]
    types: NotRequired[str]
    protocols: NotRequired[str]
    feature: NotRequired[List[FeatureTypedDict]]


class MediaProvider(BaseModel):
    identifier: Optional[str] = None

    title: Optional[str] = None

    types: Optional[str] = None

    protocols: Optional[str] = None

    feature: Annotated[Optional[List[Feature]], pydantic.Field(alias="Feature")] = None


class GetMediaProvidersMediaContainerTypedDict(TypedDict):
    size: NotRequired[int]
    allow_camera_upload: NotRequired[bool]
    allow_channel_access: NotRequired[bool]
    allow_sharing: NotRequired[bool]
    allow_sync: NotRequired[bool]
    allow_tuners: NotRequired[bool]
    background_processing: NotRequired[bool]
    certificate: NotRequired[bool]
    companion_proxy: NotRequired[bool]
    country_code: NotRequired[str]
    diagnostics: NotRequired[str]
    event_stream: NotRequired[bool]
    friendly_name: NotRequired[str]
    livetv: NotRequired[int]
    machine_identifier: NotRequired[str]
    music_analysis: NotRequired[int]
    my_plex: NotRequired[bool]
    my_plex_mapping_state: NotRequired[str]
    my_plex_signin_state: NotRequired[str]
    my_plex_subscription: NotRequired[bool]
    my_plex_username: NotRequired[str]
    offline_transcode: NotRequired[int]
    owner_features: NotRequired[str]
    platform: NotRequired[str]
    platform_version: NotRequired[str]
    plugin_host: NotRequired[bool]
    push_notifications: NotRequired[bool]
    read_only_libraries: NotRequired[bool]
    streaming_brain_abr_version: NotRequired[int]
    streaming_brain_version: NotRequired[int]
    sync: NotRequired[bool]
    transcoder_active_video_sessions: NotRequired[int]
    transcoder_audio: NotRequired[bool]
    transcoder_lyrics: NotRequired[bool]
    transcoder_subtitles: NotRequired[bool]
    transcoder_video: NotRequired[bool]
    transcoder_video_bitrates: NotRequired[str]
    transcoder_video_qualities: NotRequired[str]
    transcoder_video_resolutions: NotRequired[str]
    updated_at: NotRequired[int]
    updater: NotRequired[bool]
    version: NotRequired[str]
    voice_search: NotRequired[bool]
    media_provider: NotRequired[List[MediaProviderTypedDict]]


class GetMediaProvidersMediaContainer(BaseModel):
    size: Optional[int] = None

    allow_camera_upload: Annotated[
        Optional[bool], pydantic.Field(alias="allowCameraUpload")
    ] = None

    allow_channel_access: Annotated[
        Optional[bool], pydantic.Field(alias="allowChannelAccess")
    ] = None

    allow_sharing: Annotated[Optional[bool], pydantic.Field(alias="allowSharing")] = (
        None
    )

    allow_sync: Annotated[Optional[bool], pydantic.Field(alias="allowSync")] = None

    allow_tuners: Annotated[Optional[bool], pydantic.Field(alias="allowTuners")] = None

    background_processing: Annotated[
        Optional[bool], pydantic.Field(alias="backgroundProcessing")
    ] = None

    certificate: Optional[bool] = None

    companion_proxy: Annotated[
        Optional[bool], pydantic.Field(alias="companionProxy")
    ] = None

    country_code: Annotated[Optional[str], pydantic.Field(alias="countryCode")] = None

    diagnostics: Optional[str] = None

    event_stream: Annotated[Optional[bool], pydantic.Field(alias="eventStream")] = None

    friendly_name: Annotated[Optional[str], pydantic.Field(alias="friendlyName")] = None

    livetv: Optional[int] = None

    machine_identifier: Annotated[
        Optional[str], pydantic.Field(alias="machineIdentifier")
    ] = None

    music_analysis: Annotated[Optional[int], pydantic.Field(alias="musicAnalysis")] = (
        None
    )

    my_plex: Annotated[Optional[bool], pydantic.Field(alias="myPlex")] = None

    my_plex_mapping_state: Annotated[
        Optional[str], pydantic.Field(alias="myPlexMappingState")
    ] = None

    my_plex_signin_state: Annotated[
        Optional[str], pydantic.Field(alias="myPlexSigninState")
    ] = None

    my_plex_subscription: Annotated[
        Optional[bool], pydantic.Field(alias="myPlexSubscription")
    ] = None

    my_plex_username: Annotated[
        Optional[str], pydantic.Field(alias="myPlexUsername")
    ] = None

    offline_transcode: Annotated[
        Optional[int], pydantic.Field(alias="offlineTranscode")
    ] = None

    owner_features: Annotated[Optional[str], pydantic.Field(alias="ownerFeatures")] = (
        None
    )

    platform: Optional[str] = None

    platform_version: Annotated[
        Optional[str], pydantic.Field(alias="platformVersion")
    ] = None

    plugin_host: Annotated[Optional[bool], pydantic.Field(alias="pluginHost")] = None

    push_notifications: Annotated[
        Optional[bool], pydantic.Field(alias="pushNotifications")
    ] = None

    read_only_libraries: Annotated[
        Optional[bool], pydantic.Field(alias="readOnlyLibraries")
    ] = None

    streaming_brain_abr_version: Annotated[
        Optional[int], pydantic.Field(alias="streamingBrainABRVersion")
    ] = None

    streaming_brain_version: Annotated[
        Optional[int], pydantic.Field(alias="streamingBrainVersion")
    ] = None

    sync: Optional[bool] = None

    transcoder_active_video_sessions: Annotated[
        Optional[int], pydantic.Field(alias="transcoderActiveVideoSessions")
    ] = None

    transcoder_audio: Annotated[
        Optional[bool], pydantic.Field(alias="transcoderAudio")
    ] = None

    transcoder_lyrics: Annotated[
        Optional[bool], pydantic.Field(alias="transcoderLyrics")
    ] = None

    transcoder_subtitles: Annotated[
        Optional[bool], pydantic.Field(alias="transcoderSubtitles")
    ] = None

    transcoder_video: Annotated[
        Optional[bool], pydantic.Field(alias="transcoderVideo")
    ] = None

    transcoder_video_bitrates: Annotated[
        Optional[str], pydantic.Field(alias="transcoderVideoBitrates")
    ] = None

    transcoder_video_qualities: Annotated[
        Optional[str], pydantic.Field(alias="transcoderVideoQualities")
    ] = None

    transcoder_video_resolutions: Annotated[
        Optional[str], pydantic.Field(alias="transcoderVideoResolutions")
    ] = None

    updated_at: Annotated[Optional[int], pydantic.Field(alias="updatedAt")] = None

    updater: Optional[bool] = None

    version: Optional[str] = None

    voice_search: Annotated[Optional[bool], pydantic.Field(alias="voiceSearch")] = None

    media_provider: Annotated[
        Optional[List[MediaProvider]], pydantic.Field(alias="MediaProvider")
    ] = None


class GetMediaProvidersResponseBodyTypedDict(TypedDict):
    r"""Media providers and their features"""

    media_container: NotRequired[GetMediaProvidersMediaContainerTypedDict]


class GetMediaProvidersResponseBody(BaseModel):
    r"""Media providers and their features"""

    media_container: Annotated[
        Optional[GetMediaProvidersMediaContainer],
        pydantic.Field(alias="MediaContainer"),
    ] = None


class GetMediaProvidersResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetMediaProvidersResponseBodyTypedDict]
    r"""Media providers and their features"""


class GetMediaProvidersResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetMediaProvidersResponseBody] = None
    r"""Media providers and their features"""
