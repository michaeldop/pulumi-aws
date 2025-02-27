// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apigatewayv2

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages an Amazon API Gateway Version 2 deployment.
// More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html).
//
// > **Note:** Creating a deployment for an API requires at least one `apigatewayv2.Route` resource associated with that API. To avoid race conditions when all resources are being created together, you need to add implicit resource references via the `triggers` argument or explicit resource references using the [resource `dependsOn` meta-argument](https://www.pulumi.com/docs/intro/concepts/programming-model/#dependson).
//
// ## Example Usage
// ### Basic
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/apigatewayv2"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := apigatewayv2.NewDeployment(ctx, "example", &apigatewayv2.DeploymentArgs{
// 			ApiId:       pulumi.Any(aws_apigatewayv2_route.Example.Api_id),
// 			Description: pulumi.String("Example deployment"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Deployment struct {
	pulumi.CustomResourceState

	// The API identifier.
	ApiId pulumi.StringOutput `pulumi:"apiId"`
	// Whether the deployment was automatically released.
	AutoDeployed pulumi.BoolOutput `pulumi:"autoDeployed"`
	// The description for the deployment resource.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// A map of arbitrary keys and values that, when changed, will trigger a redeployment.
	Triggers pulumi.StringMapOutput `pulumi:"triggers"`
}

// NewDeployment registers a new resource with the given unique name, arguments, and options.
func NewDeployment(ctx *pulumi.Context,
	name string, args *DeploymentArgs, opts ...pulumi.ResourceOption) (*Deployment, error) {
	if args == nil || args.ApiId == nil {
		return nil, errors.New("missing required argument 'ApiId'")
	}
	if args == nil {
		args = &DeploymentArgs{}
	}
	var resource Deployment
	err := ctx.RegisterResource("aws:apigatewayv2/deployment:Deployment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDeployment gets an existing Deployment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDeployment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DeploymentState, opts ...pulumi.ResourceOption) (*Deployment, error) {
	var resource Deployment
	err := ctx.ReadResource("aws:apigatewayv2/deployment:Deployment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Deployment resources.
type deploymentState struct {
	// The API identifier.
	ApiId *string `pulumi:"apiId"`
	// Whether the deployment was automatically released.
	AutoDeployed *bool `pulumi:"autoDeployed"`
	// The description for the deployment resource.
	Description *string `pulumi:"description"`
	// A map of arbitrary keys and values that, when changed, will trigger a redeployment.
	Triggers map[string]string `pulumi:"triggers"`
}

type DeploymentState struct {
	// The API identifier.
	ApiId pulumi.StringPtrInput
	// Whether the deployment was automatically released.
	AutoDeployed pulumi.BoolPtrInput
	// The description for the deployment resource.
	Description pulumi.StringPtrInput
	// A map of arbitrary keys and values that, when changed, will trigger a redeployment.
	Triggers pulumi.StringMapInput
}

func (DeploymentState) ElementType() reflect.Type {
	return reflect.TypeOf((*deploymentState)(nil)).Elem()
}

type deploymentArgs struct {
	// The API identifier.
	ApiId string `pulumi:"apiId"`
	// The description for the deployment resource.
	Description *string `pulumi:"description"`
	// A map of arbitrary keys and values that, when changed, will trigger a redeployment.
	Triggers map[string]string `pulumi:"triggers"`
}

// The set of arguments for constructing a Deployment resource.
type DeploymentArgs struct {
	// The API identifier.
	ApiId pulumi.StringInput
	// The description for the deployment resource.
	Description pulumi.StringPtrInput
	// A map of arbitrary keys and values that, when changed, will trigger a redeployment.
	Triggers pulumi.StringMapInput
}

func (DeploymentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*deploymentArgs)(nil)).Elem()
}
