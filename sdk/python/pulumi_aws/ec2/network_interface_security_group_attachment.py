# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['NetworkInterfaceSecurityGroupAttachment']


class NetworkInterfaceSecurityGroupAttachment(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 security_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        This resource attaches a security group to an Elastic Network Interface (ENI).
        It can be used to attach a security group to any existing ENI, be it a
        secondary ENI or one attached as the primary interface on an instance.

        > **NOTE on instances, interfaces, and security groups:** This provider currently
        provides the capability to assign security groups via the [`ec2.Instance`][1]
        and the [`ec2.NetworkInterface`][2] resources. Using this resource in
        conjunction with security groups provided in-line in those resources will cause
        conflicts, and will lead to spurious diffs and undefined behavior - please use
        one or the other.

        [1]: https://www.terraform.io/docs/providers/aws/d/instance.html
        [2]: https://www.terraform.io/docs/providers/aws/r/network_interface.html

        ## Example Usage

        The following provides a very basic example of setting up an instance (provided
        by `instance`) in the default security group, creating a security group
        (provided by `sg`) and then attaching the security group to the instance's
        primary network interface via the `ec2.NetworkInterfaceSecurityGroupAttachment` resource,
        named `sg_attachment`:

        ```python
        import pulumi
        import pulumi_aws as aws

        ami = aws.get_ami(most_recent=True,
            filters=[aws.GetAmiFilterArgs(
                name="name",
                values=["amzn-ami-hvm-*"],
            )],
            owners=["amazon"])
        instance = aws.ec2.Instance("instance",
            instance_type="t2.micro",
            ami=ami.id,
            tags={
                "type": "test-instance",
            })
        sg = aws.ec2.SecurityGroup("sg", tags={
            "type": "test-security-group",
        })
        sg_attachment = aws.ec2.NetworkInterfaceSecurityGroupAttachment("sgAttachment",
            security_group_id=sg.id,
            network_interface_id=instance.primary_network_interface_id)
        ```

        In this example, `instance` is provided by the `ec2.Instance` data source,
        fetching an external instance, possibly not managed by this provider.
        `sg_attachment` then attaches to the output instance's `network_interface_id`:

        ```python
        import pulumi
        import pulumi_aws as aws

        instance = aws.ec2.get_instance(instance_id="i-1234567890abcdef0")
        sg = aws.ec2.SecurityGroup("sg", tags={
            "type": "test-security-group",
        })
        sg_attachment = aws.ec2.NetworkInterfaceSecurityGroupAttachment("sgAttachment",
            security_group_id=sg.id,
            network_interface_id=instance.network_interface_id)
        ```
        ## Output Reference

        There are no outputs for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] network_interface_id: The ID of the network interface to attach to.
        :param pulumi.Input[str] security_group_id: The ID of the security group.
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

            if network_interface_id is None:
                raise TypeError("Missing required property 'network_interface_id'")
            __props__['network_interface_id'] = network_interface_id
            if security_group_id is None:
                raise TypeError("Missing required property 'security_group_id'")
            __props__['security_group_id'] = security_group_id
        super(NetworkInterfaceSecurityGroupAttachment, __self__).__init__(
            'aws:ec2/networkInterfaceSecurityGroupAttachment:NetworkInterfaceSecurityGroupAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            network_interface_id: Optional[pulumi.Input[str]] = None,
            security_group_id: Optional[pulumi.Input[str]] = None) -> 'NetworkInterfaceSecurityGroupAttachment':
        """
        Get an existing NetworkInterfaceSecurityGroupAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] network_interface_id: The ID of the network interface to attach to.
        :param pulumi.Input[str] security_group_id: The ID of the security group.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["network_interface_id"] = network_interface_id
        __props__["security_group_id"] = security_group_id
        return NetworkInterfaceSecurityGroupAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[str]:
        """
        The ID of the network interface to attach to.
        """
        return pulumi.get(self, "network_interface_id")

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the security group.
        """
        return pulumi.get(self, "security_group_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

