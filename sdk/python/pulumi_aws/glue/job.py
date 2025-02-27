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

__all__ = ['Job']


class Job(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 command: Optional[pulumi.Input[pulumi.InputType['JobCommandArgs']]] = None,
                 connections: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 default_arguments: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 execution_property: Optional[pulumi.Input[pulumi.InputType['JobExecutionPropertyArgs']]] = None,
                 glue_version: Optional[pulumi.Input[str]] = None,
                 max_capacity: Optional[pulumi.Input[float]] = None,
                 max_retries: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_property: Optional[pulumi.Input[pulumi.InputType['JobNotificationPropertyArgs']]] = None,
                 number_of_workers: Optional[pulumi.Input[float]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 security_configuration: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeout: Optional[pulumi.Input[float]] = None,
                 worker_type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Glue Job resource.

        > Glue functionality, such as monitoring and logging of jobs, is typically managed with the `default_arguments` argument. See the [Special Parameters Used by AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html) topic in the Glue developer guide for additional information.

        ## Example Usage
        ### Python Job

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Job("example",
            role_arn=aws_iam_role["example"]["arn"],
            command=aws.glue.JobCommandArgs(
                script_location=f"s3://{aws_s3_bucket['example']['bucket']}/example.py",
            ))
        ```
        ### Scala Job

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Job("example",
            role_arn=aws_iam_role["example"]["arn"],
            command=aws.glue.JobCommandArgs(
                script_location=f"s3://{aws_s3_bucket['example']['bucket']}/example.scala",
            ),
            default_arguments={
                "--job-language": "scala",
            })
        ```
        ### Enabling CloudWatch Logs and Metrics

        ```python
        import pulumi
        import pulumi_aws as aws

        example_log_group = aws.cloudwatch.LogGroup("exampleLogGroup", retention_in_days=14)
        # ... other configuration ...
        example_job = aws.glue.Job("exampleJob", default_arguments={
            "--continuous-log-logGroup": example_log_group.name,
            "--enable-continuous-cloudwatch-log": "true",
            "--enable-continuous-log-filter": "true",
            "--enable-metrics": "",
        })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['JobCommandArgs']] command: The command of the job. Defined below.
        :param pulumi.Input[List[pulumi.Input[str]]] connections: The list of connections used for this job.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] default_arguments: The map of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. For information about how to specify and consume your own Job arguments, see the [Calling AWS Glue APIs in Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide. For information about the key-value pairs that AWS Glue consumes to set up your job, see the [Special Parameters Used by AWS Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-glue-arguments.html) topic in the developer guide.
        :param pulumi.Input[str] description: Description of the job.
        :param pulumi.Input[pulumi.InputType['JobExecutionPropertyArgs']] execution_property: Execution property of the job. Defined below.
        :param pulumi.Input[str] glue_version: The version of glue to use, for example "1.0". For information about available versions, see the [AWS Glue Release Notes](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html).
        :param pulumi.Input[float] max_capacity: The maximum number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. `Required` when `pythonshell` is set, accept either `0.0625` or `1.0`.
        :param pulumi.Input[float] max_retries: The maximum number of times to retry this job if it fails.
        :param pulumi.Input[str] name: The name you assign to this job. It must be unique in your account.
        :param pulumi.Input[pulumi.InputType['JobNotificationPropertyArgs']] notification_property: Notification property of the job. Defined below.
        :param pulumi.Input[float] number_of_workers: The number of workers of a defined workerType that are allocated when a job runs.
        :param pulumi.Input[str] role_arn: The ARN of the IAM role associated with this job.
        :param pulumi.Input[str] security_configuration: The name of the Security Configuration to be associated with the job.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        :param pulumi.Input[float] timeout: The job timeout in minutes. The default is 2880 minutes (48 hours).
        :param pulumi.Input[str] worker_type: The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.
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

            if command is None:
                raise TypeError("Missing required property 'command'")
            __props__['command'] = command
            __props__['connections'] = connections
            __props__['default_arguments'] = default_arguments
            __props__['description'] = description
            __props__['execution_property'] = execution_property
            __props__['glue_version'] = glue_version
            __props__['max_capacity'] = max_capacity
            __props__['max_retries'] = max_retries
            __props__['name'] = name
            __props__['notification_property'] = notification_property
            __props__['number_of_workers'] = number_of_workers
            if role_arn is None:
                raise TypeError("Missing required property 'role_arn'")
            __props__['role_arn'] = role_arn
            __props__['security_configuration'] = security_configuration
            __props__['tags'] = tags
            __props__['timeout'] = timeout
            __props__['worker_type'] = worker_type
            __props__['arn'] = None
        super(Job, __self__).__init__(
            'aws:glue/job:Job',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            command: Optional[pulumi.Input[pulumi.InputType['JobCommandArgs']]] = None,
            connections: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            default_arguments: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            execution_property: Optional[pulumi.Input[pulumi.InputType['JobExecutionPropertyArgs']]] = None,
            glue_version: Optional[pulumi.Input[str]] = None,
            max_capacity: Optional[pulumi.Input[float]] = None,
            max_retries: Optional[pulumi.Input[float]] = None,
            name: Optional[pulumi.Input[str]] = None,
            notification_property: Optional[pulumi.Input[pulumi.InputType['JobNotificationPropertyArgs']]] = None,
            number_of_workers: Optional[pulumi.Input[float]] = None,
            role_arn: Optional[pulumi.Input[str]] = None,
            security_configuration: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            timeout: Optional[pulumi.Input[float]] = None,
            worker_type: Optional[pulumi.Input[str]] = None) -> 'Job':
        """
        Get an existing Job resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of Glue Job
        :param pulumi.Input[pulumi.InputType['JobCommandArgs']] command: The command of the job. Defined below.
        :param pulumi.Input[List[pulumi.Input[str]]] connections: The list of connections used for this job.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] default_arguments: The map of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. For information about how to specify and consume your own Job arguments, see the [Calling AWS Glue APIs in Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide. For information about the key-value pairs that AWS Glue consumes to set up your job, see the [Special Parameters Used by AWS Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-glue-arguments.html) topic in the developer guide.
        :param pulumi.Input[str] description: Description of the job.
        :param pulumi.Input[pulumi.InputType['JobExecutionPropertyArgs']] execution_property: Execution property of the job. Defined below.
        :param pulumi.Input[str] glue_version: The version of glue to use, for example "1.0". For information about available versions, see the [AWS Glue Release Notes](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html).
        :param pulumi.Input[float] max_capacity: The maximum number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. `Required` when `pythonshell` is set, accept either `0.0625` or `1.0`.
        :param pulumi.Input[float] max_retries: The maximum number of times to retry this job if it fails.
        :param pulumi.Input[str] name: The name you assign to this job. It must be unique in your account.
        :param pulumi.Input[pulumi.InputType['JobNotificationPropertyArgs']] notification_property: Notification property of the job. Defined below.
        :param pulumi.Input[float] number_of_workers: The number of workers of a defined workerType that are allocated when a job runs.
        :param pulumi.Input[str] role_arn: The ARN of the IAM role associated with this job.
        :param pulumi.Input[str] security_configuration: The name of the Security Configuration to be associated with the job.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        :param pulumi.Input[float] timeout: The job timeout in minutes. The default is 2880 minutes (48 hours).
        :param pulumi.Input[str] worker_type: The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["command"] = command
        __props__["connections"] = connections
        __props__["default_arguments"] = default_arguments
        __props__["description"] = description
        __props__["execution_property"] = execution_property
        __props__["glue_version"] = glue_version
        __props__["max_capacity"] = max_capacity
        __props__["max_retries"] = max_retries
        __props__["name"] = name
        __props__["notification_property"] = notification_property
        __props__["number_of_workers"] = number_of_workers
        __props__["role_arn"] = role_arn
        __props__["security_configuration"] = security_configuration
        __props__["tags"] = tags
        __props__["timeout"] = timeout
        __props__["worker_type"] = worker_type
        return Job(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of Glue Job
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def command(self) -> pulumi.Output['outputs.JobCommand']:
        """
        The command of the job. Defined below.
        """
        return pulumi.get(self, "command")

    @property
    @pulumi.getter
    def connections(self) -> pulumi.Output[Optional[List[str]]]:
        """
        The list of connections used for this job.
        """
        return pulumi.get(self, "connections")

    @property
    @pulumi.getter(name="defaultArguments")
    def default_arguments(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The map of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. For information about how to specify and consume your own Job arguments, see the [Calling AWS Glue APIs in Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide. For information about the key-value pairs that AWS Glue consumes to set up your job, see the [Special Parameters Used by AWS Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-glue-arguments.html) topic in the developer guide.
        """
        return pulumi.get(self, "default_arguments")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the job.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="executionProperty")
    def execution_property(self) -> pulumi.Output['outputs.JobExecutionProperty']:
        """
        Execution property of the job. Defined below.
        """
        return pulumi.get(self, "execution_property")

    @property
    @pulumi.getter(name="glueVersion")
    def glue_version(self) -> pulumi.Output[str]:
        """
        The version of glue to use, for example "1.0". For information about available versions, see the [AWS Glue Release Notes](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html).
        """
        return pulumi.get(self, "glue_version")

    @property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> pulumi.Output[float]:
        """
        The maximum number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. `Required` when `pythonshell` is set, accept either `0.0625` or `1.0`.
        """
        return pulumi.get(self, "max_capacity")

    @property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> pulumi.Output[Optional[float]]:
        """
        The maximum number of times to retry this job if it fails.
        """
        return pulumi.get(self, "max_retries")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name you assign to this job. It must be unique in your account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationProperty")
    def notification_property(self) -> pulumi.Output['outputs.JobNotificationProperty']:
        """
        Notification property of the job. Defined below.
        """
        return pulumi.get(self, "notification_property")

    @property
    @pulumi.getter(name="numberOfWorkers")
    def number_of_workers(self) -> pulumi.Output[Optional[float]]:
        """
        The number of workers of a defined workerType that are allocated when a job runs.
        """
        return pulumi.get(self, "number_of_workers")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the IAM role associated with this job.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="securityConfiguration")
    def security_configuration(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the Security Configuration to be associated with the job.
        """
        return pulumi.get(self, "security_configuration")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional[float]]:
        """
        The job timeout in minutes. The default is 2880 minutes (48 hours).
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter(name="workerType")
    def worker_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.
        """
        return pulumi.get(self, "worker_type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

