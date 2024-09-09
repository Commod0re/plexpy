"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class DeviceTypedDict(TypedDict):
    id: NotRequired[float]
    name: NotRequired[str]
    platform: NotRequired[str]
    client_identifier: NotRequired[str]
    created_at: NotRequired[float]


class Device(BaseModel):
    id: Optional[float] = None

    name: Optional[str] = None

    platform: Optional[str] = None

    client_identifier: Annotated[
        Optional[str], pydantic.Field(alias="clientIdentifier")
    ] = None

    created_at: Annotated[Optional[float], pydantic.Field(alias="createdAt")] = None


class GetDevicesMediaContainerTypedDict(TypedDict):
    size: NotRequired[float]
    identifier: NotRequired[str]
    device: NotRequired[List[DeviceTypedDict]]


class GetDevicesMediaContainer(BaseModel):
    size: Optional[float] = None

    identifier: Optional[str] = None

    device: Annotated[Optional[List[Device]], pydantic.Field(alias="Device")] = None


class GetDevicesResponseBodyTypedDict(TypedDict):
    r"""Devices"""

    media_container: NotRequired[GetDevicesMediaContainerTypedDict]


class GetDevicesResponseBody(BaseModel):
    r"""Devices"""

    media_container: Annotated[
        Optional[GetDevicesMediaContainer], pydantic.Field(alias="MediaContainer")
    ] = None


class GetDevicesResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetDevicesResponseBodyTypedDict]
    r"""Devices"""


class GetDevicesResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetDevicesResponseBody] = None
    r"""Devices"""
