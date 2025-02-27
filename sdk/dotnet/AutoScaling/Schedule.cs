// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.AutoScaling
{
    /// <summary>
    /// Provides an AutoScaling Schedule resource.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var foobarGroup = new Aws.AutoScaling.Group("foobarGroup", new Aws.AutoScaling.GroupArgs
    ///         {
    ///             AvailabilityZones = 
    ///             {
    ///                 "us-west-2a",
    ///             },
    ///             MaxSize = 1,
    ///             MinSize = 1,
    ///             HealthCheckGracePeriod = 300,
    ///             HealthCheckType = "ELB",
    ///             ForceDelete = true,
    ///             TerminationPolicies = 
    ///             {
    ///                 "OldestInstance",
    ///             },
    ///         });
    ///         var foobarSchedule = new Aws.AutoScaling.Schedule("foobarSchedule", new Aws.AutoScaling.ScheduleArgs
    ///         {
    ///             ScheduledActionName = "foobar",
    ///             MinSize = 0,
    ///             MaxSize = 1,
    ///             DesiredCapacity = 0,
    ///             StartTime = "2016-12-11T18:00:00Z",
    ///             EndTime = "2016-12-12T06:00:00Z",
    ///             AutoscalingGroupName = foobarGroup.Name,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class Schedule : Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN assigned by AWS to the autoscaling schedule.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The name or Amazon Resource Name (ARN) of the Auto Scaling group.
        /// </summary>
        [Output("autoscalingGroupName")]
        public Output<string> AutoscalingGroupName { get; private set; } = null!;

        /// <summary>
        /// The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don't want to change the desired capacity at the scheduled time.
        /// </summary>
        [Output("desiredCapacity")]
        public Output<int> DesiredCapacity { get; private set; } = null!;

        /// <summary>
        /// The time for this action to end, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
        /// If you try to schedule your action in the past, Auto Scaling returns an error message.
        /// </summary>
        [Output("endTime")]
        public Output<string> EndTime { get; private set; } = null!;

        /// <summary>
        /// The maximum size for the Auto Scaling group. Default 0.
        /// Set to -1 if you don't want to change the maximum size at the scheduled time.
        /// </summary>
        [Output("maxSize")]
        public Output<int> MaxSize { get; private set; } = null!;

        /// <summary>
        /// The minimum size for the Auto Scaling group. Default 0.
        /// Set to -1 if you don't want to change the minimum size at the scheduled time.
        /// </summary>
        [Output("minSize")]
        public Output<int> MinSize { get; private set; } = null!;

        /// <summary>
        /// The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
        /// </summary>
        [Output("recurrence")]
        public Output<string> Recurrence { get; private set; } = null!;

        /// <summary>
        /// The name of this scaling action.
        /// </summary>
        [Output("scheduledActionName")]
        public Output<string> ScheduledActionName { get; private set; } = null!;

        /// <summary>
        /// The time for this action to start, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
        /// If you try to schedule your action in the past, Auto Scaling returns an error message.
        /// </summary>
        [Output("startTime")]
        public Output<string> StartTime { get; private set; } = null!;


        /// <summary>
        /// Create a Schedule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Schedule(string name, ScheduleArgs args, CustomResourceOptions? options = null)
            : base("aws:autoscaling/schedule:Schedule", name, args ?? new ScheduleArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Schedule(string name, Input<string> id, ScheduleState? state = null, CustomResourceOptions? options = null)
            : base("aws:autoscaling/schedule:Schedule", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Schedule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Schedule Get(string name, Input<string> id, ScheduleState? state = null, CustomResourceOptions? options = null)
        {
            return new Schedule(name, id, state, options);
        }
    }

    public sealed class ScheduleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name or Amazon Resource Name (ARN) of the Auto Scaling group.
        /// </summary>
        [Input("autoscalingGroupName", required: true)]
        public Input<string> AutoscalingGroupName { get; set; } = null!;

        /// <summary>
        /// The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don't want to change the desired capacity at the scheduled time.
        /// </summary>
        [Input("desiredCapacity")]
        public Input<int>? DesiredCapacity { get; set; }

        /// <summary>
        /// The time for this action to end, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
        /// If you try to schedule your action in the past, Auto Scaling returns an error message.
        /// </summary>
        [Input("endTime")]
        public Input<string>? EndTime { get; set; }

        /// <summary>
        /// The maximum size for the Auto Scaling group. Default 0.
        /// Set to -1 if you don't want to change the maximum size at the scheduled time.
        /// </summary>
        [Input("maxSize")]
        public Input<int>? MaxSize { get; set; }

        /// <summary>
        /// The minimum size for the Auto Scaling group. Default 0.
        /// Set to -1 if you don't want to change the minimum size at the scheduled time.
        /// </summary>
        [Input("minSize")]
        public Input<int>? MinSize { get; set; }

        /// <summary>
        /// The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
        /// </summary>
        [Input("recurrence")]
        public Input<string>? Recurrence { get; set; }

        /// <summary>
        /// The name of this scaling action.
        /// </summary>
        [Input("scheduledActionName", required: true)]
        public Input<string> ScheduledActionName { get; set; } = null!;

        /// <summary>
        /// The time for this action to start, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
        /// If you try to schedule your action in the past, Auto Scaling returns an error message.
        /// </summary>
        [Input("startTime")]
        public Input<string>? StartTime { get; set; }

        public ScheduleArgs()
        {
        }
    }

    public sealed class ScheduleState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN assigned by AWS to the autoscaling schedule.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The name or Amazon Resource Name (ARN) of the Auto Scaling group.
        /// </summary>
        [Input("autoscalingGroupName")]
        public Input<string>? AutoscalingGroupName { get; set; }

        /// <summary>
        /// The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don't want to change the desired capacity at the scheduled time.
        /// </summary>
        [Input("desiredCapacity")]
        public Input<int>? DesiredCapacity { get; set; }

        /// <summary>
        /// The time for this action to end, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
        /// If you try to schedule your action in the past, Auto Scaling returns an error message.
        /// </summary>
        [Input("endTime")]
        public Input<string>? EndTime { get; set; }

        /// <summary>
        /// The maximum size for the Auto Scaling group. Default 0.
        /// Set to -1 if you don't want to change the maximum size at the scheduled time.
        /// </summary>
        [Input("maxSize")]
        public Input<int>? MaxSize { get; set; }

        /// <summary>
        /// The minimum size for the Auto Scaling group. Default 0.
        /// Set to -1 if you don't want to change the minimum size at the scheduled time.
        /// </summary>
        [Input("minSize")]
        public Input<int>? MinSize { get; set; }

        /// <summary>
        /// The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
        /// </summary>
        [Input("recurrence")]
        public Input<string>? Recurrence { get; set; }

        /// <summary>
        /// The name of this scaling action.
        /// </summary>
        [Input("scheduledActionName")]
        public Input<string>? ScheduledActionName { get; set; }

        /// <summary>
        /// The time for this action to start, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
        /// If you try to schedule your action in the past, Auto Scaling returns an error message.
        /// </summary>
        [Input("startTime")]
        public Input<string>? StartTime { get; set; }

        public ScheduleState()
        {
        }
    }
}
