// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apigatewayv2

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages an Amazon API Gateway Version 2 API mapping.
// More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html).
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
// 		_, err := apigatewayv2.NewApiMapping(ctx, "example", &apigatewayv2.ApiMappingArgs{
// 			ApiId:      pulumi.Any(aws_apigatewayv2_api.Example.Id),
// 			DomainName: pulumi.Any(aws_apigatewayv2_domain_name.Example.Id),
// 			Stage:      pulumi.Any(aws_apigatewayv2_stage.Example.Id),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type ApiMapping struct {
	pulumi.CustomResourceState

	// The API identifier.
	ApiId pulumi.StringOutput `pulumi:"apiId"`
	// The [API mapping key](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-mapping-template-reference.html).
	ApiMappingKey pulumi.StringPtrOutput `pulumi:"apiMappingKey"`
	// The domain name. Use the `apigatewayv2.DomainName` resource to configure a domain name.
	DomainName pulumi.StringOutput `pulumi:"domainName"`
	// The API stage. Use the `apigatewayv2.Stage` resource to configure an API stage.
	Stage pulumi.StringOutput `pulumi:"stage"`
}

// NewApiMapping registers a new resource with the given unique name, arguments, and options.
func NewApiMapping(ctx *pulumi.Context,
	name string, args *ApiMappingArgs, opts ...pulumi.ResourceOption) (*ApiMapping, error) {
	if args == nil || args.ApiId == nil {
		return nil, errors.New("missing required argument 'ApiId'")
	}
	if args == nil || args.DomainName == nil {
		return nil, errors.New("missing required argument 'DomainName'")
	}
	if args == nil || args.Stage == nil {
		return nil, errors.New("missing required argument 'Stage'")
	}
	if args == nil {
		args = &ApiMappingArgs{}
	}
	var resource ApiMapping
	err := ctx.RegisterResource("aws:apigatewayv2/apiMapping:ApiMapping", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetApiMapping gets an existing ApiMapping resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApiMapping(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ApiMappingState, opts ...pulumi.ResourceOption) (*ApiMapping, error) {
	var resource ApiMapping
	err := ctx.ReadResource("aws:apigatewayv2/apiMapping:ApiMapping", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ApiMapping resources.
type apiMappingState struct {
	// The API identifier.
	ApiId *string `pulumi:"apiId"`
	// The [API mapping key](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-mapping-template-reference.html).
	ApiMappingKey *string `pulumi:"apiMappingKey"`
	// The domain name. Use the `apigatewayv2.DomainName` resource to configure a domain name.
	DomainName *string `pulumi:"domainName"`
	// The API stage. Use the `apigatewayv2.Stage` resource to configure an API stage.
	Stage *string `pulumi:"stage"`
}

type ApiMappingState struct {
	// The API identifier.
	ApiId pulumi.StringPtrInput
	// The [API mapping key](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-mapping-template-reference.html).
	ApiMappingKey pulumi.StringPtrInput
	// The domain name. Use the `apigatewayv2.DomainName` resource to configure a domain name.
	DomainName pulumi.StringPtrInput
	// The API stage. Use the `apigatewayv2.Stage` resource to configure an API stage.
	Stage pulumi.StringPtrInput
}

func (ApiMappingState) ElementType() reflect.Type {
	return reflect.TypeOf((*apiMappingState)(nil)).Elem()
}

type apiMappingArgs struct {
	// The API identifier.
	ApiId string `pulumi:"apiId"`
	// The [API mapping key](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-mapping-template-reference.html).
	ApiMappingKey *string `pulumi:"apiMappingKey"`
	// The domain name. Use the `apigatewayv2.DomainName` resource to configure a domain name.
	DomainName string `pulumi:"domainName"`
	// The API stage. Use the `apigatewayv2.Stage` resource to configure an API stage.
	Stage string `pulumi:"stage"`
}

// The set of arguments for constructing a ApiMapping resource.
type ApiMappingArgs struct {
	// The API identifier.
	ApiId pulumi.StringInput
	// The [API mapping key](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-mapping-template-reference.html).
	ApiMappingKey pulumi.StringPtrInput
	// The domain name. Use the `apigatewayv2.DomainName` resource to configure a domain name.
	DomainName pulumi.StringInput
	// The API stage. Use the `apigatewayv2.Stage` resource to configure an API stage.
	Stage pulumi.StringInput
}

func (ApiMappingArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*apiMappingArgs)(nil)).Elem()
}
