// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.AppSync
{
    /// <summary>
    /// Provides an AppSync DataSource.
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
    ///         var exampleTable = new Aws.DynamoDB.Table("exampleTable", new Aws.DynamoDB.TableArgs
    ///         {
    ///             ReadCapacity = 1,
    ///             WriteCapacity = 1,
    ///             HashKey = "UserId",
    ///             Attributes = 
    ///             {
    ///                 new Aws.DynamoDB.Inputs.TableAttributeArgs
    ///                 {
    ///                     Name = "UserId",
    ///                     Type = "S",
    ///                 },
    ///             },
    ///         });
    ///         var exampleRole = new Aws.Iam.Role("exampleRole", new Aws.Iam.RoleArgs
    ///         {
    ///             AssumeRolePolicy = @"{
    ///   ""Version"": ""2012-10-17"",
    ///   ""Statement"": [
    ///     {
    ///       ""Action"": ""sts:AssumeRole"",
    ///       ""Principal"": {
    ///         ""Service"": ""appsync.amazonaws.com""
    ///       },
    ///       ""Effect"": ""Allow""
    ///     }
    ///   ]
    /// }
    /// ",
    ///         });
    ///         var exampleRolePolicy = new Aws.Iam.RolePolicy("exampleRolePolicy", new Aws.Iam.RolePolicyArgs
    ///         {
    ///             Role = exampleRole.Id,
    ///             Policy = exampleTable.Arn.Apply(arn =&gt; @$"{{
    ///   ""Version"": ""2012-10-17"",
    ///   ""Statement"": [
    ///     {{
    ///       ""Action"": [
    ///         ""dynamodb:*""
    ///       ],
    ///       ""Effect"": ""Allow"",
    ///       ""Resource"": [
    ///         ""{arn}""
    ///       ]
    ///     }}
    ///   ]
    /// }}
    /// "),
    ///         });
    ///         var exampleGraphQLApi = new Aws.AppSync.GraphQLApi("exampleGraphQLApi", new Aws.AppSync.GraphQLApiArgs
    ///         {
    ///             AuthenticationType = "API_KEY",
    ///         });
    ///         var exampleDataSource = new Aws.AppSync.DataSource("exampleDataSource", new Aws.AppSync.DataSourceArgs
    ///         {
    ///             ApiId = exampleGraphQLApi.Id,
    ///             ServiceRoleArn = exampleRole.Arn,
    ///             Type = "AMAZON_DYNAMODB",
    ///             DynamodbConfig = new Aws.AppSync.Inputs.DataSourceDynamodbConfigArgs
    ///             {
    ///                 TableName = exampleTable.Name,
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class DataSource : Pulumi.CustomResource
    {
        /// <summary>
        /// The API ID for the GraphQL API for the DataSource.
        /// </summary>
        [Output("apiId")]
        public Output<string> ApiId { get; private set; } = null!;

        /// <summary>
        /// The ARN
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// A description of the DataSource.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// DynamoDB settings. See below
        /// </summary>
        [Output("dynamodbConfig")]
        public Output<Outputs.DataSourceDynamodbConfig?> DynamodbConfig { get; private set; } = null!;

        /// <summary>
        /// Amazon Elasticsearch settings. See below
        /// </summary>
        [Output("elasticsearchConfig")]
        public Output<Outputs.DataSourceElasticsearchConfig?> ElasticsearchConfig { get; private set; } = null!;

        /// <summary>
        /// HTTP settings. See below
        /// </summary>
        [Output("httpConfig")]
        public Output<Outputs.DataSourceHttpConfig?> HttpConfig { get; private set; } = null!;

        /// <summary>
        /// AWS Lambda settings. See below
        /// </summary>
        [Output("lambdaConfig")]
        public Output<Outputs.DataSourceLambdaConfig?> LambdaConfig { get; private set; } = null!;

        /// <summary>
        /// A user-supplied name for the DataSource.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The IAM service role ARN for the data source.
        /// </summary>
        [Output("serviceRoleArn")]
        public Output<string?> ServiceRoleArn { get; private set; } = null!;

        /// <summary>
        /// The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;


        /// <summary>
        /// Create a DataSource resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DataSource(string name, DataSourceArgs args, CustomResourceOptions? options = null)
            : base("aws:appsync/dataSource:DataSource", name, args ?? new DataSourceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DataSource(string name, Input<string> id, DataSourceState? state = null, CustomResourceOptions? options = null)
            : base("aws:appsync/dataSource:DataSource", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing DataSource resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DataSource Get(string name, Input<string> id, DataSourceState? state = null, CustomResourceOptions? options = null)
        {
            return new DataSource(name, id, state, options);
        }
    }

    public sealed class DataSourceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The API ID for the GraphQL API for the DataSource.
        /// </summary>
        [Input("apiId", required: true)]
        public Input<string> ApiId { get; set; } = null!;

        /// <summary>
        /// A description of the DataSource.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// DynamoDB settings. See below
        /// </summary>
        [Input("dynamodbConfig")]
        public Input<Inputs.DataSourceDynamodbConfigArgs>? DynamodbConfig { get; set; }

        /// <summary>
        /// Amazon Elasticsearch settings. See below
        /// </summary>
        [Input("elasticsearchConfig")]
        public Input<Inputs.DataSourceElasticsearchConfigArgs>? ElasticsearchConfig { get; set; }

        /// <summary>
        /// HTTP settings. See below
        /// </summary>
        [Input("httpConfig")]
        public Input<Inputs.DataSourceHttpConfigArgs>? HttpConfig { get; set; }

        /// <summary>
        /// AWS Lambda settings. See below
        /// </summary>
        [Input("lambdaConfig")]
        public Input<Inputs.DataSourceLambdaConfigArgs>? LambdaConfig { get; set; }

        /// <summary>
        /// A user-supplied name for the DataSource.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The IAM service role ARN for the data source.
        /// </summary>
        [Input("serviceRoleArn")]
        public Input<string>? ServiceRoleArn { get; set; }

        /// <summary>
        /// The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public DataSourceArgs()
        {
        }
    }

    public sealed class DataSourceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The API ID for the GraphQL API for the DataSource.
        /// </summary>
        [Input("apiId")]
        public Input<string>? ApiId { get; set; }

        /// <summary>
        /// The ARN
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// A description of the DataSource.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// DynamoDB settings. See below
        /// </summary>
        [Input("dynamodbConfig")]
        public Input<Inputs.DataSourceDynamodbConfigGetArgs>? DynamodbConfig { get; set; }

        /// <summary>
        /// Amazon Elasticsearch settings. See below
        /// </summary>
        [Input("elasticsearchConfig")]
        public Input<Inputs.DataSourceElasticsearchConfigGetArgs>? ElasticsearchConfig { get; set; }

        /// <summary>
        /// HTTP settings. See below
        /// </summary>
        [Input("httpConfig")]
        public Input<Inputs.DataSourceHttpConfigGetArgs>? HttpConfig { get; set; }

        /// <summary>
        /// AWS Lambda settings. See below
        /// </summary>
        [Input("lambdaConfig")]
        public Input<Inputs.DataSourceLambdaConfigGetArgs>? LambdaConfig { get; set; }

        /// <summary>
        /// A user-supplied name for the DataSource.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The IAM service role ARN for the data source.
        /// </summary>
        [Input("serviceRoleArn")]
        public Input<string>? ServiceRoleArn { get; set; }

        /// <summary>
        /// The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public DataSourceState()
        {
        }
    }
}
