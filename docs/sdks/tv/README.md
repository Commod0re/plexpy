# Tv
(*plex.tv*)

### Available Operations

* [get_pin](#get_pin) - Get a Pin
* [get_token](#get_token) - Get Access Token

## get_pin

Retrieve a Pin from Plex.tv for authentication flows

### Example Usage

```python
import plex_api
from plex_api.models import operations

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
)


res = s.plex.tv.get_pin(x_plex_client_identifier='string', strong=False)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_plex_client_identifier`                                                                                                                            | *str*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                    | Plex Authentication Token                                                                                                                             |
| `strong`                                                                                                                                              | *Optional[bool]*                                                                                                                                      | :heavy_minus_sign:                                                                                                                                    | Determines the kind of code returned by the API call<br/>Strong codes are used for Pin authentication flows<br/>Non-Strong codes are used for `Plex.tv/link`<br/> |
| `server_url`                                                                                                                                          | *Optional[str]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | An optional server URL to use.                                                                                                                        |


### Response

**[operations.GetPinResponse](../../models/operations/getpinresponse.md)**
### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.GetPinResponseBody | 400                       | application/json          |
| errors.SDKError           | 4x-5xx                    | */*                       |

## get_token

Retrieve an Access Token from Plex.tv after the Pin has already been authenticated

### Example Usage

```python
import plex_api
from plex_api.models import operations

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
)


res = s.plex.tv.get_token(pin_id='string', x_plex_client_identifier='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                 | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `pin_id`                                  | *str*                                     | :heavy_check_mark:                        | The PinID to retrieve an access token for |
| `x_plex_client_identifier`                | *str*                                     | :heavy_check_mark:                        | Plex Authentication Token                 |
| `server_url`                              | *Optional[str]*                           | :heavy_minus_sign:                        | An optional server URL to use.            |


### Response

**[operations.GetTokenResponse](../../models/operations/gettokenresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.GetTokenResponseBody | 400                         | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |