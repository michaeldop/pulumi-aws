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

__all__ = ['DeploymentConfig']


class DeploymentConfig(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compute_platform: Optional[pulumi.Input[str]] = None,
                 deployment_config_name: Optional[pulumi.Input[str]] = None,
                 minimum_healthy_hosts: Optional[pulumi.Input[pulumi.InputType['DeploymentConfigMinimumHealthyHostsArgs']]] = None,
                 traffic_routing_config: Optional[pulumi.Input[pulumi.InputType['DeploymentConfigTrafficRoutingConfigArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a CodeDeploy deployment config for an application

        ## Example Usage
        ### Server Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        foo_deployment_config = aws.codedeploy.DeploymentConfig("fooDeploymentConfig",
            deployment_config_name="test-deployment-config",
            minimum_healthy_hosts=aws.codedeploy.DeploymentConfigMinimumHealthyHostsArgs(
                type="HOST_COUNT",
                value=2,
            ))
        foo_deployment_group = aws.codedeploy.DeploymentGroup("fooDeploymentGroup",
            app_name=aws_codedeploy_app["foo_app"]["name"],
            deployment_group_name="bar",
            service_role_arn=aws_iam_role["foo_role"]["arn"],
            deployment_config_name=foo_deployment_config.id,
            ec2_tag_filters=[aws.codedeploy.DeploymentGroupEc2TagFilterArgs(
                key="filterkey",
                type="KEY_AND_VALUE",
                value="filtervalue",
            )],
            trigger_configurations=[aws.codedeploy.DeploymentGroupTriggerConfigurationArgs(
                trigger_events=["DeploymentFailure"],
                trigger_name="foo-trigger",
                trigger_target_arn="foo-topic-arn",
            )],
            auto_rollback_configuration=aws.codedeploy.DeploymentGroupAutoRollbackConfigurationArgs(
                enabled=True,
                events=["DEPLOYMENT_FAILURE"],
            ),
            alarm_configuration=aws.codedeploy.DeploymentGroupAlarmConfigurationArgs(
                alarms=["my-alarm-name"],
                enabled=True,
            ))
        ```
        ### Lambda Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        foo_deployment_config = aws.codedeploy.DeploymentConfig("fooDeploymentConfig",
            deployment_config_name="test-deployment-config",
            compute_platform="Lambda",
            traffic_routing_config=aws.codedeploy.DeploymentConfigTrafficRoutingConfigArgs(
                type="TimeBasedLinear",
                time_based_linear=aws.codedeploy.DeploymentConfigTrafficRoutingConfigTimeBasedLinearArgs(
                    interval=10,
                    percentage=10,
                ),
            ))
        foo_deployment_group = aws.codedeploy.DeploymentGroup("fooDeploymentGroup",
            app_name=aws_codedeploy_app["foo_app"]["name"],
            deployment_group_name="bar",
            service_role_arn=aws_iam_role["foo_role"]["arn"],
            deployment_config_name=foo_deployment_config.id,
            auto_rollback_configuration=aws.codedeploy.DeploymentGroupAutoRollbackConfigurationArgs(
                enabled=True,
                events=["DEPLOYMENT_STOP_ON_ALARM"],
            ),
            alarm_configuration=aws.codedeploy.DeploymentGroupAlarmConfigurationArgs(
                alarms=["my-alarm-name"],
                enabled=True,
            ))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_platform: The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
        :param pulumi.Input[str] deployment_config_name: The name of the deployment config.
        :param pulumi.Input[pulumi.InputType['DeploymentConfigMinimumHealthyHostsArgs']] minimum_healthy_hosts: A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
        :param pulumi.Input[pulumi.InputType['DeploymentConfigTrafficRoutingConfigArgs']] traffic_routing_config: A traffic_routing_config block. Traffic Routing Config is documented below.
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

            __props__['compute_platform'] = compute_platform
            if deployment_config_name is None:
                raise TypeError("Missing required property 'deployment_config_name'")
            __props__['deployment_config_name'] = deployment_config_name
            __props__['minimum_healthy_hosts'] = minimum_healthy_hosts
            __props__['traffic_routing_config'] = traffic_routing_config
            __props__['deployment_config_id'] = None
        super(DeploymentConfig, __self__).__init__(
            'aws:codedeploy/deploymentConfig:DeploymentConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compute_platform: Optional[pulumi.Input[str]] = None,
            deployment_config_id: Optional[pulumi.Input[str]] = None,
            deployment_config_name: Optional[pulumi.Input[str]] = None,
            minimum_healthy_hosts: Optional[pulumi.Input[pulumi.InputType['DeploymentConfigMinimumHealthyHostsArgs']]] = None,
            traffic_routing_config: Optional[pulumi.Input[pulumi.InputType['DeploymentConfigTrafficRoutingConfigArgs']]] = None) -> 'DeploymentConfig':
        """
        Get an existing DeploymentConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_platform: The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
        :param pulumi.Input[str] deployment_config_id: The AWS Assigned deployment config id
        :param pulumi.Input[str] deployment_config_name: The name of the deployment config.
        :param pulumi.Input[pulumi.InputType['DeploymentConfigMinimumHealthyHostsArgs']] minimum_healthy_hosts: A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
        :param pulumi.Input[pulumi.InputType['DeploymentConfigTrafficRoutingConfigArgs']] traffic_routing_config: A traffic_routing_config block. Traffic Routing Config is documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["compute_platform"] = compute_platform
        __props__["deployment_config_id"] = deployment_config_id
        __props__["deployment_config_name"] = deployment_config_name
        __props__["minimum_healthy_hosts"] = minimum_healthy_hosts
        __props__["traffic_routing_config"] = traffic_routing_config
        return DeploymentConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="computePlatform")
    def compute_platform(self) -> pulumi.Output[Optional[str]]:
        """
        The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
        """
        return pulumi.get(self, "compute_platform")

    @property
    @pulumi.getter(name="deploymentConfigId")
    def deployment_config_id(self) -> pulumi.Output[str]:
        """
        The AWS Assigned deployment config id
        """
        return pulumi.get(self, "deployment_config_id")

    @property
    @pulumi.getter(name="deploymentConfigName")
    def deployment_config_name(self) -> pulumi.Output[str]:
        """
        The name of the deployment config.
        """
        return pulumi.get(self, "deployment_config_name")

    @property
    @pulumi.getter(name="minimumHealthyHosts")
    def minimum_healthy_hosts(self) -> pulumi.Output[Optional['outputs.DeploymentConfigMinimumHealthyHosts']]:
        """
        A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
        """
        return pulumi.get(self, "minimum_healthy_hosts")

    @property
    @pulumi.getter(name="trafficRoutingConfig")
    def traffic_routing_config(self) -> pulumi.Output[Optional['outputs.DeploymentConfigTrafficRoutingConfig']]:
        """
        A traffic_routing_config block. Traffic Routing Config is documented below.
        """
        return pulumi.get(self, "traffic_routing_config")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

