"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import httpx
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import TypedDict
from typing_extensions import Annotated


class PathParamTaskName(str, Enum):
    r"""The name of the task to be started."""

    BACKUP_DATABASE = "BackupDatabase"
    BUILD_GRACENOTE_COLLECTIONS = "BuildGracenoteCollections"
    CHECK_FOR_UPDATES = "CheckForUpdates"
    CLEAN_OLD_BUNDLES = "CleanOldBundles"
    CLEAN_OLD_CACHE_FILES = "CleanOldCacheFiles"
    DEEP_MEDIA_ANALYSIS = "DeepMediaAnalysis"
    GENERATE_AUTO_TAGS = "GenerateAutoTags"
    GENERATE_CHAPTER_THUMBS = "GenerateChapterThumbs"
    GENERATE_MEDIA_INDEX_FILES = "GenerateMediaIndexFiles"
    OPTIMIZE_DATABASE = "OptimizeDatabase"
    REFRESH_LIBRARIES = "RefreshLibraries"
    REFRESH_LOCAL_MEDIA = "RefreshLocalMedia"
    REFRESH_PERIODIC_METADATA = "RefreshPeriodicMetadata"
    UPGRADE_MEDIA_ANALYSIS = "UpgradeMediaAnalysis"


class StopTaskRequestTypedDict(TypedDict):
    task_name: PathParamTaskName
    r"""The name of the task to be started."""


class StopTaskRequest(BaseModel):
    task_name: Annotated[
        PathParamTaskName,
        pydantic.Field(alias="taskName"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The name of the task to be started."""


class StopTaskResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class StopTaskResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
