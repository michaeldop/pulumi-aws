# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetEbsVolumesFilterResult',
    'GetSnapshotFilterResult',
    'GetSnapshotIdsFilterResult',
    'GetVolumeFilterResult',
]

@pulumi.output_type
class GetEbsVolumesFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: List[str]):
        """
        :param str name: The name of the field to filter by, as defined by
               [the underlying AWS API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumes.html).
               For example, if matching against the `size` filter, use:
        :param List[str] values: Set of values that are accepted for the given field.
               EBS Volume IDs will be selected if any one of the given values match.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the field to filter by, as defined by
        [the underlying AWS API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumes.html).
        For example, if matching against the `size` filter, use:
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        """
        Set of values that are accepted for the given field.
        EBS Volume IDs will be selected if any one of the given values match.
        """
        return pulumi.get(self, "values")


@pulumi.output_type
class GetSnapshotFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: List[str]):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        return pulumi.get(self, "values")


@pulumi.output_type
class GetSnapshotIdsFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: List[str]):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        return pulumi.get(self, "values")


@pulumi.output_type
class GetVolumeFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: List[str]):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        return pulumi.get(self, "values")


