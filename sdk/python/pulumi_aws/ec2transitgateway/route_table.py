# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['RouteTable']


class RouteTable(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 transit_gateway_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an EC2 Transit Gateway Route Table.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2transitgateway.RouteTable("example", transit_gateway_id=aws_ec2_transit_gateway["example"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value tags for the EC2 Transit Gateway Route Table.
        :param pulumi.Input[str] transit_gateway_id: Identifier of EC2 Transit Gateway.
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

            __props__['tags'] = tags
            if transit_gateway_id is None:
                raise TypeError("Missing required property 'transit_gateway_id'")
            __props__['transit_gateway_id'] = transit_gateway_id
            __props__['default_association_route_table'] = None
            __props__['default_propagation_route_table'] = None
        super(RouteTable, __self__).__init__(
            'aws:ec2transitgateway/routeTable:RouteTable',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            default_association_route_table: Optional[pulumi.Input[bool]] = None,
            default_propagation_route_table: Optional[pulumi.Input[bool]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            transit_gateway_id: Optional[pulumi.Input[str]] = None) -> 'RouteTable':
        """
        Get an existing RouteTable resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] default_association_route_table: Boolean whether this is the default association route table for the EC2 Transit Gateway.
        :param pulumi.Input[bool] default_propagation_route_table: Boolean whether this is the default propagation route table for the EC2 Transit Gateway.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value tags for the EC2 Transit Gateway Route Table.
        :param pulumi.Input[str] transit_gateway_id: Identifier of EC2 Transit Gateway.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["default_association_route_table"] = default_association_route_table
        __props__["default_propagation_route_table"] = default_propagation_route_table
        __props__["tags"] = tags
        __props__["transit_gateway_id"] = transit_gateway_id
        return RouteTable(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultAssociationRouteTable")
    def default_association_route_table(self) -> pulumi.Output[bool]:
        """
        Boolean whether this is the default association route table for the EC2 Transit Gateway.
        """
        return pulumi.get(self, "default_association_route_table")

    @property
    @pulumi.getter(name="defaultPropagationRouteTable")
    def default_propagation_route_table(self) -> pulumi.Output[bool]:
        """
        Boolean whether this is the default propagation route table for the EC2 Transit Gateway.
        """
        return pulumi.get(self, "default_propagation_route_table")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value tags for the EC2 Transit Gateway Route Table.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Output[str]:
        """
        Identifier of EC2 Transit Gateway.
        """
        return pulumi.get(self, "transit_gateway_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

