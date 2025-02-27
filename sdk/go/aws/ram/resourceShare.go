// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ram

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Resource Access Manager (RAM) Resource Share. To associate principals with the share, see the `ram.PrincipalAssociation` resource. To associate resources with the share, see the `ram.ResourceAssociation` resource.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/ram"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := ram.NewResourceShare(ctx, "example", &ram.ResourceShareArgs{
// 			AllowExternalPrincipals: pulumi.Bool(true),
// 			Tags: pulumi.StringMap{
// 				"Environment": pulumi.String("Production"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type ResourceShare struct {
	pulumi.CustomResourceState

	// Indicates whether principals outside your organization can be associated with a resource share.
	AllowExternalPrincipals pulumi.BoolPtrOutput `pulumi:"allowExternalPrincipals"`
	// The Amazon Resource Name (ARN) of the resource share.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The name of the resource share.
	Name pulumi.StringOutput `pulumi:"name"`
	// A map of tags to assign to the resource share.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
}

// NewResourceShare registers a new resource with the given unique name, arguments, and options.
func NewResourceShare(ctx *pulumi.Context,
	name string, args *ResourceShareArgs, opts ...pulumi.ResourceOption) (*ResourceShare, error) {
	if args == nil {
		args = &ResourceShareArgs{}
	}
	var resource ResourceShare
	err := ctx.RegisterResource("aws:ram/resourceShare:ResourceShare", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetResourceShare gets an existing ResourceShare resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetResourceShare(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ResourceShareState, opts ...pulumi.ResourceOption) (*ResourceShare, error) {
	var resource ResourceShare
	err := ctx.ReadResource("aws:ram/resourceShare:ResourceShare", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ResourceShare resources.
type resourceShareState struct {
	// Indicates whether principals outside your organization can be associated with a resource share.
	AllowExternalPrincipals *bool `pulumi:"allowExternalPrincipals"`
	// The Amazon Resource Name (ARN) of the resource share.
	Arn *string `pulumi:"arn"`
	// The name of the resource share.
	Name *string `pulumi:"name"`
	// A map of tags to assign to the resource share.
	Tags map[string]string `pulumi:"tags"`
}

type ResourceShareState struct {
	// Indicates whether principals outside your organization can be associated with a resource share.
	AllowExternalPrincipals pulumi.BoolPtrInput
	// The Amazon Resource Name (ARN) of the resource share.
	Arn pulumi.StringPtrInput
	// The name of the resource share.
	Name pulumi.StringPtrInput
	// A map of tags to assign to the resource share.
	Tags pulumi.StringMapInput
}

func (ResourceShareState) ElementType() reflect.Type {
	return reflect.TypeOf((*resourceShareState)(nil)).Elem()
}

type resourceShareArgs struct {
	// Indicates whether principals outside your organization can be associated with a resource share.
	AllowExternalPrincipals *bool `pulumi:"allowExternalPrincipals"`
	// The name of the resource share.
	Name *string `pulumi:"name"`
	// A map of tags to assign to the resource share.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a ResourceShare resource.
type ResourceShareArgs struct {
	// Indicates whether principals outside your organization can be associated with a resource share.
	AllowExternalPrincipals pulumi.BoolPtrInput
	// The name of the resource share.
	Name pulumi.StringPtrInput
	// A map of tags to assign to the resource share.
	Tags pulumi.StringMapInput
}

func (ResourceShareArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*resourceShareArgs)(nil)).Elem()
}
