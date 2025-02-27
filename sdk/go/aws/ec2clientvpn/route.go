// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2clientvpn

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides additional routes for AWS Client VPN endpoints. For more information on usage, please see the
// [AWS Client VPN Administrator's Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html).
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/ec2clientvpn"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		exampleEndpoint, err := ec2clientvpn.NewEndpoint(ctx, "exampleEndpoint", &ec2clientvpn.EndpointArgs{
// 			Description:          pulumi.String("Example Client VPN endpoint"),
// 			ServerCertificateArn: pulumi.Any(aws_acm_certificate.Example.Arn),
// 			ClientCidrBlock:      pulumi.String("10.0.0.0/16"),
// 			AuthenticationOptions: ec2clientvpn.EndpointAuthenticationOptionArray{
// 				&ec2clientvpn.EndpointAuthenticationOptionArgs{
// 					Type:                    pulumi.String("certificate-authentication"),
// 					RootCertificateChainArn: pulumi.Any(aws_acm_certificate.Example.Arn),
// 				},
// 			},
// 			ConnectionLogOptions: &ec2clientvpn.EndpointConnectionLogOptionsArgs{
// 				Enabled: pulumi.Bool(false),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleNetworkAssociation, err := ec2clientvpn.NewNetworkAssociation(ctx, "exampleNetworkAssociation", &ec2clientvpn.NetworkAssociationArgs{
// 			ClientVpnEndpointId: exampleEndpoint.ID(),
// 			SubnetId:            pulumi.Any(aws_subnet.Example.Id),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = ec2clientvpn.NewRoute(ctx, "exampleRoute", &ec2clientvpn.RouteArgs{
// 			ClientVpnEndpointId:  exampleEndpoint.ID(),
// 			DestinationCidrBlock: pulumi.String("0.0.0.0/0"),
// 			TargetVpcSubnetId:    exampleNetworkAssociation.SubnetId,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ## Attribute Reference
//
// In addition to all arguments above, the following attributes are exported:
//
// * `id` - The ID of the Client VPN endpoint.
// * `origin` - Indicates how the Client VPN route was added. Will be `add-route` for routes created by this resource.
// * `type` - The type of the route.
type Route struct {
	pulumi.CustomResourceState

	// The ID of the Client VPN endpoint.
	ClientVpnEndpointId pulumi.StringOutput `pulumi:"clientVpnEndpointId"`
	// A brief description of the authorization rule.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The IPv4 address range, in CIDR notation, of the route destination.
	DestinationCidrBlock pulumi.StringOutput `pulumi:"destinationCidrBlock"`
	Origin               pulumi.StringOutput `pulumi:"origin"`
	// The ID of the Subnet to route the traffic through. It must already be attached to the Client VPN.
	TargetVpcSubnetId pulumi.StringOutput `pulumi:"targetVpcSubnetId"`
	Type              pulumi.StringOutput `pulumi:"type"`
}

// NewRoute registers a new resource with the given unique name, arguments, and options.
func NewRoute(ctx *pulumi.Context,
	name string, args *RouteArgs, opts ...pulumi.ResourceOption) (*Route, error) {
	if args == nil || args.ClientVpnEndpointId == nil {
		return nil, errors.New("missing required argument 'ClientVpnEndpointId'")
	}
	if args == nil || args.DestinationCidrBlock == nil {
		return nil, errors.New("missing required argument 'DestinationCidrBlock'")
	}
	if args == nil || args.TargetVpcSubnetId == nil {
		return nil, errors.New("missing required argument 'TargetVpcSubnetId'")
	}
	if args == nil {
		args = &RouteArgs{}
	}
	var resource Route
	err := ctx.RegisterResource("aws:ec2clientvpn/route:Route", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRoute gets an existing Route resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRoute(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RouteState, opts ...pulumi.ResourceOption) (*Route, error) {
	var resource Route
	err := ctx.ReadResource("aws:ec2clientvpn/route:Route", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Route resources.
type routeState struct {
	// The ID of the Client VPN endpoint.
	ClientVpnEndpointId *string `pulumi:"clientVpnEndpointId"`
	// A brief description of the authorization rule.
	Description *string `pulumi:"description"`
	// The IPv4 address range, in CIDR notation, of the route destination.
	DestinationCidrBlock *string `pulumi:"destinationCidrBlock"`
	Origin               *string `pulumi:"origin"`
	// The ID of the Subnet to route the traffic through. It must already be attached to the Client VPN.
	TargetVpcSubnetId *string `pulumi:"targetVpcSubnetId"`
	Type              *string `pulumi:"type"`
}

type RouteState struct {
	// The ID of the Client VPN endpoint.
	ClientVpnEndpointId pulumi.StringPtrInput
	// A brief description of the authorization rule.
	Description pulumi.StringPtrInput
	// The IPv4 address range, in CIDR notation, of the route destination.
	DestinationCidrBlock pulumi.StringPtrInput
	Origin               pulumi.StringPtrInput
	// The ID of the Subnet to route the traffic through. It must already be attached to the Client VPN.
	TargetVpcSubnetId pulumi.StringPtrInput
	Type              pulumi.StringPtrInput
}

func (RouteState) ElementType() reflect.Type {
	return reflect.TypeOf((*routeState)(nil)).Elem()
}

type routeArgs struct {
	// The ID of the Client VPN endpoint.
	ClientVpnEndpointId string `pulumi:"clientVpnEndpointId"`
	// A brief description of the authorization rule.
	Description *string `pulumi:"description"`
	// The IPv4 address range, in CIDR notation, of the route destination.
	DestinationCidrBlock string `pulumi:"destinationCidrBlock"`
	// The ID of the Subnet to route the traffic through. It must already be attached to the Client VPN.
	TargetVpcSubnetId string `pulumi:"targetVpcSubnetId"`
}

// The set of arguments for constructing a Route resource.
type RouteArgs struct {
	// The ID of the Client VPN endpoint.
	ClientVpnEndpointId pulumi.StringInput
	// A brief description of the authorization rule.
	Description pulumi.StringPtrInput
	// The IPv4 address range, in CIDR notation, of the route destination.
	DestinationCidrBlock pulumi.StringInput
	// The ID of the Subnet to route the traffic through. It must already be attached to the Client VPN.
	TargetVpcSubnetId pulumi.StringInput
}

func (RouteArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*routeArgs)(nil)).Elem()
}
