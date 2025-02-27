# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'DomainAdvancedSecurityOptionsArgs',
    'DomainAdvancedSecurityOptionsMasterUserOptionsArgs',
    'DomainClusterConfigArgs',
    'DomainClusterConfigZoneAwarenessConfigArgs',
    'DomainCognitoOptionsArgs',
    'DomainDomainEndpointOptionsArgs',
    'DomainEbsOptionsArgs',
    'DomainEncryptAtRestArgs',
    'DomainLogPublishingOptionArgs',
    'DomainNodeToNodeEncryptionArgs',
    'DomainSnapshotOptionsArgs',
    'DomainVpcOptionsArgs',
]

@pulumi.input_type
class DomainAdvancedSecurityOptionsArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 internal_user_database_enabled: Optional[pulumi.Input[bool]] = None,
                 master_user_options: Optional[pulumi.Input['DomainAdvancedSecurityOptionsMasterUserOptionsArgs']] = None):
        """
        :param pulumi.Input[bool] enabled: Specifies whether Amazon Cognito authentication with Kibana is enabled or not
        :param pulumi.Input[bool] internal_user_database_enabled: Whether the internal user database is enabled. If not set, defaults to `false` by the AWS API.
        :param pulumi.Input['DomainAdvancedSecurityOptionsMasterUserOptionsArgs'] master_user_options: Credentials for the master user: username and password, or ARN
        """
        pulumi.set(__self__, "enabled", enabled)
        if internal_user_database_enabled is not None:
            pulumi.set(__self__, "internal_user_database_enabled", internal_user_database_enabled)
        if master_user_options is not None:
            pulumi.set(__self__, "master_user_options", master_user_options)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Specifies whether Amazon Cognito authentication with Kibana is enabled or not
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="internalUserDatabaseEnabled")
    def internal_user_database_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the internal user database is enabled. If not set, defaults to `false` by the AWS API.
        """
        return pulumi.get(self, "internal_user_database_enabled")

    @internal_user_database_enabled.setter
    def internal_user_database_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "internal_user_database_enabled", value)

    @property
    @pulumi.getter(name="masterUserOptions")
    def master_user_options(self) -> Optional[pulumi.Input['DomainAdvancedSecurityOptionsMasterUserOptionsArgs']]:
        """
        Credentials for the master user: username and password, or ARN
        """
        return pulumi.get(self, "master_user_options")

    @master_user_options.setter
    def master_user_options(self, value: Optional[pulumi.Input['DomainAdvancedSecurityOptionsMasterUserOptionsArgs']]):
        pulumi.set(self, "master_user_options", value)


@pulumi.input_type
class DomainAdvancedSecurityOptionsMasterUserOptionsArgs:
    def __init__(__self__, *,
                 master_user_arn: Optional[pulumi.Input[str]] = None,
                 master_user_name: Optional[pulumi.Input[str]] = None,
                 master_user_password: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] master_user_arn: ARN for the master user. Only specify if `internal_user_database_enabled` is not set or set to `false`)
        :param pulumi.Input[str] master_user_name: The master user's username, which is stored in the Amazon Elasticsearch Service domain's internal database. Only specify if `internal_user_database_enabled` is set to `true`.
        :param pulumi.Input[str] master_user_password: The master user's password, which is stored in the Amazon Elasticsearch Service domain's internal database. Only specify if `internal_user_database_enabled` is set to `true`.
        """
        if master_user_arn is not None:
            pulumi.set(__self__, "master_user_arn", master_user_arn)
        if master_user_name is not None:
            pulumi.set(__self__, "master_user_name", master_user_name)
        if master_user_password is not None:
            pulumi.set(__self__, "master_user_password", master_user_password)

    @property
    @pulumi.getter(name="masterUserArn")
    def master_user_arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN for the master user. Only specify if `internal_user_database_enabled` is not set or set to `false`)
        """
        return pulumi.get(self, "master_user_arn")

    @master_user_arn.setter
    def master_user_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "master_user_arn", value)

    @property
    @pulumi.getter(name="masterUserName")
    def master_user_name(self) -> Optional[pulumi.Input[str]]:
        """
        The master user's username, which is stored in the Amazon Elasticsearch Service domain's internal database. Only specify if `internal_user_database_enabled` is set to `true`.
        """
        return pulumi.get(self, "master_user_name")

    @master_user_name.setter
    def master_user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "master_user_name", value)

    @property
    @pulumi.getter(name="masterUserPassword")
    def master_user_password(self) -> Optional[pulumi.Input[str]]:
        """
        The master user's password, which is stored in the Amazon Elasticsearch Service domain's internal database. Only specify if `internal_user_database_enabled` is set to `true`.
        """
        return pulumi.get(self, "master_user_password")

    @master_user_password.setter
    def master_user_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "master_user_password", value)


@pulumi.input_type
class DomainClusterConfigArgs:
    def __init__(__self__, *,
                 dedicated_master_count: Optional[pulumi.Input[float]] = None,
                 dedicated_master_enabled: Optional[pulumi.Input[bool]] = None,
                 dedicated_master_type: Optional[pulumi.Input[str]] = None,
                 instance_count: Optional[pulumi.Input[float]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 warm_count: Optional[pulumi.Input[float]] = None,
                 warm_enabled: Optional[pulumi.Input[bool]] = None,
                 warm_type: Optional[pulumi.Input[str]] = None,
                 zone_awareness_config: Optional[pulumi.Input['DomainClusterConfigZoneAwarenessConfigArgs']] = None,
                 zone_awareness_enabled: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[float] dedicated_master_count: Number of dedicated master nodes in the cluster
        :param pulumi.Input[bool] dedicated_master_enabled: Indicates whether dedicated master nodes are enabled for the cluster.
        :param pulumi.Input[str] dedicated_master_type: Instance type of the dedicated master nodes in the cluster.
        :param pulumi.Input[float] instance_count: Number of instances in the cluster.
        :param pulumi.Input[str] instance_type: Instance type of data nodes in the cluster.
        :param pulumi.Input[float] warm_count: The number of warm nodes in the cluster. Valid values are between `2` and `150`. `warm_count` can be only and must be set when `warm_enabled` is set to `true`.
        :param pulumi.Input[bool] warm_enabled: Indicates whether to enable warm storage.
        :param pulumi.Input[str] warm_type: The instance type for the Elasticsearch cluster's warm nodes. Valid values are `ultrawarm1.medium.elasticsearch`, `ultrawarm1.large.elasticsearch` and `ultrawarm1.xlarge.elasticsearch`. `warm_type` can be only and must be set when `warm_enabled` is set to `true`.
        :param pulumi.Input['DomainClusterConfigZoneAwarenessConfigArgs'] zone_awareness_config: Configuration block containing zone awareness settings. Documented below.
        :param pulumi.Input[bool] zone_awareness_enabled: Indicates whether zone awareness is enabled, set to `true` for multi-az deployment. To enable awareness with three Availability Zones, the `availability_zone_count` within the `zone_awareness_config` must be set to `3`.
        """
        if dedicated_master_count is not None:
            pulumi.set(__self__, "dedicated_master_count", dedicated_master_count)
        if dedicated_master_enabled is not None:
            pulumi.set(__self__, "dedicated_master_enabled", dedicated_master_enabled)
        if dedicated_master_type is not None:
            pulumi.set(__self__, "dedicated_master_type", dedicated_master_type)
        if instance_count is not None:
            pulumi.set(__self__, "instance_count", instance_count)
        if instance_type is not None:
            pulumi.set(__self__, "instance_type", instance_type)
        if warm_count is not None:
            pulumi.set(__self__, "warm_count", warm_count)
        if warm_enabled is not None:
            pulumi.set(__self__, "warm_enabled", warm_enabled)
        if warm_type is not None:
            pulumi.set(__self__, "warm_type", warm_type)
        if zone_awareness_config is not None:
            pulumi.set(__self__, "zone_awareness_config", zone_awareness_config)
        if zone_awareness_enabled is not None:
            pulumi.set(__self__, "zone_awareness_enabled", zone_awareness_enabled)

    @property
    @pulumi.getter(name="dedicatedMasterCount")
    def dedicated_master_count(self) -> Optional[pulumi.Input[float]]:
        """
        Number of dedicated master nodes in the cluster
        """
        return pulumi.get(self, "dedicated_master_count")

    @dedicated_master_count.setter
    def dedicated_master_count(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "dedicated_master_count", value)

    @property
    @pulumi.getter(name="dedicatedMasterEnabled")
    def dedicated_master_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether dedicated master nodes are enabled for the cluster.
        """
        return pulumi.get(self, "dedicated_master_enabled")

    @dedicated_master_enabled.setter
    def dedicated_master_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dedicated_master_enabled", value)

    @property
    @pulumi.getter(name="dedicatedMasterType")
    def dedicated_master_type(self) -> Optional[pulumi.Input[str]]:
        """
        Instance type of the dedicated master nodes in the cluster.
        """
        return pulumi.get(self, "dedicated_master_type")

    @dedicated_master_type.setter
    def dedicated_master_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dedicated_master_type", value)

    @property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[float]]:
        """
        Number of instances in the cluster.
        """
        return pulumi.get(self, "instance_count")

    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "instance_count", value)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[str]]:
        """
        Instance type of data nodes in the cluster.
        """
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter(name="warmCount")
    def warm_count(self) -> Optional[pulumi.Input[float]]:
        """
        The number of warm nodes in the cluster. Valid values are between `2` and `150`. `warm_count` can be only and must be set when `warm_enabled` is set to `true`.
        """
        return pulumi.get(self, "warm_count")

    @warm_count.setter
    def warm_count(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "warm_count", value)

    @property
    @pulumi.getter(name="warmEnabled")
    def warm_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether to enable warm storage.
        """
        return pulumi.get(self, "warm_enabled")

    @warm_enabled.setter
    def warm_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "warm_enabled", value)

    @property
    @pulumi.getter(name="warmType")
    def warm_type(self) -> Optional[pulumi.Input[str]]:
        """
        The instance type for the Elasticsearch cluster's warm nodes. Valid values are `ultrawarm1.medium.elasticsearch`, `ultrawarm1.large.elasticsearch` and `ultrawarm1.xlarge.elasticsearch`. `warm_type` can be only and must be set when `warm_enabled` is set to `true`.
        """
        return pulumi.get(self, "warm_type")

    @warm_type.setter
    def warm_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "warm_type", value)

    @property
    @pulumi.getter(name="zoneAwarenessConfig")
    def zone_awareness_config(self) -> Optional[pulumi.Input['DomainClusterConfigZoneAwarenessConfigArgs']]:
        """
        Configuration block containing zone awareness settings. Documented below.
        """
        return pulumi.get(self, "zone_awareness_config")

    @zone_awareness_config.setter
    def zone_awareness_config(self, value: Optional[pulumi.Input['DomainClusterConfigZoneAwarenessConfigArgs']]):
        pulumi.set(self, "zone_awareness_config", value)

    @property
    @pulumi.getter(name="zoneAwarenessEnabled")
    def zone_awareness_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether zone awareness is enabled, set to `true` for multi-az deployment. To enable awareness with three Availability Zones, the `availability_zone_count` within the `zone_awareness_config` must be set to `3`.
        """
        return pulumi.get(self, "zone_awareness_enabled")

    @zone_awareness_enabled.setter
    def zone_awareness_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "zone_awareness_enabled", value)


@pulumi.input_type
class DomainClusterConfigZoneAwarenessConfigArgs:
    def __init__(__self__, *,
                 availability_zone_count: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[float] availability_zone_count: Number of Availability Zones for the domain to use with `zone_awareness_enabled`. Defaults to `2`. Valid values: `2` or `3`.
        """
        if availability_zone_count is not None:
            pulumi.set(__self__, "availability_zone_count", availability_zone_count)

    @property
    @pulumi.getter(name="availabilityZoneCount")
    def availability_zone_count(self) -> Optional[pulumi.Input[float]]:
        """
        Number of Availability Zones for the domain to use with `zone_awareness_enabled`. Defaults to `2`. Valid values: `2` or `3`.
        """
        return pulumi.get(self, "availability_zone_count")

    @availability_zone_count.setter
    def availability_zone_count(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "availability_zone_count", value)


@pulumi.input_type
class DomainCognitoOptionsArgs:
    def __init__(__self__, *,
                 identity_pool_id: pulumi.Input[str],
                 role_arn: pulumi.Input[str],
                 user_pool_id: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] identity_pool_id: ID of the Cognito Identity Pool to use
        :param pulumi.Input[str] role_arn: ARN of the IAM role that has the AmazonESCognitoAccess policy attached
        :param pulumi.Input[str] user_pool_id: ID of the Cognito User Pool to use
        :param pulumi.Input[bool] enabled: Specifies whether Amazon Cognito authentication with Kibana is enabled or not
        """
        pulumi.set(__self__, "identity_pool_id", identity_pool_id)
        pulumi.set(__self__, "role_arn", role_arn)
        pulumi.set(__self__, "user_pool_id", user_pool_id)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> pulumi.Input[str]:
        """
        ID of the Cognito Identity Pool to use
        """
        return pulumi.get(self, "identity_pool_id")

    @identity_pool_id.setter
    def identity_pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "identity_pool_id", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        ARN of the IAM role that has the AmazonESCognitoAccess policy attached
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[str]:
        """
        ID of the Cognito User Pool to use
        """
        return pulumi.get(self, "user_pool_id")

    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_pool_id", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether Amazon Cognito authentication with Kibana is enabled or not
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)


@pulumi.input_type
class DomainDomainEndpointOptionsArgs:
    def __init__(__self__, *,
                 enforce_https: pulumi.Input[bool],
                 tls_security_policy: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] enforce_https: Whether or not to require HTTPS
        :param pulumi.Input[str] tls_security_policy: The name of the TLS security policy that needs to be applied to the HTTPS endpoint. Valid values:  `Policy-Min-TLS-1-0-2019-07` and `Policy-Min-TLS-1-2-2019-07`. This provider will only perform drift detection if a configuration value is provided.
        """
        pulumi.set(__self__, "enforce_https", enforce_https)
        if tls_security_policy is not None:
            pulumi.set(__self__, "tls_security_policy", tls_security_policy)

    @property
    @pulumi.getter(name="enforceHttps")
    def enforce_https(self) -> pulumi.Input[bool]:
        """
        Whether or not to require HTTPS
        """
        return pulumi.get(self, "enforce_https")

    @enforce_https.setter
    def enforce_https(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enforce_https", value)

    @property
    @pulumi.getter(name="tlsSecurityPolicy")
    def tls_security_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the TLS security policy that needs to be applied to the HTTPS endpoint. Valid values:  `Policy-Min-TLS-1-0-2019-07` and `Policy-Min-TLS-1-2-2019-07`. This provider will only perform drift detection if a configuration value is provided.
        """
        return pulumi.get(self, "tls_security_policy")

    @tls_security_policy.setter
    def tls_security_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tls_security_policy", value)


@pulumi.input_type
class DomainEbsOptionsArgs:
    def __init__(__self__, *,
                 ebs_enabled: pulumi.Input[bool],
                 iops: Optional[pulumi.Input[float]] = None,
                 volume_size: Optional[pulumi.Input[float]] = None,
                 volume_type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] ebs_enabled: Whether EBS volumes are attached to data nodes in the domain.
        :param pulumi.Input[float] iops: The baseline input/output (I/O) performance of EBS volumes
               attached to data nodes. Applicable only for the Provisioned IOPS EBS volume type.
        :param pulumi.Input[float] volume_size: The size of EBS volumes attached to data nodes (in GB).
               **Required** if `ebs_enabled` is set to `true`.
        :param pulumi.Input[str] volume_type: The type of EBS volumes attached to data nodes.
        """
        pulumi.set(__self__, "ebs_enabled", ebs_enabled)
        if iops is not None:
            pulumi.set(__self__, "iops", iops)
        if volume_size is not None:
            pulumi.set(__self__, "volume_size", volume_size)
        if volume_type is not None:
            pulumi.set(__self__, "volume_type", volume_type)

    @property
    @pulumi.getter(name="ebsEnabled")
    def ebs_enabled(self) -> pulumi.Input[bool]:
        """
        Whether EBS volumes are attached to data nodes in the domain.
        """
        return pulumi.get(self, "ebs_enabled")

    @ebs_enabled.setter
    def ebs_enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "ebs_enabled", value)

    @property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[float]]:
        """
        The baseline input/output (I/O) performance of EBS volumes
        attached to data nodes. Applicable only for the Provisioned IOPS EBS volume type.
        """
        return pulumi.get(self, "iops")

    @iops.setter
    def iops(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "iops", value)

    @property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[float]]:
        """
        The size of EBS volumes attached to data nodes (in GB).
        **Required** if `ebs_enabled` is set to `true`.
        """
        return pulumi.get(self, "volume_size")

    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "volume_size", value)

    @property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of EBS volumes attached to data nodes.
        """
        return pulumi.get(self, "volume_type")

    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_type", value)


@pulumi.input_type
class DomainEncryptAtRestArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 kms_key_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] enabled: Specifies whether Amazon Cognito authentication with Kibana is enabled or not
        :param pulumi.Input[str] kms_key_id: The KMS key id to encrypt the Elasticsearch domain with. If not specified then it defaults to using the `aws/es` service KMS key.
        """
        pulumi.set(__self__, "enabled", enabled)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Specifies whether Amazon Cognito authentication with Kibana is enabled or not
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The KMS key id to encrypt the Elasticsearch domain with. If not specified then it defaults to using the `aws/es` service KMS key.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)


@pulumi.input_type
class DomainLogPublishingOptionArgs:
    def __init__(__self__, *,
                 cloudwatch_log_group_arn: pulumi.Input[str],
                 log_type: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] cloudwatch_log_group_arn: ARN of the Cloudwatch log group to which log needs to be published.
        :param pulumi.Input[str] log_type: A type of Elasticsearch log. Valid values: INDEX_SLOW_LOGS, SEARCH_SLOW_LOGS, ES_APPLICATION_LOGS
        :param pulumi.Input[bool] enabled: Specifies whether Amazon Cognito authentication with Kibana is enabled or not
        """
        pulumi.set(__self__, "cloudwatch_log_group_arn", cloudwatch_log_group_arn)
        pulumi.set(__self__, "log_type", log_type)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter(name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> pulumi.Input[str]:
        """
        ARN of the Cloudwatch log group to which log needs to be published.
        """
        return pulumi.get(self, "cloudwatch_log_group_arn")

    @cloudwatch_log_group_arn.setter
    def cloudwatch_log_group_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "cloudwatch_log_group_arn", value)

    @property
    @pulumi.getter(name="logType")
    def log_type(self) -> pulumi.Input[str]:
        """
        A type of Elasticsearch log. Valid values: INDEX_SLOW_LOGS, SEARCH_SLOW_LOGS, ES_APPLICATION_LOGS
        """
        return pulumi.get(self, "log_type")

    @log_type.setter
    def log_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "log_type", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether Amazon Cognito authentication with Kibana is enabled or not
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)


@pulumi.input_type
class DomainNodeToNodeEncryptionArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool]):
        """
        :param pulumi.Input[bool] enabled: Specifies whether Amazon Cognito authentication with Kibana is enabled or not
        """
        pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Specifies whether Amazon Cognito authentication with Kibana is enabled or not
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)


@pulumi.input_type
class DomainSnapshotOptionsArgs:
    def __init__(__self__, *,
                 automated_snapshot_start_hour: pulumi.Input[float]):
        """
        :param pulumi.Input[float] automated_snapshot_start_hour: Hour during which the service takes an automated daily
               snapshot of the indices in the domain.
        """
        pulumi.set(__self__, "automated_snapshot_start_hour", automated_snapshot_start_hour)

    @property
    @pulumi.getter(name="automatedSnapshotStartHour")
    def automated_snapshot_start_hour(self) -> pulumi.Input[float]:
        """
        Hour during which the service takes an automated daily
        snapshot of the indices in the domain.
        """
        return pulumi.get(self, "automated_snapshot_start_hour")

    @automated_snapshot_start_hour.setter
    def automated_snapshot_start_hour(self, value: pulumi.Input[float]):
        pulumi.set(self, "automated_snapshot_start_hour", value)


@pulumi.input_type
class DomainVpcOptionsArgs:
    def __init__(__self__, *,
                 availability_zones: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 security_group_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 subnet_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[List[pulumi.Input[str]]] security_group_ids: List of VPC Security Group IDs to be applied to the Elasticsearch domain endpoints. If omitted, the default Security Group for the VPC will be used.
        :param pulumi.Input[List[pulumi.Input[str]]] subnet_ids: List of VPC Subnet IDs for the Elasticsearch domain endpoints to be created in.
        """
        if availability_zones is not None:
            pulumi.set(__self__, "availability_zones", availability_zones)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[List[pulumi.Input[str]]]]:
        return pulumi.get(self, "availability_zones")

    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[List[pulumi.Input[str]]]]):
        pulumi.set(self, "availability_zones", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[List[pulumi.Input[str]]]]:
        """
        List of VPC Security Group IDs to be applied to the Elasticsearch domain endpoints. If omitted, the default Security Group for the VPC will be used.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[List[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[List[pulumi.Input[str]]]]:
        """
        List of VPC Subnet IDs for the Elasticsearch domain endpoints to be created in.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[List[pulumi.Input[str]]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


