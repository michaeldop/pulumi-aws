// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Route53
{
    /// <summary>
    /// Manages a Route53 Hosted Zone VPC association. VPC associations can only be made on private zones. See the `aws.route53.VpcAssociationAuthorization` resource for setting up cross-account associations.
    /// 
    /// &gt; **NOTE:** Unless explicit association ordering is required (e.g. a separate cross-account association authorization), usage of this resource is not recommended. Use the `vpc` configuration blocks available within the `aws.route53.Zone` resource instead.
    /// 
    /// &gt; **NOTE:** This provider provides both this standalone Zone VPC Association resource and exclusive VPC associations defined in-line in the `aws.route53.Zone` resource via `vpc` configuration blocks. At this time, you cannot use those in-line VPC associations in conjunction with this resource and the same zone ID otherwise it will cause a perpetual difference in plan output. You can optionally use [`ignoreChanges`](https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges) in the `aws.route53.Zone` resource to manage additional associations via this resource.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var primary = new Aws.Ec2.Vpc("primary", new Aws.Ec2.VpcArgs
    ///         {
    ///             CidrBlock = "10.6.0.0/16",
    ///             EnableDnsHostnames = true,
    ///             EnableDnsSupport = true,
    ///         });
    ///         var secondaryVpc = new Aws.Ec2.Vpc("secondaryVpc", new Aws.Ec2.VpcArgs
    ///         {
    ///             CidrBlock = "10.7.0.0/16",
    ///             EnableDnsHostnames = true,
    ///             EnableDnsSupport = true,
    ///         });
    ///         var example = new Aws.Route53.Zone("example", new Aws.Route53.ZoneArgs
    ///         {
    ///             Vpcs = 
    ///             {
    ///                 new Aws.Route53.Inputs.ZoneVpcArgs
    ///                 {
    ///                     VpcId = primary.Id,
    ///                 },
    ///             },
    ///         });
    ///         var secondaryZoneAssociation = new Aws.Route53.ZoneAssociation("secondaryZoneAssociation", new Aws.Route53.ZoneAssociationArgs
    ///         {
    ///             ZoneId = example.ZoneId,
    ///             VpcId = secondaryVpc.Id,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class ZoneAssociation : Pulumi.CustomResource
    {
        /// <summary>
        /// The account ID of the account that created the hosted zone.
        /// </summary>
        [Output("owningAccount")]
        public Output<string> OwningAccount { get; private set; } = null!;

        /// <summary>
        /// The VPC to associate with the private hosted zone.
        /// </summary>
        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;

        /// <summary>
        /// The VPC's region. Defaults to the region of the AWS provider.
        /// </summary>
        [Output("vpcRegion")]
        public Output<string> VpcRegion { get; private set; } = null!;

        /// <summary>
        /// The private hosted zone to associate.
        /// </summary>
        [Output("zoneId")]
        public Output<string> ZoneId { get; private set; } = null!;


        /// <summary>
        /// Create a ZoneAssociation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ZoneAssociation(string name, ZoneAssociationArgs args, CustomResourceOptions? options = null)
            : base("aws:route53/zoneAssociation:ZoneAssociation", name, args ?? new ZoneAssociationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ZoneAssociation(string name, Input<string> id, ZoneAssociationState? state = null, CustomResourceOptions? options = null)
            : base("aws:route53/zoneAssociation:ZoneAssociation", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ZoneAssociation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ZoneAssociation Get(string name, Input<string> id, ZoneAssociationState? state = null, CustomResourceOptions? options = null)
        {
            return new ZoneAssociation(name, id, state, options);
        }
    }

    public sealed class ZoneAssociationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The VPC to associate with the private hosted zone.
        /// </summary>
        [Input("vpcId", required: true)]
        public Input<string> VpcId { get; set; } = null!;

        /// <summary>
        /// The VPC's region. Defaults to the region of the AWS provider.
        /// </summary>
        [Input("vpcRegion")]
        public Input<string>? VpcRegion { get; set; }

        /// <summary>
        /// The private hosted zone to associate.
        /// </summary>
        [Input("zoneId", required: true)]
        public Input<string> ZoneId { get; set; } = null!;

        public ZoneAssociationArgs()
        {
        }
    }

    public sealed class ZoneAssociationState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The account ID of the account that created the hosted zone.
        /// </summary>
        [Input("owningAccount")]
        public Input<string>? OwningAccount { get; set; }

        /// <summary>
        /// The VPC to associate with the private hosted zone.
        /// </summary>
        [Input("vpcId")]
        public Input<string>? VpcId { get; set; }

        /// <summary>
        /// The VPC's region. Defaults to the region of the AWS provider.
        /// </summary>
        [Input("vpcRegion")]
        public Input<string>? VpcRegion { get; set; }

        /// <summary>
        /// The private hosted zone to associate.
        /// </summary>
        [Input("zoneId")]
        public Input<string>? ZoneId { get; set; }

        public ZoneAssociationState()
        {
        }
    }
}
