# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'GetDirectoryResult',
    'AwaitableGetDirectoryResult',
    'get_directory',
]

@pulumi.output_type
class GetDirectoryResult:
    """
    A collection of values returned by getDirectory.
    """
    def __init__(__self__, alias=None, customer_user_name=None, directory_id=None, directory_name=None, directory_type=None, dns_ip_addresses=None, iam_role_id=None, id=None, ip_group_ids=None, registration_code=None, self_service_permissions=None, subnet_ids=None, tags=None, workspace_security_group_id=None):
        if alias and not isinstance(alias, str):
            raise TypeError("Expected argument 'alias' to be a str")
        pulumi.set(__self__, "alias", alias)
        if customer_user_name and not isinstance(customer_user_name, str):
            raise TypeError("Expected argument 'customer_user_name' to be a str")
        pulumi.set(__self__, "customer_user_name", customer_user_name)
        if directory_id and not isinstance(directory_id, str):
            raise TypeError("Expected argument 'directory_id' to be a str")
        pulumi.set(__self__, "directory_id", directory_id)
        if directory_name and not isinstance(directory_name, str):
            raise TypeError("Expected argument 'directory_name' to be a str")
        pulumi.set(__self__, "directory_name", directory_name)
        if directory_type and not isinstance(directory_type, str):
            raise TypeError("Expected argument 'directory_type' to be a str")
        pulumi.set(__self__, "directory_type", directory_type)
        if dns_ip_addresses and not isinstance(dns_ip_addresses, list):
            raise TypeError("Expected argument 'dns_ip_addresses' to be a list")
        pulumi.set(__self__, "dns_ip_addresses", dns_ip_addresses)
        if iam_role_id and not isinstance(iam_role_id, str):
            raise TypeError("Expected argument 'iam_role_id' to be a str")
        pulumi.set(__self__, "iam_role_id", iam_role_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_group_ids and not isinstance(ip_group_ids, list):
            raise TypeError("Expected argument 'ip_group_ids' to be a list")
        pulumi.set(__self__, "ip_group_ids", ip_group_ids)
        if registration_code and not isinstance(registration_code, str):
            raise TypeError("Expected argument 'registration_code' to be a str")
        pulumi.set(__self__, "registration_code", registration_code)
        if self_service_permissions and not isinstance(self_service_permissions, list):
            raise TypeError("Expected argument 'self_service_permissions' to be a list")
        pulumi.set(__self__, "self_service_permissions", self_service_permissions)
        if subnet_ids and not isinstance(subnet_ids, list):
            raise TypeError("Expected argument 'subnet_ids' to be a list")
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if workspace_security_group_id and not isinstance(workspace_security_group_id, str):
            raise TypeError("Expected argument 'workspace_security_group_id' to be a str")
        pulumi.set(__self__, "workspace_security_group_id", workspace_security_group_id)

    @property
    @pulumi.getter
    def alias(self) -> str:
        """
        The directory alias.
        """
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter(name="customerUserName")
    def customer_user_name(self) -> str:
        """
        The user name for the service account.
        """
        return pulumi.get(self, "customer_user_name")

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> str:
        return pulumi.get(self, "directory_id")

    @property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> str:
        """
        The name of the directory.
        """
        return pulumi.get(self, "directory_name")

    @property
    @pulumi.getter(name="directoryType")
    def directory_type(self) -> str:
        """
        The directory type.
        """
        return pulumi.get(self, "directory_type")

    @property
    @pulumi.getter(name="dnsIpAddresses")
    def dns_ip_addresses(self) -> List[str]:
        """
        The IP addresses of the DNS servers for the directory.
        """
        return pulumi.get(self, "dns_ip_addresses")

    @property
    @pulumi.getter(name="iamRoleId")
    def iam_role_id(self) -> str:
        """
        The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.
        """
        return pulumi.get(self, "iam_role_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipGroupIds")
    def ip_group_ids(self) -> List[str]:
        """
        The identifiers of the IP access control groups associated with the directory.
        """
        return pulumi.get(self, "ip_group_ids")

    @property
    @pulumi.getter(name="registrationCode")
    def registration_code(self) -> str:
        """
        The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.
        """
        return pulumi.get(self, "registration_code")

    @property
    @pulumi.getter(name="selfServicePermissions")
    def self_service_permissions(self) -> List['outputs.GetDirectorySelfServicePermissionResult']:
        """
        The permissions to enable or disable self-service capabilities.
        """
        return pulumi.get(self, "self_service_permissions")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> List[str]:
        """
        The identifiers of the subnets where the directory resides.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        A map of tags assigned to the WorkSpaces directory.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="workspaceSecurityGroupId")
    def workspace_security_group_id(self) -> str:
        """
        The identifier of the security group that is assigned to new WorkSpaces.
        """
        return pulumi.get(self, "workspace_security_group_id")


class AwaitableGetDirectoryResult(GetDirectoryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDirectoryResult(
            alias=self.alias,
            customer_user_name=self.customer_user_name,
            directory_id=self.directory_id,
            directory_name=self.directory_name,
            directory_type=self.directory_type,
            dns_ip_addresses=self.dns_ip_addresses,
            iam_role_id=self.iam_role_id,
            id=self.id,
            ip_group_ids=self.ip_group_ids,
            registration_code=self.registration_code,
            self_service_permissions=self.self_service_permissions,
            subnet_ids=self.subnet_ids,
            tags=self.tags,
            workspace_security_group_id=self.workspace_security_group_id)


def get_directory(directory_id: Optional[str] = None,
                  tags: Optional[Mapping[str, str]] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDirectoryResult:
    """
    Retrieve information about an AWS WorkSpaces directory.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.workspaces.get_directory(directory_id="d-9067783251")
    ```


    :param str directory_id: The directory identifier for registration in WorkSpaces service.
    :param Mapping[str, str] tags: A map of tags assigned to the WorkSpaces directory.
    """
    __args__ = dict()
    __args__['directoryId'] = directory_id
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:workspaces/getDirectory:getDirectory', __args__, opts=opts, typ=GetDirectoryResult).value

    return AwaitableGetDirectoryResult(
        alias=__ret__.alias,
        customer_user_name=__ret__.customer_user_name,
        directory_id=__ret__.directory_id,
        directory_name=__ret__.directory_name,
        directory_type=__ret__.directory_type,
        dns_ip_addresses=__ret__.dns_ip_addresses,
        iam_role_id=__ret__.iam_role_id,
        id=__ret__.id,
        ip_group_ids=__ret__.ip_group_ids,
        registration_code=__ret__.registration_code,
        self_service_permissions=__ret__.self_service_permissions,
        subnet_ids=__ret__.subnet_ids,
        tags=__ret__.tags,
        workspace_security_group_id=__ret__.workspace_security_group_id)
