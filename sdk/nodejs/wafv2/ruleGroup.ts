// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Creates a WAFv2 Rule Group resource.
 *
 * ## Example Usage
 * ### Simple
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const example = new aws.wafv2.RuleGroup("example", {
 *     capacity: 2,
 *     rules: [{
 *         action: {
 *             allow: {},
 *         },
 *         name: "rule-1",
 *         priority: 1,
 *         statement: {
 *             geoMatchStatement: {
 *                 countryCodes: [
 *                     "US",
 *                     "NL",
 *                 ],
 *             },
 *         },
 *         visibilityConfig: {
 *             cloudwatchMetricsEnabled: false,
 *             metricName: "friendly-rule-metric-name",
 *             sampledRequestsEnabled: false,
 *         },
 *     }],
 *     scope: "REGIONAL",
 *     visibilityConfig: {
 *         cloudwatchMetricsEnabled: false,
 *         metricName: "friendly-metric-name",
 *         sampledRequestsEnabled: false,
 *     },
 * });
 * ```
 * ### Complex
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const testIpSet = new aws.wafv2.IpSet("testIpSet", {
 *     scope: "REGIONAL",
 *     ipAddressVersion: "IPV4",
 *     addresses: [
 *         "1.1.1.1/32",
 *         "2.2.2.2/32",
 *     ],
 * });
 * const testRegexPatternSet = new aws.wafv2.RegexPatternSet("testRegexPatternSet", {
 *     scope: "REGIONAL",
 *     regularExpressionList: [{
 *         regexString: "one",
 *     }],
 * });
 * const example = new aws.wafv2.RuleGroup("example", {
 *     description: "An rule group containing all statements",
 *     scope: "REGIONAL",
 *     capacity: 500,
 *     rules: [
 *         {
 *             name: "rule-1",
 *             priority: 1,
 *             action: {
 *                 block: {},
 *             },
 *             statement: {
 *                 notStatement: {
 *                     statements: [{
 *                         andStatement: {
 *                             statements: [
 *                                 {
 *                                     geoMatchStatement: {
 *                                         countryCodes: ["US"],
 *                                     },
 *                                 },
 *                                 {
 *                                     byteMatchStatement: {
 *                                         positionalConstraint: "CONTAINS",
 *                                         searchString: "word",
 *                                         fieldToMatch: {
 *                                             allQueryArguments: {},
 *                                         },
 *                                         textTransformations: [
 *                                             {
 *                                                 priority: 5,
 *                                                 type: "CMD_LINE",
 *                                             },
 *                                             {
 *                                                 priority: 2,
 *                                                 type: "LOWERCASE",
 *                                             },
 *                                         ],
 *                                     },
 *                                 },
 *                             ],
 *                         },
 *                     }],
 *                 },
 *             },
 *             visibilityConfig: {
 *                 cloudwatchMetricsEnabled: false,
 *                 metricName: "rule-1",
 *                 sampledRequestsEnabled: false,
 *             },
 *         },
 *         {
 *             name: "rule-2",
 *             priority: 2,
 *             action: {
 *                 count: {},
 *             },
 *             statement: {
 *                 orStatement: {
 *                     statements: [
 *                         {
 *                             sqliMatchStatement: {
 *                                 fieldToMatch: {
 *                                     body: {},
 *                                 },
 *                                 textTransformations: [
 *                                     {
 *                                         priority: 5,
 *                                         type: "URL_DECODE",
 *                                     },
 *                                     {
 *                                         priority: 4,
 *                                         type: "HTML_ENTITY_DECODE",
 *                                     },
 *                                     {
 *                                         priority: 3,
 *                                         type: "COMPRESS_WHITE_SPACE",
 *                                     },
 *                                 ],
 *                             },
 *                         },
 *                         {
 *                             xssMatchStatement: {
 *                                 fieldToMatch: {
 *                                     method: {},
 *                                 },
 *                                 textTransformations: [{
 *                                     priority: 2,
 *                                     type: "NONE",
 *                                 }],
 *                             },
 *                         },
 *                     ],
 *                 },
 *             },
 *             visibilityConfig: {
 *                 cloudwatchMetricsEnabled: false,
 *                 metricName: "rule-2",
 *                 sampledRequestsEnabled: false,
 *             },
 *         },
 *         {
 *             name: "rule-3",
 *             priority: 3,
 *             action: {
 *                 block: {},
 *             },
 *             statement: {
 *                 sizeConstraintStatement: {
 *                     comparisonOperator: "GT",
 *                     size: 100,
 *                     fieldToMatch: {
 *                         singleQueryArgument: {
 *                             name: "username",
 *                         },
 *                     },
 *                     textTransformations: [{
 *                         priority: 5,
 *                         type: "NONE",
 *                     }],
 *                 },
 *             },
 *             visibilityConfig: {
 *                 cloudwatchMetricsEnabled: false,
 *                 metricName: "rule-3",
 *                 sampledRequestsEnabled: false,
 *             },
 *         },
 *         {
 *             name: "rule-4",
 *             priority: 4,
 *             action: {
 *                 block: {},
 *             },
 *             statement: {
 *                 orStatement: {
 *                     statements: [
 *                         {
 *                             ipSetReferenceStatement: {
 *                                 arn: testIpSet.arn,
 *                             },
 *                         },
 *                         {
 *                             regexPatternSetReferenceStatement: {
 *                                 arn: testRegexPatternSet.arn,
 *                                 fieldToMatch: {
 *                                     singleHeader: {
 *                                         name: "referer",
 *                                     },
 *                                 },
 *                                 textTransformations: [{
 *                                     priority: 2,
 *                                     type: "NONE",
 *                                 }],
 *                             },
 *                         },
 *                     ],
 *                 },
 *             },
 *             visibilityConfig: {
 *                 cloudwatchMetricsEnabled: false,
 *                 metricName: "rule-4",
 *                 sampledRequestsEnabled: false,
 *             },
 *         },
 *     ],
 *     visibilityConfig: {
 *         cloudwatchMetricsEnabled: false,
 *         metricName: "friendly-metric-name",
 *         sampledRequestsEnabled: false,
 *     },
 *     tags: {
 *         Name: "example-and-statement",
 *         Code: "123456",
 *     },
 * });
 * ```
 */
export class RuleGroup extends pulumi.CustomResource {
    /**
     * Get an existing RuleGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RuleGroupState, opts?: pulumi.CustomResourceOptions): RuleGroup {
        return new RuleGroup(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:wafv2/ruleGroup:RuleGroup';

    /**
     * Returns true if the given object is an instance of RuleGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RuleGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RuleGroup.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the IP Set that this statement references.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The web ACL capacity units (WCUs) required for this rule group. See [here](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateRuleGroup.html#API_CreateRuleGroup_RequestSyntax) for general information and [here](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statements-list.html) for capacity specific information.
     */
    public readonly capacity!: pulumi.Output<number>;
    /**
     * A friendly description of the rule group.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    public /*out*/ readonly lockToken!: pulumi.Output<string>;
    /**
     * A friendly name of the rule group.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The rule blocks used to identify the web requests that you want to `allow`, `block`, or `count`. See Rules below for details.
     */
    public readonly rules!: pulumi.Output<outputs.wafv2.RuleGroupRule[] | undefined>;
    /**
     * Specifies whether this is for an AWS CloudFront distribution or for a regional application. Valid values are `CLOUDFRONT` or `REGIONAL`. To work with CloudFront, you must also specify the region `us-east-1` (N. Virginia) on the AWS provider.
     */
    public readonly scope!: pulumi.Output<string>;
    /**
     * An array of key:value pairs to associate with the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * Defines and enables Amazon CloudWatch metrics and web request sample collection. See Visibility Configuration below for details.
     */
    public readonly visibilityConfig!: pulumi.Output<outputs.wafv2.RuleGroupVisibilityConfig>;

    /**
     * Create a RuleGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RuleGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RuleGroupArgs | RuleGroupState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as RuleGroupState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["capacity"] = state ? state.capacity : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["lockToken"] = state ? state.lockToken : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["rules"] = state ? state.rules : undefined;
            inputs["scope"] = state ? state.scope : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["visibilityConfig"] = state ? state.visibilityConfig : undefined;
        } else {
            const args = argsOrState as RuleGroupArgs | undefined;
            if (!args || args.capacity === undefined) {
                throw new Error("Missing required property 'capacity'");
            }
            if (!args || args.scope === undefined) {
                throw new Error("Missing required property 'scope'");
            }
            if (!args || args.visibilityConfig === undefined) {
                throw new Error("Missing required property 'visibilityConfig'");
            }
            inputs["capacity"] = args ? args.capacity : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["rules"] = args ? args.rules : undefined;
            inputs["scope"] = args ? args.scope : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["visibilityConfig"] = args ? args.visibilityConfig : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["lockToken"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(RuleGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RuleGroup resources.
 */
export interface RuleGroupState {
    /**
     * The Amazon Resource Name (ARN) of the IP Set that this statement references.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The web ACL capacity units (WCUs) required for this rule group. See [here](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateRuleGroup.html#API_CreateRuleGroup_RequestSyntax) for general information and [here](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statements-list.html) for capacity specific information.
     */
    readonly capacity?: pulumi.Input<number>;
    /**
     * A friendly description of the rule group.
     */
    readonly description?: pulumi.Input<string>;
    readonly lockToken?: pulumi.Input<string>;
    /**
     * A friendly name of the rule group.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The rule blocks used to identify the web requests that you want to `allow`, `block`, or `count`. See Rules below for details.
     */
    readonly rules?: pulumi.Input<pulumi.Input<inputs.wafv2.RuleGroupRule>[]>;
    /**
     * Specifies whether this is for an AWS CloudFront distribution or for a regional application. Valid values are `CLOUDFRONT` or `REGIONAL`. To work with CloudFront, you must also specify the region `us-east-1` (N. Virginia) on the AWS provider.
     */
    readonly scope?: pulumi.Input<string>;
    /**
     * An array of key:value pairs to associate with the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Defines and enables Amazon CloudWatch metrics and web request sample collection. See Visibility Configuration below for details.
     */
    readonly visibilityConfig?: pulumi.Input<inputs.wafv2.RuleGroupVisibilityConfig>;
}

/**
 * The set of arguments for constructing a RuleGroup resource.
 */
export interface RuleGroupArgs {
    /**
     * The web ACL capacity units (WCUs) required for this rule group. See [here](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateRuleGroup.html#API_CreateRuleGroup_RequestSyntax) for general information and [here](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statements-list.html) for capacity specific information.
     */
    readonly capacity: pulumi.Input<number>;
    /**
     * A friendly description of the rule group.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A friendly name of the rule group.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The rule blocks used to identify the web requests that you want to `allow`, `block`, or `count`. See Rules below for details.
     */
    readonly rules?: pulumi.Input<pulumi.Input<inputs.wafv2.RuleGroupRule>[]>;
    /**
     * Specifies whether this is for an AWS CloudFront distribution or for a regional application. Valid values are `CLOUDFRONT` or `REGIONAL`. To work with CloudFront, you must also specify the region `us-east-1` (N. Virginia) on the AWS provider.
     */
    readonly scope: pulumi.Input<string>;
    /**
     * An array of key:value pairs to associate with the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Defines and enables Amazon CloudWatch metrics and web request sample collection. See Visibility Configuration below for details.
     */
    readonly visibilityConfig: pulumi.Input<inputs.wafv2.RuleGroupVisibilityConfig>;
}
