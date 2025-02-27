// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package wafregional

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages an association with WAF Regional Web ACL.
//
// > **Note:** An Application Load Balancer can only be associated with one WAF Regional WebACL.
//
// ## Application Load Balancer Association Example
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/alb"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/ec2"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/wafregional"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		ipset, err := wafregional.NewIpSet(ctx, "ipset", &wafregional.IpSetArgs{
// 			IpSetDescriptors: wafregional.IpSetIpSetDescriptorArray{
// 				&wafregional.IpSetIpSetDescriptorArgs{
// 					Type:  pulumi.String("IPV4"),
// 					Value: pulumi.String("192.0.7.0/24"),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		fooRule, err := wafregional.NewRule(ctx, "fooRule", &wafregional.RuleArgs{
// 			MetricName: pulumi.String("tfWAFRule"),
// 			Predicates: wafregional.RulePredicateArray{
// 				&wafregional.RulePredicateArgs{
// 					DataId:  ipset.ID(),
// 					Negated: pulumi.Bool(false),
// 					Type:    pulumi.String("IPMatch"),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		fooWebAcl, err := wafregional.NewWebAcl(ctx, "fooWebAcl", &wafregional.WebAclArgs{
// 			MetricName: pulumi.String("foo"),
// 			DefaultAction: &wafregional.WebAclDefaultActionArgs{
// 				Type: pulumi.String("ALLOW"),
// 			},
// 			Rules: wafregional.WebAclRuleArray{
// 				&wafregional.WebAclRuleArgs{
// 					Action: &wafregional.WebAclRuleActionArgs{
// 						Type: pulumi.String("BLOCK"),
// 					},
// 					Priority: pulumi.Int(1),
// 					RuleId:   fooRule.ID(),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		fooVpc, err := ec2.NewVpc(ctx, "fooVpc", &ec2.VpcArgs{
// 			CidrBlock: pulumi.String("10.1.0.0/16"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		available, err := aws.GetAvailabilityZones(ctx, nil, nil)
// 		if err != nil {
// 			return err
// 		}
// 		fooSubnet, err := ec2.NewSubnet(ctx, "fooSubnet", &ec2.SubnetArgs{
// 			VpcId:            fooVpc.ID(),
// 			CidrBlock:        pulumi.String("10.1.1.0/24"),
// 			AvailabilityZone: pulumi.String(available.Names[0]),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		bar, err := ec2.NewSubnet(ctx, "bar", &ec2.SubnetArgs{
// 			VpcId:            fooVpc.ID(),
// 			CidrBlock:        pulumi.String("10.1.2.0/24"),
// 			AvailabilityZone: pulumi.String(available.Names[1]),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		fooLoadBalancer, err := alb.NewLoadBalancer(ctx, "fooLoadBalancer", &alb.LoadBalancerArgs{
// 			Internal: pulumi.Bool(true),
// 			Subnets: pulumi.StringArray{
// 				fooSubnet.ID(),
// 				bar.ID(),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = wafregional.NewWebAclAssociation(ctx, "fooWebAclAssociation", &wafregional.WebAclAssociationArgs{
// 			ResourceArn: fooLoadBalancer.Arn,
// 			WebAclId:    fooWebAcl.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## API Gateway Association Example
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/apigateway"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/wafregional"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		ipset, err := wafregional.NewIpSet(ctx, "ipset", &wafregional.IpSetArgs{
// 			IpSetDescriptors: wafregional.IpSetIpSetDescriptorArray{
// 				&wafregional.IpSetIpSetDescriptorArgs{
// 					Type:  pulumi.String("IPV4"),
// 					Value: pulumi.String("192.0.7.0/24"),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		fooRule, err := wafregional.NewRule(ctx, "fooRule", &wafregional.RuleArgs{
// 			MetricName: pulumi.String("tfWAFRule"),
// 			Predicates: wafregional.RulePredicateArray{
// 				&wafregional.RulePredicateArgs{
// 					DataId:  ipset.ID(),
// 					Negated: pulumi.Bool(false),
// 					Type:    pulumi.String("IPMatch"),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		fooWebAcl, err := wafregional.NewWebAcl(ctx, "fooWebAcl", &wafregional.WebAclArgs{
// 			MetricName: pulumi.String("foo"),
// 			DefaultAction: &wafregional.WebAclDefaultActionArgs{
// 				Type: pulumi.String("ALLOW"),
// 			},
// 			Rules: wafregional.WebAclRuleArray{
// 				&wafregional.WebAclRuleArgs{
// 					Action: &wafregional.WebAclRuleActionArgs{
// 						Type: pulumi.String("BLOCK"),
// 					},
// 					Priority: pulumi.Int(1),
// 					RuleId:   fooRule.ID(),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		testRestApi, err := apigateway.NewRestApi(ctx, "testRestApi", nil)
// 		if err != nil {
// 			return err
// 		}
// 		testResource, err := apigateway.NewResource(ctx, "testResource", &apigateway.ResourceArgs{
// 			ParentId: testRestApi.RootResourceId,
// 			PathPart: pulumi.String("test"),
// 			RestApi:  testRestApi.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		testMethod, err := apigateway.NewMethod(ctx, "testMethod", &apigateway.MethodArgs{
// 			Authorization: pulumi.String("NONE"),
// 			HttpMethod:    pulumi.String("GET"),
// 			ResourceId:    testResource.ID(),
// 			RestApi:       testRestApi.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		testMethodResponse, err := apigateway.NewMethodResponse(ctx, "testMethodResponse", &apigateway.MethodResponseArgs{
// 			HttpMethod: testMethod.HttpMethod,
// 			ResourceId: testResource.ID(),
// 			RestApi:    testRestApi.ID(),
// 			StatusCode: pulumi.String("400"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		testIntegration, err := apigateway.NewIntegration(ctx, "testIntegration", &apigateway.IntegrationArgs{
// 			HttpMethod:            testMethod.HttpMethod,
// 			IntegrationHttpMethod: pulumi.String("GET"),
// 			ResourceId:            testResource.ID(),
// 			RestApi:               testRestApi.ID(),
// 			Type:                  pulumi.String("HTTP"),
// 			Uri:                   pulumi.String("http://www.example.com"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		testIntegrationResponse, err := apigateway.NewIntegrationResponse(ctx, "testIntegrationResponse", &apigateway.IntegrationResponseArgs{
// 			RestApi:    testRestApi.ID(),
// 			ResourceId: testResource.ID(),
// 			HttpMethod: testIntegration.HttpMethod,
// 			StatusCode: testMethodResponse.StatusCode,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		testDeployment, err := apigateway.NewDeployment(ctx, "testDeployment", &apigateway.DeploymentArgs{
// 			RestApi: testRestApi.ID(),
// 		}, pulumi.DependsOn([]pulumi.Resource{
// 			testIntegrationResponse,
// 		}))
// 		if err != nil {
// 			return err
// 		}
// 		testStage, err := apigateway.NewStage(ctx, "testStage", &apigateway.StageArgs{
// 			Deployment: testDeployment.ID(),
// 			RestApi:    testRestApi.ID(),
// 			StageName:  pulumi.String("test"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = wafregional.NewWebAclAssociation(ctx, "association", &wafregional.WebAclAssociationArgs{
// 			ResourceArn: testStage.Arn,
// 			WebAclId:    fooWebAcl.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type WebAclAssociation struct {
	pulumi.CustomResourceState

	// ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
	ResourceArn pulumi.StringOutput `pulumi:"resourceArn"`
	// The ID of the WAF Regional WebACL to create an association.
	WebAclId pulumi.StringOutput `pulumi:"webAclId"`
}

// NewWebAclAssociation registers a new resource with the given unique name, arguments, and options.
func NewWebAclAssociation(ctx *pulumi.Context,
	name string, args *WebAclAssociationArgs, opts ...pulumi.ResourceOption) (*WebAclAssociation, error) {
	if args == nil || args.ResourceArn == nil {
		return nil, errors.New("missing required argument 'ResourceArn'")
	}
	if args == nil || args.WebAclId == nil {
		return nil, errors.New("missing required argument 'WebAclId'")
	}
	if args == nil {
		args = &WebAclAssociationArgs{}
	}
	var resource WebAclAssociation
	err := ctx.RegisterResource("aws:wafregional/webAclAssociation:WebAclAssociation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetWebAclAssociation gets an existing WebAclAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWebAclAssociation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *WebAclAssociationState, opts ...pulumi.ResourceOption) (*WebAclAssociation, error) {
	var resource WebAclAssociation
	err := ctx.ReadResource("aws:wafregional/webAclAssociation:WebAclAssociation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering WebAclAssociation resources.
type webAclAssociationState struct {
	// ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
	ResourceArn *string `pulumi:"resourceArn"`
	// The ID of the WAF Regional WebACL to create an association.
	WebAclId *string `pulumi:"webAclId"`
}

type WebAclAssociationState struct {
	// ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
	ResourceArn pulumi.StringPtrInput
	// The ID of the WAF Regional WebACL to create an association.
	WebAclId pulumi.StringPtrInput
}

func (WebAclAssociationState) ElementType() reflect.Type {
	return reflect.TypeOf((*webAclAssociationState)(nil)).Elem()
}

type webAclAssociationArgs struct {
	// ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
	ResourceArn string `pulumi:"resourceArn"`
	// The ID of the WAF Regional WebACL to create an association.
	WebAclId string `pulumi:"webAclId"`
}

// The set of arguments for constructing a WebAclAssociation resource.
type WebAclAssociationArgs struct {
	// ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
	ResourceArn pulumi.StringInput
	// The ID of the WAF Regional WebACL to create an association.
	WebAclId pulumi.StringInput
}

func (WebAclAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*webAclAssociationArgs)(nil)).Elem()
}
