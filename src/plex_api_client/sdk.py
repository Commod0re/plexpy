"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, HttpClient
from .sdkconfiguration import SDKConfiguration, ServerProtocol
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
import httpx
from plex_api_client import utils
from plex_api_client._hooks import SDKHooks
from plex_api_client.activities import Activities
from plex_api_client.authentication import Authentication
from plex_api_client.butler import Butler
from plex_api_client.hubs import Hubs
from plex_api_client.library import Library
from plex_api_client.log import Log
from plex_api_client.media import Media
from plex_api_client.models import components, internal
from plex_api_client.playlists import Playlists
from plex_api_client.plex import Plex
from plex_api_client.search import Search
from plex_api_client.server import Server
from plex_api_client.sessions import Sessions
from plex_api_client.statistics import Statistics
from plex_api_client.types import OptionalNullable, UNSET
from plex_api_client.updater import Updater
from plex_api_client.video import Video
from plex_api_client.watchlist import Watchlist
from typing import Any, Callable, Dict, List, Optional, Union


class PlexAPI(BaseSDK):
    r"""Plex-API: An Open API Spec for interacting with Plex.tv and Plex Media Server"""

    server: Server
    r"""Operations against the Plex Media Server System.

    """
    media: Media
    r"""API Calls interacting with Plex Media Server Media

    """
    video: Video
    r"""API Calls that perform operations with Plex Media Server Videos

    """
    activities: Activities
    r"""Activities are awesome. They provide a way to monitor and control asynchronous operations on the server. In order to receive real-time updates for activities, a client would normally subscribe via either EventSource or Websocket endpoints.
    Activities are associated with HTTP replies via a special `X-Plex-Activity` header which contains the UUID of the activity.
    Activities are optional cancellable. If cancellable, they may be cancelled via the `DELETE` endpoint. Other details:
    - They can contain a `progress` (from 0 to 100) marking the percent completion of the activity.
    - They must contain an `type` which is used by clients to distinguish the specific activity.
    - They may contain a `Context` object with attributes which associate the activity with various specific entities (items, libraries, etc.)
    - The may contain a `Response` object which attributes which represent the result of the asynchronous operation.

    """
    butler: Butler
    r"""Butler is the task manager of the Plex Media Server Ecosystem.

    """
    plex: Plex
    r"""API Calls that perform operations directly against https://Plex.tv

    """
    hubs: Hubs
    r"""Hubs are a structured two-dimensional container for media, generally represented by multiple horizontal rows.

    """
    search: Search
    r"""API Calls that perform search operations with Plex Media Server

    """
    library: Library
    r"""API Calls interacting with Plex Media Server Libraries

    """
    watchlist: Watchlist
    r"""API Calls that perform operations with Plex Media Server Watchlists

    """
    log: Log
    r"""Submit logs to the Log Handler for Plex Media Server

    """
    playlists: Playlists
    r"""Playlists are ordered collections of media. They can be dumb (just a list of media) or smart (based on a media query, such as \"all albums from 2017\").
    They can be organized in (optionally nesting) folders.
    Retrieving a playlist, or its items, will trigger a refresh of its metadata.
    This may cause the duration and number of items to change.

    """
    authentication: Authentication
    r"""API Calls regarding authentication for Plex Media Server

    """
    statistics: Statistics
    r"""API Calls that perform operations with Plex Media Server Statistics

    """
    sessions: Sessions
    r"""API Calls that perform search operations with Plex Media Server Sessions

    """
    updater: Updater
    r"""This describes the API for searching and applying updates to the Plex Media Server.
    Updates to the status can be observed via the Event API.

    """

    def __init__(
        self,
        access_token: Optional[
            Union[Optional[str], Callable[[], Optional[str]]]
        ] = None,
        x_plex_client_identifier: Optional[str] = None,
        protocol: Optional[ServerProtocol] = None,
        ip: Optional[str] = None,
        port: Optional[str] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param access_token: The access_token required for authentication
        :param x_plex_client_identifier: Configures the x_plex_client_identifier parameter for all supported operations
        :param protocol: Allows setting the protocol variable for url substitution
        :param ip: Allows setting the ip variable for url substitution
        :param port: Allows setting the port variable for url substitution
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        if client is None:
            client = httpx.Client()

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        if async_client is None:
            async_client = httpx.AsyncClient()

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        security: Any = None
        if callable(access_token):
            security = lambda: components.Security(access_token=access_token())  # pylint: disable=unnecessary-lambda-assignment
        else:
            security = components.Security(access_token=access_token)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
        server_defaults: List[Dict[str, str]] = [
            {
                "protocol": protocol or "https",
                "ip": ip or "10.10.10.47",
                "port": port or "32400",
            },
        ]

        _globals = internal.Globals(
            x_plex_client_identifier=utils.get_global_from_env(
                x_plex_client_identifier, "X_PLEX_CLIENT_IDENTIFIER", str
            ),
        )

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                async_client=async_client,
                globals=_globals,
                security=security,
                server_url=server_url,
                server_idx=server_idx,
                server_defaults=server_defaults,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, self.sdk_configuration.client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        self._init_sdks()

    def _init_sdks(self):
        self.server = Server(self.sdk_configuration)
        self.media = Media(self.sdk_configuration)
        self.video = Video(self.sdk_configuration)
        self.activities = Activities(self.sdk_configuration)
        self.butler = Butler(self.sdk_configuration)
        self.plex = Plex(self.sdk_configuration)
        self.hubs = Hubs(self.sdk_configuration)
        self.search = Search(self.sdk_configuration)
        self.library = Library(self.sdk_configuration)
        self.watchlist = Watchlist(self.sdk_configuration)
        self.log = Log(self.sdk_configuration)
        self.playlists = Playlists(self.sdk_configuration)
        self.authentication = Authentication(self.sdk_configuration)
        self.statistics = Statistics(self.sdk_configuration)
        self.sessions = Sessions(self.sdk_configuration)
        self.updater = Updater(self.sdk_configuration)
