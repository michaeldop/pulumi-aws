# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'ClusterBootstrapActionArgs',
    'ClusterCoreInstanceGroupArgs',
    'ClusterCoreInstanceGroupEbsConfigArgs',
    'ClusterEc2AttributesArgs',
    'ClusterKerberosAttributesArgs',
    'ClusterMasterInstanceGroupArgs',
    'ClusterMasterInstanceGroupEbsConfigArgs',
    'ClusterStepArgs',
    'ClusterStepHadoopJarStepArgs',
    'InstanceGroupEbsConfigArgs',
]

@pulumi.input_type
class ClusterBootstrapActionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 path: pulumi.Input[str],
                 args: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] name: The name of the step.
        :param pulumi.Input[str] path: Location of the script to run during a bootstrap action. Can be either a location in Amazon S3 or on a local file system
        :param pulumi.Input[List[pulumi.Input[str]]] args: List of command line arguments passed to the JAR file's main function when executed.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "path", path)
        if args is not None:
            pulumi.set(__self__, "args", args)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the step.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def path(self) -> pulumi.Input[str]:
        """
        Location of the script to run during a bootstrap action. Can be either a location in Amazon S3 or on a local file system
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: pulumi.Input[str]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[List[pulumi.Input[str]]]]:
        """
        List of command line arguments passed to the JAR file's main function when executed.
        """
        return pulumi.get(self, "args")

    @args.setter
    def args(self, value: Optional[pulumi.Input[List[pulumi.Input[str]]]]):
        pulumi.set(self, "args", value)


@pulumi.input_type
class ClusterCoreInstanceGroupArgs:
    def __init__(__self__, *,
                 instance_type: pulumi.Input[str],
                 autoscaling_policy: Optional[pulumi.Input[str]] = None,
                 bid_price: Optional[pulumi.Input[str]] = None,
                 ebs_configs: Optional[pulumi.Input[List[pulumi.Input['ClusterCoreInstanceGroupEbsConfigArgs']]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 instance_count: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] instance_type: EC2 instance type for all instances in the instance group.
        :param pulumi.Input[str] autoscaling_policy: String containing the [EMR Auto Scaling Policy](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html) JSON.
        :param pulumi.Input[str] bid_price: Bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.
        :param pulumi.Input[List[pulumi.Input['ClusterCoreInstanceGroupEbsConfigArgs']]] ebs_configs: Configuration block(s) for EBS volumes attached to each instance in the instance group. Detailed below.
        :param pulumi.Input[str] id: The ID of the EMR Cluster
        :param pulumi.Input[float] instance_count: Target number of instances for the instance group. Must be 1 or 3. Defaults to 1. Launching with multiple master nodes is only supported in EMR version 5.23.0+, and requires this resource's `core_instance_group` to be configured. Public (Internet accessible) instances must be created in VPC subnets that have `map public IP on launch` enabled. Termination protection is automatically enabled when launched with multiple master nodes and this provider must have the `termination_protection = false` configuration applied before destroying this resource.
        :param pulumi.Input[str] name: The name of the step.
        """
        pulumi.set(__self__, "instance_type", instance_type)
        if autoscaling_policy is not None:
            pulumi.set(__self__, "autoscaling_policy", autoscaling_policy)
        if bid_price is not None:
            pulumi.set(__self__, "bid_price", bid_price)
        if ebs_configs is not None:
            pulumi.set(__self__, "ebs_configs", ebs_configs)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if instance_count is not None:
            pulumi.set(__self__, "instance_count", instance_count)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[str]:
        """
        EC2 instance type for all instances in the instance group.
        """
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter(name="autoscalingPolicy")
    def autoscaling_policy(self) -> Optional[pulumi.Input[str]]:
        """
        String containing the [EMR Auto Scaling Policy](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html) JSON.
        """
        return pulumi.get(self, "autoscaling_policy")

    @autoscaling_policy.setter
    def autoscaling_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "autoscaling_policy", value)

    @property
    @pulumi.getter(name="bidPrice")
    def bid_price(self) -> Optional[pulumi.Input[str]]:
        """
        Bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.
        """
        return pulumi.get(self, "bid_price")

    @bid_price.setter
    def bid_price(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bid_price", value)

    @property
    @pulumi.getter(name="ebsConfigs")
    def ebs_configs(self) -> Optional[pulumi.Input[List[pulumi.Input['ClusterCoreInstanceGroupEbsConfigArgs']]]]:
        """
        Configuration block(s) for EBS volumes attached to each instance in the instance group. Detailed below.
        """
        return pulumi.get(self, "ebs_configs")

    @ebs_configs.setter
    def ebs_configs(self, value: Optional[pulumi.Input[List[pulumi.Input['ClusterCoreInstanceGroupEbsConfigArgs']]]]):
        pulumi.set(self, "ebs_configs", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the EMR Cluster
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[float]]:
        """
        Target number of instances for the instance group. Must be 1 or 3. Defaults to 1. Launching with multiple master nodes is only supported in EMR version 5.23.0+, and requires this resource's `core_instance_group` to be configured. Public (Internet accessible) instances must be created in VPC subnets that have `map public IP on launch` enabled. Termination protection is automatically enabled when launched with multiple master nodes and this provider must have the `termination_protection = false` configuration applied before destroying this resource.
        """
        return pulumi.get(self, "instance_count")

    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "instance_count", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the step.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class ClusterCoreInstanceGroupEbsConfigArgs:
    def __init__(__self__, *,
                 size: pulumi.Input[float],
                 type: pulumi.Input[str],
                 iops: Optional[pulumi.Input[float]] = None,
                 volumes_per_instance: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[float] size: The volume size, in gibibytes (GiB).
        :param pulumi.Input[str] type: The volume type. Valid options are `gp2`, `io1`, `standard` and `st1`. See [EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html).
        :param pulumi.Input[float] iops: The number of I/O operations per second (IOPS) that the volume supports
        :param pulumi.Input[float] volumes_per_instance: The number of EBS volumes with this configuration to attach to each EC2 instance in the instance group (default is 1)
        """
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "type", type)
        if iops is not None:
            pulumi.set(__self__, "iops", iops)
        if volumes_per_instance is not None:
            pulumi.set(__self__, "volumes_per_instance", volumes_per_instance)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[float]:
        """
        The volume size, in gibibytes (GiB).
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[float]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The volume type. Valid options are `gp2`, `io1`, `standard` and `st1`. See [EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[float]]:
        """
        The number of I/O operations per second (IOPS) that the volume supports
        """
        return pulumi.get(self, "iops")

    @iops.setter
    def iops(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "iops", value)

    @property
    @pulumi.getter(name="volumesPerInstance")
    def volumes_per_instance(self) -> Optional[pulumi.Input[float]]:
        """
        The number of EBS volumes with this configuration to attach to each EC2 instance in the instance group (default is 1)
        """
        return pulumi.get(self, "volumes_per_instance")

    @volumes_per_instance.setter
    def volumes_per_instance(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "volumes_per_instance", value)


@pulumi.input_type
class ClusterEc2AttributesArgs:
    def __init__(__self__, *,
                 instance_profile: pulumi.Input[str],
                 additional_master_security_groups: Optional[pulumi.Input[str]] = None,
                 additional_slave_security_groups: Optional[pulumi.Input[str]] = None,
                 emr_managed_master_security_group: Optional[pulumi.Input[str]] = None,
                 emr_managed_slave_security_group: Optional[pulumi.Input[str]] = None,
                 key_name: Optional[pulumi.Input[str]] = None,
                 service_access_security_group: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] instance_profile: Instance Profile for EC2 instances of the cluster assume this role
        :param pulumi.Input[str] additional_master_security_groups: String containing a comma separated list of additional Amazon EC2 security group IDs for the master node
        :param pulumi.Input[str] additional_slave_security_groups: String containing a comma separated list of additional Amazon EC2 security group IDs for the slave nodes as a comma separated string
        :param pulumi.Input[str] emr_managed_master_security_group: Identifier of the Amazon EC2 EMR-Managed security group for the master node
        :param pulumi.Input[str] emr_managed_slave_security_group: Identifier of the Amazon EC2 EMR-Managed security group for the slave nodes
        :param pulumi.Input[str] key_name: Amazon EC2 key pair that can be used to ssh to the master node as the user called `hadoop`
        :param pulumi.Input[str] service_access_security_group: Identifier of the Amazon EC2 service-access security group - required when the cluster runs on a private subnet
        :param pulumi.Input[str] subnet_id: VPC subnet id where you want the job flow to launch. Cannot specify the `cc1.4xlarge` instance type for nodes of a job flow launched in a Amazon VPC
        """
        pulumi.set(__self__, "instance_profile", instance_profile)
        if additional_master_security_groups is not None:
            pulumi.set(__self__, "additional_master_security_groups", additional_master_security_groups)
        if additional_slave_security_groups is not None:
            pulumi.set(__self__, "additional_slave_security_groups", additional_slave_security_groups)
        if emr_managed_master_security_group is not None:
            pulumi.set(__self__, "emr_managed_master_security_group", emr_managed_master_security_group)
        if emr_managed_slave_security_group is not None:
            pulumi.set(__self__, "emr_managed_slave_security_group", emr_managed_slave_security_group)
        if key_name is not None:
            pulumi.set(__self__, "key_name", key_name)
        if service_access_security_group is not None:
            pulumi.set(__self__, "service_access_security_group", service_access_security_group)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="instanceProfile")
    def instance_profile(self) -> pulumi.Input[str]:
        """
        Instance Profile for EC2 instances of the cluster assume this role
        """
        return pulumi.get(self, "instance_profile")

    @instance_profile.setter
    def instance_profile(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_profile", value)

    @property
    @pulumi.getter(name="additionalMasterSecurityGroups")
    def additional_master_security_groups(self) -> Optional[pulumi.Input[str]]:
        """
        String containing a comma separated list of additional Amazon EC2 security group IDs for the master node
        """
        return pulumi.get(self, "additional_master_security_groups")

    @additional_master_security_groups.setter
    def additional_master_security_groups(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "additional_master_security_groups", value)

    @property
    @pulumi.getter(name="additionalSlaveSecurityGroups")
    def additional_slave_security_groups(self) -> Optional[pulumi.Input[str]]:
        """
        String containing a comma separated list of additional Amazon EC2 security group IDs for the slave nodes as a comma separated string
        """
        return pulumi.get(self, "additional_slave_security_groups")

    @additional_slave_security_groups.setter
    def additional_slave_security_groups(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "additional_slave_security_groups", value)

    @property
    @pulumi.getter(name="emrManagedMasterSecurityGroup")
    def emr_managed_master_security_group(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the Amazon EC2 EMR-Managed security group for the master node
        """
        return pulumi.get(self, "emr_managed_master_security_group")

    @emr_managed_master_security_group.setter
    def emr_managed_master_security_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "emr_managed_master_security_group", value)

    @property
    @pulumi.getter(name="emrManagedSlaveSecurityGroup")
    def emr_managed_slave_security_group(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the Amazon EC2 EMR-Managed security group for the slave nodes
        """
        return pulumi.get(self, "emr_managed_slave_security_group")

    @emr_managed_slave_security_group.setter
    def emr_managed_slave_security_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "emr_managed_slave_security_group", value)

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon EC2 key pair that can be used to ssh to the master node as the user called `hadoop`
        """
        return pulumi.get(self, "key_name")

    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_name", value)

    @property
    @pulumi.getter(name="serviceAccessSecurityGroup")
    def service_access_security_group(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the Amazon EC2 service-access security group - required when the cluster runs on a private subnet
        """
        return pulumi.get(self, "service_access_security_group")

    @service_access_security_group.setter
    def service_access_security_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_access_security_group", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        VPC subnet id where you want the job flow to launch. Cannot specify the `cc1.4xlarge` instance type for nodes of a job flow launched in a Amazon VPC
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)


@pulumi.input_type
class ClusterKerberosAttributesArgs:
    def __init__(__self__, *,
                 kdc_admin_password: pulumi.Input[str],
                 realm: pulumi.Input[str],
                 ad_domain_join_password: Optional[pulumi.Input[str]] = None,
                 ad_domain_join_user: Optional[pulumi.Input[str]] = None,
                 cross_realm_trust_principal_password: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] kdc_admin_password: The password used within the cluster for the kadmin service on the cluster-dedicated KDC, which maintains Kerberos principals, password policies, and keytabs for the cluster. This provider cannot perform drift detection of this configuration.
        :param pulumi.Input[str] realm: The name of the Kerberos realm to which all nodes in a cluster belong. For example, `EC2.INTERNAL`
        :param pulumi.Input[str] ad_domain_join_password: The Active Directory password for `ad_domain_join_user`. This provider cannot perform drift detection of this configuration.
        :param pulumi.Input[str] ad_domain_join_user: Required only when establishing a cross-realm trust with an Active Directory domain. A user with sufficient privileges to join resources to the domain. This provider cannot perform drift detection of this configuration.
        :param pulumi.Input[str] cross_realm_trust_principal_password: Required only when establishing a cross-realm trust with a KDC in a different realm. The cross-realm principal password, which must be identical across realms. This provider cannot perform drift detection of this configuration.
        """
        pulumi.set(__self__, "kdc_admin_password", kdc_admin_password)
        pulumi.set(__self__, "realm", realm)
        if ad_domain_join_password is not None:
            pulumi.set(__self__, "ad_domain_join_password", ad_domain_join_password)
        if ad_domain_join_user is not None:
            pulumi.set(__self__, "ad_domain_join_user", ad_domain_join_user)
        if cross_realm_trust_principal_password is not None:
            pulumi.set(__self__, "cross_realm_trust_principal_password", cross_realm_trust_principal_password)

    @property
    @pulumi.getter(name="kdcAdminPassword")
    def kdc_admin_password(self) -> pulumi.Input[str]:
        """
        The password used within the cluster for the kadmin service on the cluster-dedicated KDC, which maintains Kerberos principals, password policies, and keytabs for the cluster. This provider cannot perform drift detection of this configuration.
        """
        return pulumi.get(self, "kdc_admin_password")

    @kdc_admin_password.setter
    def kdc_admin_password(self, value: pulumi.Input[str]):
        pulumi.set(self, "kdc_admin_password", value)

    @property
    @pulumi.getter
    def realm(self) -> pulumi.Input[str]:
        """
        The name of the Kerberos realm to which all nodes in a cluster belong. For example, `EC2.INTERNAL`
        """
        return pulumi.get(self, "realm")

    @realm.setter
    def realm(self, value: pulumi.Input[str]):
        pulumi.set(self, "realm", value)

    @property
    @pulumi.getter(name="adDomainJoinPassword")
    def ad_domain_join_password(self) -> Optional[pulumi.Input[str]]:
        """
        The Active Directory password for `ad_domain_join_user`. This provider cannot perform drift detection of this configuration.
        """
        return pulumi.get(self, "ad_domain_join_password")

    @ad_domain_join_password.setter
    def ad_domain_join_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ad_domain_join_password", value)

    @property
    @pulumi.getter(name="adDomainJoinUser")
    def ad_domain_join_user(self) -> Optional[pulumi.Input[str]]:
        """
        Required only when establishing a cross-realm trust with an Active Directory domain. A user with sufficient privileges to join resources to the domain. This provider cannot perform drift detection of this configuration.
        """
        return pulumi.get(self, "ad_domain_join_user")

    @ad_domain_join_user.setter
    def ad_domain_join_user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ad_domain_join_user", value)

    @property
    @pulumi.getter(name="crossRealmTrustPrincipalPassword")
    def cross_realm_trust_principal_password(self) -> Optional[pulumi.Input[str]]:
        """
        Required only when establishing a cross-realm trust with a KDC in a different realm. The cross-realm principal password, which must be identical across realms. This provider cannot perform drift detection of this configuration.
        """
        return pulumi.get(self, "cross_realm_trust_principal_password")

    @cross_realm_trust_principal_password.setter
    def cross_realm_trust_principal_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cross_realm_trust_principal_password", value)


@pulumi.input_type
class ClusterMasterInstanceGroupArgs:
    def __init__(__self__, *,
                 instance_type: pulumi.Input[str],
                 bid_price: Optional[pulumi.Input[str]] = None,
                 ebs_configs: Optional[pulumi.Input[List[pulumi.Input['ClusterMasterInstanceGroupEbsConfigArgs']]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 instance_count: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] instance_type: EC2 instance type for all instances in the instance group.
        :param pulumi.Input[str] bid_price: Bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.
        :param pulumi.Input[List[pulumi.Input['ClusterMasterInstanceGroupEbsConfigArgs']]] ebs_configs: Configuration block(s) for EBS volumes attached to each instance in the instance group. Detailed below.
        :param pulumi.Input[str] id: The ID of the EMR Cluster
        :param pulumi.Input[float] instance_count: Target number of instances for the instance group. Must be 1 or 3. Defaults to 1. Launching with multiple master nodes is only supported in EMR version 5.23.0+, and requires this resource's `core_instance_group` to be configured. Public (Internet accessible) instances must be created in VPC subnets that have `map public IP on launch` enabled. Termination protection is automatically enabled when launched with multiple master nodes and this provider must have the `termination_protection = false` configuration applied before destroying this resource.
        :param pulumi.Input[str] name: The name of the step.
        """
        pulumi.set(__self__, "instance_type", instance_type)
        if bid_price is not None:
            pulumi.set(__self__, "bid_price", bid_price)
        if ebs_configs is not None:
            pulumi.set(__self__, "ebs_configs", ebs_configs)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if instance_count is not None:
            pulumi.set(__self__, "instance_count", instance_count)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[str]:
        """
        EC2 instance type for all instances in the instance group.
        """
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter(name="bidPrice")
    def bid_price(self) -> Optional[pulumi.Input[str]]:
        """
        Bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.
        """
        return pulumi.get(self, "bid_price")

    @bid_price.setter
    def bid_price(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bid_price", value)

    @property
    @pulumi.getter(name="ebsConfigs")
    def ebs_configs(self) -> Optional[pulumi.Input[List[pulumi.Input['ClusterMasterInstanceGroupEbsConfigArgs']]]]:
        """
        Configuration block(s) for EBS volumes attached to each instance in the instance group. Detailed below.
        """
        return pulumi.get(self, "ebs_configs")

    @ebs_configs.setter
    def ebs_configs(self, value: Optional[pulumi.Input[List[pulumi.Input['ClusterMasterInstanceGroupEbsConfigArgs']]]]):
        pulumi.set(self, "ebs_configs", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the EMR Cluster
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[float]]:
        """
        Target number of instances for the instance group. Must be 1 or 3. Defaults to 1. Launching with multiple master nodes is only supported in EMR version 5.23.0+, and requires this resource's `core_instance_group` to be configured. Public (Internet accessible) instances must be created in VPC subnets that have `map public IP on launch` enabled. Termination protection is automatically enabled when launched with multiple master nodes and this provider must have the `termination_protection = false` configuration applied before destroying this resource.
        """
        return pulumi.get(self, "instance_count")

    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "instance_count", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the step.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class ClusterMasterInstanceGroupEbsConfigArgs:
    def __init__(__self__, *,
                 size: pulumi.Input[float],
                 type: pulumi.Input[str],
                 iops: Optional[pulumi.Input[float]] = None,
                 volumes_per_instance: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[float] size: The volume size, in gibibytes (GiB).
        :param pulumi.Input[str] type: The volume type. Valid options are `gp2`, `io1`, `standard` and `st1`. See [EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html).
        :param pulumi.Input[float] iops: The number of I/O operations per second (IOPS) that the volume supports
        :param pulumi.Input[float] volumes_per_instance: The number of EBS volumes with this configuration to attach to each EC2 instance in the instance group (default is 1)
        """
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "type", type)
        if iops is not None:
            pulumi.set(__self__, "iops", iops)
        if volumes_per_instance is not None:
            pulumi.set(__self__, "volumes_per_instance", volumes_per_instance)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[float]:
        """
        The volume size, in gibibytes (GiB).
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[float]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The volume type. Valid options are `gp2`, `io1`, `standard` and `st1`. See [EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[float]]:
        """
        The number of I/O operations per second (IOPS) that the volume supports
        """
        return pulumi.get(self, "iops")

    @iops.setter
    def iops(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "iops", value)

    @property
    @pulumi.getter(name="volumesPerInstance")
    def volumes_per_instance(self) -> Optional[pulumi.Input[float]]:
        """
        The number of EBS volumes with this configuration to attach to each EC2 instance in the instance group (default is 1)
        """
        return pulumi.get(self, "volumes_per_instance")

    @volumes_per_instance.setter
    def volumes_per_instance(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "volumes_per_instance", value)


@pulumi.input_type
class ClusterStepArgs:
    def __init__(__self__, *,
                 action_on_failure: pulumi.Input[str],
                 hadoop_jar_step: pulumi.Input['ClusterStepHadoopJarStepArgs'],
                 name: pulumi.Input[str]):
        """
        :param pulumi.Input[str] action_on_failure: The action to take if the step fails. Valid values: `TERMINATE_JOB_FLOW`, `TERMINATE_CLUSTER`, `CANCEL_AND_WAIT`, and `CONTINUE`
        :param pulumi.Input['ClusterStepHadoopJarStepArgs'] hadoop_jar_step: The JAR file used for the step. Defined below.
        :param pulumi.Input[str] name: The name of the step.
        """
        pulumi.set(__self__, "action_on_failure", action_on_failure)
        pulumi.set(__self__, "hadoop_jar_step", hadoop_jar_step)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="actionOnFailure")
    def action_on_failure(self) -> pulumi.Input[str]:
        """
        The action to take if the step fails. Valid values: `TERMINATE_JOB_FLOW`, `TERMINATE_CLUSTER`, `CANCEL_AND_WAIT`, and `CONTINUE`
        """
        return pulumi.get(self, "action_on_failure")

    @action_on_failure.setter
    def action_on_failure(self, value: pulumi.Input[str]):
        pulumi.set(self, "action_on_failure", value)

    @property
    @pulumi.getter(name="hadoopJarStep")
    def hadoop_jar_step(self) -> pulumi.Input['ClusterStepHadoopJarStepArgs']:
        """
        The JAR file used for the step. Defined below.
        """
        return pulumi.get(self, "hadoop_jar_step")

    @hadoop_jar_step.setter
    def hadoop_jar_step(self, value: pulumi.Input['ClusterStepHadoopJarStepArgs']):
        pulumi.set(self, "hadoop_jar_step", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the step.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class ClusterStepHadoopJarStepArgs:
    def __init__(__self__, *,
                 jar: pulumi.Input[str],
                 args: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 main_class: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] jar: Path to a JAR file run during the step.
        :param pulumi.Input[List[pulumi.Input[str]]] args: List of command line arguments passed to the JAR file's main function when executed.
        :param pulumi.Input[str] main_class: Name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: Key-Value map of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.
        """
        pulumi.set(__self__, "jar", jar)
        if args is not None:
            pulumi.set(__self__, "args", args)
        if main_class is not None:
            pulumi.set(__self__, "main_class", main_class)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter
    def jar(self) -> pulumi.Input[str]:
        """
        Path to a JAR file run during the step.
        """
        return pulumi.get(self, "jar")

    @jar.setter
    def jar(self, value: pulumi.Input[str]):
        pulumi.set(self, "jar", value)

    @property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[List[pulumi.Input[str]]]]:
        """
        List of command line arguments passed to the JAR file's main function when executed.
        """
        return pulumi.get(self, "args")

    @args.setter
    def args(self, value: Optional[pulumi.Input[List[pulumi.Input[str]]]]):
        pulumi.set(self, "args", value)

    @property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.
        """
        return pulumi.get(self, "main_class")

    @main_class.setter
    def main_class(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "main_class", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-Value map of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "properties", value)


@pulumi.input_type
class InstanceGroupEbsConfigArgs:
    def __init__(__self__, *,
                 size: pulumi.Input[float],
                 type: pulumi.Input[str],
                 iops: Optional[pulumi.Input[float]] = None,
                 volumes_per_instance: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[float] size: The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
        :param pulumi.Input[str] type: The volume type. Valid options are 'gp2', 'io1' and 'standard'.
        :param pulumi.Input[float] iops: The number of I/O operations per second (IOPS) that the volume supports.
        :param pulumi.Input[float] volumes_per_instance: The number of EBS Volumes to attach per instance.
        """
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "type", type)
        if iops is not None:
            pulumi.set(__self__, "iops", iops)
        if volumes_per_instance is not None:
            pulumi.set(__self__, "volumes_per_instance", volumes_per_instance)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[float]:
        """
        The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[float]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The volume type. Valid options are 'gp2', 'io1' and 'standard'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[float]]:
        """
        The number of I/O operations per second (IOPS) that the volume supports.
        """
        return pulumi.get(self, "iops")

    @iops.setter
    def iops(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "iops", value)

    @property
    @pulumi.getter(name="volumesPerInstance")
    def volumes_per_instance(self) -> Optional[pulumi.Input[float]]:
        """
        The number of EBS Volumes to attach per instance.
        """
        return pulumi.get(self, "volumes_per_instance")

    @volumes_per_instance.setter
    def volumes_per_instance(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "volumes_per_instance", value)


