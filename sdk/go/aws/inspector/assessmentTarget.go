// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package inspector

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Inspector assessment target
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/inspector"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		bar, err := inspector.NewResourceGroup(ctx, "bar", &inspector.ResourceGroupArgs{
// 			Tags: pulumi.StringMap{
// 				"Name": pulumi.String("foo"),
// 				"Env":  pulumi.String("bar"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = inspector.NewAssessmentTarget(ctx, "foo", &inspector.AssessmentTargetArgs{
// 			ResourceGroupArn: bar.Arn,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type AssessmentTarget struct {
	pulumi.CustomResourceState

	// The target assessment ARN.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The name of the assessment target.
	Name pulumi.StringOutput `pulumi:"name"`
	// Inspector Resource Group Amazon Resource Name (ARN) stating tags for instance matching. If not specified, all EC2 instances in the current AWS account and region are included in the assessment target.
	ResourceGroupArn pulumi.StringPtrOutput `pulumi:"resourceGroupArn"`
}

// NewAssessmentTarget registers a new resource with the given unique name, arguments, and options.
func NewAssessmentTarget(ctx *pulumi.Context,
	name string, args *AssessmentTargetArgs, opts ...pulumi.ResourceOption) (*AssessmentTarget, error) {
	if args == nil {
		args = &AssessmentTargetArgs{}
	}
	var resource AssessmentTarget
	err := ctx.RegisterResource("aws:inspector/assessmentTarget:AssessmentTarget", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAssessmentTarget gets an existing AssessmentTarget resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAssessmentTarget(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AssessmentTargetState, opts ...pulumi.ResourceOption) (*AssessmentTarget, error) {
	var resource AssessmentTarget
	err := ctx.ReadResource("aws:inspector/assessmentTarget:AssessmentTarget", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AssessmentTarget resources.
type assessmentTargetState struct {
	// The target assessment ARN.
	Arn *string `pulumi:"arn"`
	// The name of the assessment target.
	Name *string `pulumi:"name"`
	// Inspector Resource Group Amazon Resource Name (ARN) stating tags for instance matching. If not specified, all EC2 instances in the current AWS account and region are included in the assessment target.
	ResourceGroupArn *string `pulumi:"resourceGroupArn"`
}

type AssessmentTargetState struct {
	// The target assessment ARN.
	Arn pulumi.StringPtrInput
	// The name of the assessment target.
	Name pulumi.StringPtrInput
	// Inspector Resource Group Amazon Resource Name (ARN) stating tags for instance matching. If not specified, all EC2 instances in the current AWS account and region are included in the assessment target.
	ResourceGroupArn pulumi.StringPtrInput
}

func (AssessmentTargetState) ElementType() reflect.Type {
	return reflect.TypeOf((*assessmentTargetState)(nil)).Elem()
}

type assessmentTargetArgs struct {
	// The name of the assessment target.
	Name *string `pulumi:"name"`
	// Inspector Resource Group Amazon Resource Name (ARN) stating tags for instance matching. If not specified, all EC2 instances in the current AWS account and region are included in the assessment target.
	ResourceGroupArn *string `pulumi:"resourceGroupArn"`
}

// The set of arguments for constructing a AssessmentTarget resource.
type AssessmentTargetArgs struct {
	// The name of the assessment target.
	Name pulumi.StringPtrInput
	// Inspector Resource Group Amazon Resource Name (ARN) stating tags for instance matching. If not specified, all EC2 instances in the current AWS account and region are included in the assessment target.
	ResourceGroupArn pulumi.StringPtrInput
}

func (AssessmentTargetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*assessmentTargetArgs)(nil)).Elem()
}
