// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package opsworks

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an OpsWorks User Profile resource.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/opsworks"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := opsworks.NewUserProfile(ctx, "myProfile", &opsworks.UserProfileArgs{
// 			UserArn:     pulumi.Any(aws_iam_user.User.Arn),
// 			SshUsername: pulumi.String("my_user"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type UserProfile struct {
	pulumi.CustomResourceState

	// Whether users can specify their own SSH public key through the My Settings page
	AllowSelfManagement pulumi.BoolPtrOutput `pulumi:"allowSelfManagement"`
	// The users public key
	SshPublicKey pulumi.StringPtrOutput `pulumi:"sshPublicKey"`
	// The ssh username, with witch this user wants to log in
	SshUsername pulumi.StringOutput `pulumi:"sshUsername"`
	// The user's IAM ARN
	UserArn pulumi.StringOutput `pulumi:"userArn"`
}

// NewUserProfile registers a new resource with the given unique name, arguments, and options.
func NewUserProfile(ctx *pulumi.Context,
	name string, args *UserProfileArgs, opts ...pulumi.ResourceOption) (*UserProfile, error) {
	if args == nil || args.SshUsername == nil {
		return nil, errors.New("missing required argument 'SshUsername'")
	}
	if args == nil || args.UserArn == nil {
		return nil, errors.New("missing required argument 'UserArn'")
	}
	if args == nil {
		args = &UserProfileArgs{}
	}
	var resource UserProfile
	err := ctx.RegisterResource("aws:opsworks/userProfile:UserProfile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserProfile gets an existing UserProfile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserProfile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserProfileState, opts ...pulumi.ResourceOption) (*UserProfile, error) {
	var resource UserProfile
	err := ctx.ReadResource("aws:opsworks/userProfile:UserProfile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserProfile resources.
type userProfileState struct {
	// Whether users can specify their own SSH public key through the My Settings page
	AllowSelfManagement *bool `pulumi:"allowSelfManagement"`
	// The users public key
	SshPublicKey *string `pulumi:"sshPublicKey"`
	// The ssh username, with witch this user wants to log in
	SshUsername *string `pulumi:"sshUsername"`
	// The user's IAM ARN
	UserArn *string `pulumi:"userArn"`
}

type UserProfileState struct {
	// Whether users can specify their own SSH public key through the My Settings page
	AllowSelfManagement pulumi.BoolPtrInput
	// The users public key
	SshPublicKey pulumi.StringPtrInput
	// The ssh username, with witch this user wants to log in
	SshUsername pulumi.StringPtrInput
	// The user's IAM ARN
	UserArn pulumi.StringPtrInput
}

func (UserProfileState) ElementType() reflect.Type {
	return reflect.TypeOf((*userProfileState)(nil)).Elem()
}

type userProfileArgs struct {
	// Whether users can specify their own SSH public key through the My Settings page
	AllowSelfManagement *bool `pulumi:"allowSelfManagement"`
	// The users public key
	SshPublicKey *string `pulumi:"sshPublicKey"`
	// The ssh username, with witch this user wants to log in
	SshUsername string `pulumi:"sshUsername"`
	// The user's IAM ARN
	UserArn string `pulumi:"userArn"`
}

// The set of arguments for constructing a UserProfile resource.
type UserProfileArgs struct {
	// Whether users can specify their own SSH public key through the My Settings page
	AllowSelfManagement pulumi.BoolPtrInput
	// The users public key
	SshPublicKey pulumi.StringPtrInput
	// The ssh username, with witch this user wants to log in
	SshUsername pulumi.StringInput
	// The user's IAM ARN
	UserArn pulumi.StringInput
}

func (UserProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userProfileArgs)(nil)).Elem()
}
