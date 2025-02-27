// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides a workspace in [AWS Workspaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html) Service
 *
 * > **NOTE:** During deletion of an `aws.workspaces.Workspace` resource, the service role `workspaces_DefaultRole` must be attached to the
 * policy `arn:aws:iam::aws:policy/AmazonWorkSpacesServiceAccess`, or it will leak the ENI that the Workspaces service creates for the Workspace.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const valueWindows10 = aws.workspaces.getBundle({
 *     bundleId: "wsb-bh8rsxt14",
 * });
 * const example = new aws.workspaces.Workspace("example", {
 *     directoryId: aws_workspaces_directory.example.id,
 *     bundleId: valueWindows10.then(valueWindows10 => valueWindows10.id),
 *     userName: "john.doe",
 *     rootVolumeEncryptionEnabled: true,
 *     userVolumeEncryptionEnabled: true,
 *     volumeEncryptionKey: "alias/aws/workspaces",
 *     workspaceProperties: {
 *         computeTypeName: "VALUE",
 *         userVolumeSizeGib: 10,
 *         rootVolumeSizeGib: 80,
 *         runningMode: "AUTO_STOP",
 *         runningModeAutoStopTimeoutInMinutes: 60,
 *     },
 *     tags: {
 *         Department: "IT",
 *     },
 * });
 * ```
 */
export class Workspace extends pulumi.CustomResource {
    /**
     * Get an existing Workspace resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WorkspaceState, opts?: pulumi.CustomResourceOptions): Workspace {
        return new Workspace(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:workspaces/workspace:Workspace';

    /**
     * Returns true if the given object is an instance of Workspace.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Workspace {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Workspace.__pulumiType;
    }

    /**
     * The ID of the bundle for the WorkSpace.
     */
    public readonly bundleId!: pulumi.Output<string>;
    /**
     * The name of the WorkSpace, as seen by the operating system.
     */
    public /*out*/ readonly computerName!: pulumi.Output<string>;
    /**
     * The ID of the directory for the WorkSpace.
     */
    public readonly directoryId!: pulumi.Output<string>;
    /**
     * The IP address of the WorkSpace.
     */
    public /*out*/ readonly ipAddress!: pulumi.Output<string>;
    /**
     * Indicates whether the data stored on the root volume is encrypted.
     */
    public readonly rootVolumeEncryptionEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The operational state of the WorkSpace.
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * The tags for the WorkSpace.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * The user name of the user for the WorkSpace. This user name must exist in the directory for the WorkSpace.
     */
    public readonly userName!: pulumi.Output<string>;
    /**
     * Indicates whether the data stored on the user volume is encrypted.
     */
    public readonly userVolumeEncryptionEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.
     */
    public readonly volumeEncryptionKey!: pulumi.Output<string | undefined>;
    /**
     * The WorkSpace properties.
     */
    public readonly workspaceProperties!: pulumi.Output<outputs.workspaces.WorkspaceWorkspaceProperties>;

    /**
     * Create a Workspace resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: WorkspaceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: WorkspaceArgs | WorkspaceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as WorkspaceState | undefined;
            inputs["bundleId"] = state ? state.bundleId : undefined;
            inputs["computerName"] = state ? state.computerName : undefined;
            inputs["directoryId"] = state ? state.directoryId : undefined;
            inputs["ipAddress"] = state ? state.ipAddress : undefined;
            inputs["rootVolumeEncryptionEnabled"] = state ? state.rootVolumeEncryptionEnabled : undefined;
            inputs["state"] = state ? state.state : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["userName"] = state ? state.userName : undefined;
            inputs["userVolumeEncryptionEnabled"] = state ? state.userVolumeEncryptionEnabled : undefined;
            inputs["volumeEncryptionKey"] = state ? state.volumeEncryptionKey : undefined;
            inputs["workspaceProperties"] = state ? state.workspaceProperties : undefined;
        } else {
            const args = argsOrState as WorkspaceArgs | undefined;
            if (!args || args.bundleId === undefined) {
                throw new Error("Missing required property 'bundleId'");
            }
            if (!args || args.directoryId === undefined) {
                throw new Error("Missing required property 'directoryId'");
            }
            if (!args || args.userName === undefined) {
                throw new Error("Missing required property 'userName'");
            }
            inputs["bundleId"] = args ? args.bundleId : undefined;
            inputs["directoryId"] = args ? args.directoryId : undefined;
            inputs["rootVolumeEncryptionEnabled"] = args ? args.rootVolumeEncryptionEnabled : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["userName"] = args ? args.userName : undefined;
            inputs["userVolumeEncryptionEnabled"] = args ? args.userVolumeEncryptionEnabled : undefined;
            inputs["volumeEncryptionKey"] = args ? args.volumeEncryptionKey : undefined;
            inputs["workspaceProperties"] = args ? args.workspaceProperties : undefined;
            inputs["computerName"] = undefined /*out*/;
            inputs["ipAddress"] = undefined /*out*/;
            inputs["state"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Workspace.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Workspace resources.
 */
export interface WorkspaceState {
    /**
     * The ID of the bundle for the WorkSpace.
     */
    readonly bundleId?: pulumi.Input<string>;
    /**
     * The name of the WorkSpace, as seen by the operating system.
     */
    readonly computerName?: pulumi.Input<string>;
    /**
     * The ID of the directory for the WorkSpace.
     */
    readonly directoryId?: pulumi.Input<string>;
    /**
     * The IP address of the WorkSpace.
     */
    readonly ipAddress?: pulumi.Input<string>;
    /**
     * Indicates whether the data stored on the root volume is encrypted.
     */
    readonly rootVolumeEncryptionEnabled?: pulumi.Input<boolean>;
    /**
     * The operational state of the WorkSpace.
     */
    readonly state?: pulumi.Input<string>;
    /**
     * The tags for the WorkSpace.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The user name of the user for the WorkSpace. This user name must exist in the directory for the WorkSpace.
     */
    readonly userName?: pulumi.Input<string>;
    /**
     * Indicates whether the data stored on the user volume is encrypted.
     */
    readonly userVolumeEncryptionEnabled?: pulumi.Input<boolean>;
    /**
     * The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.
     */
    readonly volumeEncryptionKey?: pulumi.Input<string>;
    /**
     * The WorkSpace properties.
     */
    readonly workspaceProperties?: pulumi.Input<inputs.workspaces.WorkspaceWorkspaceProperties>;
}

/**
 * The set of arguments for constructing a Workspace resource.
 */
export interface WorkspaceArgs {
    /**
     * The ID of the bundle for the WorkSpace.
     */
    readonly bundleId: pulumi.Input<string>;
    /**
     * The ID of the directory for the WorkSpace.
     */
    readonly directoryId: pulumi.Input<string>;
    /**
     * Indicates whether the data stored on the root volume is encrypted.
     */
    readonly rootVolumeEncryptionEnabled?: pulumi.Input<boolean>;
    /**
     * The tags for the WorkSpace.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The user name of the user for the WorkSpace. This user name must exist in the directory for the WorkSpace.
     */
    readonly userName: pulumi.Input<string>;
    /**
     * Indicates whether the data stored on the user volume is encrypted.
     */
    readonly userVolumeEncryptionEnabled?: pulumi.Input<boolean>;
    /**
     * The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.
     */
    readonly volumeEncryptionKey?: pulumi.Input<string>;
    /**
     * The WorkSpace properties.
     */
    readonly workspaceProperties?: pulumi.Input<inputs.workspaces.WorkspaceWorkspaceProperties>;
}
