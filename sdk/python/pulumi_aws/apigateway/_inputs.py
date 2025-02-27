# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'AccountThrottleSettingsArgs',
    'DocumentationPartLocationArgs',
    'DomainNameEndpointConfigurationArgs',
    'MethodSettingsSettingsArgs',
    'RestApiEndpointConfigurationArgs',
    'StageAccessLogSettingsArgs',
    'UsagePlanApiStageArgs',
    'UsagePlanQuotaSettingsArgs',
    'UsagePlanThrottleSettingsArgs',
]

@pulumi.input_type
class AccountThrottleSettingsArgs:
    def __init__(__self__, *,
                 burst_limit: Optional[pulumi.Input[float]] = None,
                 rate_limit: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[float] burst_limit: The absolute maximum number of times API Gateway allows the API to be called per second (RPS).
        :param pulumi.Input[float] rate_limit: The number of times API Gateway allows the API to be called per second on average (RPS).
        """
        if burst_limit is not None:
            pulumi.set(__self__, "burst_limit", burst_limit)
        if rate_limit is not None:
            pulumi.set(__self__, "rate_limit", rate_limit)

    @property
    @pulumi.getter(name="burstLimit")
    def burst_limit(self) -> Optional[pulumi.Input[float]]:
        """
        The absolute maximum number of times API Gateway allows the API to be called per second (RPS).
        """
        return pulumi.get(self, "burst_limit")

    @burst_limit.setter
    def burst_limit(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "burst_limit", value)

    @property
    @pulumi.getter(name="rateLimit")
    def rate_limit(self) -> Optional[pulumi.Input[float]]:
        """
        The number of times API Gateway allows the API to be called per second on average (RPS).
        """
        return pulumi.get(self, "rate_limit")

    @rate_limit.setter
    def rate_limit(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "rate_limit", value)


@pulumi.input_type
class DocumentationPartLocationArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 method: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 status_code: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: The type of API entity to which the documentation content applies. e.g. `API`, `METHOD` or `REQUEST_BODY`
        :param pulumi.Input[str] method: The HTTP verb of a method. The default value is `*` for any method.
        :param pulumi.Input[str] name: The name of the targeted API entity.
        :param pulumi.Input[str] path: The URL path of the target. The default value is `/` for the root resource.
        :param pulumi.Input[str] status_code: The HTTP status code of a response. The default value is `*` for any status code.
        """
        pulumi.set(__self__, "type", type)
        if method is not None:
            pulumi.set(__self__, "method", method)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if status_code is not None:
            pulumi.set(__self__, "status_code", status_code)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of API entity to which the documentation content applies. e.g. `API`, `METHOD` or `REQUEST_BODY`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[str]]:
        """
        The HTTP verb of a method. The default value is `*` for any method.
        """
        return pulumi.get(self, "method")

    @method.setter
    def method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "method", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the targeted API entity.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        The URL path of the target. The default value is `/` for the root resource.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[pulumi.Input[str]]:
        """
        The HTTP status code of a response. The default value is `*` for any status code.
        """
        return pulumi.get(self, "status_code")

    @status_code.setter
    def status_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status_code", value)


@pulumi.input_type
class DomainNameEndpointConfigurationArgs:
    def __init__(__self__, *,
                 types: pulumi.Input[str]):
        """
        :param pulumi.Input[str] types: A list of endpoint types. This resource currently only supports managing a single value. Valid values: `EDGE` or `REGIONAL`. If unspecified, defaults to `EDGE`. Must be declared as `REGIONAL` in non-Commercial partitions. Refer to the [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html) for more information on the difference between edge-optimized and regional APIs.
        """
        pulumi.set(__self__, "types", types)

    @property
    @pulumi.getter
    def types(self) -> pulumi.Input[str]:
        """
        A list of endpoint types. This resource currently only supports managing a single value. Valid values: `EDGE` or `REGIONAL`. If unspecified, defaults to `EDGE`. Must be declared as `REGIONAL` in non-Commercial partitions. Refer to the [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html) for more information on the difference between edge-optimized and regional APIs.
        """
        return pulumi.get(self, "types")

    @types.setter
    def types(self, value: pulumi.Input[str]):
        pulumi.set(self, "types", value)


@pulumi.input_type
class MethodSettingsSettingsArgs:
    def __init__(__self__, *,
                 cache_data_encrypted: Optional[pulumi.Input[bool]] = None,
                 cache_ttl_in_seconds: Optional[pulumi.Input[float]] = None,
                 caching_enabled: Optional[pulumi.Input[bool]] = None,
                 data_trace_enabled: Optional[pulumi.Input[bool]] = None,
                 logging_level: Optional[pulumi.Input[str]] = None,
                 metrics_enabled: Optional[pulumi.Input[bool]] = None,
                 require_authorization_for_cache_control: Optional[pulumi.Input[bool]] = None,
                 throttling_burst_limit: Optional[pulumi.Input[float]] = None,
                 throttling_rate_limit: Optional[pulumi.Input[float]] = None,
                 unauthorized_cache_control_header_strategy: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] cache_data_encrypted: Specifies whether the cached responses are encrypted.
        :param pulumi.Input[float] cache_ttl_in_seconds: Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL, the longer the response will be cached.
        :param pulumi.Input[bool] caching_enabled: Specifies whether responses should be cached and returned for requests. A cache cluster must be enabled on the stage for responses to be cached.
        :param pulumi.Input[bool] data_trace_enabled: Specifies whether data trace logging is enabled for this method, which effects the log entries pushed to Amazon CloudWatch Logs.
        :param pulumi.Input[str] logging_level: Specifies the logging level for this method, which effects the log entries pushed to Amazon CloudWatch Logs. The available levels are `OFF`, `ERROR`, and `INFO`.
        :param pulumi.Input[bool] metrics_enabled: Specifies whether Amazon CloudWatch metrics are enabled for this method.
        :param pulumi.Input[bool] require_authorization_for_cache_control: Specifies whether authorization is required for a cache invalidation request.
        :param pulumi.Input[float] throttling_burst_limit: Specifies the throttling burst limit. Default: `-1` (throttling disabled).
        :param pulumi.Input[float] throttling_rate_limit: Specifies the throttling rate limit. Default: `-1` (throttling disabled).
        :param pulumi.Input[str] unauthorized_cache_control_header_strategy: Specifies how to handle unauthorized requests for cache invalidation. The available values are `FAIL_WITH_403`, `SUCCEED_WITH_RESPONSE_HEADER`, `SUCCEED_WITHOUT_RESPONSE_HEADER`.
        """
        if cache_data_encrypted is not None:
            pulumi.set(__self__, "cache_data_encrypted", cache_data_encrypted)
        if cache_ttl_in_seconds is not None:
            pulumi.set(__self__, "cache_ttl_in_seconds", cache_ttl_in_seconds)
        if caching_enabled is not None:
            pulumi.set(__self__, "caching_enabled", caching_enabled)
        if data_trace_enabled is not None:
            pulumi.set(__self__, "data_trace_enabled", data_trace_enabled)
        if logging_level is not None:
            pulumi.set(__self__, "logging_level", logging_level)
        if metrics_enabled is not None:
            pulumi.set(__self__, "metrics_enabled", metrics_enabled)
        if require_authorization_for_cache_control is not None:
            pulumi.set(__self__, "require_authorization_for_cache_control", require_authorization_for_cache_control)
        if throttling_burst_limit is not None:
            pulumi.set(__self__, "throttling_burst_limit", throttling_burst_limit)
        if throttling_rate_limit is not None:
            pulumi.set(__self__, "throttling_rate_limit", throttling_rate_limit)
        if unauthorized_cache_control_header_strategy is not None:
            pulumi.set(__self__, "unauthorized_cache_control_header_strategy", unauthorized_cache_control_header_strategy)

    @property
    @pulumi.getter(name="cacheDataEncrypted")
    def cache_data_encrypted(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether the cached responses are encrypted.
        """
        return pulumi.get(self, "cache_data_encrypted")

    @cache_data_encrypted.setter
    def cache_data_encrypted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cache_data_encrypted", value)

    @property
    @pulumi.getter(name="cacheTtlInSeconds")
    def cache_ttl_in_seconds(self) -> Optional[pulumi.Input[float]]:
        """
        Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL, the longer the response will be cached.
        """
        return pulumi.get(self, "cache_ttl_in_seconds")

    @cache_ttl_in_seconds.setter
    def cache_ttl_in_seconds(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "cache_ttl_in_seconds", value)

    @property
    @pulumi.getter(name="cachingEnabled")
    def caching_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether responses should be cached and returned for requests. A cache cluster must be enabled on the stage for responses to be cached.
        """
        return pulumi.get(self, "caching_enabled")

    @caching_enabled.setter
    def caching_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "caching_enabled", value)

    @property
    @pulumi.getter(name="dataTraceEnabled")
    def data_trace_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether data trace logging is enabled for this method, which effects the log entries pushed to Amazon CloudWatch Logs.
        """
        return pulumi.get(self, "data_trace_enabled")

    @data_trace_enabled.setter
    def data_trace_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "data_trace_enabled", value)

    @property
    @pulumi.getter(name="loggingLevel")
    def logging_level(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the logging level for this method, which effects the log entries pushed to Amazon CloudWatch Logs. The available levels are `OFF`, `ERROR`, and `INFO`.
        """
        return pulumi.get(self, "logging_level")

    @logging_level.setter
    def logging_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logging_level", value)

    @property
    @pulumi.getter(name="metricsEnabled")
    def metrics_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether Amazon CloudWatch metrics are enabled for this method.
        """
        return pulumi.get(self, "metrics_enabled")

    @metrics_enabled.setter
    def metrics_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "metrics_enabled", value)

    @property
    @pulumi.getter(name="requireAuthorizationForCacheControl")
    def require_authorization_for_cache_control(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether authorization is required for a cache invalidation request.
        """
        return pulumi.get(self, "require_authorization_for_cache_control")

    @require_authorization_for_cache_control.setter
    def require_authorization_for_cache_control(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_authorization_for_cache_control", value)

    @property
    @pulumi.getter(name="throttlingBurstLimit")
    def throttling_burst_limit(self) -> Optional[pulumi.Input[float]]:
        """
        Specifies the throttling burst limit. Default: `-1` (throttling disabled).
        """
        return pulumi.get(self, "throttling_burst_limit")

    @throttling_burst_limit.setter
    def throttling_burst_limit(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "throttling_burst_limit", value)

    @property
    @pulumi.getter(name="throttlingRateLimit")
    def throttling_rate_limit(self) -> Optional[pulumi.Input[float]]:
        """
        Specifies the throttling rate limit. Default: `-1` (throttling disabled).
        """
        return pulumi.get(self, "throttling_rate_limit")

    @throttling_rate_limit.setter
    def throttling_rate_limit(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "throttling_rate_limit", value)

    @property
    @pulumi.getter(name="unauthorizedCacheControlHeaderStrategy")
    def unauthorized_cache_control_header_strategy(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies how to handle unauthorized requests for cache invalidation. The available values are `FAIL_WITH_403`, `SUCCEED_WITH_RESPONSE_HEADER`, `SUCCEED_WITHOUT_RESPONSE_HEADER`.
        """
        return pulumi.get(self, "unauthorized_cache_control_header_strategy")

    @unauthorized_cache_control_header_strategy.setter
    def unauthorized_cache_control_header_strategy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unauthorized_cache_control_header_strategy", value)


@pulumi.input_type
class RestApiEndpointConfigurationArgs:
    def __init__(__self__, *,
                 types: pulumi.Input[str],
                 vpc_endpoint_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] types: A list of endpoint types. This resource currently only supports managing a single value. Valid values: `EDGE`, `REGIONAL` or `PRIVATE`. If unspecified, defaults to `EDGE`. Must be declared as `REGIONAL` in non-Commercial partitions. Refer to the [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html) for more information on the difference between edge-optimized and regional APIs.
        :param pulumi.Input[List[pulumi.Input[str]]] vpc_endpoint_ids: A list of VPC Endpoint Ids. It is only supported for PRIVATE endpoint type.
        """
        pulumi.set(__self__, "types", types)
        if vpc_endpoint_ids is not None:
            pulumi.set(__self__, "vpc_endpoint_ids", vpc_endpoint_ids)

    @property
    @pulumi.getter
    def types(self) -> pulumi.Input[str]:
        """
        A list of endpoint types. This resource currently only supports managing a single value. Valid values: `EDGE`, `REGIONAL` or `PRIVATE`. If unspecified, defaults to `EDGE`. Must be declared as `REGIONAL` in non-Commercial partitions. Refer to the [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html) for more information on the difference between edge-optimized and regional APIs.
        """
        return pulumi.get(self, "types")

    @types.setter
    def types(self, value: pulumi.Input[str]):
        pulumi.set(self, "types", value)

    @property
    @pulumi.getter(name="vpcEndpointIds")
    def vpc_endpoint_ids(self) -> Optional[pulumi.Input[List[pulumi.Input[str]]]]:
        """
        A list of VPC Endpoint Ids. It is only supported for PRIVATE endpoint type.
        """
        return pulumi.get(self, "vpc_endpoint_ids")

    @vpc_endpoint_ids.setter
    def vpc_endpoint_ids(self, value: Optional[pulumi.Input[List[pulumi.Input[str]]]]):
        pulumi.set(self, "vpc_endpoint_ids", value)


@pulumi.input_type
class StageAccessLogSettingsArgs:
    def __init__(__self__, *,
                 destination_arn: pulumi.Input[str],
                 format: pulumi.Input[str]):
        """
        :param pulumi.Input[str] destination_arn: The Amazon Resource Name (ARN) of the CloudWatch Logs log group or Kinesis Data Firehose delivery stream to receive access logs. If you specify a Kinesis Data Firehose delivery stream, the stream name must begin with `amazon-apigateway-`. Automatically removes trailing `:*` if present.
        :param pulumi.Input[str] format: The formatting and values recorded in the logs. 
               For more information on configuring the log format rules visit the AWS [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html)
        """
        pulumi.set(__self__, "destination_arn", destination_arn)
        pulumi.set(__self__, "format", format)

    @property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the CloudWatch Logs log group or Kinesis Data Firehose delivery stream to receive access logs. If you specify a Kinesis Data Firehose delivery stream, the stream name must begin with `amazon-apigateway-`. Automatically removes trailing `:*` if present.
        """
        return pulumi.get(self, "destination_arn")

    @destination_arn.setter
    def destination_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination_arn", value)

    @property
    @pulumi.getter
    def format(self) -> pulumi.Input[str]:
        """
        The formatting and values recorded in the logs. 
        For more information on configuring the log format rules visit the AWS [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html)
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: pulumi.Input[str]):
        pulumi.set(self, "format", value)


@pulumi.input_type
class UsagePlanApiStageArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 stage: pulumi.Input[str]):
        """
        :param pulumi.Input[str] api_id: API Id of the associated API stage in a usage plan.
        :param pulumi.Input[str] stage: API stage name of the associated API stage in a usage plan.
        """
        pulumi.set(__self__, "api_id", api_id)
        pulumi.set(__self__, "stage", stage)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        """
        API Id of the associated API stage in a usage plan.
        """
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter
    def stage(self) -> pulumi.Input[str]:
        """
        API stage name of the associated API stage in a usage plan.
        """
        return pulumi.get(self, "stage")

    @stage.setter
    def stage(self, value: pulumi.Input[str]):
        pulumi.set(self, "stage", value)


@pulumi.input_type
class UsagePlanQuotaSettingsArgs:
    def __init__(__self__, *,
                 limit: pulumi.Input[float],
                 period: pulumi.Input[str],
                 offset: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[float] limit: The maximum number of requests that can be made in a given time period.
        :param pulumi.Input[str] period: The time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".
        :param pulumi.Input[float] offset: The number of requests subtracted from the given limit in the initial time period.
        """
        pulumi.set(__self__, "limit", limit)
        pulumi.set(__self__, "period", period)
        if offset is not None:
            pulumi.set(__self__, "offset", offset)

    @property
    @pulumi.getter
    def limit(self) -> pulumi.Input[float]:
        """
        The maximum number of requests that can be made in a given time period.
        """
        return pulumi.get(self, "limit")

    @limit.setter
    def limit(self, value: pulumi.Input[float]):
        pulumi.set(self, "limit", value)

    @property
    @pulumi.getter
    def period(self) -> pulumi.Input[str]:
        """
        The time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".
        """
        return pulumi.get(self, "period")

    @period.setter
    def period(self, value: pulumi.Input[str]):
        pulumi.set(self, "period", value)

    @property
    @pulumi.getter
    def offset(self) -> Optional[pulumi.Input[float]]:
        """
        The number of requests subtracted from the given limit in the initial time period.
        """
        return pulumi.get(self, "offset")

    @offset.setter
    def offset(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "offset", value)


@pulumi.input_type
class UsagePlanThrottleSettingsArgs:
    def __init__(__self__, *,
                 burst_limit: Optional[pulumi.Input[float]] = None,
                 rate_limit: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[float] burst_limit: The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.
        :param pulumi.Input[float] rate_limit: The API request steady-state rate limit.
        """
        if burst_limit is not None:
            pulumi.set(__self__, "burst_limit", burst_limit)
        if rate_limit is not None:
            pulumi.set(__self__, "rate_limit", rate_limit)

    @property
    @pulumi.getter(name="burstLimit")
    def burst_limit(self) -> Optional[pulumi.Input[float]]:
        """
        The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.
        """
        return pulumi.get(self, "burst_limit")

    @burst_limit.setter
    def burst_limit(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "burst_limit", value)

    @property
    @pulumi.getter(name="rateLimit")
    def rate_limit(self) -> Optional[pulumi.Input[float]]:
        """
        The API request steady-state rate limit.
        """
        return pulumi.get(self, "rate_limit")

    @rate_limit.setter
    def rate_limit(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "rate_limit", value)


