# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['Policy']


class Policy(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a resource to manage an [AWS Organizations policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.organizations.Policy("example", content=\"\"\"{
          "Version": "2012-10-17",
          "Statement": {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
          }
        }

        \"\"\")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content: The policy content to add to the new policy. For example, if you create a [service control policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html), this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see the [Service Control Policy Syntax documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html) and for more information on the Tag Policy syntax, see the [Tag Policy Syntax documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_example-tag-policies.html).
        :param pulumi.Input[str] description: A description to assign to the policy.
        :param pulumi.Input[str] name: The friendly name to assign to the policy.
        :param pulumi.Input[str] type: The type of policy to create. Valid values are `BACKUP_POLICY`, `SERVICE_CONTROL_POLICY` (SCP), and `TAG_POLICY`. Defaults to `SERVICE_CONTROL_POLICY`.
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

            if content is None:
                raise TypeError("Missing required property 'content'")
            __props__['content'] = content
            __props__['description'] = description
            __props__['name'] = name
            __props__['type'] = type
            __props__['arn'] = None
        super(Policy, __self__).__init__(
            'aws:organizations/policy:Policy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            content: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Policy':
        """
        Get an existing Policy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the policy.
        :param pulumi.Input[str] content: The policy content to add to the new policy. For example, if you create a [service control policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html), this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see the [Service Control Policy Syntax documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html) and for more information on the Tag Policy syntax, see the [Tag Policy Syntax documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_example-tag-policies.html).
        :param pulumi.Input[str] description: A description to assign to the policy.
        :param pulumi.Input[str] name: The friendly name to assign to the policy.
        :param pulumi.Input[str] type: The type of policy to create. Valid values are `BACKUP_POLICY`, `SERVICE_CONTROL_POLICY` (SCP), and `TAG_POLICY`. Defaults to `SERVICE_CONTROL_POLICY`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["content"] = content
        __props__["description"] = description
        __props__["name"] = name
        __props__["type"] = type
        return Policy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the policy.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[str]:
        """
        The policy content to add to the new policy. For example, if you create a [service control policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html), this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see the [Service Control Policy Syntax documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html) and for more information on the Tag Policy syntax, see the [Tag Policy Syntax documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_example-tag-policies.html).
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description to assign to the policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The friendly name to assign to the policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of policy to create. Valid values are `BACKUP_POLICY`, `SERVICE_CONTROL_POLICY` (SCP), and `TAG_POLICY`. Defaults to `SERVICE_CONTROL_POLICY`.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

