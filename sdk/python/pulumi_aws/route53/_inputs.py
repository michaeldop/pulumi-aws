# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'RecordAliasArgs',
    'RecordFailoverRoutingPolicyArgs',
    'RecordGeolocationRoutingPolicyArgs',
    'RecordLatencyRoutingPolicyArgs',
    'RecordWeightedRoutingPolicyArgs',
    'ResolverEndpointIpAddressArgs',
    'ResolverRuleTargetIpArgs',
    'ZoneVpcArgs',
]

@pulumi.input_type
class RecordAliasArgs:
    def __init__(__self__, *,
                 evaluate_target_health: pulumi.Input[bool],
                 name: pulumi.Input[str],
                 zone_id: pulumi.Input[str]):
        """
        :param pulumi.Input[bool] evaluate_target_health: Set to `true` if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see [related part of documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health).
        :param pulumi.Input[str] name: DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
        :param pulumi.Input[str] zone_id: Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See `resource_elb.zone_id` for example.
        """
        pulumi.set(__self__, "evaluate_target_health", evaluate_target_health)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> pulumi.Input[bool]:
        """
        Set to `true` if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see [related part of documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health).
        """
        return pulumi.get(self, "evaluate_target_health")

    @evaluate_target_health.setter
    def evaluate_target_health(self, value: pulumi.Input[bool]):
        pulumi.set(self, "evaluate_target_health", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[str]:
        """
        Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See `resource_elb.zone_id` for example.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_id", value)


@pulumi.input_type
class RecordFailoverRoutingPolicyArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[str] type: `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
        """
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class RecordGeolocationRoutingPolicyArgs:
    def __init__(__self__, *,
                 continent: Optional[pulumi.Input[str]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 subdivision: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] continent: A two-letter continent code. See http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html for code details. Either `continent` or `country` must be specified.
        :param pulumi.Input[str] country: A two-character country code or `*` to indicate a default resource record set.
        :param pulumi.Input[str] subdivision: A subdivision code for a country.
        """
        if continent is not None:
            pulumi.set(__self__, "continent", continent)
        if country is not None:
            pulumi.set(__self__, "country", country)
        if subdivision is not None:
            pulumi.set(__self__, "subdivision", subdivision)

    @property
    @pulumi.getter
    def continent(self) -> Optional[pulumi.Input[str]]:
        """
        A two-letter continent code. See http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html for code details. Either `continent` or `country` must be specified.
        """
        return pulumi.get(self, "continent")

    @continent.setter
    def continent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "continent", value)

    @property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[str]]:
        """
        A two-character country code or `*` to indicate a default resource record set.
        """
        return pulumi.get(self, "country")

    @country.setter
    def country(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country", value)

    @property
    @pulumi.getter
    def subdivision(self) -> Optional[pulumi.Input[str]]:
        """
        A subdivision code for a country.
        """
        return pulumi.get(self, "subdivision")

    @subdivision.setter
    def subdivision(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subdivision", value)


@pulumi.input_type
class RecordLatencyRoutingPolicyArgs:
    def __init__(__self__, *,
                 region: pulumi.Input[str]):
        """
        :param pulumi.Input[str] region: An AWS region from which to measure latency. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency
        """
        pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        An AWS region from which to measure latency. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class RecordWeightedRoutingPolicyArgs:
    def __init__(__self__, *,
                 weight: pulumi.Input[float]):
        """
        :param pulumi.Input[float] weight: A numeric value indicating the relative weight of the record. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted.
        """
        pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Input[float]:
        """
        A numeric value indicating the relative weight of the record. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted.
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: pulumi.Input[float]):
        pulumi.set(self, "weight", value)


@pulumi.input_type
class ResolverEndpointIpAddressArgs:
    def __init__(__self__, *,
                 subnet_id: pulumi.Input[str],
                 ip: Optional[pulumi.Input[str]] = None,
                 ip_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] subnet_id: The ID of the subnet that contains the IP address.
        :param pulumi.Input[str] ip: The IP address in the subnet that you want to use for DNS queries.
        """
        pulumi.set(__self__, "subnet_id", subnet_id)
        if ip is not None:
            pulumi.set(__self__, "ip", ip)
        if ip_id is not None:
            pulumi.set(__self__, "ip_id", ip_id)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        The ID of the subnet that contains the IP address.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address in the subnet that you want to use for DNS queries.
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)

    @property
    @pulumi.getter(name="ipId")
    def ip_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ip_id")

    @ip_id.setter
    def ip_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_id", value)


@pulumi.input_type
class ResolverRuleTargetIpArgs:
    def __init__(__self__, *,
                 ip: pulumi.Input[str],
                 port: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[str] ip: One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.
        :param pulumi.Input[float] port: The port at `ip` that you want to forward DNS queries to. Default value is `53`
        """
        pulumi.set(__self__, "ip", ip)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def ip(self) -> pulumi.Input[str]:
        """
        One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: pulumi.Input[str]):
        pulumi.set(self, "ip", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[float]]:
        """
        The port at `ip` that you want to forward DNS queries to. Default value is `53`
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "port", value)


@pulumi.input_type
class ZoneVpcArgs:
    def __init__(__self__, *,
                 vpc_id: pulumi.Input[str],
                 vpc_region: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] vpc_id: ID of the VPC to associate.
        :param pulumi.Input[str] vpc_region: Region of the VPC to associate. Defaults to AWS provider region.
        """
        pulumi.set(__self__, "vpc_id", vpc_id)
        if vpc_region is not None:
            pulumi.set(__self__, "vpc_region", vpc_region)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        """
        ID of the VPC to associate.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter(name="vpcRegion")
    def vpc_region(self) -> Optional[pulumi.Input[str]]:
        """
        Region of the VPC to associate. Defaults to AWS provider region.
        """
        return pulumi.get(self, "vpc_region")

    @vpc_region.setter
    def vpc_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_region", value)


