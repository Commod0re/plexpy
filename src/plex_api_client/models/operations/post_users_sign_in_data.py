"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
import httpx
from plex_api_client.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from plex_api_client.utils import FieldMetadata, QueryParamMetadata, RequestMetadata
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired

POST_USERS_SIGN_IN_DATA_SERVERS = [
    "https://plex.tv/api/v2/",
]


class PostUsersSignInDataGlobalsTypedDict(TypedDict):
    client_id: NotRequired[str]
    r"""The unique identifier for the client application
    This is used to track the client application and its usage
    (UUID, serial number, or other number unique per device)

    """
    client_name: NotRequired[str]
    device_name: NotRequired[str]
    client_version: NotRequired[str]
    client_platform: NotRequired[str]


class PostUsersSignInDataGlobals(BaseModel):
    client_id: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Client-Identifier"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The unique identifier for the client application
    This is used to track the client application and its usage
    (UUID, serial number, or other number unique per device)

    """

    client_name: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Product"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    device_name: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Device"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    client_version: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Version"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    client_platform: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Platform"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None


class PostUsersSignInDataRequestBodyTypedDict(TypedDict):
    r"""Login credentials"""

    login: str
    password: str
    remember_me: NotRequired[bool]
    verification_code: NotRequired[str]


class PostUsersSignInDataRequestBody(BaseModel):
    r"""Login credentials"""

    login: Annotated[str, FieldMetadata(form=True)]

    password: Annotated[str, FieldMetadata(form=True)]

    remember_me: Annotated[
        Optional[bool], pydantic.Field(alias="rememberMe"), FieldMetadata(form=True)
    ] = False

    verification_code: Annotated[
        Optional[str],
        pydantic.Field(alias="verificationCode"),
        FieldMetadata(form=True),
    ] = None


class PostUsersSignInDataRequestTypedDict(TypedDict):
    client_id: NotRequired[str]
    r"""The unique identifier for the client application
    This is used to track the client application and its usage
    (UUID, serial number, or other number unique per device)

    """
    client_name: NotRequired[str]
    device_name: NotRequired[str]
    client_version: NotRequired[str]
    client_platform: NotRequired[str]
    request_body: NotRequired[PostUsersSignInDataRequestBodyTypedDict]
    r"""Login credentials"""


class PostUsersSignInDataRequest(BaseModel):
    client_id: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Client-Identifier"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The unique identifier for the client application
    This is used to track the client application and its usage
    (UUID, serial number, or other number unique per device)

    """

    client_name: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Product"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    device_name: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Device"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    client_version: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Version"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    client_platform: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Platform"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    request_body: Annotated[
        Optional[PostUsersSignInDataRequestBody],
        FieldMetadata(
            request=RequestMetadata(media_type="application/x-www-form-urlencoded")
        ),
    ] = None
    r"""Login credentials"""


class PostUsersSignInDataMailingListStatus(str, Enum):
    r"""Your current mailing list status"""

    ACTIVE = "active"
    UNSUBSCRIBED = "unsubscribed"


class PostUsersSignInDataAutoSelectSubtitle(int, Enum):
    r"""The auto-select subtitle mode (0 = Manually selected, 1 = Shown with foreign audio, 2 = Always enabled)"""

    DISABLE = 0
    ENABLE = 1


class PostUsersSignInDataDefaultSubtitleAccessibility(int, Enum):
    r"""The subtitles for the deaf or hard-of-hearing (SDH) searches mode (0 = Prefer non-SDH subtitles, 1 = Prefer SDH subtitles, 2 = Only show SDH subtitles, 3 = Only show non-SDH subtitles)"""

    DISABLE = 0
    ENABLE = 1


class PostUsersSignInDataDefaultSubtitleForced(int, Enum):
    r"""The forced subtitles searches mode (0 = Prefer non-forced subtitles, 1 = Prefer forced subtitles, 2 = Only show forced subtitles, 3 = Only show non-forced subtitles)"""

    DISABLE = 0
    ENABLE = 1


class PostUsersSignInDataWatchedIndicator(int, Enum):
    r"""Whether or not media watched indicators are enabled (little orange dot on media)"""

    DISABLE = 0
    ENABLE = 1


class PostUsersSignInDataMediaReviewsVisibility(int, Enum):
    r"""Whether or not the account has media reviews visibility enabled"""

    DISABLE = 0
    ENABLE = 1


class PostUsersSignInDataUserProfileTypedDict(TypedDict):
    default_audio_language: Nullable[str]
    r"""The preferred audio language for the account"""
    default_subtitle_language: Nullable[str]
    r"""The preferred subtitle language for the account"""
    auto_select_audio: NotRequired[bool]
    r"""If the account has automatically select audio and subtitle tracks enabled"""
    auto_select_subtitle: NotRequired[PostUsersSignInDataAutoSelectSubtitle]
    default_subtitle_accessibility: NotRequired[
        PostUsersSignInDataDefaultSubtitleAccessibility
    ]
    default_subtitle_forced: NotRequired[PostUsersSignInDataDefaultSubtitleForced]
    watched_indicator: NotRequired[PostUsersSignInDataWatchedIndicator]
    media_reviews_visibility: NotRequired[PostUsersSignInDataMediaReviewsVisibility]


class PostUsersSignInDataUserProfile(BaseModel):
    default_audio_language: Annotated[
        Nullable[str], pydantic.Field(alias="defaultAudioLanguage")
    ]
    r"""The preferred audio language for the account"""

    default_subtitle_language: Annotated[
        Nullable[str], pydantic.Field(alias="defaultSubtitleLanguage")
    ]
    r"""The preferred subtitle language for the account"""

    auto_select_audio: Annotated[
        Optional[bool], pydantic.Field(alias="autoSelectAudio")
    ] = True
    r"""If the account has automatically select audio and subtitle tracks enabled"""

    auto_select_subtitle: Annotated[
        Optional[PostUsersSignInDataAutoSelectSubtitle],
        pydantic.Field(alias="autoSelectSubtitle"),
    ] = PostUsersSignInDataAutoSelectSubtitle.DISABLE

    default_subtitle_accessibility: Annotated[
        Optional[PostUsersSignInDataDefaultSubtitleAccessibility],
        pydantic.Field(alias="defaultSubtitleAccessibility"),
    ] = PostUsersSignInDataDefaultSubtitleAccessibility.DISABLE

    default_subtitle_forced: Annotated[
        Optional[PostUsersSignInDataDefaultSubtitleForced],
        pydantic.Field(alias="defaultSubtitleForced"),
    ] = PostUsersSignInDataDefaultSubtitleForced.DISABLE

    watched_indicator: Annotated[
        Optional[PostUsersSignInDataWatchedIndicator],
        pydantic.Field(alias="watchedIndicator"),
    ] = PostUsersSignInDataWatchedIndicator.DISABLE

    media_reviews_visibility: Annotated[
        Optional[PostUsersSignInDataMediaReviewsVisibility],
        pydantic.Field(alias="mediaReviewsVisibility"),
    ] = PostUsersSignInDataMediaReviewsVisibility.DISABLE

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "autoSelectAudio",
            "autoSelectSubtitle",
            "defaultSubtitleAccessibility",
            "defaultSubtitleForced",
            "watchedIndicator",
            "mediaReviewsVisibility",
        ]
        nullable_fields = ["defaultAudioLanguage", "defaultSubtitleLanguage"]
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


class PostUsersSignInDataStatus(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"


class PostUsersSignInDataServicesTypedDict(TypedDict):
    identifier: str
    endpoint: str
    token: Nullable[str]
    secret: Nullable[str]
    status: PostUsersSignInDataStatus


class PostUsersSignInDataServices(BaseModel):
    identifier: str

    endpoint: str

    token: Nullable[str]

    secret: Nullable[str]

    status: PostUsersSignInDataStatus

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["token", "secret"]
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


class PostUsersSignInDataFeatures(str, Enum):
    ANDROID_DOLBY_VISION = "Android - Dolby Vision"
    ANDROID_PI_P = "Android - PiP"
    CU_SUNSET = "CU Sunset"
    HRK_ENABLE_EUR = "HRK_enable_EUR"
    TREBLE_SHOW_FEATURES = "TREBLE-show-features"
    AD_COUNTDOWN_TIMER = "ad-countdown-timer"
    ADAPTIVE_BITRATE = "adaptive_bitrate"
    AMAZON_LOOP_DEBUG = "amazon-loop-debug"
    AVOD_AD_ANALYSIS = "avod-ad-analysis"
    AVOD_NEW_MEDIA = "avod-new-media"
    BLACKLIST_GET_SIGNIN = "blacklist_get_signin"
    CLIENT_RADIO_STATIONS = "client-radio-stations"
    CLOUDFLARE_TURNSTILE_REQUIRED = "cloudflare-turnstile-required"
    COLLECTIONS = "collections"
    COMMENTS_AND_REPLIES_PUSH_NOTIFICATIONS = "comments_and_replies_push_notifications"
    COMMUNITY_ACCESS_PLEX_TV = "community_access_plex_tv"
    COMPANIONS_SONOS = "companions_sonos"
    CUSTOM_HOME_REMOVAL = "custom-home-removal"
    DISABLE_HOME_USER_FRIENDSHIPS = "disable_home_user_friendships"
    DISABLE_SHARING_FRIENDSHIPS = "disable_sharing_friendships"
    DRM_SUPPORT = "drm_support"
    EXCLUDE_RESTRICTIONS = "exclude restrictions"
    FEDERATED_AUTH = "federated-auth"
    FRIEND_REQUEST_PUSH_NOTIFICATIONS = "friend_request_push_notifications"
    GUIDED_UPGRADE = "guided-upgrade"
    HOME = "home"
    INCREASE_PASSWORD_COMPLEXITY = "increase-password-complexity"
    IOS14_PRIVACY_BANNER = "ios14-privacy-banner"
    ITERABLE_NOTIFICATION_TOKENS = "iterable-notification-tokens"
    KEEP_PAYMENT_METHOD = "keep-payment-method"
    KEVIN_BACON = "kevin-bacon"
    KOREA_CONSENT = "korea-consent"
    LE_ISRG_ROOT_X1 = "le_isrg_root_x1"
    LETS_ENCRYPT = "lets_encrypt"
    LIGHTNING_DVR_PIVOT = "lightning-dvr-pivot"
    LIVE_TV_SUPPORT_INCOMPLETE_SEGMENTS = "live-tv-support-incomplete-segments"
    LIVETV = "livetv"
    METADATA_SEARCH = "metadata_search"
    NEW_PLEX_PASS_PRICES = "new_plex_pass_prices"
    NEWS_PROVIDER_SUNSET_MODAL = "news-provider-sunset-modal"
    PHOTOS_FAVORITES = "photos-favorites"
    PHOTOS_METADATA_EDITION = "photos-metadata-edition"
    PMS_HEALTH = "pms_health"
    RADIO = "radio"
    RATE_LIMIT_CLIENT_TOKEN = "rate-limit-client-token"
    SCROBBLING_SERVICE_PLEX_TV = "scrobbling-service-plex-tv"
    SHARED_SERVER_NOTIFICATION = "shared_server_notification"
    SHARED_SOURCE_NOTIFICATION = "shared_source_notification"
    SIGNIN_WITH_APPLE = "signin_with_apple"
    SPRING_SERVE_AD_PROVIDER = "spring_serve_ad_provider"
    TRANSCODER_CACHE = "transcoder_cache"
    TUNER_SHARING = "tuner-sharing"
    TWO_FACTOR_AUTHENTICATION = "two-factor-authentication"
    UNSUPPORTEDTUNERS = "unsupportedtuners"
    UPGRADE_3DS2 = "upgrade-3ds2"
    VOD_SCHEMA = "vod-schema"
    VOD_CLOUDFLARE = "vod_cloudflare"
    WATCH_TOGETHER_INVITE = "watch-together-invite"
    WEB_SERVER_DASHBOARD = "web_server_dashboard"


class PostUsersSignInDataAuthenticationStatus(str, Enum):
    r"""String representation of subscriptionActive"""

    INACTIVE = "Inactive"
    ACTIVE = "Active"


class PostUsersSignInDataSubscriptionTypedDict(TypedDict):
    r"""If the account’s Plex Pass subscription is active"""

    features: NotRequired[List[PostUsersSignInDataFeatures]]
    r"""List of features allowed on your Plex Pass subscription"""
    active: NotRequired[bool]
    r"""If the account's Plex Pass subscription is active"""
    subscribed_at: NotRequired[Nullable[str]]
    r"""Date the account subscribed to Plex Pass"""
    status: NotRequired[PostUsersSignInDataAuthenticationStatus]
    r"""String representation of subscriptionActive"""
    payment_service: NotRequired[Nullable[str]]
    r"""Payment service used for your Plex Pass subscription"""
    plan: NotRequired[Nullable[str]]
    r"""Name of Plex Pass subscription plan"""


class PostUsersSignInDataSubscription(BaseModel):
    r"""If the account’s Plex Pass subscription is active"""

    features: Optional[List[PostUsersSignInDataFeatures]] = None
    r"""List of features allowed on your Plex Pass subscription"""

    active: Optional[bool] = None
    r"""If the account's Plex Pass subscription is active"""

    subscribed_at: Annotated[
        OptionalNullable[str], pydantic.Field(alias="subscribedAt")
    ] = UNSET
    r"""Date the account subscribed to Plex Pass"""

    status: Optional[PostUsersSignInDataAuthenticationStatus] = None
    r"""String representation of subscriptionActive"""

    payment_service: Annotated[
        OptionalNullable[str], pydantic.Field(alias="paymentService")
    ] = UNSET
    r"""Payment service used for your Plex Pass subscription"""

    plan: OptionalNullable[str] = UNSET
    r"""Name of Plex Pass subscription plan"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "features",
            "active",
            "subscribedAt",
            "status",
            "paymentService",
            "plan",
        ]
        nullable_fields = ["subscribedAt", "paymentService", "plan"]
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


class PostUsersSignInDataAuthenticationFeatures(str, Enum):
    ANDROID_DOLBY_VISION = "Android - Dolby Vision"
    ANDROID_PI_P = "Android - PiP"
    CU_SUNSET = "CU Sunset"
    HRK_ENABLE_EUR = "HRK_enable_EUR"
    TREBLE_SHOW_FEATURES = "TREBLE-show-features"
    AD_COUNTDOWN_TIMER = "ad-countdown-timer"
    ADAPTIVE_BITRATE = "adaptive_bitrate"
    AMAZON_LOOP_DEBUG = "amazon-loop-debug"
    AVOD_AD_ANALYSIS = "avod-ad-analysis"
    AVOD_NEW_MEDIA = "avod-new-media"
    BLACKLIST_GET_SIGNIN = "blacklist_get_signin"
    CLIENT_RADIO_STATIONS = "client-radio-stations"
    CLOUDFLARE_TURNSTILE_REQUIRED = "cloudflare-turnstile-required"
    COLLECTIONS = "collections"
    COMMENTS_AND_REPLIES_PUSH_NOTIFICATIONS = "comments_and_replies_push_notifications"
    COMMUNITY_ACCESS_PLEX_TV = "community_access_plex_tv"
    COMPANIONS_SONOS = "companions_sonos"
    CUSTOM_HOME_REMOVAL = "custom-home-removal"
    DISABLE_HOME_USER_FRIENDSHIPS = "disable_home_user_friendships"
    DISABLE_SHARING_FRIENDSHIPS = "disable_sharing_friendships"
    DRM_SUPPORT = "drm_support"
    EXCLUDE_RESTRICTIONS = "exclude restrictions"
    FEDERATED_AUTH = "federated-auth"
    FRIEND_REQUEST_PUSH_NOTIFICATIONS = "friend_request_push_notifications"
    GUIDED_UPGRADE = "guided-upgrade"
    HOME = "home"
    INCREASE_PASSWORD_COMPLEXITY = "increase-password-complexity"
    IOS14_PRIVACY_BANNER = "ios14-privacy-banner"
    ITERABLE_NOTIFICATION_TOKENS = "iterable-notification-tokens"
    KEEP_PAYMENT_METHOD = "keep-payment-method"
    KEVIN_BACON = "kevin-bacon"
    KOREA_CONSENT = "korea-consent"
    LE_ISRG_ROOT_X1 = "le_isrg_root_x1"
    LETS_ENCRYPT = "lets_encrypt"
    LIGHTNING_DVR_PIVOT = "lightning-dvr-pivot"
    LIVE_TV_SUPPORT_INCOMPLETE_SEGMENTS = "live-tv-support-incomplete-segments"
    LIVETV = "livetv"
    METADATA_SEARCH = "metadata_search"
    NEW_PLEX_PASS_PRICES = "new_plex_pass_prices"
    NEWS_PROVIDER_SUNSET_MODAL = "news-provider-sunset-modal"
    PHOTOS_FAVORITES = "photos-favorites"
    PHOTOS_METADATA_EDITION = "photos-metadata-edition"
    PMS_HEALTH = "pms_health"
    RADIO = "radio"
    RATE_LIMIT_CLIENT_TOKEN = "rate-limit-client-token"
    SCROBBLING_SERVICE_PLEX_TV = "scrobbling-service-plex-tv"
    SHARED_SERVER_NOTIFICATION = "shared_server_notification"
    SHARED_SOURCE_NOTIFICATION = "shared_source_notification"
    SIGNIN_WITH_APPLE = "signin_with_apple"
    SPRING_SERVE_AD_PROVIDER = "spring_serve_ad_provider"
    TRANSCODER_CACHE = "transcoder_cache"
    TUNER_SHARING = "tuner-sharing"
    TWO_FACTOR_AUTHENTICATION = "two-factor-authentication"
    UNSUPPORTEDTUNERS = "unsupportedtuners"
    UPGRADE_3DS2 = "upgrade-3ds2"
    VOD_SCHEMA = "vod-schema"
    VOD_CLOUDFLARE = "vod_cloudflare"
    WATCH_TOGETHER_INVITE = "watch-together-invite"
    WEB_SERVER_DASHBOARD = "web_server_dashboard"


class PostUsersSignInDataAuthenticationResponseStatus(str, Enum):
    r"""String representation of subscriptionActive"""

    INACTIVE = "Inactive"
    ACTIVE = "Active"


class PostUsersSignInDataAuthenticationSubscriptionTypedDict(TypedDict):
    features: NotRequired[List[PostUsersSignInDataAuthenticationFeatures]]
    r"""List of features allowed on your Plex Pass subscription"""
    active: NotRequired[bool]
    r"""If the account's Plex Pass subscription is active"""
    subscribed_at: NotRequired[Nullable[str]]
    r"""Date the account subscribed to Plex Pass"""
    status: NotRequired[PostUsersSignInDataAuthenticationResponseStatus]
    r"""String representation of subscriptionActive"""
    payment_service: NotRequired[Nullable[str]]
    r"""Payment service used for your Plex Pass subscription"""
    plan: NotRequired[Nullable[str]]
    r"""Name of Plex Pass subscription plan"""


class PostUsersSignInDataAuthenticationSubscription(BaseModel):
    features: Optional[List[PostUsersSignInDataAuthenticationFeatures]] = None
    r"""List of features allowed on your Plex Pass subscription"""

    active: Optional[bool] = None
    r"""If the account's Plex Pass subscription is active"""

    subscribed_at: Annotated[
        OptionalNullable[str], pydantic.Field(alias="subscribedAt")
    ] = UNSET
    r"""Date the account subscribed to Plex Pass"""

    status: Optional[PostUsersSignInDataAuthenticationResponseStatus] = None
    r"""String representation of subscriptionActive"""

    payment_service: Annotated[
        OptionalNullable[str], pydantic.Field(alias="paymentService")
    ] = UNSET
    r"""Payment service used for your Plex Pass subscription"""

    plan: OptionalNullable[str] = UNSET
    r"""Name of Plex Pass subscription plan"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "features",
            "active",
            "subscribedAt",
            "status",
            "paymentService",
            "plan",
        ]
        nullable_fields = ["subscribedAt", "paymentService", "plan"]
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


class PostUsersSignInDataState(str, Enum):
    ENDED = "ended"


class InternalPaymentMethodTypedDict(TypedDict):
    pass


class InternalPaymentMethod(BaseModel):
    pass


class BillingTypedDict(TypedDict):
    internal_payment_method: InternalPaymentMethodTypedDict
    payment_method_id: Nullable[int]


class Billing(BaseModel):
    internal_payment_method: Annotated[
        InternalPaymentMethod, pydantic.Field(alias="internalPaymentMethod")
    ]

    payment_method_id: Annotated[Nullable[int], pydantic.Field(alias="paymentMethodId")]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["paymentMethodId"]
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


class PastSubscriptionTypedDict(TypedDict):
    id: Nullable[str]
    mode: Nullable[str]
    renews_at: Nullable[int]
    ends_at: Nullable[int]
    type: str
    transfer: Nullable[str]
    state: PostUsersSignInDataState
    billing: BillingTypedDict
    canceled: NotRequired[bool]
    grace_period: NotRequired[bool]
    on_hold: NotRequired[bool]
    can_reactivate: NotRequired[bool]
    can_upgrade: NotRequired[bool]
    can_downgrade: NotRequired[bool]
    can_convert: NotRequired[bool]


class PastSubscription(BaseModel):
    id: Nullable[str]

    mode: Nullable[str]

    renews_at: Annotated[Nullable[int], pydantic.Field(alias="renewsAt")]

    ends_at: Annotated[Nullable[int], pydantic.Field(alias="endsAt")]

    type: str

    transfer: Nullable[str]

    state: PostUsersSignInDataState

    billing: Billing

    canceled: Optional[bool] = False

    grace_period: Annotated[Optional[bool], pydantic.Field(alias="gracePeriod")] = False

    on_hold: Annotated[Optional[bool], pydantic.Field(alias="onHold")] = False

    can_reactivate: Annotated[Optional[bool], pydantic.Field(alias="canReactivate")] = (
        False
    )

    can_upgrade: Annotated[Optional[bool], pydantic.Field(alias="canUpgrade")] = False

    can_downgrade: Annotated[Optional[bool], pydantic.Field(alias="canDowngrade")] = (
        False
    )

    can_convert: Annotated[Optional[bool], pydantic.Field(alias="canConvert")] = False

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "canceled",
            "gracePeriod",
            "onHold",
            "canReactivate",
            "canUpgrade",
            "canDowngrade",
            "canConvert",
        ]
        nullable_fields = ["id", "mode", "renewsAt", "endsAt", "transfer"]
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


class TrialsTypedDict(TypedDict):
    pass


class Trials(BaseModel):
    pass


class PostUsersSignInDataUserPlexAccountTypedDict(TypedDict):
    r"""Returns the user account data with a valid auth token"""

    ads_consent: Nullable[bool]
    r"""Unknown"""
    ads_consent_reminder_at: Nullable[datetime]
    r"""Unknown"""
    ads_consent_set_at: Nullable[datetime]
    r"""Unknown"""
    auth_token: str
    r"""The account token"""
    country: str
    r"""The account country"""
    email: str
    r"""The account email address"""
    friendly_name: str
    r"""Your account full name"""
    entitlements: List[str]
    r"""List of devices your allowed to use with this account"""
    home_size: int
    r"""The number of accounts in the Plex Home"""
    id: int
    r"""The Plex account ID"""
    joined_at: int
    r"""Unix epoch datetime in seconds"""
    locale: Nullable[str]
    r"""The account locale"""
    mailing_list_status: PostUsersSignInDataMailingListStatus
    r"""Your current mailing list status"""
    max_home_size: int
    r"""The maximum number of accounts allowed in the Plex Home"""
    profile: PostUsersSignInDataUserProfileTypedDict
    remember_expires_at: int
    r"""Unix epoch datetime in seconds"""
    scrobble_types: str
    r"""Unknown"""
    services: List[PostUsersSignInDataServicesTypedDict]
    subscription: PostUsersSignInDataSubscriptionTypedDict
    r"""If the account’s Plex Pass subscription is active"""
    subscription_description: Nullable[str]
    r"""Description of the Plex Pass subscription"""
    subscriptions: List[PostUsersSignInDataAuthenticationSubscriptionTypedDict]
    thumb: str
    r"""URL of the account thumbnail"""
    title: str
    r"""The title of the account (username or friendly name)"""
    username: str
    r"""The account username"""
    uuid: str
    r"""The account UUID"""
    attribution_partner: Nullable[str]
    past_subscriptions: List[PastSubscriptionTypedDict]
    trials: List[TrialsTypedDict]
    anonymous: NotRequired[Nullable[bool]]
    r"""Unknown"""
    backup_codes_created: NotRequired[bool]
    r"""If the two-factor authentication backup codes have been created"""
    confirmed: NotRequired[bool]
    r"""If the account has been confirmed"""
    email_only_auth: NotRequired[bool]
    r"""If login with email only is enabled"""
    experimental_features: NotRequired[bool]
    r"""If experimental features are enabled"""
    guest: NotRequired[bool]
    r"""If the account is a Plex Home guest user"""
    has_password: NotRequired[bool]
    r"""If the account has a password"""
    home: NotRequired[bool]
    r"""If the account is a Plex Home user"""
    home_admin: NotRequired[bool]
    r"""If the account is the Plex Home admin"""
    mailing_list_active: NotRequired[bool]
    r"""If you are subscribed to the Plex newsletter"""
    pin: NotRequired[str]
    r"""[Might be removed] The hashed Plex Home PIN"""
    protected: NotRequired[bool]
    r"""If the account has a Plex Home PIN enabled"""
    restricted: NotRequired[bool]
    r"""If the account is a Plex Home managed user"""
    roles: NotRequired[List[str]]
    r"""[Might be removed] List of account roles. Plexpass membership listed here"""
    two_factor_enabled: NotRequired[bool]
    r"""If two-factor authentication is enabled"""


class PostUsersSignInDataUserPlexAccount(BaseModel):
    r"""Returns the user account data with a valid auth token"""

    ads_consent: Annotated[Nullable[bool], pydantic.Field(alias="adsConsent")]
    r"""Unknown"""

    ads_consent_reminder_at: Annotated[
        Nullable[datetime], pydantic.Field(alias="adsConsentReminderAt")
    ]
    r"""Unknown"""

    ads_consent_set_at: Annotated[
        Nullable[datetime], pydantic.Field(alias="adsConsentSetAt")
    ]
    r"""Unknown"""

    auth_token: Annotated[str, pydantic.Field(alias="authToken")]
    r"""The account token"""

    country: str
    r"""The account country"""

    email: str
    r"""The account email address"""

    friendly_name: Annotated[str, pydantic.Field(alias="friendlyName")]
    r"""Your account full name"""

    entitlements: List[str]
    r"""List of devices your allowed to use with this account"""

    home_size: Annotated[int, pydantic.Field(alias="homeSize")]
    r"""The number of accounts in the Plex Home"""

    id: int
    r"""The Plex account ID"""

    joined_at: Annotated[int, pydantic.Field(alias="joinedAt")]
    r"""Unix epoch datetime in seconds"""

    locale: Nullable[str]
    r"""The account locale"""

    mailing_list_status: Annotated[
        PostUsersSignInDataMailingListStatus, pydantic.Field(alias="mailingListStatus")
    ]
    r"""Your current mailing list status"""

    max_home_size: Annotated[int, pydantic.Field(alias="maxHomeSize")]
    r"""The maximum number of accounts allowed in the Plex Home"""

    profile: PostUsersSignInDataUserProfile

    remember_expires_at: Annotated[int, pydantic.Field(alias="rememberExpiresAt")]
    r"""Unix epoch datetime in seconds"""

    scrobble_types: Annotated[str, pydantic.Field(alias="scrobbleTypes")]
    r"""Unknown"""

    services: List[PostUsersSignInDataServices]

    subscription: PostUsersSignInDataSubscription
    r"""If the account’s Plex Pass subscription is active"""

    subscription_description: Annotated[
        Nullable[str], pydantic.Field(alias="subscriptionDescription")
    ]
    r"""Description of the Plex Pass subscription"""

    subscriptions: List[PostUsersSignInDataAuthenticationSubscription]

    thumb: str
    r"""URL of the account thumbnail"""

    title: str
    r"""The title of the account (username or friendly name)"""

    username: str
    r"""The account username"""

    uuid: str
    r"""The account UUID"""

    attribution_partner: Annotated[
        Nullable[str], pydantic.Field(alias="attributionPartner")
    ]

    past_subscriptions: Annotated[
        List[PastSubscription], pydantic.Field(alias="pastSubscriptions")
    ]

    trials: List[Trials]

    anonymous: OptionalNullable[bool] = False
    r"""Unknown"""

    backup_codes_created: Annotated[
        Optional[bool], pydantic.Field(alias="backupCodesCreated")
    ] = False
    r"""If the two-factor authentication backup codes have been created"""

    confirmed: Optional[bool] = False
    r"""If the account has been confirmed"""

    email_only_auth: Annotated[
        Optional[bool], pydantic.Field(alias="emailOnlyAuth")
    ] = False
    r"""If login with email only is enabled"""

    experimental_features: Annotated[
        Optional[bool], pydantic.Field(alias="experimentalFeatures")
    ] = False
    r"""If experimental features are enabled"""

    guest: Optional[bool] = False
    r"""If the account is a Plex Home guest user"""

    has_password: Annotated[Optional[bool], pydantic.Field(alias="hasPassword")] = True
    r"""If the account has a password"""

    home: Optional[bool] = False
    r"""If the account is a Plex Home user"""

    home_admin: Annotated[Optional[bool], pydantic.Field(alias="homeAdmin")] = False
    r"""If the account is the Plex Home admin"""

    mailing_list_active: Annotated[
        Optional[bool], pydantic.Field(alias="mailingListActive")
    ] = False
    r"""If you are subscribed to the Plex newsletter"""

    pin: Annotated[
        Optional[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None
    r"""[Might be removed] The hashed Plex Home PIN"""

    protected: Optional[bool] = False
    r"""If the account has a Plex Home PIN enabled"""

    restricted: Optional[bool] = False
    r"""If the account is a Plex Home managed user"""

    roles: Optional[List[str]] = None
    r"""[Might be removed] List of account roles. Plexpass membership listed here"""

    two_factor_enabled: Annotated[
        Optional[bool], pydantic.Field(alias="twoFactorEnabled")
    ] = False
    r"""If two-factor authentication is enabled"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "anonymous",
            "backupCodesCreated",
            "confirmed",
            "emailOnlyAuth",
            "experimentalFeatures",
            "guest",
            "hasPassword",
            "home",
            "homeAdmin",
            "mailingListActive",
            "pin",
            "protected",
            "restricted",
            "roles",
            "twoFactorEnabled",
        ]
        nullable_fields = [
            "adsConsent",
            "adsConsentReminderAt",
            "adsConsentSetAt",
            "locale",
            "subscriptionDescription",
            "attributionPartner",
            "anonymous",
        ]
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


class PostUsersSignInDataResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    user_plex_account: NotRequired[PostUsersSignInDataUserPlexAccountTypedDict]
    r"""Returns the user account data with a valid auth token"""


class PostUsersSignInDataResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    user_plex_account: Optional[PostUsersSignInDataUserPlexAccount] = None
    r"""Returns the user account data with a valid auth token"""
