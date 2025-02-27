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
    'GetCoipPoolsResult',
    'AwaitableGetCoipPoolsResult',
    'get_coip_pools',
]

@pulumi.output_type
class GetCoipPoolsResult:
    """
    A collection of values returned by getCoipPools.
    """
    def __init__(__self__, filters=None, id=None, pool_ids=None, tags=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if pool_ids and not isinstance(pool_ids, list):
            raise TypeError("Expected argument 'pool_ids' to be a list")
        pulumi.set(__self__, "pool_ids", pool_ids)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def filters(self) -> Optional[List['outputs.GetCoipPoolsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="poolIds")
    def pool_ids(self) -> List[str]:
        """
        Set of COIP Pool Identifiers
        """
        return pulumi.get(self, "pool_ids")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        return pulumi.get(self, "tags")


class AwaitableGetCoipPoolsResult(GetCoipPoolsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCoipPoolsResult(
            filters=self.filters,
            id=self.id,
            pool_ids=self.pool_ids,
            tags=self.tags)


def get_coip_pools(filters: Optional[List[pulumi.InputType['GetCoipPoolsFilterArgs']]] = None,
                   tags: Optional[Mapping[str, str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCoipPoolsResult:
    """
    Provides information for multiple EC2 Customer-Owned IP Pools, such as their identifiers.


    :param List[pulumi.InputType['GetCoipPoolsFilterArgs']] filters: Custom filter block as described below.
    :param Mapping[str, str] tags: A mapping of tags, each pair of which must exactly match
           a pair on the desired aws_ec2_coip_pools.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ec2/getCoipPools:getCoipPools', __args__, opts=opts, typ=GetCoipPoolsResult).value

    return AwaitableGetCoipPoolsResult(
        filters=__ret__.filters,
        id=__ret__.id,
        pool_ids=__ret__.pool_ids,
        tags=__ret__.tags)
