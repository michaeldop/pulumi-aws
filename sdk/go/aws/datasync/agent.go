// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package datasync

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages an AWS DataSync Agent deployed on premises.
//
// > **NOTE:** One of `activationKey` or `ipAddress` must be provided for resource creation (agent activation). Neither is required for resource import. If using `ipAddress`, this provider must be able to make an HTTP (port 80) GET request to the specified IP address from where it is running. The agent will turn off that HTTP server after activation.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/datasync"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := datasync.NewAgent(ctx, "example", &datasync.AgentArgs{
// 			IpAddress: pulumi.String("1.2.3.4"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Agent struct {
	pulumi.CustomResourceState

	// DataSync Agent activation key during resource creation. Conflicts with `ipAddress`. If an `ipAddress` is provided instead, the provider will retrieve the `activationKey` as part of the resource creation.
	ActivationKey pulumi.StringOutput `pulumi:"activationKey"`
	// Amazon Resource Name (ARN) of the DataSync Agent.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with `activationKey`. DataSync Agent must be accessible on port 80 from where the provider is running.
	IpAddress pulumi.StringOutput `pulumi:"ipAddress"`
	// Name of the DataSync Agent.
	Name pulumi.StringOutput `pulumi:"name"`
	// Key-value pairs of resource tags to assign to the DataSync Agent.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
}

// NewAgent registers a new resource with the given unique name, arguments, and options.
func NewAgent(ctx *pulumi.Context,
	name string, args *AgentArgs, opts ...pulumi.ResourceOption) (*Agent, error) {
	if args == nil {
		args = &AgentArgs{}
	}
	var resource Agent
	err := ctx.RegisterResource("aws:datasync/agent:Agent", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAgent gets an existing Agent resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAgent(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AgentState, opts ...pulumi.ResourceOption) (*Agent, error) {
	var resource Agent
	err := ctx.ReadResource("aws:datasync/agent:Agent", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Agent resources.
type agentState struct {
	// DataSync Agent activation key during resource creation. Conflicts with `ipAddress`. If an `ipAddress` is provided instead, the provider will retrieve the `activationKey` as part of the resource creation.
	ActivationKey *string `pulumi:"activationKey"`
	// Amazon Resource Name (ARN) of the DataSync Agent.
	Arn *string `pulumi:"arn"`
	// DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with `activationKey`. DataSync Agent must be accessible on port 80 from where the provider is running.
	IpAddress *string `pulumi:"ipAddress"`
	// Name of the DataSync Agent.
	Name *string `pulumi:"name"`
	// Key-value pairs of resource tags to assign to the DataSync Agent.
	Tags map[string]string `pulumi:"tags"`
}

type AgentState struct {
	// DataSync Agent activation key during resource creation. Conflicts with `ipAddress`. If an `ipAddress` is provided instead, the provider will retrieve the `activationKey` as part of the resource creation.
	ActivationKey pulumi.StringPtrInput
	// Amazon Resource Name (ARN) of the DataSync Agent.
	Arn pulumi.StringPtrInput
	// DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with `activationKey`. DataSync Agent must be accessible on port 80 from where the provider is running.
	IpAddress pulumi.StringPtrInput
	// Name of the DataSync Agent.
	Name pulumi.StringPtrInput
	// Key-value pairs of resource tags to assign to the DataSync Agent.
	Tags pulumi.StringMapInput
}

func (AgentState) ElementType() reflect.Type {
	return reflect.TypeOf((*agentState)(nil)).Elem()
}

type agentArgs struct {
	// DataSync Agent activation key during resource creation. Conflicts with `ipAddress`. If an `ipAddress` is provided instead, the provider will retrieve the `activationKey` as part of the resource creation.
	ActivationKey *string `pulumi:"activationKey"`
	// DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with `activationKey`. DataSync Agent must be accessible on port 80 from where the provider is running.
	IpAddress *string `pulumi:"ipAddress"`
	// Name of the DataSync Agent.
	Name *string `pulumi:"name"`
	// Key-value pairs of resource tags to assign to the DataSync Agent.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a Agent resource.
type AgentArgs struct {
	// DataSync Agent activation key during resource creation. Conflicts with `ipAddress`. If an `ipAddress` is provided instead, the provider will retrieve the `activationKey` as part of the resource creation.
	ActivationKey pulumi.StringPtrInput
	// DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with `activationKey`. DataSync Agent must be accessible on port 80 from where the provider is running.
	IpAddress pulumi.StringPtrInput
	// Name of the DataSync Agent.
	Name pulumi.StringPtrInput
	// Key-value pairs of resource tags to assign to the DataSync Agent.
	Tags pulumi.StringMapInput
}

func (AgentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*agentArgs)(nil)).Elem()
}
