# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['Configuration']


class Configuration(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 engine_type: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an MQ Configuration Resource.

        For more information on Amazon MQ, see [Amazon MQ documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.mq.Configuration("example",
            data=\"\"\"<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <broker xmlns="http://activemq.apache.org/schema/core">
          <plugins>
            <forcePersistencyModeBrokerPlugin persistenceFlag="true"/>
            <statisticsBrokerPlugin/>
            <timeStampingBrokerPlugin ttlCeiling="86400000" zeroExpirationOverride="86400000"/>
          </plugins>
        </broker>

        \"\"\",
            description="Example Configuration",
            engine_type="ActiveMQ",
            engine_version="5.15.0")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data: The broker configuration in XML format.
               See [official docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html)
               for supported parameters and format of the XML.
        :param pulumi.Input[str] description: The description of the configuration.
        :param pulumi.Input[str] engine_type: The type of broker engine.
        :param pulumi.Input[str] engine_version: The version of the broker engine.
        :param pulumi.Input[str] name: The name of the configuration
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

            if data is None:
                raise TypeError("Missing required property 'data'")
            __props__['data'] = data
            __props__['description'] = description
            if engine_type is None:
                raise TypeError("Missing required property 'engine_type'")
            __props__['engine_type'] = engine_type
            if engine_version is None:
                raise TypeError("Missing required property 'engine_version'")
            __props__['engine_version'] = engine_version
            __props__['name'] = name
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['latest_revision'] = None
        super(Configuration, __self__).__init__(
            'aws:mq/configuration:Configuration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            data: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            engine_type: Optional[pulumi.Input[str]] = None,
            engine_version: Optional[pulumi.Input[str]] = None,
            latest_revision: Optional[pulumi.Input[float]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Configuration':
        """
        Get an existing Configuration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the configuration.
        :param pulumi.Input[str] data: The broker configuration in XML format.
               See [official docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html)
               for supported parameters and format of the XML.
        :param pulumi.Input[str] description: The description of the configuration.
        :param pulumi.Input[str] engine_type: The type of broker engine.
        :param pulumi.Input[str] engine_version: The version of the broker engine.
        :param pulumi.Input[float] latest_revision: The latest revision of the configuration.
        :param pulumi.Input[str] name: The name of the configuration
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["data"] = data
        __props__["description"] = description
        __props__["engine_type"] = engine_type
        __props__["engine_version"] = engine_version
        __props__["latest_revision"] = latest_revision
        __props__["name"] = name
        __props__["tags"] = tags
        return Configuration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the configuration.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def data(self) -> pulumi.Output[str]:
        """
        The broker configuration in XML format.
        See [official docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html)
        for supported parameters and format of the XML.
        """
        return pulumi.get(self, "data")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the configuration.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> pulumi.Output[str]:
        """
        The type of broker engine.
        """
        return pulumi.get(self, "engine_type")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[str]:
        """
        The version of the broker engine.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="latestRevision")
    def latest_revision(self) -> pulumi.Output[float]:
        """
        The latest revision of the configuration.
        """
        return pulumi.get(self, "latest_revision")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the configuration
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

