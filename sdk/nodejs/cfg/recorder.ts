// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides an AWS Config Configuration Recorder. Please note that this resource **does not start** the created recorder automatically.
 *
 * > **Note:** _Starting_ the Configuration Recorder requires a `delivery channel` (while delivery channel creation requires Configuration Recorder). This is why `aws.cfg.RecorderStatus` is a separate resource.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const role = new aws.iam.Role("role", {assumeRolePolicy: `{
 *   "Version": "2012-10-17",
 *   "Statement": [
 *     {
 *       "Action": "sts:AssumeRole",
 *       "Principal": {
 *         "Service": "config.amazonaws.com"
 *       },
 *       "Effect": "Allow",
 *       "Sid": ""
 *     }
 *   ]
 * }
 * `});
 * const foo = new aws.cfg.Recorder("foo", {roleArn: role.arn});
 * ```
 */
export class Recorder extends pulumi.CustomResource {
    /**
     * Get an existing Recorder resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RecorderState, opts?: pulumi.CustomResourceOptions): Recorder {
        return new Recorder(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:cfg/recorder:Recorder';

    /**
     * Returns true if the given object is an instance of Recorder.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Recorder {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Recorder.__pulumiType;
    }

    /**
     * The name of the recorder. Defaults to `default`. Changing it recreates the resource.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Recording group - see below.
     */
    public readonly recordingGroup!: pulumi.Output<outputs.cfg.RecorderRecordingGroup>;
    /**
     * Amazon Resource Name (ARN) of the IAM role.
     * used to make read or write requests to the delivery channel and to describe the AWS resources associated with the account.
     * See [AWS Docs](http://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html) for more details.
     */
    public readonly roleArn!: pulumi.Output<string>;

    /**
     * Create a Recorder resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RecorderArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RecorderArgs | RecorderState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as RecorderState | undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["recordingGroup"] = state ? state.recordingGroup : undefined;
            inputs["roleArn"] = state ? state.roleArn : undefined;
        } else {
            const args = argsOrState as RecorderArgs | undefined;
            if (!args || args.roleArn === undefined) {
                throw new Error("Missing required property 'roleArn'");
            }
            inputs["name"] = args ? args.name : undefined;
            inputs["recordingGroup"] = args ? args.recordingGroup : undefined;
            inputs["roleArn"] = args ? args.roleArn : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Recorder.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Recorder resources.
 */
export interface RecorderState {
    /**
     * The name of the recorder. Defaults to `default`. Changing it recreates the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Recording group - see below.
     */
    readonly recordingGroup?: pulumi.Input<inputs.cfg.RecorderRecordingGroup>;
    /**
     * Amazon Resource Name (ARN) of the IAM role.
     * used to make read or write requests to the delivery channel and to describe the AWS resources associated with the account.
     * See [AWS Docs](http://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html) for more details.
     */
    readonly roleArn?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Recorder resource.
 */
export interface RecorderArgs {
    /**
     * The name of the recorder. Defaults to `default`. Changing it recreates the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Recording group - see below.
     */
    readonly recordingGroup?: pulumi.Input<inputs.cfg.RecorderRecordingGroup>;
    /**
     * Amazon Resource Name (ARN) of the IAM role.
     * used to make read or write requests to the delivery channel and to describe the AWS resources associated with the account.
     * See [AWS Docs](http://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html) for more details.
     */
    readonly roleArn: pulumi.Input<string>;
}
