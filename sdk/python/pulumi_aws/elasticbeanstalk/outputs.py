# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'ApplicationAppversionLifecycle',
    'ConfigurationTemplateSetting',
    'EnvironmentAllSetting',
    'EnvironmentSetting',
    'GetApplicationAppversionLifecycleResult',
]

@pulumi.output_type
class ApplicationAppversionLifecycle(dict):
    def __init__(__self__, *,
                 service_role: str,
                 delete_source_from_s3: Optional[bool] = None,
                 max_age_in_days: Optional[float] = None,
                 max_count: Optional[float] = None):
        """
        :param str service_role: The ARN of an IAM service role under which the application version is deleted.  Elastic Beanstalk must have permission to assume this role.
        :param bool delete_source_from_s3: Set to `true` to delete a version's source bundle from S3 when the application version is deleted.
        :param float max_age_in_days: The number of days to retain an application version ('max_age_in_days' and 'max_count' cannot be enabled simultaneously.).
        :param float max_count: The maximum number of application versions to retain ('max_age_in_days' and 'max_count' cannot be enabled simultaneously.).
        """
        pulumi.set(__self__, "service_role", service_role)
        if delete_source_from_s3 is not None:
            pulumi.set(__self__, "delete_source_from_s3", delete_source_from_s3)
        if max_age_in_days is not None:
            pulumi.set(__self__, "max_age_in_days", max_age_in_days)
        if max_count is not None:
            pulumi.set(__self__, "max_count", max_count)

    @property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> str:
        """
        The ARN of an IAM service role under which the application version is deleted.  Elastic Beanstalk must have permission to assume this role.
        """
        return pulumi.get(self, "service_role")

    @property
    @pulumi.getter(name="deleteSourceFromS3")
    def delete_source_from_s3(self) -> Optional[bool]:
        """
        Set to `true` to delete a version's source bundle from S3 when the application version is deleted.
        """
        return pulumi.get(self, "delete_source_from_s3")

    @property
    @pulumi.getter(name="maxAgeInDays")
    def max_age_in_days(self) -> Optional[float]:
        """
        The number of days to retain an application version ('max_age_in_days' and 'max_count' cannot be enabled simultaneously.).
        """
        return pulumi.get(self, "max_age_in_days")

    @property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[float]:
        """
        The maximum number of application versions to retain ('max_age_in_days' and 'max_count' cannot be enabled simultaneously.).
        """
        return pulumi.get(self, "max_count")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ConfigurationTemplateSetting(dict):
    def __init__(__self__, *,
                 name: str,
                 namespace: str,
                 value: str,
                 resource: Optional[str] = None):
        """
        :param str name: A unique name for this Template.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "value", value)
        if resource is not None:
            pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A unique name for this Template.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")

    @property
    @pulumi.getter
    def resource(self) -> Optional[str]:
        return pulumi.get(self, "resource")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EnvironmentAllSetting(dict):
    def __init__(__self__, *,
                 name: str,
                 namespace: str,
                 value: str,
                 resource: Optional[str] = None):
        """
        :param str name: A unique name for this Environment. This name is used
               in the application URL
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "value", value)
        if resource is not None:
            pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A unique name for this Environment. This name is used
        in the application URL
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")

    @property
    @pulumi.getter
    def resource(self) -> Optional[str]:
        return pulumi.get(self, "resource")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EnvironmentSetting(dict):
    def __init__(__self__, *,
                 name: str,
                 namespace: str,
                 value: str,
                 resource: Optional[str] = None):
        """
        :param str name: A unique name for this Environment. This name is used
               in the application URL
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "value", value)
        if resource is not None:
            pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A unique name for this Environment. This name is used
        in the application URL
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")

    @property
    @pulumi.getter
    def resource(self) -> Optional[str]:
        return pulumi.get(self, "resource")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetApplicationAppversionLifecycleResult(dict):
    def __init__(__self__, *,
                 delete_source_from_s3: bool,
                 max_age_in_days: float,
                 max_count: float,
                 service_role: str):
        """
        :param bool delete_source_from_s3: Specifies whether delete a version's source bundle from S3 when the application version is deleted.
        :param float max_age_in_days: The number of days to retain an application version.
        :param float max_count: The maximum number of application versions to retain.
        :param str service_role: The ARN of an IAM service role under which the application version is deleted.  Elastic Beanstalk must have permission to assume this role.
        """
        pulumi.set(__self__, "delete_source_from_s3", delete_source_from_s3)
        pulumi.set(__self__, "max_age_in_days", max_age_in_days)
        pulumi.set(__self__, "max_count", max_count)
        pulumi.set(__self__, "service_role", service_role)

    @property
    @pulumi.getter(name="deleteSourceFromS3")
    def delete_source_from_s3(self) -> bool:
        """
        Specifies whether delete a version's source bundle from S3 when the application version is deleted.
        """
        return pulumi.get(self, "delete_source_from_s3")

    @property
    @pulumi.getter(name="maxAgeInDays")
    def max_age_in_days(self) -> float:
        """
        The number of days to retain an application version.
        """
        return pulumi.get(self, "max_age_in_days")

    @property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> float:
        """
        The maximum number of application versions to retain.
        """
        return pulumi.get(self, "max_count")

    @property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> str:
        """
        The ARN of an IAM service role under which the application version is deleted.  Elastic Beanstalk must have permission to assume this role.
        """
        return pulumi.get(self, "service_role")


