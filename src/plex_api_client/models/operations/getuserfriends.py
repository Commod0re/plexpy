"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import httpx
from plex_api_client.types import BaseModel, Nullable, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired

GET_USER_FRIENDS_SERVERS = [
    "https://plex.tv/api/v2/",
]


class SharedServersTypedDict(TypedDict):
    pass


class SharedServers(BaseModel):
    pass


class SharedSourcesTypedDict(TypedDict):
    pass


class SharedSources(BaseModel):
    pass


class Status(str, Enum):
    r"""Current friend request status"""

    ACCEPTED = "accepted"


class FriendTypedDict(TypedDict):
    email: str
    r"""The account email address"""
    friendly_name: Nullable[str]
    r"""The account full name"""
    home: bool
    r"""If the account is a Plex Home user"""
    id: int
    r"""The Plex account ID"""
    shared_servers: List[SharedServersTypedDict]
    shared_sources: List[SharedSourcesTypedDict]
    status: Status
    r"""Current friend request status"""
    thumb: str
    r"""URL of the account thumbnail"""
    title: str
    r"""The title of the account (username or friendly name)"""
    username: str
    r"""The account username"""
    uuid: str
    r"""The account Universally Unique Identifier (UUID)"""
    restricted: NotRequired[bool]
    r"""If the account is a Plex Home managed user"""


class Friend(BaseModel):
    email: str
    r"""The account email address"""

    friendly_name: Annotated[Nullable[str], pydantic.Field(alias="friendlyName")]
    r"""The account full name"""

    home: bool
    r"""If the account is a Plex Home user"""

    id: int
    r"""The Plex account ID"""

    shared_servers: Annotated[
        List[SharedServers], pydantic.Field(alias="sharedServers")
    ]

    shared_sources: Annotated[
        List[SharedSources], pydantic.Field(alias="sharedSources")
    ]

    status: Status
    r"""Current friend request status"""

    thumb: str
    r"""URL of the account thumbnail"""

    title: str
    r"""The title of the account (username or friendly name)"""

    username: str
    r"""The account username"""

    uuid: str
    r"""The account Universally Unique Identifier (UUID)"""

    restricted: Optional[bool] = False
    r"""If the account is a Plex Home managed user"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["restricted"]
        nullable_fields = ["friendlyName"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class GetUserFriendsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    friends: NotRequired[List[FriendTypedDict]]
    r"""Friends Data"""


class GetUserFriendsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    friends: Optional[List[Friend]] = None
    r"""Friends Data"""
