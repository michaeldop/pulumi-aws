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

__all__ = ['AmiFromInstance']


class AmiFromInstance(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ebs_block_devices: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['AmiFromInstanceEbsBlockDeviceArgs']]]]] = None,
                 ephemeral_block_devices: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['AmiFromInstanceEphemeralBlockDeviceArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 snapshot_without_reboot: Optional[pulumi.Input[bool]] = None,
                 source_instance_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The "AMI from instance" resource allows the creation of an Amazon Machine
        Image (AMI) modelled after an existing EBS-backed EC2 instance.

        The created AMI will refer to implicitly-created snapshots of the instance's
        EBS volumes and mimick its assigned block device configuration at the time
        the resource is created.

        This resource is best applied to an instance that is stopped when this instance
        is created, so that the contents of the created image are predictable. When
        applied to an instance that is running, *the instance will be stopped before taking
        the snapshots and then started back up again*, resulting in a period of
        downtime.

        Note that the source instance is inspected only at the initial creation of this
        resource. Ongoing updates to the referenced instance will not be propagated into
        the generated AMI. Users may taint or otherwise recreate the resource in order
        to produce a fresh snapshot.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2.AmiFromInstance("example", source_instance_id="i-xxxxxxxx")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A longer, human-readable description for the AMI.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['AmiFromInstanceEbsBlockDeviceArgs']]]] ebs_block_devices: Nested block describing an EBS block device that should be
               attached to created instances. The structure of this block is described below.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['AmiFromInstanceEphemeralBlockDeviceArgs']]]] ephemeral_block_devices: Nested block describing an ephemeral block device that
               should be attached to created instances. The structure of this block is described below.
        :param pulumi.Input[str] name: A region-unique name for the AMI.
        :param pulumi.Input[bool] snapshot_without_reboot: Boolean that overrides the behavior of stopping
               the instance before snapshotting. This is risky since it may cause a snapshot of an
               inconsistent filesystem state, but can be used to avoid downtime if the user otherwise
               guarantees that no filesystem writes will be underway at the time of snapshot.
        :param pulumi.Input[str] source_instance_id: The id of the instance to use as the basis of the AMI.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
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

            __props__['description'] = description
            __props__['ebs_block_devices'] = ebs_block_devices
            __props__['ephemeral_block_devices'] = ephemeral_block_devices
            __props__['name'] = name
            __props__['snapshot_without_reboot'] = snapshot_without_reboot
            if source_instance_id is None:
                raise TypeError("Missing required property 'source_instance_id'")
            __props__['source_instance_id'] = source_instance_id
            __props__['tags'] = tags
            __props__['architecture'] = None
            __props__['arn'] = None
            __props__['ena_support'] = None
            __props__['image_location'] = None
            __props__['kernel_id'] = None
            __props__['manage_ebs_snapshots'] = None
            __props__['ramdisk_id'] = None
            __props__['root_device_name'] = None
            __props__['root_snapshot_id'] = None
            __props__['sriov_net_support'] = None
            __props__['virtualization_type'] = None
        super(AmiFromInstance, __self__).__init__(
            'aws:ec2/amiFromInstance:AmiFromInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            architecture: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            ebs_block_devices: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['AmiFromInstanceEbsBlockDeviceArgs']]]]] = None,
            ena_support: Optional[pulumi.Input[bool]] = None,
            ephemeral_block_devices: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['AmiFromInstanceEphemeralBlockDeviceArgs']]]]] = None,
            image_location: Optional[pulumi.Input[str]] = None,
            kernel_id: Optional[pulumi.Input[str]] = None,
            manage_ebs_snapshots: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            ramdisk_id: Optional[pulumi.Input[str]] = None,
            root_device_name: Optional[pulumi.Input[str]] = None,
            root_snapshot_id: Optional[pulumi.Input[str]] = None,
            snapshot_without_reboot: Optional[pulumi.Input[bool]] = None,
            source_instance_id: Optional[pulumi.Input[str]] = None,
            sriov_net_support: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            virtualization_type: Optional[pulumi.Input[str]] = None) -> 'AmiFromInstance':
        """
        Get an existing AmiFromInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] architecture: Machine architecture for created instances. Defaults to "x86_64".
        :param pulumi.Input[str] arn: The ARN of the AMI.
        :param pulumi.Input[str] description: A longer, human-readable description for the AMI.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['AmiFromInstanceEbsBlockDeviceArgs']]]] ebs_block_devices: Nested block describing an EBS block device that should be
               attached to created instances. The structure of this block is described below.
        :param pulumi.Input[bool] ena_support: Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['AmiFromInstanceEphemeralBlockDeviceArgs']]]] ephemeral_block_devices: Nested block describing an ephemeral block device that
               should be attached to created instances. The structure of this block is described below.
        :param pulumi.Input[str] image_location: Path to an S3 object containing an image manifest, e.g. created
               by the `ec2-upload-bundle` command in the EC2 command line tools.
        :param pulumi.Input[str] kernel_id: The id of the kernel image (AKI) that will be used as the paravirtual
               kernel in created instances.
        :param pulumi.Input[str] name: A region-unique name for the AMI.
        :param pulumi.Input[str] ramdisk_id: The id of an initrd image (ARI) that will be used when booting the
               created instances.
        :param pulumi.Input[str] root_device_name: The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).
        :param pulumi.Input[bool] snapshot_without_reboot: Boolean that overrides the behavior of stopping
               the instance before snapshotting. This is risky since it may cause a snapshot of an
               inconsistent filesystem state, but can be used to avoid downtime if the user otherwise
               guarantees that no filesystem writes will be underway at the time of snapshot.
        :param pulumi.Input[str] source_instance_id: The id of the instance to use as the basis of the AMI.
        :param pulumi.Input[str] sriov_net_support: When set to "simple" (the default), enables enhanced networking
               for created instances. No other value is supported at this time.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] virtualization_type: Keyword to choose what virtualization mode created instances
               will use. Can be either "paravirtual" (the default) or "hvm". The choice of virtualization type
               changes the set of further arguments that are required, as described below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["architecture"] = architecture
        __props__["arn"] = arn
        __props__["description"] = description
        __props__["ebs_block_devices"] = ebs_block_devices
        __props__["ena_support"] = ena_support
        __props__["ephemeral_block_devices"] = ephemeral_block_devices
        __props__["image_location"] = image_location
        __props__["kernel_id"] = kernel_id
        __props__["manage_ebs_snapshots"] = manage_ebs_snapshots
        __props__["name"] = name
        __props__["ramdisk_id"] = ramdisk_id
        __props__["root_device_name"] = root_device_name
        __props__["root_snapshot_id"] = root_snapshot_id
        __props__["snapshot_without_reboot"] = snapshot_without_reboot
        __props__["source_instance_id"] = source_instance_id
        __props__["sriov_net_support"] = sriov_net_support
        __props__["tags"] = tags
        __props__["virtualization_type"] = virtualization_type
        return AmiFromInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def architecture(self) -> pulumi.Output[str]:
        """
        Machine architecture for created instances. Defaults to "x86_64".
        """
        return pulumi.get(self, "architecture")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the AMI.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A longer, human-readable description for the AMI.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ebsBlockDevices")
    def ebs_block_devices(self) -> pulumi.Output[List['outputs.AmiFromInstanceEbsBlockDevice']]:
        """
        Nested block describing an EBS block device that should be
        attached to created instances. The structure of this block is described below.
        """
        return pulumi.get(self, "ebs_block_devices")

    @property
    @pulumi.getter(name="enaSupport")
    def ena_support(self) -> pulumi.Output[bool]:
        """
        Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.
        """
        return pulumi.get(self, "ena_support")

    @property
    @pulumi.getter(name="ephemeralBlockDevices")
    def ephemeral_block_devices(self) -> pulumi.Output[List['outputs.AmiFromInstanceEphemeralBlockDevice']]:
        """
        Nested block describing an ephemeral block device that
        should be attached to created instances. The structure of this block is described below.
        """
        return pulumi.get(self, "ephemeral_block_devices")

    @property
    @pulumi.getter(name="imageLocation")
    def image_location(self) -> pulumi.Output[str]:
        """
        Path to an S3 object containing an image manifest, e.g. created
        by the `ec2-upload-bundle` command in the EC2 command line tools.
        """
        return pulumi.get(self, "image_location")

    @property
    @pulumi.getter(name="kernelId")
    def kernel_id(self) -> pulumi.Output[str]:
        """
        The id of the kernel image (AKI) that will be used as the paravirtual
        kernel in created instances.
        """
        return pulumi.get(self, "kernel_id")

    @property
    @pulumi.getter(name="manageEbsSnapshots")
    def manage_ebs_snapshots(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "manage_ebs_snapshots")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A region-unique name for the AMI.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ramdiskId")
    def ramdisk_id(self) -> pulumi.Output[str]:
        """
        The id of an initrd image (ARI) that will be used when booting the
        created instances.
        """
        return pulumi.get(self, "ramdisk_id")

    @property
    @pulumi.getter(name="rootDeviceName")
    def root_device_name(self) -> pulumi.Output[str]:
        """
        The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).
        """
        return pulumi.get(self, "root_device_name")

    @property
    @pulumi.getter(name="rootSnapshotId")
    def root_snapshot_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "root_snapshot_id")

    @property
    @pulumi.getter(name="snapshotWithoutReboot")
    def snapshot_without_reboot(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean that overrides the behavior of stopping
        the instance before snapshotting. This is risky since it may cause a snapshot of an
        inconsistent filesystem state, but can be used to avoid downtime if the user otherwise
        guarantees that no filesystem writes will be underway at the time of snapshot.
        """
        return pulumi.get(self, "snapshot_without_reboot")

    @property
    @pulumi.getter(name="sourceInstanceId")
    def source_instance_id(self) -> pulumi.Output[str]:
        """
        The id of the instance to use as the basis of the AMI.
        """
        return pulumi.get(self, "source_instance_id")

    @property
    @pulumi.getter(name="sriovNetSupport")
    def sriov_net_support(self) -> pulumi.Output[str]:
        """
        When set to "simple" (the default), enables enhanced networking
        for created instances. No other value is supported at this time.
        """
        return pulumi.get(self, "sriov_net_support")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="virtualizationType")
    def virtualization_type(self) -> pulumi.Output[str]:
        """
        Keyword to choose what virtualization mode created instances
        will use. Can be either "paravirtual" (the default) or "hvm". The choice of virtualization type
        changes the set of further arguments that are required, as described below.
        """
        return pulumi.get(self, "virtualization_type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

