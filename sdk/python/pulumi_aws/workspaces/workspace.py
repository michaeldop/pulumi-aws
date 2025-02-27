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

__all__ = ['Workspace']


class Workspace(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bundle_id: Optional[pulumi.Input[str]] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 root_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 user_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 volume_encryption_key: Optional[pulumi.Input[str]] = None,
                 workspace_properties: Optional[pulumi.Input[pulumi.InputType['WorkspaceWorkspacePropertiesArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a workspace in [AWS Workspaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html) Service

        > **NOTE:** During deletion of an `workspaces.Workspace` resource, the service role `workspaces_DefaultRole` must be attached to the
        policy `arn:aws:iam::aws:policy/AmazonWorkSpacesServiceAccess`, or it will leak the ENI that the Workspaces service creates for the Workspace.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        value_windows10 = aws.workspaces.get_bundle(bundle_id="wsb-bh8rsxt14")
        example = aws.workspaces.Workspace("example",
            directory_id=aws_workspaces_directory["example"]["id"],
            bundle_id=value_windows10.id,
            user_name="john.doe",
            root_volume_encryption_enabled=True,
            user_volume_encryption_enabled=True,
            volume_encryption_key="alias/aws/workspaces",
            workspace_properties=aws.workspaces.WorkspaceWorkspacePropertiesArgs(
                compute_type_name="VALUE",
                user_volume_size_gib=10,
                root_volume_size_gib=80,
                running_mode="AUTO_STOP",
                running_mode_auto_stop_timeout_in_minutes=60,
            ),
            tags={
                "Department": "IT",
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bundle_id: The ID of the bundle for the WorkSpace.
        :param pulumi.Input[str] directory_id: The ID of the directory for the WorkSpace.
        :param pulumi.Input[bool] root_volume_encryption_enabled: Indicates whether the data stored on the root volume is encrypted.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags for the WorkSpace.
        :param pulumi.Input[str] user_name: The user name of the user for the WorkSpace. This user name must exist in the directory for the WorkSpace.
        :param pulumi.Input[bool] user_volume_encryption_enabled: Indicates whether the data stored on the user volume is encrypted.
        :param pulumi.Input[str] volume_encryption_key: The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.
        :param pulumi.Input[pulumi.InputType['WorkspaceWorkspacePropertiesArgs']] workspace_properties: The WorkSpace properties.
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

            if bundle_id is None:
                raise TypeError("Missing required property 'bundle_id'")
            __props__['bundle_id'] = bundle_id
            if directory_id is None:
                raise TypeError("Missing required property 'directory_id'")
            __props__['directory_id'] = directory_id
            __props__['root_volume_encryption_enabled'] = root_volume_encryption_enabled
            __props__['tags'] = tags
            if user_name is None:
                raise TypeError("Missing required property 'user_name'")
            __props__['user_name'] = user_name
            __props__['user_volume_encryption_enabled'] = user_volume_encryption_enabled
            __props__['volume_encryption_key'] = volume_encryption_key
            __props__['workspace_properties'] = workspace_properties
            __props__['computer_name'] = None
            __props__['ip_address'] = None
            __props__['state'] = None
        super(Workspace, __self__).__init__(
            'aws:workspaces/workspace:Workspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bundle_id: Optional[pulumi.Input[str]] = None,
            computer_name: Optional[pulumi.Input[str]] = None,
            directory_id: Optional[pulumi.Input[str]] = None,
            ip_address: Optional[pulumi.Input[str]] = None,
            root_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
            state: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            user_name: Optional[pulumi.Input[str]] = None,
            user_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
            volume_encryption_key: Optional[pulumi.Input[str]] = None,
            workspace_properties: Optional[pulumi.Input[pulumi.InputType['WorkspaceWorkspacePropertiesArgs']]] = None) -> 'Workspace':
        """
        Get an existing Workspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bundle_id: The ID of the bundle for the WorkSpace.
        :param pulumi.Input[str] computer_name: The name of the WorkSpace, as seen by the operating system.
        :param pulumi.Input[str] directory_id: The ID of the directory for the WorkSpace.
        :param pulumi.Input[str] ip_address: The IP address of the WorkSpace.
        :param pulumi.Input[bool] root_volume_encryption_enabled: Indicates whether the data stored on the root volume is encrypted.
        :param pulumi.Input[str] state: The operational state of the WorkSpace.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags for the WorkSpace.
        :param pulumi.Input[str] user_name: The user name of the user for the WorkSpace. This user name must exist in the directory for the WorkSpace.
        :param pulumi.Input[bool] user_volume_encryption_enabled: Indicates whether the data stored on the user volume is encrypted.
        :param pulumi.Input[str] volume_encryption_key: The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.
        :param pulumi.Input[pulumi.InputType['WorkspaceWorkspacePropertiesArgs']] workspace_properties: The WorkSpace properties.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["bundle_id"] = bundle_id
        __props__["computer_name"] = computer_name
        __props__["directory_id"] = directory_id
        __props__["ip_address"] = ip_address
        __props__["root_volume_encryption_enabled"] = root_volume_encryption_enabled
        __props__["state"] = state
        __props__["tags"] = tags
        __props__["user_name"] = user_name
        __props__["user_volume_encryption_enabled"] = user_volume_encryption_enabled
        __props__["volume_encryption_key"] = volume_encryption_key
        __props__["workspace_properties"] = workspace_properties
        return Workspace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Output[str]:
        """
        The ID of the bundle for the WorkSpace.
        """
        return pulumi.get(self, "bundle_id")

    @property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> pulumi.Output[str]:
        """
        The name of the WorkSpace, as seen by the operating system.
        """
        return pulumi.get(self, "computer_name")

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Output[str]:
        """
        The ID of the directory for the WorkSpace.
        """
        return pulumi.get(self, "directory_id")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[str]:
        """
        The IP address of the WorkSpace.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="rootVolumeEncryptionEnabled")
    def root_volume_encryption_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the data stored on the root volume is encrypted.
        """
        return pulumi.get(self, "root_volume_encryption_enabled")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The operational state of the WorkSpace.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The tags for the WorkSpace.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[str]:
        """
        The user name of the user for the WorkSpace. This user name must exist in the directory for the WorkSpace.
        """
        return pulumi.get(self, "user_name")

    @property
    @pulumi.getter(name="userVolumeEncryptionEnabled")
    def user_volume_encryption_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the data stored on the user volume is encrypted.
        """
        return pulumi.get(self, "user_volume_encryption_enabled")

    @property
    @pulumi.getter(name="volumeEncryptionKey")
    def volume_encryption_key(self) -> pulumi.Output[Optional[str]]:
        """
        The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.
        """
        return pulumi.get(self, "volume_encryption_key")

    @property
    @pulumi.getter(name="workspaceProperties")
    def workspace_properties(self) -> pulumi.Output['outputs.WorkspaceWorkspaceProperties']:
        """
        The WorkSpace properties.
        """
        return pulumi.get(self, "workspace_properties")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

