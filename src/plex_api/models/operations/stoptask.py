"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from enum import Enum


class PathParamTaskName(str, Enum):
    r"""The name of the task to be started."""
    BACKUP_DATABASE = 'BackupDatabase'
    BUILD_GRACENOTE_COLLECTIONS = 'BuildGracenoteCollections'
    CHECK_FOR_UPDATES = 'CheckForUpdates'
    CLEAN_OLD_BUNDLES = 'CleanOldBundles'
    CLEAN_OLD_CACHE_FILES = 'CleanOldCacheFiles'
    DEEP_MEDIA_ANALYSIS = 'DeepMediaAnalysis'
    GENERATE_AUTO_TAGS = 'GenerateAutoTags'
    GENERATE_CHAPTER_THUMBS = 'GenerateChapterThumbs'
    GENERATE_MEDIA_INDEX_FILES = 'GenerateMediaIndexFiles'
    OPTIMIZE_DATABASE = 'OptimizeDatabase'
    REFRESH_LIBRARIES = 'RefreshLibraries'
    REFRESH_LOCAL_MEDIA = 'RefreshLocalMedia'
    REFRESH_PERIODIC_METADATA = 'RefreshPeriodicMetadata'
    UPGRADE_MEDIA_ANALYSIS = 'UpgradeMediaAnalysis'


@dataclasses.dataclass
class StopTaskRequest:
    task_name: PathParamTaskName = dataclasses.field(metadata={'path_param': { 'field_name': 'taskName', 'style': 'simple', 'explode': False }})
    r"""The name of the task to be started."""
    



@dataclasses.dataclass
class StopTaskResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

