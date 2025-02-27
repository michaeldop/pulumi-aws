// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const mytopic = new aws.sns.Topic("mytopic", {});
 * const myerrortopic = new aws.sns.Topic("myerrortopic", {});
 * const role = new aws.iam.Role("role", {assumeRolePolicy: `{
 *   "Version": "2012-10-17",
 *   "Statement": [
 *     {
 *       "Effect": "Allow",
 *       "Principal": {
 *         "Service": "iot.amazonaws.com"
 *       },
 *       "Action": "sts:AssumeRole"
 *     }
 *   ]
 * }
 * `});
 * const rule = new aws.iot.TopicRule("rule", {
 *     description: "Example rule",
 *     enabled: true,
 *     sql: "SELECT * FROM 'topic/test'",
 *     sqlVersion: "2016-03-23",
 *     sns: {
 *         messageFormat: "RAW",
 *         roleArn: role.arn,
 *         targetArn: mytopic.arn,
 *     },
 *     errorAction: {
 *         sns: {
 *             messageFormat: "RAW",
 *             roleArn: role.arn,
 *             targetArn: myerrortopic.arn,
 *         },
 *     },
 * });
 * const iamPolicyForLambda = new aws.iam.RolePolicy("iamPolicyForLambda", {
 *     role: role.id,
 *     policy: pulumi.interpolate`{
 *   "Version": "2012-10-17",
 *   "Statement": [
 *     {
 *         "Effect": "Allow",
 *         "Action": [
 *             "sns:Publish"
 *         ],
 *         "Resource": "${mytopic.arn}"
 *     }
 *   ]
 * }
 * `,
 * });
 * ```
 */
export class TopicRule extends pulumi.CustomResource {
    /**
     * Get an existing TopicRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicRuleState, opts?: pulumi.CustomResourceOptions): TopicRule {
        return new TopicRule(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:iot/topicRule:TopicRule';

    /**
     * Returns true if the given object is an instance of TopicRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TopicRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TopicRule.__pulumiType;
    }

    /**
     * The ARN of the topic rule
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly cloudwatchAlarm!: pulumi.Output<outputs.iot.TopicRuleCloudwatchAlarm | undefined>;
    public readonly cloudwatchMetric!: pulumi.Output<outputs.iot.TopicRuleCloudwatchMetric | undefined>;
    /**
     * The description of the rule.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly dynamodb!: pulumi.Output<outputs.iot.TopicRuleDynamodb | undefined>;
    public readonly dynamodbv2s!: pulumi.Output<outputs.iot.TopicRuleDynamodbv2[] | undefined>;
    public readonly elasticsearch!: pulumi.Output<outputs.iot.TopicRuleElasticsearch | undefined>;
    /**
     * Specifies whether the rule is enabled.
     */
    public readonly enabled!: pulumi.Output<boolean>;
    /**
     * Configuration block with error action to be associated with the rule. See the documentation for `cloudwatchAlarm`, `cloudwatchMetric`, `dynamodb`, `dynamodbv2`, `elasticsearch`, `firehose`, `iotAnalytics`, `iotEvents`, `kinesis`, `lambda`, `republish`, `s3`, `stepFunctions`, `sns`, `sqs` configuration blocks for further configuration details.
     */
    public readonly errorAction!: pulumi.Output<outputs.iot.TopicRuleErrorAction | undefined>;
    public readonly firehose!: pulumi.Output<outputs.iot.TopicRuleFirehose | undefined>;
    public readonly iotAnalytics!: pulumi.Output<outputs.iot.TopicRuleIotAnalytic[] | undefined>;
    public readonly iotEvents!: pulumi.Output<outputs.iot.TopicRuleIotEvent[] | undefined>;
    public readonly kinesis!: pulumi.Output<outputs.iot.TopicRuleKinesis | undefined>;
    public readonly lambda!: pulumi.Output<outputs.iot.TopicRuleLambda | undefined>;
    /**
     * The name of the rule.
     */
    public readonly name!: pulumi.Output<string>;
    public readonly republish!: pulumi.Output<outputs.iot.TopicRuleRepublish | undefined>;
    public readonly s3!: pulumi.Output<outputs.iot.TopicRuleS3 | undefined>;
    public readonly sns!: pulumi.Output<outputs.iot.TopicRuleSns | undefined>;
    /**
     * The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.
     */
    public readonly sql!: pulumi.Output<string>;
    /**
     * The version of the SQL rules engine to use when evaluating the rule.
     */
    public readonly sqlVersion!: pulumi.Output<string>;
    public readonly sqs!: pulumi.Output<outputs.iot.TopicRuleSqs | undefined>;
    public readonly stepFunctions!: pulumi.Output<outputs.iot.TopicRuleStepFunction[] | undefined>;
    /**
     * Key-value map of resource tags
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;

    /**
     * Create a TopicRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TopicRuleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TopicRuleArgs | TopicRuleState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as TopicRuleState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["cloudwatchAlarm"] = state ? state.cloudwatchAlarm : undefined;
            inputs["cloudwatchMetric"] = state ? state.cloudwatchMetric : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["dynamodb"] = state ? state.dynamodb : undefined;
            inputs["dynamodbv2s"] = state ? state.dynamodbv2s : undefined;
            inputs["elasticsearch"] = state ? state.elasticsearch : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["errorAction"] = state ? state.errorAction : undefined;
            inputs["firehose"] = state ? state.firehose : undefined;
            inputs["iotAnalytics"] = state ? state.iotAnalytics : undefined;
            inputs["iotEvents"] = state ? state.iotEvents : undefined;
            inputs["kinesis"] = state ? state.kinesis : undefined;
            inputs["lambda"] = state ? state.lambda : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["republish"] = state ? state.republish : undefined;
            inputs["s3"] = state ? state.s3 : undefined;
            inputs["sns"] = state ? state.sns : undefined;
            inputs["sql"] = state ? state.sql : undefined;
            inputs["sqlVersion"] = state ? state.sqlVersion : undefined;
            inputs["sqs"] = state ? state.sqs : undefined;
            inputs["stepFunctions"] = state ? state.stepFunctions : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as TopicRuleArgs | undefined;
            if (!args || args.enabled === undefined) {
                throw new Error("Missing required property 'enabled'");
            }
            if (!args || args.sql === undefined) {
                throw new Error("Missing required property 'sql'");
            }
            if (!args || args.sqlVersion === undefined) {
                throw new Error("Missing required property 'sqlVersion'");
            }
            inputs["cloudwatchAlarm"] = args ? args.cloudwatchAlarm : undefined;
            inputs["cloudwatchMetric"] = args ? args.cloudwatchMetric : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["dynamodb"] = args ? args.dynamodb : undefined;
            inputs["dynamodbv2s"] = args ? args.dynamodbv2s : undefined;
            inputs["elasticsearch"] = args ? args.elasticsearch : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["errorAction"] = args ? args.errorAction : undefined;
            inputs["firehose"] = args ? args.firehose : undefined;
            inputs["iotAnalytics"] = args ? args.iotAnalytics : undefined;
            inputs["iotEvents"] = args ? args.iotEvents : undefined;
            inputs["kinesis"] = args ? args.kinesis : undefined;
            inputs["lambda"] = args ? args.lambda : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["republish"] = args ? args.republish : undefined;
            inputs["s3"] = args ? args.s3 : undefined;
            inputs["sns"] = args ? args.sns : undefined;
            inputs["sql"] = args ? args.sql : undefined;
            inputs["sqlVersion"] = args ? args.sqlVersion : undefined;
            inputs["sqs"] = args ? args.sqs : undefined;
            inputs["stepFunctions"] = args ? args.stepFunctions : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(TopicRule.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering TopicRule resources.
 */
export interface TopicRuleState {
    /**
     * The ARN of the topic rule
     */
    readonly arn?: pulumi.Input<string>;
    readonly cloudwatchAlarm?: pulumi.Input<inputs.iot.TopicRuleCloudwatchAlarm>;
    readonly cloudwatchMetric?: pulumi.Input<inputs.iot.TopicRuleCloudwatchMetric>;
    /**
     * The description of the rule.
     */
    readonly description?: pulumi.Input<string>;
    readonly dynamodb?: pulumi.Input<inputs.iot.TopicRuleDynamodb>;
    readonly dynamodbv2s?: pulumi.Input<pulumi.Input<inputs.iot.TopicRuleDynamodbv2>[]>;
    readonly elasticsearch?: pulumi.Input<inputs.iot.TopicRuleElasticsearch>;
    /**
     * Specifies whether the rule is enabled.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * Configuration block with error action to be associated with the rule. See the documentation for `cloudwatchAlarm`, `cloudwatchMetric`, `dynamodb`, `dynamodbv2`, `elasticsearch`, `firehose`, `iotAnalytics`, `iotEvents`, `kinesis`, `lambda`, `republish`, `s3`, `stepFunctions`, `sns`, `sqs` configuration blocks for further configuration details.
     */
    readonly errorAction?: pulumi.Input<inputs.iot.TopicRuleErrorAction>;
    readonly firehose?: pulumi.Input<inputs.iot.TopicRuleFirehose>;
    readonly iotAnalytics?: pulumi.Input<pulumi.Input<inputs.iot.TopicRuleIotAnalytic>[]>;
    readonly iotEvents?: pulumi.Input<pulumi.Input<inputs.iot.TopicRuleIotEvent>[]>;
    readonly kinesis?: pulumi.Input<inputs.iot.TopicRuleKinesis>;
    readonly lambda?: pulumi.Input<inputs.iot.TopicRuleLambda>;
    /**
     * The name of the rule.
     */
    readonly name?: pulumi.Input<string>;
    readonly republish?: pulumi.Input<inputs.iot.TopicRuleRepublish>;
    readonly s3?: pulumi.Input<inputs.iot.TopicRuleS3>;
    readonly sns?: pulumi.Input<inputs.iot.TopicRuleSns>;
    /**
     * The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.
     */
    readonly sql?: pulumi.Input<string>;
    /**
     * The version of the SQL rules engine to use when evaluating the rule.
     */
    readonly sqlVersion?: pulumi.Input<string>;
    readonly sqs?: pulumi.Input<inputs.iot.TopicRuleSqs>;
    readonly stepFunctions?: pulumi.Input<pulumi.Input<inputs.iot.TopicRuleStepFunction>[]>;
    /**
     * Key-value map of resource tags
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The set of arguments for constructing a TopicRule resource.
 */
export interface TopicRuleArgs {
    readonly cloudwatchAlarm?: pulumi.Input<inputs.iot.TopicRuleCloudwatchAlarm>;
    readonly cloudwatchMetric?: pulumi.Input<inputs.iot.TopicRuleCloudwatchMetric>;
    /**
     * The description of the rule.
     */
    readonly description?: pulumi.Input<string>;
    readonly dynamodb?: pulumi.Input<inputs.iot.TopicRuleDynamodb>;
    readonly dynamodbv2s?: pulumi.Input<pulumi.Input<inputs.iot.TopicRuleDynamodbv2>[]>;
    readonly elasticsearch?: pulumi.Input<inputs.iot.TopicRuleElasticsearch>;
    /**
     * Specifies whether the rule is enabled.
     */
    readonly enabled: pulumi.Input<boolean>;
    /**
     * Configuration block with error action to be associated with the rule. See the documentation for `cloudwatchAlarm`, `cloudwatchMetric`, `dynamodb`, `dynamodbv2`, `elasticsearch`, `firehose`, `iotAnalytics`, `iotEvents`, `kinesis`, `lambda`, `republish`, `s3`, `stepFunctions`, `sns`, `sqs` configuration blocks for further configuration details.
     */
    readonly errorAction?: pulumi.Input<inputs.iot.TopicRuleErrorAction>;
    readonly firehose?: pulumi.Input<inputs.iot.TopicRuleFirehose>;
    readonly iotAnalytics?: pulumi.Input<pulumi.Input<inputs.iot.TopicRuleIotAnalytic>[]>;
    readonly iotEvents?: pulumi.Input<pulumi.Input<inputs.iot.TopicRuleIotEvent>[]>;
    readonly kinesis?: pulumi.Input<inputs.iot.TopicRuleKinesis>;
    readonly lambda?: pulumi.Input<inputs.iot.TopicRuleLambda>;
    /**
     * The name of the rule.
     */
    readonly name?: pulumi.Input<string>;
    readonly republish?: pulumi.Input<inputs.iot.TopicRuleRepublish>;
    readonly s3?: pulumi.Input<inputs.iot.TopicRuleS3>;
    readonly sns?: pulumi.Input<inputs.iot.TopicRuleSns>;
    /**
     * The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.
     */
    readonly sql: pulumi.Input<string>;
    /**
     * The version of the SQL rules engine to use when evaluating the rule.
     */
    readonly sqlVersion: pulumi.Input<string>;
    readonly sqs?: pulumi.Input<inputs.iot.TopicRuleSqs>;
    readonly stepFunctions?: pulumi.Input<pulumi.Input<inputs.iot.TopicRuleStepFunction>[]>;
    /**
     * Key-value map of resource tags
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
