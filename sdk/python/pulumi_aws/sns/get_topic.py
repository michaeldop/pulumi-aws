# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetTopicResult',
    'AwaitableGetTopicResult',
    'get_topic',
]

@pulumi.output_type
class GetTopicResult:
    """
    A collection of values returned by getTopic.
    """
    def __init__(__self__, arn=None, id=None, name=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        Set to the ARN of the found topic, suitable for referencing in other resources that support SNS topics.
        """
        return pulumi.get(self, "arn")

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


class AwaitableGetTopicResult(GetTopicResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTopicResult(
            arn=self.arn,
            id=self.id,
            name=self.name)


def get_topic(name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTopicResult:
    """
    Use this data source to get the ARN of a topic in AWS Simple Notification
    Service (SNS). By using this data source, you can reference SNS topics
    without having to hard code the ARNs as input.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.sns.get_topic(name="an_example_topic")
    ```


    :param str name: The friendly name of the topic to match.
    """
    __args__ = dict()
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:sns/getTopic:getTopic', __args__, opts=opts, typ=GetTopicResult).value

    return AwaitableGetTopicResult(
        arn=__ret__.arn,
        id=__ret__.id,
        name=__ret__.name)
