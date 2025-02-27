// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package pinpoint

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Pinpoint ADM (Amazon Device Messaging) Channel resource.
//
// > **Note:** All arguments including the Client ID and Client Secret will be stored in the raw state as plain-text.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/pinpoint"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		app, err := pinpoint.NewApp(ctx, "app", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = pinpoint.NewAdmChannel(ctx, "channel", &pinpoint.AdmChannelArgs{
// 			ApplicationId: app.ApplicationId,
// 			ClientId:      pulumi.String(""),
// 			ClientSecret:  pulumi.String(""),
// 			Enabled:       pulumi.Bool(true),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type AdmChannel struct {
	pulumi.CustomResourceState

	// The application ID.
	ApplicationId pulumi.StringOutput `pulumi:"applicationId"`
	// Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.
	ClientId pulumi.StringOutput `pulumi:"clientId"`
	// Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.
	ClientSecret pulumi.StringOutput `pulumi:"clientSecret"`
	// Specifies whether to enable the channel. Defaults to `true`.
	Enabled pulumi.BoolPtrOutput `pulumi:"enabled"`
}

// NewAdmChannel registers a new resource with the given unique name, arguments, and options.
func NewAdmChannel(ctx *pulumi.Context,
	name string, args *AdmChannelArgs, opts ...pulumi.ResourceOption) (*AdmChannel, error) {
	if args == nil || args.ApplicationId == nil {
		return nil, errors.New("missing required argument 'ApplicationId'")
	}
	if args == nil || args.ClientId == nil {
		return nil, errors.New("missing required argument 'ClientId'")
	}
	if args == nil || args.ClientSecret == nil {
		return nil, errors.New("missing required argument 'ClientSecret'")
	}
	if args == nil {
		args = &AdmChannelArgs{}
	}
	var resource AdmChannel
	err := ctx.RegisterResource("aws:pinpoint/admChannel:AdmChannel", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAdmChannel gets an existing AdmChannel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAdmChannel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AdmChannelState, opts ...pulumi.ResourceOption) (*AdmChannel, error) {
	var resource AdmChannel
	err := ctx.ReadResource("aws:pinpoint/admChannel:AdmChannel", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AdmChannel resources.
type admChannelState struct {
	// The application ID.
	ApplicationId *string `pulumi:"applicationId"`
	// Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.
	ClientId *string `pulumi:"clientId"`
	// Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.
	ClientSecret *string `pulumi:"clientSecret"`
	// Specifies whether to enable the channel. Defaults to `true`.
	Enabled *bool `pulumi:"enabled"`
}

type AdmChannelState struct {
	// The application ID.
	ApplicationId pulumi.StringPtrInput
	// Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.
	ClientId pulumi.StringPtrInput
	// Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.
	ClientSecret pulumi.StringPtrInput
	// Specifies whether to enable the channel. Defaults to `true`.
	Enabled pulumi.BoolPtrInput
}

func (AdmChannelState) ElementType() reflect.Type {
	return reflect.TypeOf((*admChannelState)(nil)).Elem()
}

type admChannelArgs struct {
	// The application ID.
	ApplicationId string `pulumi:"applicationId"`
	// Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.
	ClientId string `pulumi:"clientId"`
	// Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.
	ClientSecret string `pulumi:"clientSecret"`
	// Specifies whether to enable the channel. Defaults to `true`.
	Enabled *bool `pulumi:"enabled"`
}

// The set of arguments for constructing a AdmChannel resource.
type AdmChannelArgs struct {
	// The application ID.
	ApplicationId pulumi.StringInput
	// Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.
	ClientId pulumi.StringInput
	// Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.
	ClientSecret pulumi.StringInput
	// Specifies whether to enable the channel. Defaults to `true`.
	Enabled pulumi.BoolPtrInput
}

func (AdmChannelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*admChannelArgs)(nil)).Elem()
}
