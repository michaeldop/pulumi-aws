// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudwatch

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a CloudWatch Log Stream resource.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/cloudwatch"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		yada, err := cloudwatch.NewLogGroup(ctx, "yada", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = cloudwatch.NewLogStream(ctx, "foo", &cloudwatch.LogStreamArgs{
// 			LogGroupName: yada.Name,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type LogStream struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) specifying the log stream.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The name of the log group under which the log stream is to be created.
	LogGroupName pulumi.StringOutput `pulumi:"logGroupName"`
	// The name of the log stream. Must not be longer than 512 characters and must not contain `:`
	Name pulumi.StringOutput `pulumi:"name"`
}

// NewLogStream registers a new resource with the given unique name, arguments, and options.
func NewLogStream(ctx *pulumi.Context,
	name string, args *LogStreamArgs, opts ...pulumi.ResourceOption) (*LogStream, error) {
	if args == nil || args.LogGroupName == nil {
		return nil, errors.New("missing required argument 'LogGroupName'")
	}
	if args == nil {
		args = &LogStreamArgs{}
	}
	var resource LogStream
	err := ctx.RegisterResource("aws:cloudwatch/logStream:LogStream", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLogStream gets an existing LogStream resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLogStream(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LogStreamState, opts ...pulumi.ResourceOption) (*LogStream, error) {
	var resource LogStream
	err := ctx.ReadResource("aws:cloudwatch/logStream:LogStream", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LogStream resources.
type logStreamState struct {
	// The Amazon Resource Name (ARN) specifying the log stream.
	Arn *string `pulumi:"arn"`
	// The name of the log group under which the log stream is to be created.
	LogGroupName *string `pulumi:"logGroupName"`
	// The name of the log stream. Must not be longer than 512 characters and must not contain `:`
	Name *string `pulumi:"name"`
}

type LogStreamState struct {
	// The Amazon Resource Name (ARN) specifying the log stream.
	Arn pulumi.StringPtrInput
	// The name of the log group under which the log stream is to be created.
	LogGroupName pulumi.StringPtrInput
	// The name of the log stream. Must not be longer than 512 characters and must not contain `:`
	Name pulumi.StringPtrInput
}

func (LogStreamState) ElementType() reflect.Type {
	return reflect.TypeOf((*logStreamState)(nil)).Elem()
}

type logStreamArgs struct {
	// The name of the log group under which the log stream is to be created.
	LogGroupName string `pulumi:"logGroupName"`
	// The name of the log stream. Must not be longer than 512 characters and must not contain `:`
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a LogStream resource.
type LogStreamArgs struct {
	// The name of the log group under which the log stream is to be created.
	LogGroupName pulumi.StringInput
	// The name of the log stream. Must not be longer than 512 characters and must not contain `:`
	Name pulumi.StringPtrInput
}

func (LogStreamArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*logStreamArgs)(nil)).Elem()
}
