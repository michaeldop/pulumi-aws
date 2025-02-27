// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package elasticache

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an ElastiCache Subnet Group resource.
//
// > **NOTE:** ElastiCache Subnet Groups are only for use when working with an
// ElastiCache cluster **inside** of a VPC. If you are on EC2 Classic, see the
// ElastiCache Security Group resource.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/ec2"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/elasticache"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		fooVpc, err := ec2.NewVpc(ctx, "fooVpc", &ec2.VpcArgs{
// 			CidrBlock: pulumi.String("10.0.0.0/16"),
// 			Tags: pulumi.StringMap{
// 				"Name": pulumi.String("tf-test"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		fooSubnet, err := ec2.NewSubnet(ctx, "fooSubnet", &ec2.SubnetArgs{
// 			VpcId:            fooVpc.ID(),
// 			CidrBlock:        pulumi.String("10.0.0.0/24"),
// 			AvailabilityZone: pulumi.String("us-west-2a"),
// 			Tags: pulumi.StringMap{
// 				"Name": pulumi.String("tf-test"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = elasticache.NewSubnetGroup(ctx, "bar", &elasticache.SubnetGroupArgs{
// 			SubnetIds: pulumi.StringArray{
// 				fooSubnet.ID(),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type SubnetGroup struct {
	pulumi.CustomResourceState

	// Description for the cache subnet group. Defaults to "Managed by Pulumi".
	Description pulumi.StringOutput `pulumi:"description"`
	// Name for the cache subnet group. Elasticache converts this name to lowercase.
	Name pulumi.StringOutput `pulumi:"name"`
	// List of VPC Subnet IDs for the cache subnet group
	SubnetIds pulumi.StringArrayOutput `pulumi:"subnetIds"`
}

// NewSubnetGroup registers a new resource with the given unique name, arguments, and options.
func NewSubnetGroup(ctx *pulumi.Context,
	name string, args *SubnetGroupArgs, opts ...pulumi.ResourceOption) (*SubnetGroup, error) {
	if args == nil || args.SubnetIds == nil {
		return nil, errors.New("missing required argument 'SubnetIds'")
	}
	if args == nil {
		args = &SubnetGroupArgs{}
	}
	if args.Description == nil {
		args.Description = pulumi.StringPtr("Managed by Pulumi")
	}
	var resource SubnetGroup
	err := ctx.RegisterResource("aws:elasticache/subnetGroup:SubnetGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSubnetGroup gets an existing SubnetGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSubnetGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SubnetGroupState, opts ...pulumi.ResourceOption) (*SubnetGroup, error) {
	var resource SubnetGroup
	err := ctx.ReadResource("aws:elasticache/subnetGroup:SubnetGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SubnetGroup resources.
type subnetGroupState struct {
	// Description for the cache subnet group. Defaults to "Managed by Pulumi".
	Description *string `pulumi:"description"`
	// Name for the cache subnet group. Elasticache converts this name to lowercase.
	Name *string `pulumi:"name"`
	// List of VPC Subnet IDs for the cache subnet group
	SubnetIds []string `pulumi:"subnetIds"`
}

type SubnetGroupState struct {
	// Description for the cache subnet group. Defaults to "Managed by Pulumi".
	Description pulumi.StringPtrInput
	// Name for the cache subnet group. Elasticache converts this name to lowercase.
	Name pulumi.StringPtrInput
	// List of VPC Subnet IDs for the cache subnet group
	SubnetIds pulumi.StringArrayInput
}

func (SubnetGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*subnetGroupState)(nil)).Elem()
}

type subnetGroupArgs struct {
	// Description for the cache subnet group. Defaults to "Managed by Pulumi".
	Description *string `pulumi:"description"`
	// Name for the cache subnet group. Elasticache converts this name to lowercase.
	Name *string `pulumi:"name"`
	// List of VPC Subnet IDs for the cache subnet group
	SubnetIds []string `pulumi:"subnetIds"`
}

// The set of arguments for constructing a SubnetGroup resource.
type SubnetGroupArgs struct {
	// Description for the cache subnet group. Defaults to "Managed by Pulumi".
	Description pulumi.StringPtrInput
	// Name for the cache subnet group. Elasticache converts this name to lowercase.
	Name pulumi.StringPtrInput
	// List of VPC Subnet IDs for the cache subnet group
	SubnetIds pulumi.StringArrayInput
}

func (SubnetGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*subnetGroupArgs)(nil)).Elem()
}
