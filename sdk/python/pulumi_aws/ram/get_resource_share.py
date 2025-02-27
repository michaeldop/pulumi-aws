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

__all__ = [
    'GetResourceShareResult',
    'AwaitableGetResourceShareResult',
    'get_resource_share',
]

@pulumi.output_type
class GetResourceShareResult:
    """
    A collection of values returned by getResourceShare.
    """
    def __init__(__self__, arn=None, filters=None, id=None, name=None, owning_account_id=None, resource_owner=None, status=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if owning_account_id and not isinstance(owning_account_id, str):
            raise TypeError("Expected argument 'owning_account_id' to be a str")
        pulumi.set(__self__, "owning_account_id", owning_account_id)
        if resource_owner and not isinstance(resource_owner, str):
            raise TypeError("Expected argument 'resource_owner' to be a str")
        pulumi.set(__self__, "resource_owner", resource_owner)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the resource share.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def filters(self) -> Optional[List['outputs.GetResourceShareFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="owningAccountId")
    def owning_account_id(self) -> str:
        """
        The ID of the AWS account that owns the resource share.
        """
        return pulumi.get(self, "owning_account_id")

    @property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> str:
        return pulumi.get(self, "resource_owner")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The Status of the RAM share.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        The Tags attached to the RAM share
        """
        return pulumi.get(self, "tags")


class AwaitableGetResourceShareResult(GetResourceShareResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourceShareResult(
            arn=self.arn,
            filters=self.filters,
            id=self.id,
            name=self.name,
            owning_account_id=self.owning_account_id,
            resource_owner=self.resource_owner,
            status=self.status,
            tags=self.tags)


def get_resource_share(filters: Optional[List[pulumi.InputType['GetResourceShareFilterArgs']]] = None,
                       name: Optional[str] = None,
                       resource_owner: Optional[str] = None,
                       tags: Optional[Mapping[str, str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourceShareResult:
    """
    `ram.ResourceShare` Retrieve information about a RAM Resource Share.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ram.get_resource_share(name="example",
        resource_owner="SELF")
    ```
    ## Search by filters

    ```python
    import pulumi
    import pulumi_aws as aws

    tag_filter = aws.ram.get_resource_share(filters=[aws.ram.GetResourceShareFilterArgs(
            name="NameOfTag",
            values=["exampleNameTagValue"],
        )],
        name="MyResourceName",
        resource_owner="SELF")
    ```


    :param List[pulumi.InputType['GetResourceShareFilterArgs']] filters: A filter used to scope the list e.g. by tags. See [related docs] (https://docs.aws.amazon.com/ram/latest/APIReference/API_TagFilter.html).
    :param str name: The name of the tag key to filter on.
    :param str resource_owner: The owner of the resource share. Valid values are SELF or OTHER-ACCOUNTS
    :param Mapping[str, str] tags: The Tags attached to the RAM share
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['name'] = name
    __args__['resourceOwner'] = resource_owner
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ram/getResourceShare:getResourceShare', __args__, opts=opts, typ=GetResourceShareResult).value

    return AwaitableGetResourceShareResult(
        arn=__ret__.arn,
        filters=__ret__.filters,
        id=__ret__.id,
        name=__ret__.name,
        owning_account_id=__ret__.owning_account_id,
        resource_owner=__ret__.resource_owner,
        status=__ret__.status,
        tags=__ret__.tags)
