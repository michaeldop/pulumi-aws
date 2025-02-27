# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['SamplingRule']


class SamplingRule(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 fixed_rate: Optional[pulumi.Input[float]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 http_method: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[float]] = None,
                 reservoir_size: Optional[pulumi.Input[float]] = None,
                 resource_arn: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 service_type: Optional[pulumi.Input[str]] = None,
                 url_path: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[float]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates and manages an AWS XRay Sampling Rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.xray.SamplingRule("example",
            attributes={
                "Hello": "Tris",
            },
            fixed_rate=0.05,
            host="*",
            http_method="*",
            priority=10000,
            reservoir_size=1,
            resource_arn="*",
            rule_name="example",
            service_name="*",
            service_type="*",
            url_path="*",
            version=1)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] attributes: Matches attributes derived from the request.
        :param pulumi.Input[float] fixed_rate: The percentage of matching requests to instrument, after the reservoir is exhausted.
        :param pulumi.Input[str] host: Matches the hostname from a request URL.
        :param pulumi.Input[str] http_method: Matches the HTTP method of a request.
        :param pulumi.Input[float] priority: The priority of the sampling rule.
        :param pulumi.Input[float] reservoir_size: A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.
        :param pulumi.Input[str] resource_arn: Matches the ARN of the AWS resource on which the service runs.
        :param pulumi.Input[str] rule_name: The name of the sampling rule.
        :param pulumi.Input[str] service_name: Matches the `name` that the service uses to identify itself in segments.
        :param pulumi.Input[str] service_type: Matches the `origin` that the service uses to identify its type in segments.
        :param pulumi.Input[str] url_path: Matches the path from a request URL.
        :param pulumi.Input[float] version: The version of the sampling rule format (`1` )
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['attributes'] = attributes
            if fixed_rate is None:
                raise TypeError("Missing required property 'fixed_rate'")
            __props__['fixed_rate'] = fixed_rate
            if host is None:
                raise TypeError("Missing required property 'host'")
            __props__['host'] = host
            if http_method is None:
                raise TypeError("Missing required property 'http_method'")
            __props__['http_method'] = http_method
            if priority is None:
                raise TypeError("Missing required property 'priority'")
            __props__['priority'] = priority
            if reservoir_size is None:
                raise TypeError("Missing required property 'reservoir_size'")
            __props__['reservoir_size'] = reservoir_size
            if resource_arn is None:
                raise TypeError("Missing required property 'resource_arn'")
            __props__['resource_arn'] = resource_arn
            __props__['rule_name'] = rule_name
            if service_name is None:
                raise TypeError("Missing required property 'service_name'")
            __props__['service_name'] = service_name
            if service_type is None:
                raise TypeError("Missing required property 'service_type'")
            __props__['service_type'] = service_type
            if url_path is None:
                raise TypeError("Missing required property 'url_path'")
            __props__['url_path'] = url_path
            if version is None:
                raise TypeError("Missing required property 'version'")
            __props__['version'] = version
            __props__['arn'] = None
        super(SamplingRule, __self__).__init__(
            'aws:xray/samplingRule:SamplingRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            fixed_rate: Optional[pulumi.Input[float]] = None,
            host: Optional[pulumi.Input[str]] = None,
            http_method: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[float]] = None,
            reservoir_size: Optional[pulumi.Input[float]] = None,
            resource_arn: Optional[pulumi.Input[str]] = None,
            rule_name: Optional[pulumi.Input[str]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            service_type: Optional[pulumi.Input[str]] = None,
            url_path: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[float]] = None) -> 'SamplingRule':
        """
        Get an existing SamplingRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the sampling rule.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] attributes: Matches attributes derived from the request.
        :param pulumi.Input[float] fixed_rate: The percentage of matching requests to instrument, after the reservoir is exhausted.
        :param pulumi.Input[str] host: Matches the hostname from a request URL.
        :param pulumi.Input[str] http_method: Matches the HTTP method of a request.
        :param pulumi.Input[float] priority: The priority of the sampling rule.
        :param pulumi.Input[float] reservoir_size: A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.
        :param pulumi.Input[str] resource_arn: Matches the ARN of the AWS resource on which the service runs.
        :param pulumi.Input[str] rule_name: The name of the sampling rule.
        :param pulumi.Input[str] service_name: Matches the `name` that the service uses to identify itself in segments.
        :param pulumi.Input[str] service_type: Matches the `origin` that the service uses to identify its type in segments.
        :param pulumi.Input[str] url_path: Matches the path from a request URL.
        :param pulumi.Input[float] version: The version of the sampling rule format (`1` )
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["attributes"] = attributes
        __props__["fixed_rate"] = fixed_rate
        __props__["host"] = host
        __props__["http_method"] = http_method
        __props__["priority"] = priority
        __props__["reservoir_size"] = reservoir_size
        __props__["resource_arn"] = resource_arn
        __props__["rule_name"] = rule_name
        __props__["service_name"] = service_name
        __props__["service_type"] = service_type
        __props__["url_path"] = url_path
        __props__["version"] = version
        return SamplingRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the sampling rule.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Matches attributes derived from the request.
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="fixedRate")
    def fixed_rate(self) -> pulumi.Output[float]:
        """
        The percentage of matching requests to instrument, after the reservoir is exhausted.
        """
        return pulumi.get(self, "fixed_rate")

    @property
    @pulumi.getter
    def host(self) -> pulumi.Output[str]:
        """
        Matches the hostname from a request URL.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> pulumi.Output[str]:
        """
        Matches the HTTP method of a request.
        """
        return pulumi.get(self, "http_method")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[float]:
        """
        The priority of the sampling rule.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="reservoirSize")
    def reservoir_size(self) -> pulumi.Output[float]:
        """
        A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.
        """
        return pulumi.get(self, "reservoir_size")

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[str]:
        """
        Matches the ARN of the AWS resource on which the service runs.
        """
        return pulumi.get(self, "resource_arn")

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the sampling rule.
        """
        return pulumi.get(self, "rule_name")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        Matches the `name` that the service uses to identify itself in segments.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> pulumi.Output[str]:
        """
        Matches the `origin` that the service uses to identify its type in segments.
        """
        return pulumi.get(self, "service_type")

    @property
    @pulumi.getter(name="urlPath")
    def url_path(self) -> pulumi.Output[str]:
        """
        Matches the path from a request URL.
        """
        return pulumi.get(self, "url_path")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[float]:
        """
        The version of the sampling rule format (`1` )
        """
        return pulumi.get(self, "version")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

