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

__all__ = ['Fleet']


class Fleet(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 excess_capacity_termination_policy: Optional[pulumi.Input[str]] = None,
                 launch_template_config: Optional[pulumi.Input[pulumi.InputType['FleetLaunchTemplateConfigArgs']]] = None,
                 on_demand_options: Optional[pulumi.Input[pulumi.InputType['FleetOnDemandOptionsArgs']]] = None,
                 replace_unhealthy_instances: Optional[pulumi.Input[bool]] = None,
                 spot_options: Optional[pulumi.Input[pulumi.InputType['FleetSpotOptionsArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_capacity_specification: Optional[pulumi.Input[pulumi.InputType['FleetTargetCapacitySpecificationArgs']]] = None,
                 terminate_instances: Optional[pulumi.Input[bool]] = None,
                 terminate_instances_with_expiration: Optional[pulumi.Input[bool]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a resource to manage EC2 Fleets.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2.Fleet("example",
            launch_template_config=aws.ec2.FleetLaunchTemplateConfigArgs(
                launch_template_specification=aws.ec2.FleetLaunchTemplateConfigLaunchTemplateSpecificationArgs(
                    launch_template_id=aws_launch_template["example"]["id"],
                    version=aws_launch_template["example"]["latest_version"],
                ),
            ),
            target_capacity_specification=aws.ec2.FleetTargetCapacitySpecificationArgs(
                default_target_capacity_type="spot",
                total_target_capacity=5,
            ))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] excess_capacity_termination_policy: Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
        :param pulumi.Input[pulumi.InputType['FleetLaunchTemplateConfigArgs']] launch_template_config: Nested argument containing EC2 Launch Template configurations. Defined below.
        :param pulumi.Input[pulumi.InputType['FleetOnDemandOptionsArgs']] on_demand_options: Nested argument containing On-Demand configurations. Defined below.
        :param pulumi.Input[bool] replace_unhealthy_instances: Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
        :param pulumi.Input[pulumi.InputType['FleetSpotOptionsArgs']] spot_options: Nested argument containing Spot configurations. Defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.
        :param pulumi.Input[pulumi.InputType['FleetTargetCapacitySpecificationArgs']] target_capacity_specification: Nested argument containing target capacity configurations. Defined below.
        :param pulumi.Input[bool] terminate_instances: Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
        :param pulumi.Input[bool] terminate_instances_with_expiration: Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
        :param pulumi.Input[str] type: The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
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

            __props__['excess_capacity_termination_policy'] = excess_capacity_termination_policy
            if launch_template_config is None:
                raise TypeError("Missing required property 'launch_template_config'")
            __props__['launch_template_config'] = launch_template_config
            __props__['on_demand_options'] = on_demand_options
            __props__['replace_unhealthy_instances'] = replace_unhealthy_instances
            __props__['spot_options'] = spot_options
            __props__['tags'] = tags
            if target_capacity_specification is None:
                raise TypeError("Missing required property 'target_capacity_specification'")
            __props__['target_capacity_specification'] = target_capacity_specification
            __props__['terminate_instances'] = terminate_instances
            __props__['terminate_instances_with_expiration'] = terminate_instances_with_expiration
            __props__['type'] = type
        super(Fleet, __self__).__init__(
            'aws:ec2/fleet:Fleet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            excess_capacity_termination_policy: Optional[pulumi.Input[str]] = None,
            launch_template_config: Optional[pulumi.Input[pulumi.InputType['FleetLaunchTemplateConfigArgs']]] = None,
            on_demand_options: Optional[pulumi.Input[pulumi.InputType['FleetOnDemandOptionsArgs']]] = None,
            replace_unhealthy_instances: Optional[pulumi.Input[bool]] = None,
            spot_options: Optional[pulumi.Input[pulumi.InputType['FleetSpotOptionsArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            target_capacity_specification: Optional[pulumi.Input[pulumi.InputType['FleetTargetCapacitySpecificationArgs']]] = None,
            terminate_instances: Optional[pulumi.Input[bool]] = None,
            terminate_instances_with_expiration: Optional[pulumi.Input[bool]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Fleet':
        """
        Get an existing Fleet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] excess_capacity_termination_policy: Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
        :param pulumi.Input[pulumi.InputType['FleetLaunchTemplateConfigArgs']] launch_template_config: Nested argument containing EC2 Launch Template configurations. Defined below.
        :param pulumi.Input[pulumi.InputType['FleetOnDemandOptionsArgs']] on_demand_options: Nested argument containing On-Demand configurations. Defined below.
        :param pulumi.Input[bool] replace_unhealthy_instances: Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
        :param pulumi.Input[pulumi.InputType['FleetSpotOptionsArgs']] spot_options: Nested argument containing Spot configurations. Defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.
        :param pulumi.Input[pulumi.InputType['FleetTargetCapacitySpecificationArgs']] target_capacity_specification: Nested argument containing target capacity configurations. Defined below.
        :param pulumi.Input[bool] terminate_instances: Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
        :param pulumi.Input[bool] terminate_instances_with_expiration: Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
        :param pulumi.Input[str] type: The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["excess_capacity_termination_policy"] = excess_capacity_termination_policy
        __props__["launch_template_config"] = launch_template_config
        __props__["on_demand_options"] = on_demand_options
        __props__["replace_unhealthy_instances"] = replace_unhealthy_instances
        __props__["spot_options"] = spot_options
        __props__["tags"] = tags
        __props__["target_capacity_specification"] = target_capacity_specification
        __props__["terminate_instances"] = terminate_instances
        __props__["terminate_instances_with_expiration"] = terminate_instances_with_expiration
        __props__["type"] = type
        return Fleet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="excessCapacityTerminationPolicy")
    def excess_capacity_termination_policy(self) -> pulumi.Output[Optional[str]]:
        """
        Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
        """
        return pulumi.get(self, "excess_capacity_termination_policy")

    @property
    @pulumi.getter(name="launchTemplateConfig")
    def launch_template_config(self) -> pulumi.Output['outputs.FleetLaunchTemplateConfig']:
        """
        Nested argument containing EC2 Launch Template configurations. Defined below.
        """
        return pulumi.get(self, "launch_template_config")

    @property
    @pulumi.getter(name="onDemandOptions")
    def on_demand_options(self) -> pulumi.Output[Optional['outputs.FleetOnDemandOptions']]:
        """
        Nested argument containing On-Demand configurations. Defined below.
        """
        return pulumi.get(self, "on_demand_options")

    @property
    @pulumi.getter(name="replaceUnhealthyInstances")
    def replace_unhealthy_instances(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
        """
        return pulumi.get(self, "replace_unhealthy_instances")

    @property
    @pulumi.getter(name="spotOptions")
    def spot_options(self) -> pulumi.Output[Optional['outputs.FleetSpotOptions']]:
        """
        Nested argument containing Spot configurations. Defined below.
        """
        return pulumi.get(self, "spot_options")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetCapacitySpecification")
    def target_capacity_specification(self) -> pulumi.Output['outputs.FleetTargetCapacitySpecification']:
        """
        Nested argument containing target capacity configurations. Defined below.
        """
        return pulumi.get(self, "target_capacity_specification")

    @property
    @pulumi.getter(name="terminateInstances")
    def terminate_instances(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
        """
        return pulumi.get(self, "terminate_instances")

    @property
    @pulumi.getter(name="terminateInstancesWithExpiration")
    def terminate_instances_with_expiration(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
        """
        return pulumi.get(self, "terminate_instances_with_expiration")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

