"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class MyPlexTypedDict(TypedDict):
    auth_token: NotRequired[str]
    username: NotRequired[str]
    mapping_state: NotRequired[str]
    mapping_error: NotRequired[str]
    sign_in_state: NotRequired[str]
    public_address: NotRequired[str]
    public_port: NotRequired[float]
    private_address: NotRequired[str]
    private_port: NotRequired[float]
    subscription_features: NotRequired[str]
    subscription_active: NotRequired[bool]
    subscription_state: NotRequired[str]


class MyPlex(BaseModel):
    auth_token: Annotated[Optional[str], pydantic.Field(alias="authToken")] = None

    username: Optional[str] = None

    mapping_state: Annotated[Optional[str], pydantic.Field(alias="mappingState")] = None

    mapping_error: Annotated[Optional[str], pydantic.Field(alias="mappingError")] = None

    sign_in_state: Annotated[Optional[str], pydantic.Field(alias="signInState")] = None

    public_address: Annotated[Optional[str], pydantic.Field(alias="publicAddress")] = (
        None
    )

    public_port: Annotated[Optional[float], pydantic.Field(alias="publicPort")] = None

    private_address: Annotated[
        Optional[str], pydantic.Field(alias="privateAddress")
    ] = None

    private_port: Annotated[Optional[float], pydantic.Field(alias="privatePort")] = None

    subscription_features: Annotated[
        Optional[str], pydantic.Field(alias="subscriptionFeatures")
    ] = None

    subscription_active: Annotated[
        Optional[bool], pydantic.Field(alias="subscriptionActive")
    ] = None

    subscription_state: Annotated[
        Optional[str], pydantic.Field(alias="subscriptionState")
    ] = None


class GetMyPlexAccountResponseBodyTypedDict(TypedDict):
    r"""MyPlex Account"""

    my_plex: NotRequired[MyPlexTypedDict]


class GetMyPlexAccountResponseBody(BaseModel):
    r"""MyPlex Account"""

    my_plex: Annotated[Optional[MyPlex], pydantic.Field(alias="MyPlex")] = None


class GetMyPlexAccountResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetMyPlexAccountResponseBodyTypedDict]
    r"""MyPlex Account"""


class GetMyPlexAccountResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetMyPlexAccountResponseBody] = None
    r"""MyPlex Account"""
