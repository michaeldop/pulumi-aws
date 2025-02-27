// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.ApiGateway
{
    /// <summary>
    /// Provides a resource to manage an API Gateway Documentation Version.
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
    ///         var exampleRestApi = new Aws.ApiGateway.RestApi("exampleRestApi", new Aws.ApiGateway.RestApiArgs
    ///         {
    ///         });
    ///         var exampleDocumentationPart = new Aws.ApiGateway.DocumentationPart("exampleDocumentationPart", new Aws.ApiGateway.DocumentationPartArgs
    ///         {
    ///             Location = new Aws.ApiGateway.Inputs.DocumentationPartLocationArgs
    ///             {
    ///                 Type = "API",
    ///             },
    ///             Properties = "{\"description\":\"Example\"}",
    ///             RestApiId = exampleRestApi.Id,
    ///         });
    ///         var exampleDocumentationVersion = new Aws.ApiGateway.DocumentationVersion("exampleDocumentationVersion", new Aws.ApiGateway.DocumentationVersionArgs
    ///         {
    ///             Version = "example_version",
    ///             RestApiId = exampleRestApi.Id,
    ///             Description = "Example description",
    ///         }, new CustomResourceOptions
    ///         {
    ///             DependsOn = 
    ///             {
    ///                 exampleDocumentationPart,
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class DocumentationVersion : Pulumi.CustomResource
    {
        /// <summary>
        /// The description of the API documentation version.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The ID of the associated Rest API
        /// </summary>
        [Output("restApiId")]
        public Output<string> RestApiId { get; private set; } = null!;

        /// <summary>
        /// The version identifier of the API documentation snapshot.
        /// </summary>
        [Output("version")]
        public Output<string> Version { get; private set; } = null!;


        /// <summary>
        /// Create a DocumentationVersion resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DocumentationVersion(string name, DocumentationVersionArgs args, CustomResourceOptions? options = null)
            : base("aws:apigateway/documentationVersion:DocumentationVersion", name, args ?? new DocumentationVersionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DocumentationVersion(string name, Input<string> id, DocumentationVersionState? state = null, CustomResourceOptions? options = null)
            : base("aws:apigateway/documentationVersion:DocumentationVersion", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing DocumentationVersion resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DocumentationVersion Get(string name, Input<string> id, DocumentationVersionState? state = null, CustomResourceOptions? options = null)
        {
            return new DocumentationVersion(name, id, state, options);
        }
    }

    public sealed class DocumentationVersionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the API documentation version.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The ID of the associated Rest API
        /// </summary>
        [Input("restApiId", required: true)]
        public Input<string> RestApiId { get; set; } = null!;

        /// <summary>
        /// The version identifier of the API documentation snapshot.
        /// </summary>
        [Input("version", required: true)]
        public Input<string> Version { get; set; } = null!;

        public DocumentationVersionArgs()
        {
        }
    }

    public sealed class DocumentationVersionState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the API documentation version.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The ID of the associated Rest API
        /// </summary>
        [Input("restApiId")]
        public Input<string>? RestApiId { get; set; }

        /// <summary>
        /// The version identifier of the API documentation snapshot.
        /// </summary>
        [Input("version")]
        public Input<string>? Version { get; set; }

        public DocumentationVersionState()
        {
        }
    }
}
