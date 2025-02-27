// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides an Traffic mirror filter rule.\
 * Read [limits and considerations](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-considerations.html) for traffic mirroring
 *
 * ## Example Usage
 *
 * To create a basic traffic mirror session
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const filter = new aws.ec2.TrafficMirrorFilter("filter", {
 *     description: "traffic mirror filter - example",
 *     networkServices: ["amazon-dns"],
 * });
 * const ruleout = new aws.ec2.TrafficMirrorFilterRule("ruleout", {
 *     description: "test rule",
 *     trafficMirrorFilterId: filter.id,
 *     destinationCidrBlock: "10.0.0.0/8",
 *     sourceCidrBlock: "10.0.0.0/8",
 *     ruleNumber: 1,
 *     ruleAction: "accept",
 *     trafficDirection: "egress",
 * });
 * const rulein = new aws.ec2.TrafficMirrorFilterRule("rulein", {
 *     description: "test rule",
 *     trafficMirrorFilterId: filter.id,
 *     destinationCidrBlock: "10.0.0.0/8",
 *     sourceCidrBlock: "10.0.0.0/8",
 *     ruleNumber: 1,
 *     ruleAction: "accept",
 *     trafficDirection: "ingress",
 *     protocol: 6,
 *     destinationPortRange: {
 *         fromPort: 22,
 *         toPort: 53,
 *     },
 *     sourcePortRange: {
 *         fromPort: 0,
 *         toPort: 10,
 *     },
 * });
 * ```
 */
export class TrafficMirrorFilterRule extends pulumi.CustomResource {
    /**
     * Get an existing TrafficMirrorFilterRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TrafficMirrorFilterRuleState, opts?: pulumi.CustomResourceOptions): TrafficMirrorFilterRule {
        return new TrafficMirrorFilterRule(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:ec2/trafficMirrorFilterRule:TrafficMirrorFilterRule';

    /**
     * Returns true if the given object is an instance of TrafficMirrorFilterRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TrafficMirrorFilterRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TrafficMirrorFilterRule.__pulumiType;
    }

    /**
     * A description of the traffic mirror filter rule.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The destination CIDR block to assign to the Traffic Mirror rule.
     */
    public readonly destinationCidrBlock!: pulumi.Output<string>;
    /**
     * The destination port range. Supported only when the protocol is set to TCP(6) or UDP(17). See Traffic mirror port range documented below
     */
    public readonly destinationPortRange!: pulumi.Output<outputs.ec2.TrafficMirrorFilterRuleDestinationPortRange | undefined>;
    /**
     * The protocol number, for example 17 (UDP), to assign to the Traffic Mirror rule. For information about the protocol value, see [Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) on the Internet Assigned Numbers Authority (IANA) website.
     */
    public readonly protocol!: pulumi.Output<number | undefined>;
    /**
     * The action to take (accept | reject) on the filtered traffic. Valid values are `accept` and `reject`
     */
    public readonly ruleAction!: pulumi.Output<string>;
    /**
     * The number of the Traffic Mirror rule. This number must be unique for each Traffic Mirror rule in a given direction. The rules are processed in ascending order by rule number.
     */
    public readonly ruleNumber!: pulumi.Output<number>;
    /**
     * The source CIDR block to assign to the Traffic Mirror rule.
     */
    public readonly sourceCidrBlock!: pulumi.Output<string>;
    /**
     * The source port range. Supported only when the protocol is set to TCP(6) or UDP(17). See Traffic mirror port range documented below
     */
    public readonly sourcePortRange!: pulumi.Output<outputs.ec2.TrafficMirrorFilterRuleSourcePortRange | undefined>;
    /**
     * The direction of traffic to be captured. Valid values are `ingress` and `egress`
     */
    public readonly trafficDirection!: pulumi.Output<string>;
    /**
     * ID of the traffic mirror filter to which this rule should be added
     */
    public readonly trafficMirrorFilterId!: pulumi.Output<string>;

    /**
     * Create a TrafficMirrorFilterRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TrafficMirrorFilterRuleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TrafficMirrorFilterRuleArgs | TrafficMirrorFilterRuleState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as TrafficMirrorFilterRuleState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["destinationCidrBlock"] = state ? state.destinationCidrBlock : undefined;
            inputs["destinationPortRange"] = state ? state.destinationPortRange : undefined;
            inputs["protocol"] = state ? state.protocol : undefined;
            inputs["ruleAction"] = state ? state.ruleAction : undefined;
            inputs["ruleNumber"] = state ? state.ruleNumber : undefined;
            inputs["sourceCidrBlock"] = state ? state.sourceCidrBlock : undefined;
            inputs["sourcePortRange"] = state ? state.sourcePortRange : undefined;
            inputs["trafficDirection"] = state ? state.trafficDirection : undefined;
            inputs["trafficMirrorFilterId"] = state ? state.trafficMirrorFilterId : undefined;
        } else {
            const args = argsOrState as TrafficMirrorFilterRuleArgs | undefined;
            if (!args || args.destinationCidrBlock === undefined) {
                throw new Error("Missing required property 'destinationCidrBlock'");
            }
            if (!args || args.ruleAction === undefined) {
                throw new Error("Missing required property 'ruleAction'");
            }
            if (!args || args.ruleNumber === undefined) {
                throw new Error("Missing required property 'ruleNumber'");
            }
            if (!args || args.sourceCidrBlock === undefined) {
                throw new Error("Missing required property 'sourceCidrBlock'");
            }
            if (!args || args.trafficDirection === undefined) {
                throw new Error("Missing required property 'trafficDirection'");
            }
            if (!args || args.trafficMirrorFilterId === undefined) {
                throw new Error("Missing required property 'trafficMirrorFilterId'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["destinationCidrBlock"] = args ? args.destinationCidrBlock : undefined;
            inputs["destinationPortRange"] = args ? args.destinationPortRange : undefined;
            inputs["protocol"] = args ? args.protocol : undefined;
            inputs["ruleAction"] = args ? args.ruleAction : undefined;
            inputs["ruleNumber"] = args ? args.ruleNumber : undefined;
            inputs["sourceCidrBlock"] = args ? args.sourceCidrBlock : undefined;
            inputs["sourcePortRange"] = args ? args.sourcePortRange : undefined;
            inputs["trafficDirection"] = args ? args.trafficDirection : undefined;
            inputs["trafficMirrorFilterId"] = args ? args.trafficMirrorFilterId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(TrafficMirrorFilterRule.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering TrafficMirrorFilterRule resources.
 */
export interface TrafficMirrorFilterRuleState {
    /**
     * A description of the traffic mirror filter rule.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The destination CIDR block to assign to the Traffic Mirror rule.
     */
    readonly destinationCidrBlock?: pulumi.Input<string>;
    /**
     * The destination port range. Supported only when the protocol is set to TCP(6) or UDP(17). See Traffic mirror port range documented below
     */
    readonly destinationPortRange?: pulumi.Input<inputs.ec2.TrafficMirrorFilterRuleDestinationPortRange>;
    /**
     * The protocol number, for example 17 (UDP), to assign to the Traffic Mirror rule. For information about the protocol value, see [Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) on the Internet Assigned Numbers Authority (IANA) website.
     */
    readonly protocol?: pulumi.Input<number>;
    /**
     * The action to take (accept | reject) on the filtered traffic. Valid values are `accept` and `reject`
     */
    readonly ruleAction?: pulumi.Input<string>;
    /**
     * The number of the Traffic Mirror rule. This number must be unique for each Traffic Mirror rule in a given direction. The rules are processed in ascending order by rule number.
     */
    readonly ruleNumber?: pulumi.Input<number>;
    /**
     * The source CIDR block to assign to the Traffic Mirror rule.
     */
    readonly sourceCidrBlock?: pulumi.Input<string>;
    /**
     * The source port range. Supported only when the protocol is set to TCP(6) or UDP(17). See Traffic mirror port range documented below
     */
    readonly sourcePortRange?: pulumi.Input<inputs.ec2.TrafficMirrorFilterRuleSourcePortRange>;
    /**
     * The direction of traffic to be captured. Valid values are `ingress` and `egress`
     */
    readonly trafficDirection?: pulumi.Input<string>;
    /**
     * ID of the traffic mirror filter to which this rule should be added
     */
    readonly trafficMirrorFilterId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a TrafficMirrorFilterRule resource.
 */
export interface TrafficMirrorFilterRuleArgs {
    /**
     * A description of the traffic mirror filter rule.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The destination CIDR block to assign to the Traffic Mirror rule.
     */
    readonly destinationCidrBlock: pulumi.Input<string>;
    /**
     * The destination port range. Supported only when the protocol is set to TCP(6) or UDP(17). See Traffic mirror port range documented below
     */
    readonly destinationPortRange?: pulumi.Input<inputs.ec2.TrafficMirrorFilterRuleDestinationPortRange>;
    /**
     * The protocol number, for example 17 (UDP), to assign to the Traffic Mirror rule. For information about the protocol value, see [Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) on the Internet Assigned Numbers Authority (IANA) website.
     */
    readonly protocol?: pulumi.Input<number>;
    /**
     * The action to take (accept | reject) on the filtered traffic. Valid values are `accept` and `reject`
     */
    readonly ruleAction: pulumi.Input<string>;
    /**
     * The number of the Traffic Mirror rule. This number must be unique for each Traffic Mirror rule in a given direction. The rules are processed in ascending order by rule number.
     */
    readonly ruleNumber: pulumi.Input<number>;
    /**
     * The source CIDR block to assign to the Traffic Mirror rule.
     */
    readonly sourceCidrBlock: pulumi.Input<string>;
    /**
     * The source port range. Supported only when the protocol is set to TCP(6) or UDP(17). See Traffic mirror port range documented below
     */
    readonly sourcePortRange?: pulumi.Input<inputs.ec2.TrafficMirrorFilterRuleSourcePortRange>;
    /**
     * The direction of traffic to be captured. Valid values are `ingress` and `egress`
     */
    readonly trafficDirection: pulumi.Input<string>;
    /**
     * ID of the traffic mirror filter to which this rule should be added
     */
    readonly trafficMirrorFilterId: pulumi.Input<string>;
}
