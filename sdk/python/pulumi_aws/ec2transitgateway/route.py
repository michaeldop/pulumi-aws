# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['Route']


class Route(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 blackhole: Optional[pulumi.Input[bool]] = None,
                 destination_cidr_block: Optional[pulumi.Input[str]] = None,
                 transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
                 transit_gateway_route_table_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an EC2 Transit Gateway Route.

        ## Example Usage
        ### Standard usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2transitgateway.Route("example",
            destination_cidr_block="0.0.0.0/0",
            transit_gateway_attachment_id=aws_ec2_transit_gateway_vpc_attachment["example"]["id"],
            transit_gateway_route_table_id=aws_ec2_transit_gateway["example"]["association_default_route_table_id"])
        ```
        ### Blackhole route

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2transitgateway.Route("example",
            destination_cidr_block="0.0.0.0/0",
            blackhole=True,
            transit_gateway_route_table_id=aws_ec2_transit_gateway["example"]["association_default_route_table_id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] blackhole: Indicates whether to drop traffic that matches this route (default to `false`).
        :param pulumi.Input[str] destination_cidr_block: IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.
        :param pulumi.Input[str] transit_gateway_attachment_id: Identifier of EC2 Transit Gateway Attachment (required if `blackhole` is set to false).
        :param pulumi.Input[str] transit_gateway_route_table_id: Identifier of EC2 Transit Gateway Route Table.
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

            __props__['blackhole'] = blackhole
            if destination_cidr_block is None:
                raise TypeError("Missing required property 'destination_cidr_block'")
            __props__['destination_cidr_block'] = destination_cidr_block
            __props__['transit_gateway_attachment_id'] = transit_gateway_attachment_id
            if transit_gateway_route_table_id is None:
                raise TypeError("Missing required property 'transit_gateway_route_table_id'")
            __props__['transit_gateway_route_table_id'] = transit_gateway_route_table_id
        super(Route, __self__).__init__(
            'aws:ec2transitgateway/route:Route',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            blackhole: Optional[pulumi.Input[bool]] = None,
            destination_cidr_block: Optional[pulumi.Input[str]] = None,
            transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
            transit_gateway_route_table_id: Optional[pulumi.Input[str]] = None) -> 'Route':
        """
        Get an existing Route resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] blackhole: Indicates whether to drop traffic that matches this route (default to `false`).
        :param pulumi.Input[str] destination_cidr_block: IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.
        :param pulumi.Input[str] transit_gateway_attachment_id: Identifier of EC2 Transit Gateway Attachment (required if `blackhole` is set to false).
        :param pulumi.Input[str] transit_gateway_route_table_id: Identifier of EC2 Transit Gateway Route Table.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["blackhole"] = blackhole
        __props__["destination_cidr_block"] = destination_cidr_block
        __props__["transit_gateway_attachment_id"] = transit_gateway_attachment_id
        __props__["transit_gateway_route_table_id"] = transit_gateway_route_table_id
        return Route(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def blackhole(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether to drop traffic that matches this route (default to `false`).
        """
        return pulumi.get(self, "blackhole")

    @property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> pulumi.Output[str]:
        """
        IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.
        """
        return pulumi.get(self, "destination_cidr_block")

    @property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Output[Optional[str]]:
        """
        Identifier of EC2 Transit Gateway Attachment (required if `blackhole` is set to false).
        """
        return pulumi.get(self, "transit_gateway_attachment_id")

    @property
    @pulumi.getter(name="transitGatewayRouteTableId")
    def transit_gateway_route_table_id(self) -> pulumi.Output[str]:
        """
        Identifier of EC2 Transit Gateway Route Table.
        """
        return pulumi.get(self, "transit_gateway_route_table_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

