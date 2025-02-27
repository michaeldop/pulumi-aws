# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['Model']


class Model(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rest_api: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Model for a REST API Gateway.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        my_demo_api = aws.apigateway.RestApi("myDemoAPI", description="This is my API for demonstration purposes")
        my_demo_model = aws.apigateway.Model("myDemoModel",
            rest_api=my_demo_api.id,
            description="a JSON schema",
            content_type="application/json",
            schema=\"\"\"{
          "type": "object"
        }
        \"\"\")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content_type: The content type of the model
        :param pulumi.Input[str] description: The description of the model
        :param pulumi.Input[str] name: The name of the model
        :param pulumi.Input[str] rest_api: The ID of the associated REST API
        :param pulumi.Input[str] schema: The schema of the model in a JSON form
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

            if content_type is None:
                raise TypeError("Missing required property 'content_type'")
            __props__['content_type'] = content_type
            __props__['description'] = description
            __props__['name'] = name
            if rest_api is None:
                raise TypeError("Missing required property 'rest_api'")
            __props__['rest_api'] = rest_api
            __props__['schema'] = schema
        super(Model, __self__).__init__(
            'aws:apigateway/model:Model',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            content_type: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            rest_api: Optional[pulumi.Input[str]] = None,
            schema: Optional[pulumi.Input[str]] = None) -> 'Model':
        """
        Get an existing Model resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content_type: The content type of the model
        :param pulumi.Input[str] description: The description of the model
        :param pulumi.Input[str] name: The name of the model
        :param pulumi.Input[str] rest_api: The ID of the associated REST API
        :param pulumi.Input[str] schema: The schema of the model in a JSON form
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["content_type"] = content_type
        __props__["description"] = description
        __props__["name"] = name
        __props__["rest_api"] = rest_api
        __props__["schema"] = schema
        return Model(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[str]:
        """
        The content type of the model
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the model
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the model
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Output[str]:
        """
        The ID of the associated REST API
        """
        return pulumi.get(self, "rest_api")

    @property
    @pulumi.getter
    def schema(self) -> pulumi.Output[Optional[str]]:
        """
        The schema of the model in a JSON form
        """
        return pulumi.get(self, "schema")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

