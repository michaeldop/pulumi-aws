# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['StackSet']


class StackSet(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administration_role_arn: Optional[pulumi.Input[str]] = None,
                 capabilities: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 execution_role_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 template_body: Optional[pulumi.Input[str]] = None,
                 template_url: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a CloudFormation StackSet. StackSets allow CloudFormation templates to be easily deployed across multiple accounts and regions via StackSet Instances (`cloudformation.StackSetInstance` resource). Additional information about StackSets can be found in the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html).

        > **NOTE:** All template parameters, including those with a `Default`, must be configured or ignored with the `lifecycle` configuration block `ignore_changes` argument.

        > **NOTE:** All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignore_changes` argument.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        a_ws_cloud_formation_stack_set_administration_role_assume_role_policy = aws.iam.get_policy_document(statements=[aws.iam.GetPolicyDocumentStatementArgs(
            actions=["sts:AssumeRole"],
            effect="Allow",
            principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                identifiers=["cloudformation.amazonaws.com"],
                type="Service",
            )],
        )])
        a_ws_cloud_formation_stack_set_administration_role = aws.iam.Role("aWSCloudFormationStackSetAdministrationRole", assume_role_policy=a_ws_cloud_formation_stack_set_administration_role_assume_role_policy.json)
        example = aws.cloudformation.StackSet("example",
            administration_role_arn=a_ws_cloud_formation_stack_set_administration_role.arn,
            parameters={
                "VPCCidr": "10.0.0.0/16",
            },
            template_body=\"\"\"{
          "Parameters" : {
            "VPCCidr" : {
              "Type" : "String",
              "Default" : "10.0.0.0/16",
              "Description" : "Enter the CIDR block for the VPC. Default is 10.0.0.0/16."
            }
          },
          "Resources" : {
            "myVpc": {
              "Type" : "AWS::EC2::VPC",
              "Properties" : {
                "CidrBlock" : { "Ref" : "VPCCidr" },
                "Tags" : [
                  {"Key": "Name", "Value": "Primary_CF_VPC"}
                ]
              }
            }
          }
        }
        \"\"\")
        a_ws_cloud_formation_stack_set_administration_role_execution_policy_policy_document = example.execution_role_name.apply(lambda execution_role_name: aws.iam.get_policy_document(statements=[aws.iam.GetPolicyDocumentStatementArgs(
            actions=["sts:AssumeRole"],
            effect="Allow",
            resources=[f"arn:aws:iam::*:role/{execution_role_name}"],
        )]))
        a_ws_cloud_formation_stack_set_administration_role_execution_policy_role_policy = aws.iam.RolePolicy("aWSCloudFormationStackSetAdministrationRoleExecutionPolicyRolePolicy",
            policy=a_ws_cloud_formation_stack_set_administration_role_execution_policy_policy_document.json,
            role=a_ws_cloud_formation_stack_set_administration_role.name)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] administration_role_arn: Amazon Resource Number (ARN) of the IAM Role in the administrator account.
        :param pulumi.Input[List[pulumi.Input[str]]] capabilities: A list of capabilities. Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPABILITY_AUTO_EXPAND`.
        :param pulumi.Input[str] description: Description of the StackSet.
        :param pulumi.Input[str] execution_role_name: Name of the IAM Role in all target accounts for StackSet operations. Defaults to `AWSCloudFormationStackSetExecutionRole`.
        :param pulumi.Input[str] name: Name of the StackSet. The name must be unique in the region where you create your StackSet. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: Key-value map of input parameters for the StackSet template. All template parameters, including those with a `Default`, must be configured or ignored with `lifecycle` configuration block `ignore_changes` argument. All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignore_changes` argument.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags to associate with this StackSet and the Stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the Stacks. A maximum number of 50 tags can be specified.
        :param pulumi.Input[str] template_body: String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts with `template_url`.
        :param pulumi.Input[str] template_url: String containing the location of a file containing the CloudFormation template body. The URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 460,800 bytes. Conflicts with `template_body`.
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

            if administration_role_arn is None:
                raise TypeError("Missing required property 'administration_role_arn'")
            __props__['administration_role_arn'] = administration_role_arn
            __props__['capabilities'] = capabilities
            __props__['description'] = description
            __props__['execution_role_name'] = execution_role_name
            __props__['name'] = name
            __props__['parameters'] = parameters
            __props__['tags'] = tags
            __props__['template_body'] = template_body
            __props__['template_url'] = template_url
            __props__['arn'] = None
            __props__['stack_set_id'] = None
        super(StackSet, __self__).__init__(
            'aws:cloudformation/stackSet:StackSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            administration_role_arn: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            capabilities: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            execution_role_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            stack_set_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            template_body: Optional[pulumi.Input[str]] = None,
            template_url: Optional[pulumi.Input[str]] = None) -> 'StackSet':
        """
        Get an existing StackSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] administration_role_arn: Amazon Resource Number (ARN) of the IAM Role in the administrator account.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the StackSet.
        :param pulumi.Input[List[pulumi.Input[str]]] capabilities: A list of capabilities. Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPABILITY_AUTO_EXPAND`.
        :param pulumi.Input[str] description: Description of the StackSet.
        :param pulumi.Input[str] execution_role_name: Name of the IAM Role in all target accounts for StackSet operations. Defaults to `AWSCloudFormationStackSetExecutionRole`.
        :param pulumi.Input[str] name: Name of the StackSet. The name must be unique in the region where you create your StackSet. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: Key-value map of input parameters for the StackSet template. All template parameters, including those with a `Default`, must be configured or ignored with `lifecycle` configuration block `ignore_changes` argument. All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignore_changes` argument.
        :param pulumi.Input[str] stack_set_id: Unique identifier of the StackSet.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags to associate with this StackSet and the Stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the Stacks. A maximum number of 50 tags can be specified.
        :param pulumi.Input[str] template_body: String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts with `template_url`.
        :param pulumi.Input[str] template_url: String containing the location of a file containing the CloudFormation template body. The URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 460,800 bytes. Conflicts with `template_body`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["administration_role_arn"] = administration_role_arn
        __props__["arn"] = arn
        __props__["capabilities"] = capabilities
        __props__["description"] = description
        __props__["execution_role_name"] = execution_role_name
        __props__["name"] = name
        __props__["parameters"] = parameters
        __props__["stack_set_id"] = stack_set_id
        __props__["tags"] = tags
        __props__["template_body"] = template_body
        __props__["template_url"] = template_url
        return StackSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administrationRoleArn")
    def administration_role_arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Number (ARN) of the IAM Role in the administrator account.
        """
        return pulumi.get(self, "administration_role_arn")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the StackSet.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def capabilities(self) -> pulumi.Output[Optional[List[str]]]:
        """
        A list of capabilities. Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPABILITY_AUTO_EXPAND`.
        """
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the StackSet.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="executionRoleName")
    def execution_role_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the IAM Role in all target accounts for StackSet operations. Defaults to `AWSCloudFormationStackSetExecutionRole`.
        """
        return pulumi.get(self, "execution_role_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the StackSet. The name must be unique in the region where you create your StackSet. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of input parameters for the StackSet template. All template parameters, including those with a `Default`, must be configured or ignored with `lifecycle` configuration block `ignore_changes` argument. All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignore_changes` argument.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="stackSetId")
    def stack_set_id(self) -> pulumi.Output[str]:
        """
        Unique identifier of the StackSet.
        """
        return pulumi.get(self, "stack_set_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of tags to associate with this StackSet and the Stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the Stacks. A maximum number of 50 tags can be specified.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> pulumi.Output[str]:
        """
        String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts with `template_url`.
        """
        return pulumi.get(self, "template_body")

    @property
    @pulumi.getter(name="templateUrl")
    def template_url(self) -> pulumi.Output[Optional[str]]:
        """
        String containing the location of a file containing the CloudFormation template body. The URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 460,800 bytes. Conflicts with `template_body`.
        """
        return pulumi.get(self, "template_url")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

