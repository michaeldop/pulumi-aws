// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an API Gateway Resource.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/apigateway"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		myDemoAPI, err := apigateway.NewRestApi(ctx, "myDemoAPI", &apigateway.RestApiArgs{
// 			Description: pulumi.String("This is my API for demonstration purposes"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = apigateway.NewResource(ctx, "myDemoResource", &apigateway.ResourceArgs{
// 			RestApi:  myDemoAPI.ID(),
// 			ParentId: myDemoAPI.RootResourceId,
// 			PathPart: pulumi.String("mydemoresource"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Resource struct {
	pulumi.CustomResourceState

	// The ID of the parent API resource
	ParentId pulumi.StringOutput `pulumi:"parentId"`
	// The complete path for this API resource, including all parent paths.
	Path pulumi.StringOutput `pulumi:"path"`
	// The last path segment of this API resource.
	PathPart pulumi.StringOutput `pulumi:"pathPart"`
	// The ID of the associated REST API
	RestApi pulumi.StringOutput `pulumi:"restApi"`
}

// NewResource registers a new resource with the given unique name, arguments, and options.
func NewResource(ctx *pulumi.Context,
	name string, args *ResourceArgs, opts ...pulumi.ResourceOption) (*Resource, error) {
	if args == nil || args.ParentId == nil {
		return nil, errors.New("missing required argument 'ParentId'")
	}
	if args == nil || args.PathPart == nil {
		return nil, errors.New("missing required argument 'PathPart'")
	}
	if args == nil || args.RestApi == nil {
		return nil, errors.New("missing required argument 'RestApi'")
	}
	if args == nil {
		args = &ResourceArgs{}
	}
	var resource Resource
	err := ctx.RegisterResource("aws:apigateway/resource:Resource", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetResource gets an existing Resource resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetResource(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ResourceState, opts ...pulumi.ResourceOption) (*Resource, error) {
	var resource Resource
	err := ctx.ReadResource("aws:apigateway/resource:Resource", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Resource resources.
type resourceState struct {
	// The ID of the parent API resource
	ParentId *string `pulumi:"parentId"`
	// The complete path for this API resource, including all parent paths.
	Path *string `pulumi:"path"`
	// The last path segment of this API resource.
	PathPart *string `pulumi:"pathPart"`
	// The ID of the associated REST API
	RestApi *string `pulumi:"restApi"`
}

type ResourceState struct {
	// The ID of the parent API resource
	ParentId pulumi.StringPtrInput
	// The complete path for this API resource, including all parent paths.
	Path pulumi.StringPtrInput
	// The last path segment of this API resource.
	PathPart pulumi.StringPtrInput
	// The ID of the associated REST API
	RestApi pulumi.StringPtrInput
}

func (ResourceState) ElementType() reflect.Type {
	return reflect.TypeOf((*resourceState)(nil)).Elem()
}

type resourceArgs struct {
	// The ID of the parent API resource
	ParentId string `pulumi:"parentId"`
	// The last path segment of this API resource.
	PathPart string `pulumi:"pathPart"`
	// The ID of the associated REST API
	RestApi interface{} `pulumi:"restApi"`
}

// The set of arguments for constructing a Resource resource.
type ResourceArgs struct {
	// The ID of the parent API resource
	ParentId pulumi.StringInput
	// The last path segment of this API resource.
	PathPart pulumi.StringInput
	// The ID of the associated REST API
	RestApi pulumi.Input
}

func (ResourceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*resourceArgs)(nil)).Elem()
}
