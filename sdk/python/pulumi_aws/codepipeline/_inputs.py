# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'PipelineArtifactStoreArgs',
    'PipelineArtifactStoreEncryptionKeyArgs',
    'PipelineStageArgs',
    'PipelineStageActionArgs',
    'WebhookAuthenticationConfigurationArgs',
    'WebhookFilterArgs',
]

@pulumi.input_type
class PipelineArtifactStoreArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 type: pulumi.Input[str],
                 encryption_key: Optional[pulumi.Input['PipelineArtifactStoreEncryptionKeyArgs']] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] location: The location where AWS CodePipeline stores artifacts for a pipeline; currently only `S3` is supported.
        :param pulumi.Input[str] type: The type of the artifact store, such as Amazon S3
        :param pulumi.Input['PipelineArtifactStoreEncryptionKeyArgs'] encryption_key: The encryption key block AWS CodePipeline uses to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If you don't specify a key, AWS CodePipeline uses the default key for Amazon Simple Storage Service (Amazon S3). An `encryption_key` block is documented below.
        :param pulumi.Input[str] region: The region where the artifact store is located. Required for a cross-region CodePipeline, do not provide for a single-region CodePipeline.
        """
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "type", type)
        if encryption_key is not None:
            pulumi.set(__self__, "encryption_key", encryption_key)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The location where AWS CodePipeline stores artifacts for a pipeline; currently only `S3` is supported.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of the artifact store, such as Amazon S3
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[pulumi.Input['PipelineArtifactStoreEncryptionKeyArgs']]:
        """
        The encryption key block AWS CodePipeline uses to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If you don't specify a key, AWS CodePipeline uses the default key for Amazon Simple Storage Service (Amazon S3). An `encryption_key` block is documented below.
        """
        return pulumi.get(self, "encryption_key")

    @encryption_key.setter
    def encryption_key(self, value: Optional[pulumi.Input['PipelineArtifactStoreEncryptionKeyArgs']]):
        pulumi.set(self, "encryption_key", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region where the artifact store is located. Required for a cross-region CodePipeline, do not provide for a single-region CodePipeline.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class PipelineArtifactStoreEncryptionKeyArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[str] id: The KMS key ARN or ID
        :param pulumi.Input[str] type: The type of key; currently only `KMS` is supported
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        The KMS key ARN or ID
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of key; currently only `KMS` is supported
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class PipelineStageArgs:
    def __init__(__self__, *,
                 actions: pulumi.Input[List[pulumi.Input['PipelineStageActionArgs']]],
                 name: pulumi.Input[str]):
        """
        :param pulumi.Input[List[pulumi.Input['PipelineStageActionArgs']]] actions: The action(s) to include in the stage. Defined as an `action` block below
        :param pulumi.Input[str] name: The name of the stage.
        """
        pulumi.set(__self__, "actions", actions)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Input[List[pulumi.Input['PipelineStageActionArgs']]]:
        """
        The action(s) to include in the stage. Defined as an `action` block below
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: pulumi.Input[List[pulumi.Input['PipelineStageActionArgs']]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the stage.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class PipelineStageActionArgs:
    def __init__(__self__, *,
                 category: pulumi.Input[str],
                 name: pulumi.Input[str],
                 owner: pulumi.Input[str],
                 provider: pulumi.Input[str],
                 version: pulumi.Input[str],
                 configuration: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 input_artifacts: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 output_artifacts: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 run_order: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[str] category: A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Possible values are `Approval`, `Build`, `Deploy`, `Invoke`, `Source` and `Test`.
        :param pulumi.Input[str] name: The action declaration's name.
        :param pulumi.Input[str] owner: The creator of the action being called. Possible values are `AWS`, `Custom` and `ThirdParty`.
        :param pulumi.Input[str] provider: The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
        :param pulumi.Input[str] version: A string that identifies the action type.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] configuration: A map of the action declaration's configuration. Configurations options for action types and providers can be found in the [Pipeline Structure Reference](http://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements) and [Action Structure Reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference.html) documentation.
        :param pulumi.Input[List[pulumi.Input[str]]] input_artifacts: A list of artifact names to be worked on.
        :param pulumi.Input[str] namespace: The namespace all output variables will be accessed from.
        :param pulumi.Input[List[pulumi.Input[str]]] output_artifacts: A list of artifact names to output. Output artifact names must be unique within a pipeline.
        :param pulumi.Input[str] region: The region in which to run the action.
        :param pulumi.Input[str] role_arn: The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.
        :param pulumi.Input[float] run_order: The order in which actions are run.
        """
        pulumi.set(__self__, "category", category)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "owner", owner)
        pulumi.set(__self__, "provider", provider)
        pulumi.set(__self__, "version", version)
        if configuration is not None:
            pulumi.set(__self__, "configuration", configuration)
        if input_artifacts is not None:
            pulumi.set(__self__, "input_artifacts", input_artifacts)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if output_artifacts is not None:
            pulumi.set(__self__, "output_artifacts", output_artifacts)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)
        if run_order is not None:
            pulumi.set(__self__, "run_order", run_order)

    @property
    @pulumi.getter
    def category(self) -> pulumi.Input[str]:
        """
        A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Possible values are `Approval`, `Build`, `Deploy`, `Invoke`, `Source` and `Test`.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: pulumi.Input[str]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The action declaration's name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Input[str]:
        """
        The creator of the action being called. Possible values are `AWS`, `Custom` and `ThirdParty`.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: pulumi.Input[str]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def provider(self) -> pulumi.Input[str]:
        """
        The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
        """
        return pulumi.get(self, "provider")

    @provider.setter
    def provider(self, value: pulumi.Input[str]):
        pulumi.set(self, "provider", value)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Input[str]:
        """
        A string that identifies the action type.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[str]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of the action declaration's configuration. Configurations options for action types and providers can be found in the [Pipeline Structure Reference](http://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements) and [Action Structure Reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference.html) documentation.
        """
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter(name="inputArtifacts")
    def input_artifacts(self) -> Optional[pulumi.Input[List[pulumi.Input[str]]]]:
        """
        A list of artifact names to be worked on.
        """
        return pulumi.get(self, "input_artifacts")

    @input_artifacts.setter
    def input_artifacts(self, value: Optional[pulumi.Input[List[pulumi.Input[str]]]]):
        pulumi.set(self, "input_artifacts", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace all output variables will be accessed from.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="outputArtifacts")
    def output_artifacts(self) -> Optional[pulumi.Input[List[pulumi.Input[str]]]]:
        """
        A list of artifact names to output. Output artifact names must be unique within a pipeline.
        """
        return pulumi.get(self, "output_artifacts")

    @output_artifacts.setter
    def output_artifacts(self, value: Optional[pulumi.Input[List[pulumi.Input[str]]]]):
        pulumi.set(self, "output_artifacts", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to run the action.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="runOrder")
    def run_order(self) -> Optional[pulumi.Input[float]]:
        """
        The order in which actions are run.
        """
        return pulumi.get(self, "run_order")

    @run_order.setter
    def run_order(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "run_order", value)


@pulumi.input_type
class WebhookAuthenticationConfigurationArgs:
    def __init__(__self__, *,
                 allowed_ip_range: Optional[pulumi.Input[str]] = None,
                 secret_token: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] allowed_ip_range: A valid CIDR block for `IP` filtering. Required for `IP`.
        :param pulumi.Input[str] secret_token: The shared secret for the GitHub repository webhook. Set this as `secret` in your `github_repository_webhook`'s `configuration` block. Required for `GITHUB_HMAC`.
        """
        if allowed_ip_range is not None:
            pulumi.set(__self__, "allowed_ip_range", allowed_ip_range)
        if secret_token is not None:
            pulumi.set(__self__, "secret_token", secret_token)

    @property
    @pulumi.getter(name="allowedIpRange")
    def allowed_ip_range(self) -> Optional[pulumi.Input[str]]:
        """
        A valid CIDR block for `IP` filtering. Required for `IP`.
        """
        return pulumi.get(self, "allowed_ip_range")

    @allowed_ip_range.setter
    def allowed_ip_range(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allowed_ip_range", value)

    @property
    @pulumi.getter(name="secretToken")
    def secret_token(self) -> Optional[pulumi.Input[str]]:
        """
        The shared secret for the GitHub repository webhook. Set this as `secret` in your `github_repository_webhook`'s `configuration` block. Required for `GITHUB_HMAC`.
        """
        return pulumi.get(self, "secret_token")

    @secret_token.setter
    def secret_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_token", value)


@pulumi.input_type
class WebhookFilterArgs:
    def __init__(__self__, *,
                 json_path: pulumi.Input[str],
                 match_equals: pulumi.Input[str]):
        """
        :param pulumi.Input[str] json_path: The [JSON path](https://github.com/json-path/JsonPath) to filter on.
        :param pulumi.Input[str] match_equals: The value to match on (e.g. `refs/heads/{Branch}`). See [AWS docs](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_WebhookFilterRule.html) for details.
        """
        pulumi.set(__self__, "json_path", json_path)
        pulumi.set(__self__, "match_equals", match_equals)

    @property
    @pulumi.getter(name="jsonPath")
    def json_path(self) -> pulumi.Input[str]:
        """
        The [JSON path](https://github.com/json-path/JsonPath) to filter on.
        """
        return pulumi.get(self, "json_path")

    @json_path.setter
    def json_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "json_path", value)

    @property
    @pulumi.getter(name="matchEquals")
    def match_equals(self) -> pulumi.Input[str]:
        """
        The value to match on (e.g. `refs/heads/{Branch}`). See [AWS docs](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_WebhookFilterRule.html) for details.
        """
        return pulumi.get(self, "match_equals")

    @match_equals.setter
    def match_equals(self, value: pulumi.Input[str]):
        pulumi.set(self, "match_equals", value)


