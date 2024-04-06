"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from plex_api import utils
from plex_api._hooks import AfterErrorContext, AfterSuccessContext, BeforeRequestContext, HookContext
from plex_api.models import errors, operations
from typing import Optional

class Plex:
    r"""API Calls that perform operations directly against https://Plex.tv"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def get_pin(self, strong: Optional[bool] = None, x_plex_client_identifier: Optional[str] = None, server_url: Optional[str] = None) -> operations.GetPinResponse:
        r"""Get a Pin
        Retrieve a Pin from Plex.tv for authentication flows
        """
        hook_ctx = HookContext(operation_id='getPin', oauth2_scopes=[], security_source=None)
        request = operations.GetPinRequest(
            strong=strong,
            x_plex_client_identifier=x_plex_client_identifier,
        )
        
        base_url = utils.template_url(operations.GET_PIN_SERVERS[0], {
        })
        if server_url is not None:
            base_url = server_url
        
        url = base_url + '/pins'
        
        headers = {}
        query_params = {}
        
        headers = { **utils.get_headers(request, self.sdk_configuration.globals), **headers }
        query_params = { **utils.get_query_params(operations.GetPinRequest, request, self.sdk_configuration.globals), **query_params }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('POST', url, params=query_params, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['400','4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        res = operations.GetPinResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type') or '', raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetPinResponseBody])
                res.object = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400:
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.GetPinResponseBody)
                out.raw_response = http_res
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_token(self, pin_id: str, x_plex_client_identifier: Optional[str] = None, server_url: Optional[str] = None) -> operations.GetTokenResponse:
        r"""Get Access Token
        Retrieve an Access Token from Plex.tv after the Pin has already been authenticated
        """
        hook_ctx = HookContext(operation_id='getToken', oauth2_scopes=[], security_source=None)
        request = operations.GetTokenRequest(
            pin_id=pin_id,
            x_plex_client_identifier=x_plex_client_identifier,
        )
        
        base_url = utils.template_url(operations.GET_TOKEN_SERVERS[0], {
        })
        if server_url is not None:
            base_url = server_url
        
        url = utils.generate_url(operations.GetTokenRequest, base_url, '/pins/{pinID}', request, self.sdk_configuration.globals)
        
        headers = {}
        
        headers = { **utils.get_headers(request, self.sdk_configuration.globals), **headers }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('GET', url, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['400','4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        res = operations.GetTokenResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type') or '', raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code == 400:
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.GetTokenResponseBody)
                out.raw_response = http_res
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    

