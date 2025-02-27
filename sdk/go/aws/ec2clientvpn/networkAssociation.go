// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2clientvpn

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides network associations for AWS Client VPN endpoints. For more information on usage, please see the
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
// 		_, err := ec2clientvpn.NewNetworkAssociation(ctx, "example", &ec2clientvpn.NetworkAssociationArgs{
// 			ClientVpnEndpointId: pulumi.Any(aws_ec2_client_vpn_endpoint.Example.Id),
// 			SubnetId:            pulumi.Any(aws_subnet.Example.Id),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type NetworkAssociation struct {
	pulumi.CustomResourceState

	// The ID of the Client VPN endpoint.
	ClientVpnEndpointId pulumi.StringOutput `pulumi:"clientVpnEndpointId"`
	// The IDs of the security groups applied to the target network association.
	SecurityGroups pulumi.StringArrayOutput `pulumi:"securityGroups"`
	// The current state of the target network association.
	Status pulumi.StringOutput `pulumi:"status"`
	// The ID of the subnet to associate with the Client VPN endpoint.
	SubnetId pulumi.StringOutput `pulumi:"subnetId"`
	// The ID of the VPC in which the target network (subnet) is located.
	VpcId pulumi.StringOutput `pulumi:"vpcId"`
}

// NewNetworkAssociation registers a new resource with the given unique name, arguments, and options.
func NewNetworkAssociation(ctx *pulumi.Context,
	name string, args *NetworkAssociationArgs, opts ...pulumi.ResourceOption) (*NetworkAssociation, error) {
	if args == nil || args.ClientVpnEndpointId == nil {
		return nil, errors.New("missing required argument 'ClientVpnEndpointId'")
	}
	if args == nil || args.SubnetId == nil {
		return nil, errors.New("missing required argument 'SubnetId'")
	}
	if args == nil {
		args = &NetworkAssociationArgs{}
	}
	var resource NetworkAssociation
	err := ctx.RegisterResource("aws:ec2clientvpn/networkAssociation:NetworkAssociation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNetworkAssociation gets an existing NetworkAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetworkAssociation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NetworkAssociationState, opts ...pulumi.ResourceOption) (*NetworkAssociation, error) {
	var resource NetworkAssociation
	err := ctx.ReadResource("aws:ec2clientvpn/networkAssociation:NetworkAssociation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NetworkAssociation resources.
type networkAssociationState struct {
	// The ID of the Client VPN endpoint.
	ClientVpnEndpointId *string `pulumi:"clientVpnEndpointId"`
	// The IDs of the security groups applied to the target network association.
	SecurityGroups []string `pulumi:"securityGroups"`
	// The current state of the target network association.
	Status *string `pulumi:"status"`
	// The ID of the subnet to associate with the Client VPN endpoint.
	SubnetId *string `pulumi:"subnetId"`
	// The ID of the VPC in which the target network (subnet) is located.
	VpcId *string `pulumi:"vpcId"`
}

type NetworkAssociationState struct {
	// The ID of the Client VPN endpoint.
	ClientVpnEndpointId pulumi.StringPtrInput
	// The IDs of the security groups applied to the target network association.
	SecurityGroups pulumi.StringArrayInput
	// The current state of the target network association.
	Status pulumi.StringPtrInput
	// The ID of the subnet to associate with the Client VPN endpoint.
	SubnetId pulumi.StringPtrInput
	// The ID of the VPC in which the target network (subnet) is located.
	VpcId pulumi.StringPtrInput
}

func (NetworkAssociationState) ElementType() reflect.Type {
	return reflect.TypeOf((*networkAssociationState)(nil)).Elem()
}

type networkAssociationArgs struct {
	// The ID of the Client VPN endpoint.
	ClientVpnEndpointId string `pulumi:"clientVpnEndpointId"`
	// The ID of the subnet to associate with the Client VPN endpoint.
	SubnetId string `pulumi:"subnetId"`
}

// The set of arguments for constructing a NetworkAssociation resource.
type NetworkAssociationArgs struct {
	// The ID of the Client VPN endpoint.
	ClientVpnEndpointId pulumi.StringInput
	// The ID of the subnet to associate with the Client VPN endpoint.
	SubnetId pulumi.StringInput
}

func (NetworkAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*networkAssociationArgs)(nil)).Elem()
}
