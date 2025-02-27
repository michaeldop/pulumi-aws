// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides a CodeDeploy Deployment Group for a CodeDeploy Application
 *
 * > **NOTE on blue/green deployments:** When using `greenFleetProvisioningOption` with the `COPY_AUTO_SCALING_GROUP` action, CodeDeploy will create a new ASG with a different name. This ASG is _not_ managed by this provider and will conflict with existing configuration and state. You may want to use a different approach to managing deployments that involve multiple ASG, such as `DISCOVER_EXISTING` with separate blue and green ASG.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const exampleRole = new aws.iam.Role("exampleRole", {assumeRolePolicy: `{
 *   "Version": "2012-10-17",
 *   "Statement": [
 *     {
 *       "Sid": "",
 *       "Effect": "Allow",
 *       "Principal": {
 *         "Service": "codedeploy.amazonaws.com"
 *       },
 *       "Action": "sts:AssumeRole"
 *     }
 *   ]
 * }
 * `});
 * const aWSCodeDeployRole = new aws.iam.RolePolicyAttachment("aWSCodeDeployRole", {
 *     policyArn: "arn:aws:iam::aws:policy/service-role/AWSCodeDeployRole",
 *     role: exampleRole.name,
 * });
 * const exampleApplication = new aws.codedeploy.Application("exampleApplication", {});
 * const exampleTopic = new aws.sns.Topic("exampleTopic", {});
 * const exampleDeploymentGroup = new aws.codedeploy.DeploymentGroup("exampleDeploymentGroup", {
 *     appName: exampleApplication.name,
 *     deploymentGroupName: "example-group",
 *     serviceRoleArn: exampleRole.arn,
 *     ec2TagSets: [{
 *         ec2TagFilters: [
 *             {
 *                 key: "filterkey1",
 *                 type: "KEY_AND_VALUE",
 *                 value: "filtervalue",
 *             },
 *             {
 *                 key: "filterkey2",
 *                 type: "KEY_AND_VALUE",
 *                 value: "filtervalue",
 *             },
 *         ],
 *     }],
 *     triggerConfigurations: [{
 *         triggerEvents: ["DeploymentFailure"],
 *         triggerName: "example-trigger",
 *         triggerTargetArn: exampleTopic.arn,
 *     }],
 *     autoRollbackConfiguration: {
 *         enabled: true,
 *         events: ["DEPLOYMENT_FAILURE"],
 *     },
 *     alarmConfiguration: {
 *         alarms: ["my-alarm-name"],
 *         enabled: true,
 *     },
 * });
 * ```
 * ### Blue Green Deployments with ECS
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const exampleApplication = new aws.codedeploy.Application("exampleApplication", {computePlatform: "ECS"});
 * const exampleDeploymentGroup = new aws.codedeploy.DeploymentGroup("exampleDeploymentGroup", {
 *     appName: exampleApplication.name,
 *     deploymentConfigName: "CodeDeployDefault.ECSAllAtOnce",
 *     deploymentGroupName: "example",
 *     serviceRoleArn: aws_iam_role.example.arn,
 *     autoRollbackConfiguration: {
 *         enabled: true,
 *         events: ["DEPLOYMENT_FAILURE"],
 *     },
 *     blueGreenDeploymentConfig: {
 *         deploymentReadyOption: {
 *             actionOnTimeout: "CONTINUE_DEPLOYMENT",
 *         },
 *         terminateBlueInstancesOnDeploymentSuccess: {
 *             action: "TERMINATE",
 *             terminationWaitTimeInMinutes: 5,
 *         },
 *     },
 *     deploymentStyle: {
 *         deploymentOption: "WITH_TRAFFIC_CONTROL",
 *         deploymentType: "BLUE_GREEN",
 *     },
 *     ecsService: {
 *         clusterName: aws_ecs_cluster.example.name,
 *         serviceName: aws_ecs_service.example.name,
 *     },
 *     loadBalancerInfo: {
 *         targetGroupPairInfo: {
 *             prodTrafficRoute: {
 *                 listenerArns: [aws_lb_listener.example.arn],
 *             },
 *             targetGroups: [
 *                 {
 *                     name: aws_lb_target_group.blue.name,
 *                 },
 *                 {
 *                     name: aws_lb_target_group.green.name,
 *                 },
 *             ],
 *         },
 *     },
 * });
 * ```
 * ### Blue Green Deployments with Servers and Classic ELB
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const exampleApplication = new aws.codedeploy.Application("exampleApplication", {});
 * const exampleDeploymentGroup = new aws.codedeploy.DeploymentGroup("exampleDeploymentGroup", {
 *     appName: exampleApplication.name,
 *     deploymentGroupName: "example-group",
 *     serviceRoleArn: aws_iam_role.example.arn,
 *     deploymentStyle: {
 *         deploymentOption: "WITH_TRAFFIC_CONTROL",
 *         deploymentType: "BLUE_GREEN",
 *     },
 *     loadBalancerInfo: {
 *         elbInfos: [{
 *             name: aws_elb.example.name,
 *         }],
 *     },
 *     blueGreenDeploymentConfig: {
 *         deploymentReadyOption: {
 *             actionOnTimeout: "STOP_DEPLOYMENT",
 *             waitTimeInMinutes: 60,
 *         },
 *         greenFleetProvisioningOption: {
 *             action: "DISCOVER_EXISTING",
 *         },
 *         terminateBlueInstancesOnDeploymentSuccess: {
 *             action: "KEEP_ALIVE",
 *         },
 *     },
 * });
 * ```
 */
export class DeploymentGroup extends pulumi.CustomResource {
    /**
     * Get an existing DeploymentGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DeploymentGroupState, opts?: pulumi.CustomResourceOptions): DeploymentGroup {
        return new DeploymentGroup(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:codedeploy/deploymentGroup:DeploymentGroup';

    /**
     * Returns true if the given object is an instance of DeploymentGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DeploymentGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DeploymentGroup.__pulumiType;
    }

    /**
     * Configuration block of alarms associated with the deployment group (documented below).
     */
    public readonly alarmConfiguration!: pulumi.Output<outputs.codedeploy.DeploymentGroupAlarmConfiguration | undefined>;
    /**
     * The name of the application.
     */
    public readonly appName!: pulumi.Output<string>;
    /**
     * Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
     */
    public readonly autoRollbackConfiguration!: pulumi.Output<outputs.codedeploy.DeploymentGroupAutoRollbackConfiguration | undefined>;
    /**
     * Autoscaling groups associated with the deployment group.
     */
    public readonly autoscalingGroups!: pulumi.Output<string[] | undefined>;
    /**
     * Configuration block of the blue/green deployment options for a deployment group (documented below).
     */
    public readonly blueGreenDeploymentConfig!: pulumi.Output<outputs.codedeploy.DeploymentGroupBlueGreenDeploymentConfig>;
    /**
     * The name of the group's deployment config. The default is "CodeDeployDefault.OneAtATime".
     */
    public readonly deploymentConfigName!: pulumi.Output<string | undefined>;
    /**
     * The name of the deployment group.
     */
    public readonly deploymentGroupName!: pulumi.Output<string>;
    /**
     * Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
     */
    public readonly deploymentStyle!: pulumi.Output<outputs.codedeploy.DeploymentGroupDeploymentStyle | undefined>;
    /**
     * Tag filters associated with the deployment group. See the AWS docs for details.
     */
    public readonly ec2TagFilters!: pulumi.Output<outputs.codedeploy.DeploymentGroupEc2TagFilter[] | undefined>;
    /**
     * Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
     */
    public readonly ec2TagSets!: pulumi.Output<outputs.codedeploy.DeploymentGroupEc2TagSet[] | undefined>;
    /**
     * Configuration block(s) of the ECS services for a deployment group (documented below).
     */
    public readonly ecsService!: pulumi.Output<outputs.codedeploy.DeploymentGroupEcsService | undefined>;
    /**
     * Single configuration block of the load balancer to use in a blue/green deployment (documented below).
     */
    public readonly loadBalancerInfo!: pulumi.Output<outputs.codedeploy.DeploymentGroupLoadBalancerInfo | undefined>;
    /**
     * On premise tag filters associated with the group. See the AWS docs for details.
     */
    public readonly onPremisesInstanceTagFilters!: pulumi.Output<outputs.codedeploy.DeploymentGroupOnPremisesInstanceTagFilter[] | undefined>;
    /**
     * The service role ARN that allows deployments.
     */
    public readonly serviceRoleArn!: pulumi.Output<string>;
    /**
     * Configuration block(s) of the triggers for the deployment group (documented below).
     */
    public readonly triggerConfigurations!: pulumi.Output<outputs.codedeploy.DeploymentGroupTriggerConfiguration[] | undefined>;

    /**
     * Create a DeploymentGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DeploymentGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DeploymentGroupArgs | DeploymentGroupState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DeploymentGroupState | undefined;
            inputs["alarmConfiguration"] = state ? state.alarmConfiguration : undefined;
            inputs["appName"] = state ? state.appName : undefined;
            inputs["autoRollbackConfiguration"] = state ? state.autoRollbackConfiguration : undefined;
            inputs["autoscalingGroups"] = state ? state.autoscalingGroups : undefined;
            inputs["blueGreenDeploymentConfig"] = state ? state.blueGreenDeploymentConfig : undefined;
            inputs["deploymentConfigName"] = state ? state.deploymentConfigName : undefined;
            inputs["deploymentGroupName"] = state ? state.deploymentGroupName : undefined;
            inputs["deploymentStyle"] = state ? state.deploymentStyle : undefined;
            inputs["ec2TagFilters"] = state ? state.ec2TagFilters : undefined;
            inputs["ec2TagSets"] = state ? state.ec2TagSets : undefined;
            inputs["ecsService"] = state ? state.ecsService : undefined;
            inputs["loadBalancerInfo"] = state ? state.loadBalancerInfo : undefined;
            inputs["onPremisesInstanceTagFilters"] = state ? state.onPremisesInstanceTagFilters : undefined;
            inputs["serviceRoleArn"] = state ? state.serviceRoleArn : undefined;
            inputs["triggerConfigurations"] = state ? state.triggerConfigurations : undefined;
        } else {
            const args = argsOrState as DeploymentGroupArgs | undefined;
            if (!args || args.appName === undefined) {
                throw new Error("Missing required property 'appName'");
            }
            if (!args || args.deploymentGroupName === undefined) {
                throw new Error("Missing required property 'deploymentGroupName'");
            }
            if (!args || args.serviceRoleArn === undefined) {
                throw new Error("Missing required property 'serviceRoleArn'");
            }
            inputs["alarmConfiguration"] = args ? args.alarmConfiguration : undefined;
            inputs["appName"] = args ? args.appName : undefined;
            inputs["autoRollbackConfiguration"] = args ? args.autoRollbackConfiguration : undefined;
            inputs["autoscalingGroups"] = args ? args.autoscalingGroups : undefined;
            inputs["blueGreenDeploymentConfig"] = args ? args.blueGreenDeploymentConfig : undefined;
            inputs["deploymentConfigName"] = args ? args.deploymentConfigName : undefined;
            inputs["deploymentGroupName"] = args ? args.deploymentGroupName : undefined;
            inputs["deploymentStyle"] = args ? args.deploymentStyle : undefined;
            inputs["ec2TagFilters"] = args ? args.ec2TagFilters : undefined;
            inputs["ec2TagSets"] = args ? args.ec2TagSets : undefined;
            inputs["ecsService"] = args ? args.ecsService : undefined;
            inputs["loadBalancerInfo"] = args ? args.loadBalancerInfo : undefined;
            inputs["onPremisesInstanceTagFilters"] = args ? args.onPremisesInstanceTagFilters : undefined;
            inputs["serviceRoleArn"] = args ? args.serviceRoleArn : undefined;
            inputs["triggerConfigurations"] = args ? args.triggerConfigurations : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(DeploymentGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DeploymentGroup resources.
 */
export interface DeploymentGroupState {
    /**
     * Configuration block of alarms associated with the deployment group (documented below).
     */
    readonly alarmConfiguration?: pulumi.Input<inputs.codedeploy.DeploymentGroupAlarmConfiguration>;
    /**
     * The name of the application.
     */
    readonly appName?: pulumi.Input<string>;
    /**
     * Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
     */
    readonly autoRollbackConfiguration?: pulumi.Input<inputs.codedeploy.DeploymentGroupAutoRollbackConfiguration>;
    /**
     * Autoscaling groups associated with the deployment group.
     */
    readonly autoscalingGroups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Configuration block of the blue/green deployment options for a deployment group (documented below).
     */
    readonly blueGreenDeploymentConfig?: pulumi.Input<inputs.codedeploy.DeploymentGroupBlueGreenDeploymentConfig>;
    /**
     * The name of the group's deployment config. The default is "CodeDeployDefault.OneAtATime".
     */
    readonly deploymentConfigName?: pulumi.Input<string>;
    /**
     * The name of the deployment group.
     */
    readonly deploymentGroupName?: pulumi.Input<string>;
    /**
     * Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
     */
    readonly deploymentStyle?: pulumi.Input<inputs.codedeploy.DeploymentGroupDeploymentStyle>;
    /**
     * Tag filters associated with the deployment group. See the AWS docs for details.
     */
    readonly ec2TagFilters?: pulumi.Input<pulumi.Input<inputs.codedeploy.DeploymentGroupEc2TagFilter>[]>;
    /**
     * Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
     */
    readonly ec2TagSets?: pulumi.Input<pulumi.Input<inputs.codedeploy.DeploymentGroupEc2TagSet>[]>;
    /**
     * Configuration block(s) of the ECS services for a deployment group (documented below).
     */
    readonly ecsService?: pulumi.Input<inputs.codedeploy.DeploymentGroupEcsService>;
    /**
     * Single configuration block of the load balancer to use in a blue/green deployment (documented below).
     */
    readonly loadBalancerInfo?: pulumi.Input<inputs.codedeploy.DeploymentGroupLoadBalancerInfo>;
    /**
     * On premise tag filters associated with the group. See the AWS docs for details.
     */
    readonly onPremisesInstanceTagFilters?: pulumi.Input<pulumi.Input<inputs.codedeploy.DeploymentGroupOnPremisesInstanceTagFilter>[]>;
    /**
     * The service role ARN that allows deployments.
     */
    readonly serviceRoleArn?: pulumi.Input<string>;
    /**
     * Configuration block(s) of the triggers for the deployment group (documented below).
     */
    readonly triggerConfigurations?: pulumi.Input<pulumi.Input<inputs.codedeploy.DeploymentGroupTriggerConfiguration>[]>;
}

/**
 * The set of arguments for constructing a DeploymentGroup resource.
 */
export interface DeploymentGroupArgs {
    /**
     * Configuration block of alarms associated with the deployment group (documented below).
     */
    readonly alarmConfiguration?: pulumi.Input<inputs.codedeploy.DeploymentGroupAlarmConfiguration>;
    /**
     * The name of the application.
     */
    readonly appName: pulumi.Input<string>;
    /**
     * Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
     */
    readonly autoRollbackConfiguration?: pulumi.Input<inputs.codedeploy.DeploymentGroupAutoRollbackConfiguration>;
    /**
     * Autoscaling groups associated with the deployment group.
     */
    readonly autoscalingGroups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Configuration block of the blue/green deployment options for a deployment group (documented below).
     */
    readonly blueGreenDeploymentConfig?: pulumi.Input<inputs.codedeploy.DeploymentGroupBlueGreenDeploymentConfig>;
    /**
     * The name of the group's deployment config. The default is "CodeDeployDefault.OneAtATime".
     */
    readonly deploymentConfigName?: pulumi.Input<string>;
    /**
     * The name of the deployment group.
     */
    readonly deploymentGroupName: pulumi.Input<string>;
    /**
     * Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
     */
    readonly deploymentStyle?: pulumi.Input<inputs.codedeploy.DeploymentGroupDeploymentStyle>;
    /**
     * Tag filters associated with the deployment group. See the AWS docs for details.
     */
    readonly ec2TagFilters?: pulumi.Input<pulumi.Input<inputs.codedeploy.DeploymentGroupEc2TagFilter>[]>;
    /**
     * Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
     */
    readonly ec2TagSets?: pulumi.Input<pulumi.Input<inputs.codedeploy.DeploymentGroupEc2TagSet>[]>;
    /**
     * Configuration block(s) of the ECS services for a deployment group (documented below).
     */
    readonly ecsService?: pulumi.Input<inputs.codedeploy.DeploymentGroupEcsService>;
    /**
     * Single configuration block of the load balancer to use in a blue/green deployment (documented below).
     */
    readonly loadBalancerInfo?: pulumi.Input<inputs.codedeploy.DeploymentGroupLoadBalancerInfo>;
    /**
     * On premise tag filters associated with the group. See the AWS docs for details.
     */
    readonly onPremisesInstanceTagFilters?: pulumi.Input<pulumi.Input<inputs.codedeploy.DeploymentGroupOnPremisesInstanceTagFilter>[]>;
    /**
     * The service role ARN that allows deployments.
     */
    readonly serviceRoleArn: pulumi.Input<string>;
    /**
     * Configuration block(s) of the triggers for the deployment group (documented below).
     */
    readonly triggerConfigurations?: pulumi.Input<pulumi.Input<inputs.codedeploy.DeploymentGroupTriggerConfiguration>[]>;
}
