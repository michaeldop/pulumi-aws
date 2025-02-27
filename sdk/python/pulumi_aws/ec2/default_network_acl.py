# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['DefaultNetworkAcl']


class DefaultNetworkAcl(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_network_acl_id: Optional[pulumi.Input[str]] = None,
                 egress: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['DefaultNetworkAclEgressArgs']]]]] = None,
                 ingress: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['DefaultNetworkAclIngressArgs']]]]] = None,
                 subnet_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a resource to manage the default AWS Network ACL. VPC Only.

        Each VPC created in AWS comes with a Default Network ACL that can be managed, but not
        destroyed. **This is an advanced resource**, and has special caveats to be aware
        of when using it. Please read this document in its entirety before using this
        resource.

        The `ec2.DefaultNetworkAcl` behaves differently from normal resources, in that
        this provider does not _create_ this resource, but instead attempts to "adopt" it
        into management. We can do this because each VPC created has a Default Network
        ACL that cannot be destroyed, and is created with a known set of default rules.

        When this provider first adopts the Default Network ACL, it **immediately removes all
        rules in the ACL**. It then proceeds to create any rules specified in the
        configuration. This step is required so that only the rules specified in the
        configuration are created.

        This resource treats its inline rules as absolute; only the rules defined
        inline are created, and any additions/removals external to this resource will
        result in diffs being shown. For these reasons, this resource is incompatible with the
        `ec2.NetworkAclRule` resource.

        For more information about Network ACLs, see the AWS Documentation on
        [Network ACLs][aws-network-acls].

        ## Basic Example Usage, with default rules

        The following config gives the Default Network ACL the same rules that AWS
        includes, but pulls the resource under management by this provider. This means that
        any ACL rules added or changed will be detected as drift.

        ```python
        import pulumi
        import pulumi_aws as aws

        mainvpc = aws.ec2.Vpc("mainvpc", cidr_block="10.1.0.0/16")
        default = aws.ec2.DefaultNetworkAcl("default",
            default_network_acl_id=mainvpc.default_network_acl_id,
            ingress=[aws.ec2.DefaultNetworkAclIngressArgs(
                protocol="-1",
                rule_no=100,
                action="allow",
                cidr_block=mainvpc.cidr_block,
                from_port=0,
                to_port=0,
            )],
            egress=[aws.ec2.DefaultNetworkAclEgressArgs(
                protocol="-1",
                rule_no=100,
                action="allow",
                cidr_block="0.0.0.0/0",
                from_port=0,
                to_port=0,
            )])
        ```

        ## Example config to deny all Egress traffic, allowing Ingress

        The following denies all Egress traffic by omitting any `egress` rules, while
        including the default `ingress` rule to allow all traffic.

        ```python
        import pulumi
        import pulumi_aws as aws

        mainvpc = aws.ec2.Vpc("mainvpc", cidr_block="10.1.0.0/16")
        default = aws.ec2.DefaultNetworkAcl("default",
            default_network_acl_id=mainvpc.default_network_acl_id,
            ingress=[aws.ec2.DefaultNetworkAclIngressArgs(
                protocol="-1",
                rule_no=100,
                action="allow",
                cidr_block=mainvpc.cidr_block,
                from_port=0,
                to_port=0,
            )])
        ```

        ## Example config to deny all traffic to any Subnet in the Default Network ACL

        This config denies all traffic in the Default ACL. This can be useful if you
        want a locked down default to force all resources in the VPC to assign a
        non-default ACL.

        ```python
        import pulumi
        import pulumi_aws as aws

        mainvpc = aws.ec2.Vpc("mainvpc", cidr_block="10.1.0.0/16")
        default = aws.ec2.DefaultNetworkAcl("default", default_network_acl_id=mainvpc.default_network_acl_id)
        # no rules defined, deny all traffic in this ACL
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_network_acl_id: The Network ACL ID to manage. This
               attribute is exported from `ec2.Vpc`, or manually found via the AWS Console.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['DefaultNetworkAclEgressArgs']]]] egress: Specifies an egress rule. Parameters defined below.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['DefaultNetworkAclIngressArgs']]]] ingress: Specifies an ingress rule. Parameters defined below.
        :param pulumi.Input[List[pulumi.Input[str]]] subnet_ids: A list of Subnet IDs to apply the ACL to. See the
               notes below on managing Subnets in the Default Network ACL
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

            if default_network_acl_id is None:
                raise TypeError("Missing required property 'default_network_acl_id'")
            __props__['default_network_acl_id'] = default_network_acl_id
            __props__['egress'] = egress
            __props__['ingress'] = ingress
            __props__['subnet_ids'] = subnet_ids
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['owner_id'] = None
            __props__['vpc_id'] = None
        super(DefaultNetworkAcl, __self__).__init__(
            'aws:ec2/defaultNetworkAcl:DefaultNetworkAcl',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            default_network_acl_id: Optional[pulumi.Input[str]] = None,
            egress: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['DefaultNetworkAclEgressArgs']]]]] = None,
            ingress: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['DefaultNetworkAclIngressArgs']]]]] = None,
            owner_id: Optional[pulumi.Input[str]] = None,
            subnet_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None) -> 'DefaultNetworkAcl':
        """
        Get an existing DefaultNetworkAcl resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the Default Network ACL
        :param pulumi.Input[str] default_network_acl_id: The Network ACL ID to manage. This
               attribute is exported from `ec2.Vpc`, or manually found via the AWS Console.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['DefaultNetworkAclEgressArgs']]]] egress: Specifies an egress rule. Parameters defined below.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['DefaultNetworkAclIngressArgs']]]] ingress: Specifies an ingress rule. Parameters defined below.
        :param pulumi.Input[str] owner_id: The ID of the AWS account that owns the Default Network ACL
        :param pulumi.Input[List[pulumi.Input[str]]] subnet_ids: A list of Subnet IDs to apply the ACL to. See the
               notes below on managing Subnets in the Default Network ACL
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] vpc_id: The ID of the associated VPC
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["default_network_acl_id"] = default_network_acl_id
        __props__["egress"] = egress
        __props__["ingress"] = ingress
        __props__["owner_id"] = owner_id
        __props__["subnet_ids"] = subnet_ids
        __props__["tags"] = tags
        __props__["vpc_id"] = vpc_id
        return DefaultNetworkAcl(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the Default Network ACL
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="defaultNetworkAclId")
    def default_network_acl_id(self) -> pulumi.Output[str]:
        """
        The Network ACL ID to manage. This
        attribute is exported from `ec2.Vpc`, or manually found via the AWS Console.
        """
        return pulumi.get(self, "default_network_acl_id")

    @property
    @pulumi.getter
    def egress(self) -> pulumi.Output[Optional[List['outputs.DefaultNetworkAclEgress']]]:
        """
        Specifies an egress rule. Parameters defined below.
        """
        return pulumi.get(self, "egress")

    @property
    @pulumi.getter
    def ingress(self) -> pulumi.Output[Optional[List['outputs.DefaultNetworkAclIngress']]]:
        """
        Specifies an ingress rule. Parameters defined below.
        """
        return pulumi.get(self, "ingress")

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[str]:
        """
        The ID of the AWS account that owns the Default Network ACL
        """
        return pulumi.get(self, "owner_id")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Optional[List[str]]]:
        """
        A list of Subnet IDs to apply the ACL to. See the
        notes below on managing Subnets in the Default Network ACL
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        The ID of the associated VPC
        """
        return pulumi.get(self, "vpc_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

