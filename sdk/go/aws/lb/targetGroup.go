// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package lb

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Target Group resource for use with Load Balancer resources.
//
// > **Note:** `alb.TargetGroup` is known as `lb.TargetGroup`. The functionality is identical.
//
// ## Example Usage
// ### Instance Target Group
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/ec2"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/lb"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		main, err := ec2.NewVpc(ctx, "main", &ec2.VpcArgs{
// 			CidrBlock: pulumi.String("10.0.0.0/16"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = lb.NewTargetGroup(ctx, "test", &lb.TargetGroupArgs{
// 			Port:     pulumi.Int(80),
// 			Protocol: pulumi.String("HTTP"),
// 			VpcId:    main.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### IP Target Group
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/ec2"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/lb"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		main, err := ec2.NewVpc(ctx, "main", &ec2.VpcArgs{
// 			CidrBlock: pulumi.String("10.0.0.0/16"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = lb.NewTargetGroup(ctx, "ip_example", &lb.TargetGroupArgs{
// 			Port:       pulumi.Int(80),
// 			Protocol:   pulumi.String("HTTP"),
// 			TargetType: pulumi.String("ip"),
// 			VpcId:      main.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Lambda Target Group
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
// 		_, err := lb.NewTargetGroup(ctx, "lambda_example", &lb.TargetGroupArgs{
// 			TargetType: pulumi.String("lambda"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type TargetGroup struct {
	pulumi.CustomResourceState

	// The ARN of the Target Group (matches `id`)
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The ARN suffix for use with CloudWatch Metrics.
	ArnSuffix pulumi.StringOutput `pulumi:"arnSuffix"`
	// The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
	DeregistrationDelay pulumi.IntPtrOutput `pulumi:"deregistrationDelay"`
	// A Health Check block. Health Check blocks are documented below.
	HealthCheck TargetGroupHealthCheckOutput `pulumi:"healthCheck"`
	// Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `targetType` is `lambda`.
	LambdaMultiValueHeadersEnabled pulumi.BoolPtrOutput `pulumi:"lambdaMultiValueHeadersEnabled"`
	// Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `roundRobin` or `leastOutstandingRequests`. The default is `roundRobin`.
	LoadBalancingAlgorithmType pulumi.StringOutput `pulumi:"loadBalancingAlgorithmType"`
	// The name of the target group. If omitted, this provider will assign a random, unique name.
	Name pulumi.StringOutput `pulumi:"name"`
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
	NamePrefix pulumi.StringPtrOutput `pulumi:"namePrefix"`
	// The port on which targets receive traffic, unless overridden when registering a specific target. Required when `targetType` is `instance` or `ip`. Does not apply when `targetType` is `lambda`.
	Port pulumi.IntPtrOutput `pulumi:"port"`
	// The protocol to use for routing traffic to the targets. Should be one of "TCP", "TLS", "UDP", "TCP_UDP", "HTTP" or "HTTPS". Required when `targetType` is `instance` or `ip`. Does not apply when `targetType` is `lambda`.
	Protocol pulumi.StringPtrOutput `pulumi:"protocol"`
	// Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
	ProxyProtocolV2 pulumi.BoolPtrOutput `pulumi:"proxyProtocolV2"`
	// The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
	SlowStart pulumi.IntPtrOutput `pulumi:"slowStart"`
	// A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
	Stickiness TargetGroupStickinessOutput `pulumi:"stickiness"`
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// The type of target that you must specify when registering targets with this target group.
	// The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
	// The default is `instance`. Note that you can't specify targets for a target group using both instance IDs and IP addresses.
	// If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
	// the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
	// You can't specify publicly routable IP addresses.
	TargetType pulumi.StringPtrOutput `pulumi:"targetType"`
	// The identifier of the VPC in which to create the target group. Required when `targetType` is `instance` or `ip`. Does not apply when `targetType` is `lambda`.
	VpcId pulumi.StringPtrOutput `pulumi:"vpcId"`
}

// NewTargetGroup registers a new resource with the given unique name, arguments, and options.
func NewTargetGroup(ctx *pulumi.Context,
	name string, args *TargetGroupArgs, opts ...pulumi.ResourceOption) (*TargetGroup, error) {
	if args == nil {
		args = &TargetGroupArgs{}
	}
	aliases := pulumi.Aliases([]pulumi.Alias{
		{
			Type: pulumi.String("aws:elasticloadbalancingv2/targetGroup:TargetGroup"),
		},
	})
	opts = append(opts, aliases)
	var resource TargetGroup
	err := ctx.RegisterResource("aws:lb/targetGroup:TargetGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTargetGroup gets an existing TargetGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTargetGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TargetGroupState, opts ...pulumi.ResourceOption) (*TargetGroup, error) {
	var resource TargetGroup
	err := ctx.ReadResource("aws:lb/targetGroup:TargetGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TargetGroup resources.
type targetGroupState struct {
	// The ARN of the Target Group (matches `id`)
	Arn *string `pulumi:"arn"`
	// The ARN suffix for use with CloudWatch Metrics.
	ArnSuffix *string `pulumi:"arnSuffix"`
	// The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
	DeregistrationDelay *int `pulumi:"deregistrationDelay"`
	// A Health Check block. Health Check blocks are documented below.
	HealthCheck *TargetGroupHealthCheck `pulumi:"healthCheck"`
	// Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `targetType` is `lambda`.
	LambdaMultiValueHeadersEnabled *bool `pulumi:"lambdaMultiValueHeadersEnabled"`
	// Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `roundRobin` or `leastOutstandingRequests`. The default is `roundRobin`.
	LoadBalancingAlgorithmType *string `pulumi:"loadBalancingAlgorithmType"`
	// The name of the target group. If omitted, this provider will assign a random, unique name.
	Name *string `pulumi:"name"`
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
	NamePrefix *string `pulumi:"namePrefix"`
	// The port on which targets receive traffic, unless overridden when registering a specific target. Required when `targetType` is `instance` or `ip`. Does not apply when `targetType` is `lambda`.
	Port *int `pulumi:"port"`
	// The protocol to use for routing traffic to the targets. Should be one of "TCP", "TLS", "UDP", "TCP_UDP", "HTTP" or "HTTPS". Required when `targetType` is `instance` or `ip`. Does not apply when `targetType` is `lambda`.
	Protocol *string `pulumi:"protocol"`
	// Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
	ProxyProtocolV2 *bool `pulumi:"proxyProtocolV2"`
	// The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
	SlowStart *int `pulumi:"slowStart"`
	// A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
	Stickiness *TargetGroupStickiness `pulumi:"stickiness"`
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// The type of target that you must specify when registering targets with this target group.
	// The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
	// The default is `instance`. Note that you can't specify targets for a target group using both instance IDs and IP addresses.
	// If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
	// the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
	// You can't specify publicly routable IP addresses.
	TargetType *string `pulumi:"targetType"`
	// The identifier of the VPC in which to create the target group. Required when `targetType` is `instance` or `ip`. Does not apply when `targetType` is `lambda`.
	VpcId *string `pulumi:"vpcId"`
}

type TargetGroupState struct {
	// The ARN of the Target Group (matches `id`)
	Arn pulumi.StringPtrInput
	// The ARN suffix for use with CloudWatch Metrics.
	ArnSuffix pulumi.StringPtrInput
	// The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
	DeregistrationDelay pulumi.IntPtrInput
	// A Health Check block. Health Check blocks are documented below.
	HealthCheck TargetGroupHealthCheckPtrInput
	// Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `targetType` is `lambda`.
	LambdaMultiValueHeadersEnabled pulumi.BoolPtrInput
	// Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `roundRobin` or `leastOutstandingRequests`. The default is `roundRobin`.
	LoadBalancingAlgorithmType pulumi.StringPtrInput
	// The name of the target group. If omitted, this provider will assign a random, unique name.
	Name pulumi.StringPtrInput
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
	NamePrefix pulumi.StringPtrInput
	// The port on which targets receive traffic, unless overridden when registering a specific target. Required when `targetType` is `instance` or `ip`. Does not apply when `targetType` is `lambda`.
	Port pulumi.IntPtrInput
	// The protocol to use for routing traffic to the targets. Should be one of "TCP", "TLS", "UDP", "TCP_UDP", "HTTP" or "HTTPS". Required when `targetType` is `instance` or `ip`. Does not apply when `targetType` is `lambda`.
	Protocol pulumi.StringPtrInput
	// Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
	ProxyProtocolV2 pulumi.BoolPtrInput
	// The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
	SlowStart pulumi.IntPtrInput
	// A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
	Stickiness TargetGroupStickinessPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// The type of target that you must specify when registering targets with this target group.
	// The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
	// The default is `instance`. Note that you can't specify targets for a target group using both instance IDs and IP addresses.
	// If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
	// the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
	// You can't specify publicly routable IP addresses.
	TargetType pulumi.StringPtrInput
	// The identifier of the VPC in which to create the target group. Required when `targetType` is `instance` or `ip`. Does not apply when `targetType` is `lambda`.
	VpcId pulumi.StringPtrInput
}

func (TargetGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*targetGroupState)(nil)).Elem()
}

type targetGroupArgs struct {
	// The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
	DeregistrationDelay *int `pulumi:"deregistrationDelay"`
	// A Health Check block. Health Check blocks are documented below.
	HealthCheck *TargetGroupHealthCheck `pulumi:"healthCheck"`
	// Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `targetType` is `lambda`.
	LambdaMultiValueHeadersEnabled *bool `pulumi:"lambdaMultiValueHeadersEnabled"`
	// Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `roundRobin` or `leastOutstandingRequests`. The default is `roundRobin`.
	LoadBalancingAlgorithmType *string `pulumi:"loadBalancingAlgorithmType"`
	// The name of the target group. If omitted, this provider will assign a random, unique name.
	Name *string `pulumi:"name"`
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
	NamePrefix *string `pulumi:"namePrefix"`
	// The port on which targets receive traffic, unless overridden when registering a specific target. Required when `targetType` is `instance` or `ip`. Does not apply when `targetType` is `lambda`.
	Port *int `pulumi:"port"`
	// The protocol to use for routing traffic to the targets. Should be one of "TCP", "TLS", "UDP", "TCP_UDP", "HTTP" or "HTTPS". Required when `targetType` is `instance` or `ip`. Does not apply when `targetType` is `lambda`.
	Protocol *string `pulumi:"protocol"`
	// Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
	ProxyProtocolV2 *bool `pulumi:"proxyProtocolV2"`
	// The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
	SlowStart *int `pulumi:"slowStart"`
	// A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
	Stickiness *TargetGroupStickiness `pulumi:"stickiness"`
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// The type of target that you must specify when registering targets with this target group.
	// The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
	// The default is `instance`. Note that you can't specify targets for a target group using both instance IDs and IP addresses.
	// If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
	// the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
	// You can't specify publicly routable IP addresses.
	TargetType *string `pulumi:"targetType"`
	// The identifier of the VPC in which to create the target group. Required when `targetType` is `instance` or `ip`. Does not apply when `targetType` is `lambda`.
	VpcId *string `pulumi:"vpcId"`
}

// The set of arguments for constructing a TargetGroup resource.
type TargetGroupArgs struct {
	// The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
	DeregistrationDelay pulumi.IntPtrInput
	// A Health Check block. Health Check blocks are documented below.
	HealthCheck TargetGroupHealthCheckPtrInput
	// Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `targetType` is `lambda`.
	LambdaMultiValueHeadersEnabled pulumi.BoolPtrInput
	// Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `roundRobin` or `leastOutstandingRequests`. The default is `roundRobin`.
	LoadBalancingAlgorithmType pulumi.StringPtrInput
	// The name of the target group. If omitted, this provider will assign a random, unique name.
	Name pulumi.StringPtrInput
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
	NamePrefix pulumi.StringPtrInput
	// The port on which targets receive traffic, unless overridden when registering a specific target. Required when `targetType` is `instance` or `ip`. Does not apply when `targetType` is `lambda`.
	Port pulumi.IntPtrInput
	// The protocol to use for routing traffic to the targets. Should be one of "TCP", "TLS", "UDP", "TCP_UDP", "HTTP" or "HTTPS". Required when `targetType` is `instance` or `ip`. Does not apply when `targetType` is `lambda`.
	Protocol pulumi.StringPtrInput
	// Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
	ProxyProtocolV2 pulumi.BoolPtrInput
	// The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
	SlowStart pulumi.IntPtrInput
	// A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
	Stickiness TargetGroupStickinessPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// The type of target that you must specify when registering targets with this target group.
	// The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
	// The default is `instance`. Note that you can't specify targets for a target group using both instance IDs and IP addresses.
	// If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
	// the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
	// You can't specify publicly routable IP addresses.
	TargetType pulumi.StringPtrInput
	// The identifier of the VPC in which to create the target group. Required when `targetType` is `instance` or `ip`. Does not apply when `targetType` is `lambda`.
	VpcId pulumi.StringPtrInput
}

func (TargetGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*targetGroupArgs)(nil)).Elem()
}
