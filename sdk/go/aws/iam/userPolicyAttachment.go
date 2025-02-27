// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Attaches a Managed IAM Policy to an IAM user
//
// > **NOTE:** The usage of this resource conflicts with the `iam.PolicyAttachment` resource and will permanently show a difference if both are defined.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/iam"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		user, err := iam.NewUser(ctx, "user", nil)
// 		if err != nil {
// 			return err
// 		}
// 		policy, err := iam.NewPolicy(ctx, "policy", &iam.PolicyArgs{
// 			Description: pulumi.String("A test policy"),
// 			Policy:      pulumi.String(""),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = iam.NewUserPolicyAttachment(ctx, "test_attach", &iam.UserPolicyAttachmentArgs{
// 			PolicyArn: policy.Arn,
// 			User:      user.Name,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type UserPolicyAttachment struct {
	pulumi.CustomResourceState

	// The ARN of the policy you want to apply
	PolicyArn pulumi.StringOutput `pulumi:"policyArn"`
	// The user the policy should be applied to
	User pulumi.StringOutput `pulumi:"user"`
}

// NewUserPolicyAttachment registers a new resource with the given unique name, arguments, and options.
func NewUserPolicyAttachment(ctx *pulumi.Context,
	name string, args *UserPolicyAttachmentArgs, opts ...pulumi.ResourceOption) (*UserPolicyAttachment, error) {
	if args == nil || args.PolicyArn == nil {
		return nil, errors.New("missing required argument 'PolicyArn'")
	}
	if args == nil || args.User == nil {
		return nil, errors.New("missing required argument 'User'")
	}
	if args == nil {
		args = &UserPolicyAttachmentArgs{}
	}
	var resource UserPolicyAttachment
	err := ctx.RegisterResource("aws:iam/userPolicyAttachment:UserPolicyAttachment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserPolicyAttachment gets an existing UserPolicyAttachment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserPolicyAttachment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserPolicyAttachmentState, opts ...pulumi.ResourceOption) (*UserPolicyAttachment, error) {
	var resource UserPolicyAttachment
	err := ctx.ReadResource("aws:iam/userPolicyAttachment:UserPolicyAttachment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserPolicyAttachment resources.
type userPolicyAttachmentState struct {
	// The ARN of the policy you want to apply
	PolicyArn *string `pulumi:"policyArn"`
	// The user the policy should be applied to
	User *string `pulumi:"user"`
}

type UserPolicyAttachmentState struct {
	// The ARN of the policy you want to apply
	PolicyArn pulumi.StringPtrInput
	// The user the policy should be applied to
	User pulumi.StringPtrInput
}

func (UserPolicyAttachmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*userPolicyAttachmentState)(nil)).Elem()
}

type userPolicyAttachmentArgs struct {
	// The ARN of the policy you want to apply
	PolicyArn string `pulumi:"policyArn"`
	// The user the policy should be applied to
	User interface{} `pulumi:"user"`
}

// The set of arguments for constructing a UserPolicyAttachment resource.
type UserPolicyAttachmentArgs struct {
	// The ARN of the policy you want to apply
	PolicyArn pulumi.StringInput
	// The user the policy should be applied to
	User pulumi.Input
}

func (UserPolicyAttachmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userPolicyAttachmentArgs)(nil)).Elem()
}
