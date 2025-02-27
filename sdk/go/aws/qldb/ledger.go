// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package qldb

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an AWS Quantum Ledger Database (QLDB) resource
//
// > **NOTE:** Deletion protection is enabled by default. To successfully delete this resource via this provider, `deletionProtection = false` must be applied before attempting deletion.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/qldb"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := qldb.NewLedger(ctx, "sample_ledger", nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Ledger struct {
	pulumi.CustomResourceState

	// The ARN of the QLDB Ledger
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The deletion protection for the QLDB Ledger instance. By default it is `true`. To delete this resource via this provider, this value must be configured to `false` and applied first before attempting deletion.
	DeletionProtection pulumi.BoolPtrOutput `pulumi:"deletionProtection"`
	// The friendly name for the QLDB Ledger instance. This is atuo generated by default.
	Name pulumi.StringOutput `pulumi:"name"`
	// Key-value mapping of resource tags
	Tags pulumi.StringMapOutput `pulumi:"tags"`
}

// NewLedger registers a new resource with the given unique name, arguments, and options.
func NewLedger(ctx *pulumi.Context,
	name string, args *LedgerArgs, opts ...pulumi.ResourceOption) (*Ledger, error) {
	if args == nil {
		args = &LedgerArgs{}
	}
	var resource Ledger
	err := ctx.RegisterResource("aws:qldb/ledger:Ledger", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLedger gets an existing Ledger resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLedger(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LedgerState, opts ...pulumi.ResourceOption) (*Ledger, error) {
	var resource Ledger
	err := ctx.ReadResource("aws:qldb/ledger:Ledger", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Ledger resources.
type ledgerState struct {
	// The ARN of the QLDB Ledger
	Arn *string `pulumi:"arn"`
	// The deletion protection for the QLDB Ledger instance. By default it is `true`. To delete this resource via this provider, this value must be configured to `false` and applied first before attempting deletion.
	DeletionProtection *bool `pulumi:"deletionProtection"`
	// The friendly name for the QLDB Ledger instance. This is atuo generated by default.
	Name *string `pulumi:"name"`
	// Key-value mapping of resource tags
	Tags map[string]string `pulumi:"tags"`
}

type LedgerState struct {
	// The ARN of the QLDB Ledger
	Arn pulumi.StringPtrInput
	// The deletion protection for the QLDB Ledger instance. By default it is `true`. To delete this resource via this provider, this value must be configured to `false` and applied first before attempting deletion.
	DeletionProtection pulumi.BoolPtrInput
	// The friendly name for the QLDB Ledger instance. This is atuo generated by default.
	Name pulumi.StringPtrInput
	// Key-value mapping of resource tags
	Tags pulumi.StringMapInput
}

func (LedgerState) ElementType() reflect.Type {
	return reflect.TypeOf((*ledgerState)(nil)).Elem()
}

type ledgerArgs struct {
	// The deletion protection for the QLDB Ledger instance. By default it is `true`. To delete this resource via this provider, this value must be configured to `false` and applied first before attempting deletion.
	DeletionProtection *bool `pulumi:"deletionProtection"`
	// The friendly name for the QLDB Ledger instance. This is atuo generated by default.
	Name *string `pulumi:"name"`
	// Key-value mapping of resource tags
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a Ledger resource.
type LedgerArgs struct {
	// The deletion protection for the QLDB Ledger instance. By default it is `true`. To delete this resource via this provider, this value must be configured to `false` and applied first before attempting deletion.
	DeletionProtection pulumi.BoolPtrInput
	// The friendly name for the QLDB Ledger instance. This is atuo generated by default.
	Name pulumi.StringPtrInput
	// Key-value mapping of resource tags
	Tags pulumi.StringMapInput
}

func (LedgerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ledgerArgs)(nil)).Elem()
}
