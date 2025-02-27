// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.RedShift
{
    /// <summary>
    /// Creates a new Amazon Redshift subnet group. You must provide a list of one or more subnets in your existing Amazon Virtual Private Cloud (Amazon VPC) when creating Amazon Redshift subnet group.
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
    ///         var fooVpc = new Aws.Ec2.Vpc("fooVpc", new Aws.Ec2.VpcArgs
    ///         {
    ///             CidrBlock = "10.1.0.0/16",
    ///         });
    ///         var fooSubnet = new Aws.Ec2.Subnet("fooSubnet", new Aws.Ec2.SubnetArgs
    ///         {
    ///             CidrBlock = "10.1.1.0/24",
    ///             AvailabilityZone = "us-west-2a",
    ///             VpcId = fooVpc.Id,
    ///             Tags = 
    ///             {
    ///                 { "Name", "tf-dbsubnet-test-1" },
    ///             },
    ///         });
    ///         var bar = new Aws.Ec2.Subnet("bar", new Aws.Ec2.SubnetArgs
    ///         {
    ///             CidrBlock = "10.1.2.0/24",
    ///             AvailabilityZone = "us-west-2b",
    ///             VpcId = fooVpc.Id,
    ///             Tags = 
    ///             {
    ///                 { "Name", "tf-dbsubnet-test-2" },
    ///             },
    ///         });
    ///         var fooSubnetGroup = new Aws.RedShift.SubnetGroup("fooSubnetGroup", new Aws.RedShift.SubnetGroupArgs
    ///         {
    ///             SubnetIds = 
    ///             {
    ///                 fooSubnet.Id,
    ///                 bar.Id,
    ///             },
    ///             Tags = 
    ///             {
    ///                 { "environment", "Production" },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class SubnetGroup : Pulumi.CustomResource
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the Redshift Subnet group name
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The description of the Redshift Subnet group. Defaults to "Managed by Pulumi".
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The name of the Redshift Subnet group.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// An array of VPC subnet IDs.
        /// </summary>
        [Output("subnetIds")]
        public Output<ImmutableArray<string>> SubnetIds { get; private set; } = null!;

        /// <summary>
        /// A map of tags to assign to the resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a SubnetGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SubnetGroup(string name, SubnetGroupArgs args, CustomResourceOptions? options = null)
            : base("aws:redshift/subnetGroup:SubnetGroup", name, args ?? new SubnetGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SubnetGroup(string name, Input<string> id, SubnetGroupState? state = null, CustomResourceOptions? options = null)
            : base("aws:redshift/subnetGroup:SubnetGroup", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SubnetGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SubnetGroup Get(string name, Input<string> id, SubnetGroupState? state = null, CustomResourceOptions? options = null)
        {
            return new SubnetGroup(name, id, state, options);
        }
    }

    public sealed class SubnetGroupArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the Redshift Subnet group. Defaults to "Managed by Pulumi".
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the Redshift Subnet group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("subnetIds", required: true)]
        private InputList<string>? _subnetIds;

        /// <summary>
        /// An array of VPC subnet IDs.
        /// </summary>
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A map of tags to assign to the resource.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        public SubnetGroupArgs()
        {
            Description = "Managed by Pulumi";
        }
    }

    public sealed class SubnetGroupState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the Redshift Subnet group name
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The description of the Redshift Subnet group. Defaults to "Managed by Pulumi".
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the Redshift Subnet group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("subnetIds")]
        private InputList<string>? _subnetIds;

        /// <summary>
        /// An array of VPC subnet IDs.
        /// </summary>
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A map of tags to assign to the resource.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        public SubnetGroupState()
        {
            Description = "Managed by Pulumi";
        }
    }
}
