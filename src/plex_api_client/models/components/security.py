"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, SecurityMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class SecurityTypedDict(TypedDict):
    access_token: NotRequired[str]


class Security(BaseModel):
    access_token: Annotated[
        Optional[str],
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="apiKey",
                sub_type="query",
                field_name="X-Plex-Token",
            )
        ),
    ] = None
