// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ebs

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Creates a Snapshot of a snapshot.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/ebs"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		example, err := ebs.NewVolume(ctx, "example", &ebs.VolumeArgs{
// 			AvailabilityZone: pulumi.String("us-west-2a"),
// 			Size:             pulumi.Int(40),
// 			Tags: pulumi.StringMap{
// 				"Name": pulumi.String("HelloWorld"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleSnapshot, err := ebs.NewSnapshot(ctx, "exampleSnapshot", &ebs.SnapshotArgs{
// 			VolumeId: example.ID(),
// 			Tags: pulumi.StringMap{
// 				"Name": pulumi.String("HelloWorld_snap"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = ebs.NewSnapshotCopy(ctx, "exampleCopy", &ebs.SnapshotCopyArgs{
// 			SourceSnapshotId: exampleSnapshot.ID(),
// 			SourceRegion:     pulumi.String("us-west-2"),
// 			Tags: pulumi.StringMap{
// 				"Name": pulumi.String("HelloWorld_copy_snap"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type SnapshotCopy struct {
	pulumi.CustomResourceState

	// Amazon Resource Name (ARN) of the EBS Snapshot.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The data encryption key identifier for the snapshot.
	// * `sourceSnapshotId` The ARN of the copied snapshot.
	// * `sourceRegion` The region of the source snapshot.
	DataEncryptionKeyId pulumi.StringOutput `pulumi:"dataEncryptionKeyId"`
	// A description of what the snapshot is.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Whether the snapshot is encrypted.
	Encrypted pulumi.BoolPtrOutput `pulumi:"encrypted"`
	// The ARN for the KMS encryption key.
	KmsKeyId pulumi.StringPtrOutput `pulumi:"kmsKeyId"`
	// Value from an Amazon-maintained list (`amazon`, `aws-marketplace`, `microsoft`) of snapshot owners.
	OwnerAlias pulumi.StringOutput `pulumi:"ownerAlias"`
	// The AWS account ID of the snapshot owner.
	OwnerId pulumi.StringOutput `pulumi:"ownerId"`
	// The region of the source snapshot.
	SourceRegion pulumi.StringOutput `pulumi:"sourceRegion"`
	// The ARN for the snapshot to be copied.
	SourceSnapshotId pulumi.StringOutput `pulumi:"sourceSnapshotId"`
	// A map of tags for the snapshot.
	Tags     pulumi.StringMapOutput `pulumi:"tags"`
	VolumeId pulumi.StringOutput    `pulumi:"volumeId"`
	// The size of the drive in GiBs.
	VolumeSize pulumi.IntOutput `pulumi:"volumeSize"`
}

// NewSnapshotCopy registers a new resource with the given unique name, arguments, and options.
func NewSnapshotCopy(ctx *pulumi.Context,
	name string, args *SnapshotCopyArgs, opts ...pulumi.ResourceOption) (*SnapshotCopy, error) {
	if args == nil || args.SourceRegion == nil {
		return nil, errors.New("missing required argument 'SourceRegion'")
	}
	if args == nil || args.SourceSnapshotId == nil {
		return nil, errors.New("missing required argument 'SourceSnapshotId'")
	}
	if args == nil {
		args = &SnapshotCopyArgs{}
	}
	var resource SnapshotCopy
	err := ctx.RegisterResource("aws:ebs/snapshotCopy:SnapshotCopy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSnapshotCopy gets an existing SnapshotCopy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSnapshotCopy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SnapshotCopyState, opts ...pulumi.ResourceOption) (*SnapshotCopy, error) {
	var resource SnapshotCopy
	err := ctx.ReadResource("aws:ebs/snapshotCopy:SnapshotCopy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SnapshotCopy resources.
type snapshotCopyState struct {
	// Amazon Resource Name (ARN) of the EBS Snapshot.
	Arn *string `pulumi:"arn"`
	// The data encryption key identifier for the snapshot.
	// * `sourceSnapshotId` The ARN of the copied snapshot.
	// * `sourceRegion` The region of the source snapshot.
	DataEncryptionKeyId *string `pulumi:"dataEncryptionKeyId"`
	// A description of what the snapshot is.
	Description *string `pulumi:"description"`
	// Whether the snapshot is encrypted.
	Encrypted *bool `pulumi:"encrypted"`
	// The ARN for the KMS encryption key.
	KmsKeyId *string `pulumi:"kmsKeyId"`
	// Value from an Amazon-maintained list (`amazon`, `aws-marketplace`, `microsoft`) of snapshot owners.
	OwnerAlias *string `pulumi:"ownerAlias"`
	// The AWS account ID of the snapshot owner.
	OwnerId *string `pulumi:"ownerId"`
	// The region of the source snapshot.
	SourceRegion *string `pulumi:"sourceRegion"`
	// The ARN for the snapshot to be copied.
	SourceSnapshotId *string `pulumi:"sourceSnapshotId"`
	// A map of tags for the snapshot.
	Tags     map[string]string `pulumi:"tags"`
	VolumeId *string           `pulumi:"volumeId"`
	// The size of the drive in GiBs.
	VolumeSize *int `pulumi:"volumeSize"`
}

type SnapshotCopyState struct {
	// Amazon Resource Name (ARN) of the EBS Snapshot.
	Arn pulumi.StringPtrInput
	// The data encryption key identifier for the snapshot.
	// * `sourceSnapshotId` The ARN of the copied snapshot.
	// * `sourceRegion` The region of the source snapshot.
	DataEncryptionKeyId pulumi.StringPtrInput
	// A description of what the snapshot is.
	Description pulumi.StringPtrInput
	// Whether the snapshot is encrypted.
	Encrypted pulumi.BoolPtrInput
	// The ARN for the KMS encryption key.
	KmsKeyId pulumi.StringPtrInput
	// Value from an Amazon-maintained list (`amazon`, `aws-marketplace`, `microsoft`) of snapshot owners.
	OwnerAlias pulumi.StringPtrInput
	// The AWS account ID of the snapshot owner.
	OwnerId pulumi.StringPtrInput
	// The region of the source snapshot.
	SourceRegion pulumi.StringPtrInput
	// The ARN for the snapshot to be copied.
	SourceSnapshotId pulumi.StringPtrInput
	// A map of tags for the snapshot.
	Tags     pulumi.StringMapInput
	VolumeId pulumi.StringPtrInput
	// The size of the drive in GiBs.
	VolumeSize pulumi.IntPtrInput
}

func (SnapshotCopyState) ElementType() reflect.Type {
	return reflect.TypeOf((*snapshotCopyState)(nil)).Elem()
}

type snapshotCopyArgs struct {
	// A description of what the snapshot is.
	Description *string `pulumi:"description"`
	// Whether the snapshot is encrypted.
	Encrypted *bool `pulumi:"encrypted"`
	// The ARN for the KMS encryption key.
	KmsKeyId *string `pulumi:"kmsKeyId"`
	// The region of the source snapshot.
	SourceRegion string `pulumi:"sourceRegion"`
	// The ARN for the snapshot to be copied.
	SourceSnapshotId string `pulumi:"sourceSnapshotId"`
	// A map of tags for the snapshot.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a SnapshotCopy resource.
type SnapshotCopyArgs struct {
	// A description of what the snapshot is.
	Description pulumi.StringPtrInput
	// Whether the snapshot is encrypted.
	Encrypted pulumi.BoolPtrInput
	// The ARN for the KMS encryption key.
	KmsKeyId pulumi.StringPtrInput
	// The region of the source snapshot.
	SourceRegion pulumi.StringInput
	// The ARN for the snapshot to be copied.
	SourceSnapshotId pulumi.StringInput
	// A map of tags for the snapshot.
	Tags pulumi.StringMapInput
}

func (SnapshotCopyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*snapshotCopyArgs)(nil)).Elem()
}
