# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'TriggerTriggerArgs',
]

@pulumi.input_type
class TriggerTriggerArgs:
    def __init__(__self__, *,
                 destination_arn: pulumi.Input[str],
                 events: pulumi.Input[List[pulumi.Input[str]]],
                 name: pulumi.Input[str],
                 branches: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 custom_data: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] destination_arn: The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in Amazon Simple Notification Service (SNS).
        :param pulumi.Input[List[pulumi.Input[str]]] events: The repository events that will cause the trigger to run actions in another service, such as sending a notification through Amazon Simple Notification Service (SNS). If no events are specified, the trigger will run for all repository events. Event types include: `all`, `updateReference`, `createReference`, `deleteReference`.
        :param pulumi.Input[str] name: The name of the trigger.
        :param pulumi.Input[List[pulumi.Input[str]]] branches: The branches that will be included in the trigger configuration. If no branches are specified, the trigger will apply to all branches.
        :param pulumi.Input[str] custom_data: Any custom data associated with the trigger that will be included in the information sent to the target of the trigger.
        """
        pulumi.set(__self__, "destination_arn", destination_arn)
        pulumi.set(__self__, "events", events)
        pulumi.set(__self__, "name", name)
        if branches is not None:
            pulumi.set(__self__, "branches", branches)
        if custom_data is not None:
            pulumi.set(__self__, "custom_data", custom_data)

    @property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in Amazon Simple Notification Service (SNS).
        """
        return pulumi.get(self, "destination_arn")

    @destination_arn.setter
    def destination_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination_arn", value)

    @property
    @pulumi.getter
    def events(self) -> pulumi.Input[List[pulumi.Input[str]]]:
        """
        The repository events that will cause the trigger to run actions in another service, such as sending a notification through Amazon Simple Notification Service (SNS). If no events are specified, the trigger will run for all repository events. Event types include: `all`, `updateReference`, `createReference`, `deleteReference`.
        """
        return pulumi.get(self, "events")

    @events.setter
    def events(self, value: pulumi.Input[List[pulumi.Input[str]]]):
        pulumi.set(self, "events", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the trigger.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def branches(self) -> Optional[pulumi.Input[List[pulumi.Input[str]]]]:
        """
        The branches that will be included in the trigger configuration. If no branches are specified, the trigger will apply to all branches.
        """
        return pulumi.get(self, "branches")

    @branches.setter
    def branches(self, value: Optional[pulumi.Input[List[pulumi.Input[str]]]]):
        pulumi.set(self, "branches", value)

    @property
    @pulumi.getter(name="customData")
    def custom_data(self) -> Optional[pulumi.Input[str]]:
        """
        Any custom data associated with the trigger that will be included in the information sent to the target of the trigger.
        """
        return pulumi.get(self, "custom_data")

    @custom_data.setter
    def custom_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_data", value)


