// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ec2
{
    /// <summary>
    /// Provides a VPC/Subnet/ENI Flow Log to capture IP traffic for a specific network
    /// interface, subnet, or VPC. Logs are sent to a CloudWatch Log Group or a S3 Bucket.
    /// 
    /// ## Example Usage
    /// ### CloudWatch Logging
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var exampleLogGroup = new Aws.CloudWatch.LogGroup("exampleLogGroup", new Aws.CloudWatch.LogGroupArgs
    ///         {
    ///         });
    ///         var exampleRole = new Aws.Iam.Role("exampleRole", new Aws.Iam.RoleArgs
    ///         {
    ///             AssumeRolePolicy = @"{
    ///   ""Version"": ""2012-10-17"",
    ///   ""Statement"": [
    ///     {
    ///       ""Sid"": """",
    ///       ""Effect"": ""Allow"",
    ///       ""Principal"": {
    ///         ""Service"": ""vpc-flow-logs.amazonaws.com""
    ///       },
    ///       ""Action"": ""sts:AssumeRole""
    ///     }
    ///   ]
    /// }
    /// ",
    ///         });
    ///         var exampleFlowLog = new Aws.Ec2.FlowLog("exampleFlowLog", new Aws.Ec2.FlowLogArgs
    ///         {
    ///             IamRoleArn = exampleRole.Arn,
    ///             LogDestination = exampleLogGroup.Arn,
    ///             TrafficType = "ALL",
    ///             VpcId = aws_vpc.Example.Id,
    ///         });
    ///         var exampleRolePolicy = new Aws.Iam.RolePolicy("exampleRolePolicy", new Aws.Iam.RolePolicyArgs
    ///         {
    ///             Role = exampleRole.Id,
    ///             Policy = @"{
    ///   ""Version"": ""2012-10-17"",
    ///   ""Statement"": [
    ///     {
    ///       ""Action"": [
    ///         ""logs:CreateLogGroup"",
    ///         ""logs:CreateLogStream"",
    ///         ""logs:PutLogEvents"",
    ///         ""logs:DescribeLogGroups"",
    ///         ""logs:DescribeLogStreams""
    ///       ],
    ///       ""Effect"": ""Allow"",
    ///       ""Resource"": ""*""
    ///     }
    ///   ]
    /// }
    /// ",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ### S3 Logging
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var exampleBucket = new Aws.S3.Bucket("exampleBucket", new Aws.S3.BucketArgs
    ///         {
    ///         });
    ///         var exampleFlowLog = new Aws.Ec2.FlowLog("exampleFlowLog", new Aws.Ec2.FlowLogArgs
    ///         {
    ///             LogDestination = exampleBucket.Arn,
    ///             LogDestinationType = "s3",
    ///             TrafficType = "ALL",
    ///             VpcId = aws_vpc.Example.Id,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class FlowLog : Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of the Flow Log.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Elastic Network Interface ID to attach to
        /// </summary>
        [Output("eniId")]
        public Output<string?> EniId { get; private set; } = null!;

        /// <summary>
        /// The ARN for the IAM role that's used to post flow logs to a CloudWatch Logs log group
        /// </summary>
        [Output("iamRoleArn")]
        public Output<string?> IamRoleArn { get; private set; } = null!;

        /// <summary>
        /// The ARN of the logging destination.
        /// </summary>
        [Output("logDestination")]
        public Output<string> LogDestination { get; private set; } = null!;

        /// <summary>
        /// The type of the logging destination. Valid values: `cloud-watch-logs`, `s3`. Default: `cloud-watch-logs`.
        /// </summary>
        [Output("logDestinationType")]
        public Output<string?> LogDestinationType { get; private set; } = null!;

        /// <summary>
        /// The fields to include in the flow log record, in the order in which they should appear.
        /// </summary>
        [Output("logFormat")]
        public Output<string> LogFormat { get; private set; } = null!;

        /// <summary>
        /// *Deprecated:* Use `log_destination` instead. The name of the CloudWatch log group.
        /// </summary>
        [Output("logGroupName")]
        public Output<string> LogGroupName { get; private set; } = null!;

        /// <summary>
        /// The maximum interval of time
        /// during which a flow of packets is captured and aggregated into a flow
        /// log record. Valid Values: `60` seconds (1 minute) or `600` seconds (10
        /// minutes). Default: `600`.
        /// </summary>
        [Output("maxAggregationInterval")]
        public Output<int?> MaxAggregationInterval { get; private set; } = null!;

        /// <summary>
        /// Subnet ID to attach to
        /// </summary>
        [Output("subnetId")]
        public Output<string?> SubnetId { get; private set; } = null!;

        /// <summary>
        /// Key-value map of resource tags
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;

        /// <summary>
        /// The type of traffic to capture. Valid values: `ACCEPT`,`REJECT`, `ALL`.
        /// </summary>
        [Output("trafficType")]
        public Output<string> TrafficType { get; private set; } = null!;

        /// <summary>
        /// VPC ID to attach to
        /// </summary>
        [Output("vpcId")]
        public Output<string?> VpcId { get; private set; } = null!;


        /// <summary>
        /// Create a FlowLog resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FlowLog(string name, FlowLogArgs args, CustomResourceOptions? options = null)
            : base("aws:ec2/flowLog:FlowLog", name, args ?? new FlowLogArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FlowLog(string name, Input<string> id, FlowLogState? state = null, CustomResourceOptions? options = null)
            : base("aws:ec2/flowLog:FlowLog", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing FlowLog resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FlowLog Get(string name, Input<string> id, FlowLogState? state = null, CustomResourceOptions? options = null)
        {
            return new FlowLog(name, id, state, options);
        }
    }

    public sealed class FlowLogArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Elastic Network Interface ID to attach to
        /// </summary>
        [Input("eniId")]
        public Input<string>? EniId { get; set; }

        /// <summary>
        /// The ARN for the IAM role that's used to post flow logs to a CloudWatch Logs log group
        /// </summary>
        [Input("iamRoleArn")]
        public Input<string>? IamRoleArn { get; set; }

        /// <summary>
        /// The ARN of the logging destination.
        /// </summary>
        [Input("logDestination")]
        public Input<string>? LogDestination { get; set; }

        /// <summary>
        /// The type of the logging destination. Valid values: `cloud-watch-logs`, `s3`. Default: `cloud-watch-logs`.
        /// </summary>
        [Input("logDestinationType")]
        public Input<string>? LogDestinationType { get; set; }

        /// <summary>
        /// The fields to include in the flow log record, in the order in which they should appear.
        /// </summary>
        [Input("logFormat")]
        public Input<string>? LogFormat { get; set; }

        /// <summary>
        /// *Deprecated:* Use `log_destination` instead. The name of the CloudWatch log group.
        /// </summary>
        [Input("logGroupName")]
        public Input<string>? LogGroupName { get; set; }

        /// <summary>
        /// The maximum interval of time
        /// during which a flow of packets is captured and aggregated into a flow
        /// log record. Valid Values: `60` seconds (1 minute) or `600` seconds (10
        /// minutes). Default: `600`.
        /// </summary>
        [Input("maxAggregationInterval")]
        public Input<int>? MaxAggregationInterval { get; set; }

        /// <summary>
        /// Subnet ID to attach to
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// Key-value map of resource tags
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The type of traffic to capture. Valid values: `ACCEPT`,`REJECT`, `ALL`.
        /// </summary>
        [Input("trafficType", required: true)]
        public Input<string> TrafficType { get; set; } = null!;

        /// <summary>
        /// VPC ID to attach to
        /// </summary>
        [Input("vpcId")]
        public Input<string>? VpcId { get; set; }

        public FlowLogArgs()
        {
        }
    }

    public sealed class FlowLogState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN of the Flow Log.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// Elastic Network Interface ID to attach to
        /// </summary>
        [Input("eniId")]
        public Input<string>? EniId { get; set; }

        /// <summary>
        /// The ARN for the IAM role that's used to post flow logs to a CloudWatch Logs log group
        /// </summary>
        [Input("iamRoleArn")]
        public Input<string>? IamRoleArn { get; set; }

        /// <summary>
        /// The ARN of the logging destination.
        /// </summary>
        [Input("logDestination")]
        public Input<string>? LogDestination { get; set; }

        /// <summary>
        /// The type of the logging destination. Valid values: `cloud-watch-logs`, `s3`. Default: `cloud-watch-logs`.
        /// </summary>
        [Input("logDestinationType")]
        public Input<string>? LogDestinationType { get; set; }

        /// <summary>
        /// The fields to include in the flow log record, in the order in which they should appear.
        /// </summary>
        [Input("logFormat")]
        public Input<string>? LogFormat { get; set; }

        /// <summary>
        /// *Deprecated:* Use `log_destination` instead. The name of the CloudWatch log group.
        /// </summary>
        [Input("logGroupName")]
        public Input<string>? LogGroupName { get; set; }

        /// <summary>
        /// The maximum interval of time
        /// during which a flow of packets is captured and aggregated into a flow
        /// log record. Valid Values: `60` seconds (1 minute) or `600` seconds (10
        /// minutes). Default: `600`.
        /// </summary>
        [Input("maxAggregationInterval")]
        public Input<int>? MaxAggregationInterval { get; set; }

        /// <summary>
        /// Subnet ID to attach to
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// Key-value map of resource tags
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The type of traffic to capture. Valid values: `ACCEPT`,`REJECT`, `ALL`.
        /// </summary>
        [Input("trafficType")]
        public Input<string>? TrafficType { get; set; }

        /// <summary>
        /// VPC ID to attach to
        /// </summary>
        [Input("vpcId")]
        public Input<string>? VpcId { get; set; }

        public FlowLogState()
        {
        }
    }
}
