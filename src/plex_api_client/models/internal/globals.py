"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GlobalsTypedDict(TypedDict):
    x_plex_client_identifier: NotRequired[str]
    r"""The unique identifier for the client application
    This is used to track the client application and its usage
    (UUID, serial number, or other number unique per device)

    """


class Globals(BaseModel):
    x_plex_client_identifier: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Client-Identifier"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The unique identifier for the client application
    This is used to track the client application and its usage
    (UUID, serial number, or other number unique per device)

    """
