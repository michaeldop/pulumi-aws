# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetIpsetResult',
    'AwaitableGetIpsetResult',
    'get_ipset',
]

@pulumi.output_type
class GetIpsetResult:
    """
    A collection of values returned by getIpset.
    """
    def __init__(__self__, id=None, name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

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


class AwaitableGetIpsetResult(GetIpsetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIpsetResult(
            id=self.id,
            name=self.name)


def get_ipset(name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIpsetResult:
    """
    `wafregional.IpSet` Retrieves a WAF Regional IP Set Resource Id.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.wafregional.get_ipset(name="tfWAFRegionalIPSet")
    ```


    :param str name: The name of the WAF Regional IP set.
    """
    __args__ = dict()
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:wafregional/getIpset:getIpset', __args__, opts=opts, typ=GetIpsetResult).value

    return AwaitableGetIpsetResult(
        id=__ret__.id,
        name=__ret__.name)
