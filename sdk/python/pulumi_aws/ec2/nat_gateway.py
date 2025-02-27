# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['NatGateway']


class NatGateway(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocation_id: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a resource to create a VPC NAT Gateway.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        gw = aws.ec2.NatGateway("gw",
            allocation_id=aws_eip["nat"]["id"],
            subnet_id=aws_subnet["example"]["id"])
        ```

        Usage with tags:

        ```python
        import pulumi
        import pulumi_aws as aws

        gw = aws.ec2.NatGateway("gw",
            allocation_id=aws_eip["nat"]["id"],
            subnet_id=aws_subnet["example"]["id"],
            tags={
                "Name": "gw NAT",
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] allocation_id: The Allocation ID of the Elastic IP address for the gateway.
        :param pulumi.Input[str] subnet_id: The Subnet ID of the subnet in which to place the gateway.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
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

            if allocation_id is None:
                raise TypeError("Missing required property 'allocation_id'")
            __props__['allocation_id'] = allocation_id
            if subnet_id is None:
                raise TypeError("Missing required property 'subnet_id'")
            __props__['subnet_id'] = subnet_id
            __props__['tags'] = tags
            __props__['network_interface_id'] = None
            __props__['private_ip'] = None
            __props__['public_ip'] = None
        super(NatGateway, __self__).__init__(
            'aws:ec2/natGateway:NatGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allocation_id: Optional[pulumi.Input[str]] = None,
            network_interface_id: Optional[pulumi.Input[str]] = None,
            private_ip: Optional[pulumi.Input[str]] = None,
            public_ip: Optional[pulumi.Input[str]] = None,
            subnet_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'NatGateway':
        """
        Get an existing NatGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] allocation_id: The Allocation ID of the Elastic IP address for the gateway.
        :param pulumi.Input[str] network_interface_id: The ENI ID of the network interface created by the NAT gateway.
        :param pulumi.Input[str] private_ip: The private IP address of the NAT Gateway.
        :param pulumi.Input[str] public_ip: The public IP address of the NAT Gateway.
        :param pulumi.Input[str] subnet_id: The Subnet ID of the subnet in which to place the gateway.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["allocation_id"] = allocation_id
        __props__["network_interface_id"] = network_interface_id
        __props__["private_ip"] = private_ip
        __props__["public_ip"] = public_ip
        __props__["subnet_id"] = subnet_id
        __props__["tags"] = tags
        return NatGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> pulumi.Output[str]:
        """
        The Allocation ID of the Elastic IP address for the gateway.
        """
        return pulumi.get(self, "allocation_id")

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[str]:
        """
        The ENI ID of the network interface created by the NAT gateway.
        """
        return pulumi.get(self, "network_interface_id")

    @property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> pulumi.Output[str]:
        """
        The private IP address of the NAT Gateway.
        """
        return pulumi.get(self, "private_ip")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> pulumi.Output[str]:
        """
        The public IP address of the NAT Gateway.
        """
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        The Subnet ID of the subnet in which to place the gateway.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

