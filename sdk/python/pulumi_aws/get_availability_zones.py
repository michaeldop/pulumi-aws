# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = [
    'GetAvailabilityZonesResult',
    'AwaitableGetAvailabilityZonesResult',
    'get_availability_zones',
]

@pulumi.output_type
class GetAvailabilityZonesResult:
    """
    A collection of values returned by getAvailabilityZones.
    """
    def __init__(__self__, all_availability_zones=None, exclude_names=None, exclude_zone_ids=None, filters=None, group_names=None, id=None, names=None, state=None, zone_ids=None):
        if all_availability_zones and not isinstance(all_availability_zones, bool):
            raise TypeError("Expected argument 'all_availability_zones' to be a bool")
        pulumi.set(__self__, "all_availability_zones", all_availability_zones)
        if exclude_names and not isinstance(exclude_names, list):
            raise TypeError("Expected argument 'exclude_names' to be a list")
        pulumi.set(__self__, "exclude_names", exclude_names)
        if exclude_zone_ids and not isinstance(exclude_zone_ids, list):
            raise TypeError("Expected argument 'exclude_zone_ids' to be a list")
        pulumi.set(__self__, "exclude_zone_ids", exclude_zone_ids)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if group_names and not isinstance(group_names, list):
            raise TypeError("Expected argument 'group_names' to be a list")
        pulumi.set(__self__, "group_names", group_names)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if zone_ids and not isinstance(zone_ids, list):
            raise TypeError("Expected argument 'zone_ids' to be a list")
        pulumi.set(__self__, "zone_ids", zone_ids)

    @property
    @pulumi.getter(name="allAvailabilityZones")
    def all_availability_zones(self) -> Optional[bool]:
        return pulumi.get(self, "all_availability_zones")

    @property
    @pulumi.getter(name="excludeNames")
    def exclude_names(self) -> Optional[List[str]]:
        return pulumi.get(self, "exclude_names")

    @property
    @pulumi.getter(name="excludeZoneIds")
    def exclude_zone_ids(self) -> Optional[List[str]]:
        return pulumi.get(self, "exclude_zone_ids")

    @property
    @pulumi.getter
    def filters(self) -> Optional[List['outputs.GetAvailabilityZonesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="groupNames")
    def group_names(self) -> List[str]:
        return pulumi.get(self, "group_names")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def names(self) -> List[str]:
        """
        A list of the Availability Zone names available to the account.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="zoneIds")
    def zone_ids(self) -> List[str]:
        """
        A list of the Availability Zone IDs available to the account.
        """
        return pulumi.get(self, "zone_ids")


class AwaitableGetAvailabilityZonesResult(GetAvailabilityZonesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAvailabilityZonesResult(
            all_availability_zones=self.all_availability_zones,
            exclude_names=self.exclude_names,
            exclude_zone_ids=self.exclude_zone_ids,
            filters=self.filters,
            group_names=self.group_names,
            id=self.id,
            names=self.names,
            state=self.state,
            zone_ids=self.zone_ids)


def get_availability_zones(all_availability_zones: Optional[bool] = None,
                           exclude_names: Optional[List[str]] = None,
                           exclude_zone_ids: Optional[List[str]] = None,
                           filters: Optional[List[pulumi.InputType['GetAvailabilityZonesFilterArgs']]] = None,
                           state: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAvailabilityZonesResult:
    """
    The Availability Zones data source allows access to the list of AWS
    Availability Zones which can be accessed by an AWS account within the region
    configured in the provider.

    This is different from the `getAvailabilityZone` (singular) data source,
    which provides some details about a specific availability zone.

    > When [Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) are enabled in a region, by default the API and this data source include both Local Zones and Availability Zones. To return only Availability Zones, see the example section below.

    ## Example Usage
    ### By State

    ```python
    import pulumi
    import pulumi_aws as aws

    available = aws.get_availability_zones(state="available")
    primary = aws.ec2.Subnet("primary", availability_zone=available.names[0])
    # ...
    secondary = aws.ec2.Subnet("secondary", availability_zone=available.names[1])
    # ...
    ```
    ### By Filter

    All Local Zones (regardless of opt-in status):

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.get_availability_zones(all_availability_zones=True,
        filters=[aws.GetAvailabilityZonesFilterArgs(
            name="opt-in-status",
            values=[
                "not-opted-in",
                "opted-in",
            ],
        )])
    ```

    Only Availability Zones (no Local Zones):

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.get_availability_zones(filters=[aws.GetAvailabilityZonesFilterArgs(
        name="opt-in-status",
        values=["opt-in-not-required"],
    )])
    ```


    :param bool all_availability_zones: Set to `true` to include all Availability Zones and Local Zones regardless of your opt in status.
    :param List[str] exclude_names: List of Availability Zone names to exclude.
    :param List[str] exclude_zone_ids: List of Availability Zone IDs to exclude.
    :param List[pulumi.InputType['GetAvailabilityZonesFilterArgs']] filters: Configuration block(s) for filtering. Detailed below.
    :param str state: Allows to filter list of Availability Zones based on their
           current state. Can be either `"available"`, `"information"`, `"impaired"` or
           `"unavailable"`. By default the list includes a complete set of Availability Zones
           to which the underlying AWS account has access, regardless of their state.
    """
    __args__ = dict()
    __args__['allAvailabilityZones'] = all_availability_zones
    __args__['excludeNames'] = exclude_names
    __args__['excludeZoneIds'] = exclude_zone_ids
    __args__['filters'] = filters
    __args__['state'] = state
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:index/getAvailabilityZones:getAvailabilityZones', __args__, opts=opts, typ=GetAvailabilityZonesResult).value

    return AwaitableGetAvailabilityZonesResult(
        all_availability_zones=__ret__.all_availability_zones,
        exclude_names=__ret__.exclude_names,
        exclude_zone_ids=__ret__.exclude_zone_ids,
        filters=__ret__.filters,
        group_names=__ret__.group_names,
        id=__ret__.id,
        names=__ret__.names,
        state=__ret__.state,
        zone_ids=__ret__.zone_ids)
