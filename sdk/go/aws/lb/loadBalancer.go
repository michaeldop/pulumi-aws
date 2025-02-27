// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package lb

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Load Balancer resource.
//
// > **Note:** `alb.LoadBalancer` is known as `lb.LoadBalancer`. The functionality is identical.
//
// ## Example Usage
// ### Specifying Elastic IPs
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/lb"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := lb.NewLoadBalancer(ctx, "example", &lb.LoadBalancerArgs{
// 			LoadBalancerType: pulumi.String("network"),
// 			SubnetMappings: lb.LoadBalancerSubnetMappingArray{
// 				&lb.LoadBalancerSubnetMappingArgs{
// 					SubnetId:     pulumi.Any(aws_subnet.Example1.Id),
// 					AllocationId: pulumi.Any(aws_eip.Example1.Id),
// 				},
// 				&lb.LoadBalancerSubnetMappingArgs{
// 					SubnetId:     pulumi.Any(aws_subnet.Example2.Id),
// 					AllocationId: pulumi.Any(aws_eip.Example2.Id),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Specifying private IP addresses for an internal-facing load balancer
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/lb"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := lb.NewLoadBalancer(ctx, "example", &lb.LoadBalancerArgs{
// 			LoadBalancerType: pulumi.String("network"),
// 			SubnetMappings: lb.LoadBalancerSubnetMappingArray{
// 				&lb.LoadBalancerSubnetMappingArgs{
// 					PrivateIpv4Address: pulumi.String("10.0.1.15"),
// 					SubnetId:           pulumi.Any(aws_subnet.Example1.Id),
// 				},
// 				&lb.LoadBalancerSubnetMappingArgs{
// 					PrivateIpv4Address: pulumi.String("10.0.2.15"),
// 					SubnetId:           pulumi.Any(aws_subnet.Example2.Id),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type LoadBalancer struct {
	pulumi.CustomResourceState

	// An Access Logs block. Access Logs documented below.
	AccessLogs LoadBalancerAccessLogsPtrOutput `pulumi:"accessLogs"`
	// The ARN of the load balancer (matches `id`).
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The ARN suffix for use with CloudWatch Metrics.
	ArnSuffix pulumi.StringOutput `pulumi:"arnSuffix"`
	// The DNS name of the load balancer.
	DnsName pulumi.StringOutput `pulumi:"dnsName"`
	// Indicates whether HTTP headers with header fields that are not valid are removed by the load balancer (true) or routed to targets (false). The default is false. Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens. Only valid for Load Balancers of type `application`.
	DropInvalidHeaderFields pulumi.BoolPtrOutput `pulumi:"dropInvalidHeaderFields"`
	// If true, cross-zone load balancing of the load balancer will be enabled.
	// This is a `network` load balancer feature. Defaults to `false`.
	EnableCrossZoneLoadBalancing pulumi.BoolPtrOutput `pulumi:"enableCrossZoneLoadBalancing"`
	// If true, deletion of the load balancer will be disabled via
	// the AWS API. This will prevent this provider from deleting the load balancer. Defaults to `false`.
	EnableDeletionProtection pulumi.BoolPtrOutput `pulumi:"enableDeletionProtection"`
	// Indicates whether HTTP/2 is enabled in `application` load balancers. Defaults to `true`.
	EnableHttp2 pulumi.BoolPtrOutput `pulumi:"enableHttp2"`
	// The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type `application`. Default: 60.
	IdleTimeout pulumi.IntPtrOutput `pulumi:"idleTimeout"`
	// If true, the LB will be internal.
	Internal pulumi.BoolOutput `pulumi:"internal"`
	// The type of IP addresses used by the subnets for your load balancer. The possible values are `ipv4` and `dualstack`
	IpAddressType pulumi.StringOutput `pulumi:"ipAddressType"`
	// The type of load balancer to create. Possible values are `application` or `network`. The default value is `application`.
	LoadBalancerType pulumi.StringPtrOutput `pulumi:"loadBalancerType"`
	// The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
	// must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
	// this provider will autogenerate a name beginning with `tf-lb`.
	Name pulumi.StringOutput `pulumi:"name"`
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrOutput `pulumi:"namePrefix"`
	// A list of security group IDs to assign to the LB. Only valid for Load Balancers of type `application`.
	SecurityGroups pulumi.StringArrayOutput `pulumi:"securityGroups"`
	// A subnet mapping block as documented below.
	SubnetMappings LoadBalancerSubnetMappingArrayOutput `pulumi:"subnetMappings"`
	// A list of subnet IDs to attach to the LB. Subnets
	// cannot be updated for Load Balancers of type `network`. Changing this value
	// for load balancers of type `network` will force a recreation of the resource.
	Subnets pulumi.StringArrayOutput `pulumi:"subnets"`
	// A map of tags to assign to the resource.
	Tags  pulumi.StringMapOutput `pulumi:"tags"`
	VpcId pulumi.StringOutput    `pulumi:"vpcId"`
	// The canonical hosted zone ID of the load balancer (to be used in a Route 53 Alias record).
	ZoneId pulumi.StringOutput `pulumi:"zoneId"`
}

// NewLoadBalancer registers a new resource with the given unique name, arguments, and options.
func NewLoadBalancer(ctx *pulumi.Context,
	name string, args *LoadBalancerArgs, opts ...pulumi.ResourceOption) (*LoadBalancer, error) {
	if args == nil {
		args = &LoadBalancerArgs{}
	}
	aliases := pulumi.Aliases([]pulumi.Alias{
		{
			Type: pulumi.String("aws:elasticloadbalancingv2/loadBalancer:LoadBalancer"),
		},
	})
	opts = append(opts, aliases)
	var resource LoadBalancer
	err := ctx.RegisterResource("aws:lb/loadBalancer:LoadBalancer", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLoadBalancer gets an existing LoadBalancer resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLoadBalancer(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LoadBalancerState, opts ...pulumi.ResourceOption) (*LoadBalancer, error) {
	var resource LoadBalancer
	err := ctx.ReadResource("aws:lb/loadBalancer:LoadBalancer", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LoadBalancer resources.
type loadBalancerState struct {
	// An Access Logs block. Access Logs documented below.
	AccessLogs *LoadBalancerAccessLogs `pulumi:"accessLogs"`
	// The ARN of the load balancer (matches `id`).
	Arn *string `pulumi:"arn"`
	// The ARN suffix for use with CloudWatch Metrics.
	ArnSuffix *string `pulumi:"arnSuffix"`
	// The DNS name of the load balancer.
	DnsName *string `pulumi:"dnsName"`
	// Indicates whether HTTP headers with header fields that are not valid are removed by the load balancer (true) or routed to targets (false). The default is false. Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens. Only valid for Load Balancers of type `application`.
	DropInvalidHeaderFields *bool `pulumi:"dropInvalidHeaderFields"`
	// If true, cross-zone load balancing of the load balancer will be enabled.
	// This is a `network` load balancer feature. Defaults to `false`.
	EnableCrossZoneLoadBalancing *bool `pulumi:"enableCrossZoneLoadBalancing"`
	// If true, deletion of the load balancer will be disabled via
	// the AWS API. This will prevent this provider from deleting the load balancer. Defaults to `false`.
	EnableDeletionProtection *bool `pulumi:"enableDeletionProtection"`
	// Indicates whether HTTP/2 is enabled in `application` load balancers. Defaults to `true`.
	EnableHttp2 *bool `pulumi:"enableHttp2"`
	// The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type `application`. Default: 60.
	IdleTimeout *int `pulumi:"idleTimeout"`
	// If true, the LB will be internal.
	Internal *bool `pulumi:"internal"`
	// The type of IP addresses used by the subnets for your load balancer. The possible values are `ipv4` and `dualstack`
	IpAddressType *string `pulumi:"ipAddressType"`
	// The type of load balancer to create. Possible values are `application` or `network`. The default value is `application`.
	LoadBalancerType *string `pulumi:"loadBalancerType"`
	// The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
	// must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
	// this provider will autogenerate a name beginning with `tf-lb`.
	Name *string `pulumi:"name"`
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix *string `pulumi:"namePrefix"`
	// A list of security group IDs to assign to the LB. Only valid for Load Balancers of type `application`.
	SecurityGroups []string `pulumi:"securityGroups"`
	// A subnet mapping block as documented below.
	SubnetMappings []LoadBalancerSubnetMapping `pulumi:"subnetMappings"`
	// A list of subnet IDs to attach to the LB. Subnets
	// cannot be updated for Load Balancers of type `network`. Changing this value
	// for load balancers of type `network` will force a recreation of the resource.
	Subnets []string `pulumi:"subnets"`
	// A map of tags to assign to the resource.
	Tags  map[string]string `pulumi:"tags"`
	VpcId *string           `pulumi:"vpcId"`
	// The canonical hosted zone ID of the load balancer (to be used in a Route 53 Alias record).
	ZoneId *string `pulumi:"zoneId"`
}

type LoadBalancerState struct {
	// An Access Logs block. Access Logs documented below.
	AccessLogs LoadBalancerAccessLogsPtrInput
	// The ARN of the load balancer (matches `id`).
	Arn pulumi.StringPtrInput
	// The ARN suffix for use with CloudWatch Metrics.
	ArnSuffix pulumi.StringPtrInput
	// The DNS name of the load balancer.
	DnsName pulumi.StringPtrInput
	// Indicates whether HTTP headers with header fields that are not valid are removed by the load balancer (true) or routed to targets (false). The default is false. Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens. Only valid for Load Balancers of type `application`.
	DropInvalidHeaderFields pulumi.BoolPtrInput
	// If true, cross-zone load balancing of the load balancer will be enabled.
	// This is a `network` load balancer feature. Defaults to `false`.
	EnableCrossZoneLoadBalancing pulumi.BoolPtrInput
	// If true, deletion of the load balancer will be disabled via
	// the AWS API. This will prevent this provider from deleting the load balancer. Defaults to `false`.
	EnableDeletionProtection pulumi.BoolPtrInput
	// Indicates whether HTTP/2 is enabled in `application` load balancers. Defaults to `true`.
	EnableHttp2 pulumi.BoolPtrInput
	// The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type `application`. Default: 60.
	IdleTimeout pulumi.IntPtrInput
	// If true, the LB will be internal.
	Internal pulumi.BoolPtrInput
	// The type of IP addresses used by the subnets for your load balancer. The possible values are `ipv4` and `dualstack`
	IpAddressType pulumi.StringPtrInput
	// The type of load balancer to create. Possible values are `application` or `network`. The default value is `application`.
	LoadBalancerType pulumi.StringPtrInput
	// The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
	// must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
	// this provider will autogenerate a name beginning with `tf-lb`.
	Name pulumi.StringPtrInput
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrInput
	// A list of security group IDs to assign to the LB. Only valid for Load Balancers of type `application`.
	SecurityGroups pulumi.StringArrayInput
	// A subnet mapping block as documented below.
	SubnetMappings LoadBalancerSubnetMappingArrayInput
	// A list of subnet IDs to attach to the LB. Subnets
	// cannot be updated for Load Balancers of type `network`. Changing this value
	// for load balancers of type `network` will force a recreation of the resource.
	Subnets pulumi.StringArrayInput
	// A map of tags to assign to the resource.
	Tags  pulumi.StringMapInput
	VpcId pulumi.StringPtrInput
	// The canonical hosted zone ID of the load balancer (to be used in a Route 53 Alias record).
	ZoneId pulumi.StringPtrInput
}

func (LoadBalancerState) ElementType() reflect.Type {
	return reflect.TypeOf((*loadBalancerState)(nil)).Elem()
}

type loadBalancerArgs struct {
	// An Access Logs block. Access Logs documented below.
	AccessLogs *LoadBalancerAccessLogs `pulumi:"accessLogs"`
	// Indicates whether HTTP headers with header fields that are not valid are removed by the load balancer (true) or routed to targets (false). The default is false. Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens. Only valid for Load Balancers of type `application`.
	DropInvalidHeaderFields *bool `pulumi:"dropInvalidHeaderFields"`
	// If true, cross-zone load balancing of the load balancer will be enabled.
	// This is a `network` load balancer feature. Defaults to `false`.
	EnableCrossZoneLoadBalancing *bool `pulumi:"enableCrossZoneLoadBalancing"`
	// If true, deletion of the load balancer will be disabled via
	// the AWS API. This will prevent this provider from deleting the load balancer. Defaults to `false`.
	EnableDeletionProtection *bool `pulumi:"enableDeletionProtection"`
	// Indicates whether HTTP/2 is enabled in `application` load balancers. Defaults to `true`.
	EnableHttp2 *bool `pulumi:"enableHttp2"`
	// The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type `application`. Default: 60.
	IdleTimeout *int `pulumi:"idleTimeout"`
	// If true, the LB will be internal.
	Internal *bool `pulumi:"internal"`
	// The type of IP addresses used by the subnets for your load balancer. The possible values are `ipv4` and `dualstack`
	IpAddressType *string `pulumi:"ipAddressType"`
	// The type of load balancer to create. Possible values are `application` or `network`. The default value is `application`.
	LoadBalancerType *string `pulumi:"loadBalancerType"`
	// The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
	// must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
	// this provider will autogenerate a name beginning with `tf-lb`.
	Name *string `pulumi:"name"`
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix *string `pulumi:"namePrefix"`
	// A list of security group IDs to assign to the LB. Only valid for Load Balancers of type `application`.
	SecurityGroups []string `pulumi:"securityGroups"`
	// A subnet mapping block as documented below.
	SubnetMappings []LoadBalancerSubnetMapping `pulumi:"subnetMappings"`
	// A list of subnet IDs to attach to the LB. Subnets
	// cannot be updated for Load Balancers of type `network`. Changing this value
	// for load balancers of type `network` will force a recreation of the resource.
	Subnets []string `pulumi:"subnets"`
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a LoadBalancer resource.
type LoadBalancerArgs struct {
	// An Access Logs block. Access Logs documented below.
	AccessLogs LoadBalancerAccessLogsPtrInput
	// Indicates whether HTTP headers with header fields that are not valid are removed by the load balancer (true) or routed to targets (false). The default is false. Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens. Only valid for Load Balancers of type `application`.
	DropInvalidHeaderFields pulumi.BoolPtrInput
	// If true, cross-zone load balancing of the load balancer will be enabled.
	// This is a `network` load balancer feature. Defaults to `false`.
	EnableCrossZoneLoadBalancing pulumi.BoolPtrInput
	// If true, deletion of the load balancer will be disabled via
	// the AWS API. This will prevent this provider from deleting the load balancer. Defaults to `false`.
	EnableDeletionProtection pulumi.BoolPtrInput
	// Indicates whether HTTP/2 is enabled in `application` load balancers. Defaults to `true`.
	EnableHttp2 pulumi.BoolPtrInput
	// The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type `application`. Default: 60.
	IdleTimeout pulumi.IntPtrInput
	// If true, the LB will be internal.
	Internal pulumi.BoolPtrInput
	// The type of IP addresses used by the subnets for your load balancer. The possible values are `ipv4` and `dualstack`
	IpAddressType pulumi.StringPtrInput
	// The type of load balancer to create. Possible values are `application` or `network`. The default value is `application`.
	LoadBalancerType pulumi.StringPtrInput
	// The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
	// must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
	// this provider will autogenerate a name beginning with `tf-lb`.
	Name pulumi.StringPtrInput
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrInput
	// A list of security group IDs to assign to the LB. Only valid for Load Balancers of type `application`.
	SecurityGroups pulumi.StringArrayInput
	// A subnet mapping block as documented below.
	SubnetMappings LoadBalancerSubnetMappingArrayInput
	// A list of subnet IDs to attach to the LB. Subnets
	// cannot be updated for Load Balancers of type `network`. Changing this value
	// for load balancers of type `network` will force a recreation of the resource.
	Subnets pulumi.StringArrayInput
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
}

func (LoadBalancerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*loadBalancerArgs)(nil)).Elem()
}
