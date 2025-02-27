// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to lookup information about IAM Server Certificates.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/elb"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/iam"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := "my-domain.org"
// 		opt1 := true
// 		my_domain, err := iam.LookupServerCertificate(ctx, &iam.LookupServerCertificateArgs{
// 			NamePrefix: &opt0,
// 			Latest:     &opt1,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = elb.NewLoadBalancer(ctx, "elb", &elb.LoadBalancerArgs{
// 			Listeners: elb.LoadBalancerListenerArray{
// 				&elb.LoadBalancerListenerArgs{
// 					InstancePort:     pulumi.Int(8000),
// 					InstanceProtocol: pulumi.String("https"),
// 					LbPort:           pulumi.Int(443),
// 					LbProtocol:       pulumi.String("https"),
// 					SslCertificateId: pulumi.String(my_domain.Arn),
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
// ## Import
//
// The import function will read in certificate body, certificate chain (if it exists), id, name, path, and arn.
// It will not retrieve the private key which is not available through the AWS API.
func LookupServerCertificate(ctx *pulumi.Context, args *LookupServerCertificateArgs, opts ...pulumi.InvokeOption) (*LookupServerCertificateResult, error) {
	var rv LookupServerCertificateResult
	err := ctx.Invoke("aws:iam/getServerCertificate:getServerCertificate", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getServerCertificate.
type LookupServerCertificateArgs struct {
	// sort results by expiration date. returns the certificate with expiration date in furthest in the future.
	Latest *bool `pulumi:"latest"`
	// exact name of the cert to lookup
	Name *string `pulumi:"name"`
	// prefix of cert to filter by
	NamePrefix *string `pulumi:"namePrefix"`
	// prefix of path to filter by
	PathPrefix *string `pulumi:"pathPrefix"`
}

// A collection of values returned by getServerCertificate.
type LookupServerCertificateResult struct {
	Arn              string `pulumi:"arn"`
	CertificateBody  string `pulumi:"certificateBody"`
	CertificateChain string `pulumi:"certificateChain"`
	ExpirationDate   string `pulumi:"expirationDate"`
	// The provider-assigned unique ID for this managed resource.
	Id         string  `pulumi:"id"`
	Latest     *bool   `pulumi:"latest"`
	Name       string  `pulumi:"name"`
	NamePrefix *string `pulumi:"namePrefix"`
	Path       string  `pulumi:"path"`
	PathPrefix *string `pulumi:"pathPrefix"`
	UploadDate string  `pulumi:"uploadDate"`
}
