"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from plex_api_client import utils
from plex_api_client._hooks import HookContext
from plex_api_client.models import errors, operations
from plex_api_client.types import OptionalNullable, UNSET
from typing import Any, Optional, Union


class Authentication(BaseSDK):
    r"""API Calls regarding authentication for Plex Media Server"""

    def get_transient_token(
        self,
        *,
        type_: operations.GetTransientTokenQueryParamType,
        scope: operations.Scope,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetTransientTokenResponse:
        r"""Get a Transient Token

        This endpoint provides the caller with a temporary token with the same access level as the caller's token. These tokens are valid for up to 48 hours and are destroyed if the server instance is restarted.


        :param type: `delegation` - This is the only supported `type` parameter.
        :param scope: `all` - This is the only supported `scope` parameter.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = operations.GetTransientTokenRequest(
            type=type_,
            scope=scope,
        )

        req = self.build_request(
            method="GET",
            path="/security/token",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="getTransientToken",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "*"):
            return operations.GetTransientTokenResponse(
                status_code=http_res.status_code,
                content_type=http_res.headers.get("Content-Type") or "",
                raw_response=http_res,
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetTransientTokenBadRequestData
            )
            data.raw_response = http_res
            raise errors.GetTransientTokenBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetTransientTokenUnauthorizedData
            )
            data.raw_response = http_res
            raise errors.GetTransientTokenUnauthorized(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def get_transient_token_async(
        self,
        *,
        type_: operations.GetTransientTokenQueryParamType,
        scope: operations.Scope,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetTransientTokenResponse:
        r"""Get a Transient Token

        This endpoint provides the caller with a temporary token with the same access level as the caller's token. These tokens are valid for up to 48 hours and are destroyed if the server instance is restarted.


        :param type: `delegation` - This is the only supported `type` parameter.
        :param scope: `all` - This is the only supported `scope` parameter.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = operations.GetTransientTokenRequest(
            type=type_,
            scope=scope,
        )

        req = self.build_request_async(
            method="GET",
            path="/security/token",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="getTransientToken",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "*"):
            return operations.GetTransientTokenResponse(
                status_code=http_res.status_code,
                content_type=http_res.headers.get("Content-Type") or "",
                raw_response=http_res,
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetTransientTokenBadRequestData
            )
            data.raw_response = http_res
            raise errors.GetTransientTokenBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetTransientTokenUnauthorizedData
            )
            data.raw_response = http_res
            raise errors.GetTransientTokenUnauthorized(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    def get_source_connection_information(
        self,
        *,
        source: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetSourceConnectionInformationResponse:
        r"""Get Source Connection Information

        If a caller requires connection details and a transient token for a source that is known to the server, for example a cloud media provider or shared PMS, then this endpoint can be called. This endpoint is only accessible with either an admin token or a valid transient token generated from an admin token.
        Note: requires Plex Media Server >= 1.15.4.


        :param source: The source identifier with an included prefix.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = operations.GetSourceConnectionInformationRequest(
            source=source,
        )

        req = self.build_request(
            method="GET",
            path="/security/resources",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="getSourceConnectionInformation",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "*"):
            return operations.GetSourceConnectionInformationResponse(
                status_code=http_res.status_code,
                content_type=http_res.headers.get("Content-Type") or "",
                raw_response=http_res,
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetSourceConnectionInformationBadRequestData
            )
            data.raw_response = http_res
            raise errors.GetSourceConnectionInformationBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetSourceConnectionInformationUnauthorizedData
            )
            data.raw_response = http_res
            raise errors.GetSourceConnectionInformationUnauthorized(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def get_source_connection_information_async(
        self,
        *,
        source: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetSourceConnectionInformationResponse:
        r"""Get Source Connection Information

        If a caller requires connection details and a transient token for a source that is known to the server, for example a cloud media provider or shared PMS, then this endpoint can be called. This endpoint is only accessible with either an admin token or a valid transient token generated from an admin token.
        Note: requires Plex Media Server >= 1.15.4.


        :param source: The source identifier with an included prefix.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = operations.GetSourceConnectionInformationRequest(
            source=source,
        )

        req = self.build_request_async(
            method="GET",
            path="/security/resources",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="getSourceConnectionInformation",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "*"):
            return operations.GetSourceConnectionInformationResponse(
                status_code=http_res.status_code,
                content_type=http_res.headers.get("Content-Type") or "",
                raw_response=http_res,
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetSourceConnectionInformationBadRequestData
            )
            data.raw_response = http_res
            raise errors.GetSourceConnectionInformationBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetSourceConnectionInformationUnauthorizedData
            )
            data.raw_response = http_res
            raise errors.GetSourceConnectionInformationUnauthorized(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    def get_token_details(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetTokenDetailsResponse:
        r"""Get Token Details

        Get the User data from the provided X-Plex-Token

        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = operations.GET_TOKEN_DETAILS_SERVERS[0]
        req = self.build_request(
            method="GET",
            path="/user",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="getTokenDetails",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetTokenDetailsResponse(
                user_plex_account=utils.unmarshal_json(
                    http_res.text, Optional[operations.GetTokenDetailsUserPlexAccount]
                ),
                status_code=http_res.status_code,
                content_type=http_res.headers.get("Content-Type") or "",
                raw_response=http_res,
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetTokenDetailsBadRequestData
            )
            data.raw_response = http_res
            raise errors.GetTokenDetailsBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetTokenDetailsUnauthorizedData
            )
            data.raw_response = http_res
            raise errors.GetTokenDetailsUnauthorized(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def get_token_details_async(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetTokenDetailsResponse:
        r"""Get Token Details

        Get the User data from the provided X-Plex-Token

        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = operations.GET_TOKEN_DETAILS_SERVERS[0]
        req = self.build_request_async(
            method="GET",
            path="/user",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="getTokenDetails",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetTokenDetailsResponse(
                user_plex_account=utils.unmarshal_json(
                    http_res.text, Optional[operations.GetTokenDetailsUserPlexAccount]
                ),
                status_code=http_res.status_code,
                content_type=http_res.headers.get("Content-Type") or "",
                raw_response=http_res,
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetTokenDetailsBadRequestData
            )
            data.raw_response = http_res
            raise errors.GetTokenDetailsBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetTokenDetailsUnauthorizedData
            )
            data.raw_response = http_res
            raise errors.GetTokenDetailsUnauthorized(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    def post_users_sign_in_data(
        self,
        *,
        client_id: Optional[str] = None,
        request_body: Optional[
            Union[
                operations.PostUsersSignInDataRequestBody,
                operations.PostUsersSignInDataRequestBodyTypedDict,
            ]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.PostUsersSignInDataResponse:
        r"""Get User Sign In Data

        Sign in user with username and password and return user data with Plex authentication token

        :param client_id: The unique identifier for the client application This is used to track the client application and its usage (UUID, serial number, or other number unique per device)
        :param request_body: Login credentials
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = operations.POST_USERS_SIGN_IN_DATA_SERVERS[0]

        request = operations.PostUsersSignInDataRequest(
            client_id=client_id,
            request_body=utils.get_pydantic_model(
                request_body, Optional[operations.PostUsersSignInDataRequestBody]
            ),
        )

        req = self.build_request(
            method="POST",
            path="/users/signin",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            _globals=operations.PostUsersSignInDataGlobals(
                client_id=self.sdk_configuration.globals.client_id,
            ),
            get_serialized_body=lambda: utils.serialize_request_body(
                request.request_body,
                False,
                True,
                "form",
                Optional[operations.PostUsersSignInDataRequestBody],
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="post-users-sign-in-data",
                oauth2_scopes=[],
                security_source=None,
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "201", "application/json"):
            return operations.PostUsersSignInDataResponse(
                user_plex_account=utils.unmarshal_json(
                    http_res.text,
                    Optional[operations.PostUsersSignInDataUserPlexAccount],
                ),
                status_code=http_res.status_code,
                content_type=http_res.headers.get("Content-Type") or "",
                raw_response=http_res,
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.PostUsersSignInDataBadRequestData
            )
            data.raw_response = http_res
            raise errors.PostUsersSignInDataBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.PostUsersSignInDataUnauthorizedData
            )
            data.raw_response = http_res
            raise errors.PostUsersSignInDataUnauthorized(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def post_users_sign_in_data_async(
        self,
        *,
        client_id: Optional[str] = None,
        request_body: Optional[
            Union[
                operations.PostUsersSignInDataRequestBody,
                operations.PostUsersSignInDataRequestBodyTypedDict,
            ]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.PostUsersSignInDataResponse:
        r"""Get User Sign In Data

        Sign in user with username and password and return user data with Plex authentication token

        :param client_id: The unique identifier for the client application This is used to track the client application and its usage (UUID, serial number, or other number unique per device)
        :param request_body: Login credentials
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = operations.POST_USERS_SIGN_IN_DATA_SERVERS[0]

        request = operations.PostUsersSignInDataRequest(
            client_id=client_id,
            request_body=utils.get_pydantic_model(
                request_body, Optional[operations.PostUsersSignInDataRequestBody]
            ),
        )

        req = self.build_request_async(
            method="POST",
            path="/users/signin",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            _globals=operations.PostUsersSignInDataGlobals(
                client_id=self.sdk_configuration.globals.client_id,
            ),
            get_serialized_body=lambda: utils.serialize_request_body(
                request.request_body,
                False,
                True,
                "form",
                Optional[operations.PostUsersSignInDataRequestBody],
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="post-users-sign-in-data",
                oauth2_scopes=[],
                security_source=None,
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "201", "application/json"):
            return operations.PostUsersSignInDataResponse(
                user_plex_account=utils.unmarshal_json(
                    http_res.text,
                    Optional[operations.PostUsersSignInDataUserPlexAccount],
                ),
                status_code=http_res.status_code,
                content_type=http_res.headers.get("Content-Type") or "",
                raw_response=http_res,
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.PostUsersSignInDataBadRequestData
            )
            data.raw_response = http_res
            raise errors.PostUsersSignInDataBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.PostUsersSignInDataUnauthorizedData
            )
            data.raw_response = http_res
            raise errors.PostUsersSignInDataUnauthorized(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )