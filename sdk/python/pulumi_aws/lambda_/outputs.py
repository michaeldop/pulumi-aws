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
    'AliasRoutingConfig',
    'EventSourceMappingDestinationConfig',
    'EventSourceMappingDestinationConfigOnFailure',
    'FunctionDeadLetterConfig',
    'FunctionEnvironment',
    'FunctionEventInvokeConfigDestinationConfig',
    'FunctionEventInvokeConfigDestinationConfigOnFailure',
    'FunctionEventInvokeConfigDestinationConfigOnSuccess',
    'FunctionFileSystemConfig',
    'FunctionTracingConfig',
    'FunctionVpcConfig',
    'GetFunctionDeadLetterConfigResult',
    'GetFunctionEnvironmentResult',
    'GetFunctionFileSystemConfigResult',
    'GetFunctionTracingConfigResult',
    'GetFunctionVpcConfigResult',
]

@pulumi.output_type
class AliasRoutingConfig(dict):
    def __init__(__self__, *,
                 additional_version_weights: Optional[Mapping[str, float]] = None):
        """
        :param Mapping[str, float] additional_version_weights: A map that defines the proportion of events that should be sent to different versions of a lambda function.
        """
        if additional_version_weights is not None:
            pulumi.set(__self__, "additional_version_weights", additional_version_weights)

    @property
    @pulumi.getter(name="additionalVersionWeights")
    def additional_version_weights(self) -> Optional[Mapping[str, float]]:
        """
        A map that defines the proportion of events that should be sent to different versions of a lambda function.
        """
        return pulumi.get(self, "additional_version_weights")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EventSourceMappingDestinationConfig(dict):
    def __init__(__self__, *,
                 on_failure: Optional['outputs.EventSourceMappingDestinationConfigOnFailure'] = None):
        """
        :param 'EventSourceMappingDestinationConfigOnFailureArgs' on_failure: The destination configuration for failed invocations. Detailed below.
        """
        if on_failure is not None:
            pulumi.set(__self__, "on_failure", on_failure)

    @property
    @pulumi.getter(name="onFailure")
    def on_failure(self) -> Optional['outputs.EventSourceMappingDestinationConfigOnFailure']:
        """
        The destination configuration for failed invocations. Detailed below.
        """
        return pulumi.get(self, "on_failure")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EventSourceMappingDestinationConfigOnFailure(dict):
    def __init__(__self__, *,
                 destination_arn: str):
        """
        :param str destination_arn: The Amazon Resource Name (ARN) of the destination resource.
        """
        pulumi.set(__self__, "destination_arn", destination_arn)

    @property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the destination resource.
        """
        return pulumi.get(self, "destination_arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FunctionDeadLetterConfig(dict):
    def __init__(__self__, *,
                 target_arn: str):
        """
        :param str target_arn: The ARN of an SNS topic or SQS queue to notify when an invocation fails. If this
               option is used, the function's IAM role must be granted suitable access to write to the target object,
               which means allowing either the `sns:Publish` or `sqs:SendMessage` action on this ARN, depending on
               which service is targeted.
        """
        pulumi.set(__self__, "target_arn", target_arn)

    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> str:
        """
        The ARN of an SNS topic or SQS queue to notify when an invocation fails. If this
        option is used, the function's IAM role must be granted suitable access to write to the target object,
        which means allowing either the `sns:Publish` or `sqs:SendMessage` action on this ARN, depending on
        which service is targeted.
        """
        return pulumi.get(self, "target_arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FunctionEnvironment(dict):
    def __init__(__self__, *,
                 variables: Optional[Mapping[str, str]] = None):
        """
        :param Mapping[str, str] variables: A map that defines environment variables for the Lambda function.
        """
        if variables is not None:
            pulumi.set(__self__, "variables", variables)

    @property
    @pulumi.getter
    def variables(self) -> Optional[Mapping[str, str]]:
        """
        A map that defines environment variables for the Lambda function.
        """
        return pulumi.get(self, "variables")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FunctionEventInvokeConfigDestinationConfig(dict):
    def __init__(__self__, *,
                 on_failure: Optional['outputs.FunctionEventInvokeConfigDestinationConfigOnFailure'] = None,
                 on_success: Optional['outputs.FunctionEventInvokeConfigDestinationConfigOnSuccess'] = None):
        """
        :param 'FunctionEventInvokeConfigDestinationConfigOnFailureArgs' on_failure: Configuration block with destination configuration for failed asynchronous invocations. See below for details.
        :param 'FunctionEventInvokeConfigDestinationConfigOnSuccessArgs' on_success: Configuration block with destination configuration for successful asynchronous invocations. See below for details.
        """
        if on_failure is not None:
            pulumi.set(__self__, "on_failure", on_failure)
        if on_success is not None:
            pulumi.set(__self__, "on_success", on_success)

    @property
    @pulumi.getter(name="onFailure")
    def on_failure(self) -> Optional['outputs.FunctionEventInvokeConfigDestinationConfigOnFailure']:
        """
        Configuration block with destination configuration for failed asynchronous invocations. See below for details.
        """
        return pulumi.get(self, "on_failure")

    @property
    @pulumi.getter(name="onSuccess")
    def on_success(self) -> Optional['outputs.FunctionEventInvokeConfigDestinationConfigOnSuccess']:
        """
        Configuration block with destination configuration for successful asynchronous invocations. See below for details.
        """
        return pulumi.get(self, "on_success")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FunctionEventInvokeConfigDestinationConfigOnFailure(dict):
    def __init__(__self__, *,
                 destination: str):
        """
        :param str destination: Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
        """
        pulumi.set(__self__, "destination", destination)

    @property
    @pulumi.getter
    def destination(self) -> str:
        """
        Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
        """
        return pulumi.get(self, "destination")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FunctionEventInvokeConfigDestinationConfigOnSuccess(dict):
    def __init__(__self__, *,
                 destination: str):
        """
        :param str destination: Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
        """
        pulumi.set(__self__, "destination", destination)

    @property
    @pulumi.getter
    def destination(self) -> str:
        """
        Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
        """
        return pulumi.get(self, "destination")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FunctionFileSystemConfig(dict):
    def __init__(__self__, *,
                 arn: str,
                 local_mount_path: str):
        """
        :param str arn: The Amazon Resource Name (ARN) of the Amazon EFS Access Point that provides access to the file system.
        :param str local_mount_path: The path where the function can access the file system, starting with /mnt/.
        """
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "local_mount_path", local_mount_path)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the Amazon EFS Access Point that provides access to the file system.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="localMountPath")
    def local_mount_path(self) -> str:
        """
        The path where the function can access the file system, starting with /mnt/.
        """
        return pulumi.get(self, "local_mount_path")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FunctionTracingConfig(dict):
    def __init__(__self__, *,
                 mode: str):
        """
        :param str mode: Can be either `PassThrough` or `Active`. If PassThrough, Lambda will only trace
               the request from an upstream service if it contains a tracing header with
               "sampled=1". If Active, Lambda will respect any tracing header it receives
               from an upstream service. If no tracing header is received, Lambda will call
               X-Ray for a tracing decision.
        """
        pulumi.set(__self__, "mode", mode)

    @property
    @pulumi.getter
    def mode(self) -> str:
        """
        Can be either `PassThrough` or `Active`. If PassThrough, Lambda will only trace
        the request from an upstream service if it contains a tracing header with
        "sampled=1". If Active, Lambda will respect any tracing header it receives
        from an upstream service. If no tracing header is received, Lambda will call
        X-Ray for a tracing decision.
        """
        return pulumi.get(self, "mode")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FunctionVpcConfig(dict):
    def __init__(__self__, *,
                 security_group_ids: List[str],
                 subnet_ids: List[str],
                 vpc_id: Optional[str] = None):
        """
        :param List[str] security_group_ids: A list of security group IDs associated with the Lambda function.
        :param List[str] subnet_ids: A list of subnet IDs associated with the Lambda function.
        """
        pulumi.set(__self__, "security_group_ids", security_group_ids)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> List[str]:
        """
        A list of security group IDs associated with the Lambda function.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> List[str]:
        """
        A list of subnet IDs associated with the Lambda function.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[str]:
        return pulumi.get(self, "vpc_id")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetFunctionDeadLetterConfigResult(dict):
    def __init__(__self__, *,
                 target_arn: str):
        pulumi.set(__self__, "target_arn", target_arn)

    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> str:
        return pulumi.get(self, "target_arn")


@pulumi.output_type
class GetFunctionEnvironmentResult(dict):
    def __init__(__self__, *,
                 variables: Mapping[str, str]):
        pulumi.set(__self__, "variables", variables)

    @property
    @pulumi.getter
    def variables(self) -> Mapping[str, str]:
        return pulumi.get(self, "variables")


@pulumi.output_type
class GetFunctionFileSystemConfigResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 local_mount_path: str):
        """
        :param str arn: Unqualified (no `:QUALIFIER` or `:VERSION` suffix) Amazon Resource Name (ARN) identifying your Lambda Function. See also `qualified_arn`.
        """
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "local_mount_path", local_mount_path)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        Unqualified (no `:QUALIFIER` or `:VERSION` suffix) Amazon Resource Name (ARN) identifying your Lambda Function. See also `qualified_arn`.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="localMountPath")
    def local_mount_path(self) -> str:
        return pulumi.get(self, "local_mount_path")


@pulumi.output_type
class GetFunctionTracingConfigResult(dict):
    def __init__(__self__, *,
                 mode: str):
        pulumi.set(__self__, "mode", mode)

    @property
    @pulumi.getter
    def mode(self) -> str:
        return pulumi.get(self, "mode")


@pulumi.output_type
class GetFunctionVpcConfigResult(dict):
    def __init__(__self__, *,
                 security_group_ids: List[str],
                 subnet_ids: List[str],
                 vpc_id: str):
        pulumi.set(__self__, "security_group_ids", security_group_ids)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> List[str]:
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> List[str]:
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        return pulumi.get(self, "vpc_id")


