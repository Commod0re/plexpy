"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class PerformSearchRequest:
    query: str = dataclasses.field(metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""The query term"""
    limit: Optional[float] = dataclasses.field(default=3, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""The number of items to return per hub"""
    section_id: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sectionId', 'style': 'form', 'explode': True }})
    r"""This gives context to the search, and can result in re-ordering of search result hubs"""
    



@dataclasses.dataclass
class PerformSearchResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    
