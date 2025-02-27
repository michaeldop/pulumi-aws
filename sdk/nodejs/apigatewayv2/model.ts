// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages an Amazon API Gateway Version 2 [model](https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html#models-mappings-models).
 *
 * ## Example Usage
 * ### Basic
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const example = new aws.apigatewayv2.Model("example", {
 *     apiId: aws_apigatewayv2_api.example.id,
 *     contentType: "application/json",
 *     schema: `{
 *   "$schema": "http://json-schema.org/draft-04/schema#",
 *   "title": "ExampleModel",
 *   "type": "object",
 *   "properties": {
 *     "id": { "type": "string" }
 *   }
 * }
 * `,
 * });
 * ```
 */
export class Model extends pulumi.CustomResource {
    /**
     * Get an existing Model resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ModelState, opts?: pulumi.CustomResourceOptions): Model {
        return new Model(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:apigatewayv2/model:Model';

    /**
     * Returns true if the given object is an instance of Model.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Model {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Model.__pulumiType;
    }

    /**
     * The API identifier.
     */
    public readonly apiId!: pulumi.Output<string>;
    /**
     * The content-type for the model, for example, `application/json`.
     */
    public readonly contentType!: pulumi.Output<string>;
    /**
     * The description of the model.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The name of the model. Must be alphanumeric.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The schema for the model. This should be a [JSON schema draft 4](https://tools.ietf.org/html/draft-zyp-json-schema-04) model.
     */
    public readonly schema!: pulumi.Output<string>;

    /**
     * Create a Model resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ModelArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ModelArgs | ModelState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ModelState | undefined;
            inputs["apiId"] = state ? state.apiId : undefined;
            inputs["contentType"] = state ? state.contentType : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["schema"] = state ? state.schema : undefined;
        } else {
            const args = argsOrState as ModelArgs | undefined;
            if (!args || args.apiId === undefined) {
                throw new Error("Missing required property 'apiId'");
            }
            if (!args || args.contentType === undefined) {
                throw new Error("Missing required property 'contentType'");
            }
            if (!args || args.schema === undefined) {
                throw new Error("Missing required property 'schema'");
            }
            inputs["apiId"] = args ? args.apiId : undefined;
            inputs["contentType"] = args ? args.contentType : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["schema"] = args ? args.schema : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Model.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Model resources.
 */
export interface ModelState {
    /**
     * The API identifier.
     */
    readonly apiId?: pulumi.Input<string>;
    /**
     * The content-type for the model, for example, `application/json`.
     */
    readonly contentType?: pulumi.Input<string>;
    /**
     * The description of the model.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name of the model. Must be alphanumeric.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The schema for the model. This should be a [JSON schema draft 4](https://tools.ietf.org/html/draft-zyp-json-schema-04) model.
     */
    readonly schema?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Model resource.
 */
export interface ModelArgs {
    /**
     * The API identifier.
     */
    readonly apiId: pulumi.Input<string>;
    /**
     * The content-type for the model, for example, `application/json`.
     */
    readonly contentType: pulumi.Input<string>;
    /**
     * The description of the model.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name of the model. Must be alphanumeric.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The schema for the model. This should be a [JSON schema draft 4](https://tools.ietf.org/html/draft-zyp-json-schema-04) model.
     */
    readonly schema: pulumi.Input<string>;
}
