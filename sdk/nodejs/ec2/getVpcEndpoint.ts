// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * The VPC Endpoint data source provides details about
 * a specific VPC endpoint.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const s3 = aws.ec2.getVpcEndpoint({
 *     vpcId: aws_vpc.foo.id,
 *     serviceName: "com.amazonaws.us-west-2.s3",
 * });
 * const privateS3 = new aws.ec2.VpcEndpointRouteTableAssociation("privateS3", {
 *     vpcEndpointId: s3.then(s3 => s3.id),
 *     routeTableId: aws_route_table["private"].id,
 * });
 * ```
 */
export function getVpcEndpoint(args?: GetVpcEndpointArgs, opts?: pulumi.InvokeOptions): Promise<GetVpcEndpointResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("aws:ec2/getVpcEndpoint:getVpcEndpoint", {
        "filters": args.filters,
        "id": args.id,
        "serviceName": args.serviceName,
        "state": args.state,
        "tags": args.tags,
        "vpcId": args.vpcId,
    }, opts);
}

/**
 * A collection of arguments for invoking getVpcEndpoint.
 */
export interface GetVpcEndpointArgs {
    /**
     * Custom filter block as described below.
     */
    readonly filters?: inputs.ec2.GetVpcEndpointFilter[];
    /**
     * The ID of the specific VPC Endpoint to retrieve.
     */
    readonly id?: string;
    /**
     * The service name of the specific VPC Endpoint to retrieve. For AWS services the service name is usually in the form `com.amazonaws.<region>.<service>` (the SageMaker Notebook service is an exception to this rule, the service name is in the form `aws.sagemaker.<region>.notebook`).
     */
    readonly serviceName?: string;
    /**
     * The state of the specific VPC Endpoint to retrieve.
     */
    readonly state?: string;
    /**
     * A map of tags, each pair of which must exactly match
     * a pair on the specific VPC Endpoint to retrieve.
     */
    readonly tags?: {[key: string]: string};
    /**
     * The ID of the VPC in which the specific VPC Endpoint is used.
     */
    readonly vpcId?: string;
}

/**
 * A collection of values returned by getVpcEndpoint.
 */
export interface GetVpcEndpointResult {
    /**
     * The Amazon Resource Name (ARN) of the VPC endpoint.
     */
    readonly arn: string;
    /**
     * The list of CIDR blocks for the exposed AWS service. Applicable for endpoints of type `Gateway`.
     */
    readonly cidrBlocks: string[];
    /**
     * The DNS entries for the VPC Endpoint. Applicable for endpoints of type `Interface`. DNS blocks are documented below.
     */
    readonly dnsEntries: outputs.ec2.GetVpcEndpointDnsEntry[];
    readonly filters?: outputs.ec2.GetVpcEndpointFilter[];
    readonly id: string;
    /**
     * One or more network interfaces for the VPC Endpoint. Applicable for endpoints of type `Interface`.
     */
    readonly networkInterfaceIds: string[];
    /**
     * The ID of the AWS account that owns the VPC endpoint.
     */
    readonly ownerId: string;
    /**
     * The policy document associated with the VPC Endpoint. Applicable for endpoints of type `Gateway`.
     */
    readonly policy: string;
    /**
     * The prefix list ID of the exposed AWS service. Applicable for endpoints of type `Gateway`.
     */
    readonly prefixListId: string;
    /**
     * Whether or not the VPC is associated with a private hosted zone - `true` or `false`. Applicable for endpoints of type `Interface`.
     */
    readonly privateDnsEnabled: boolean;
    /**
     * Whether or not the VPC Endpoint is being managed by its service - `true` or `false`.
     */
    readonly requesterManaged: boolean;
    /**
     * One or more route tables associated with the VPC Endpoint. Applicable for endpoints of type `Gateway`.
     */
    readonly routeTableIds: string[];
    /**
     * One or more security groups associated with the network interfaces. Applicable for endpoints of type `Interface`.
     */
    readonly securityGroupIds: string[];
    readonly serviceName: string;
    readonly state: string;
    /**
     * One or more subnets in which the VPC Endpoint is located. Applicable for endpoints of type `Interface`.
     */
    readonly subnetIds: string[];
    readonly tags: {[key: string]: string};
    /**
     * The VPC Endpoint type, `Gateway` or `Interface`.
     */
    readonly vpcEndpointType: string;
    readonly vpcId: string;
}
