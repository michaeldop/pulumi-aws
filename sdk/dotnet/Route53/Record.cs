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
    /// Provides a Route53 record resource.
    /// 
    /// ## Example Usage
    /// ### Simple routing policy
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var www = new Aws.Route53.Record("www", new Aws.Route53.RecordArgs
    ///         {
    ///             ZoneId = aws_route53_zone.Primary.Zone_id,
    ///             Name = "www.example.com",
    ///             Type = "A",
    ///             Ttl = 300,
    ///             Records = 
    ///             {
    ///                 aws_eip.Lb.Public_ip,
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ### Weighted routing policy
    /// Other routing policies are configured similarly. See [AWS Route53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html) for details.
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var www_dev = new Aws.Route53.Record("www-dev", new Aws.Route53.RecordArgs
    ///         {
    ///             ZoneId = aws_route53_zone.Primary.Zone_id,
    ///             Name = "www",
    ///             Type = "CNAME",
    ///             Ttl = 5,
    ///             WeightedRoutingPolicies = 
    ///             {
    ///                 new Aws.Route53.Inputs.RecordWeightedRoutingPolicyArgs
    ///                 {
    ///                     Weight = 10,
    ///                 },
    ///             },
    ///             SetIdentifier = "dev",
    ///             Records = 
    ///             {
    ///                 "dev.example.com",
    ///             },
    ///         });
    ///         var www_live = new Aws.Route53.Record("www-live", new Aws.Route53.RecordArgs
    ///         {
    ///             ZoneId = aws_route53_zone.Primary.Zone_id,
    ///             Name = "www",
    ///             Type = "CNAME",
    ///             Ttl = 5,
    ///             WeightedRoutingPolicies = 
    ///             {
    ///                 new Aws.Route53.Inputs.RecordWeightedRoutingPolicyArgs
    ///                 {
    ///                     Weight = 90,
    ///                 },
    ///             },
    ///             SetIdentifier = "live",
    ///             Records = 
    ///             {
    ///                 "live.example.com",
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ### Alias record
    /// See [related part of AWS Route53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html)
    /// to understand differences between alias and non-alias records.
    /// 
    /// TTL for all alias records is [60 seconds](https://aws.amazon.com/route53/faqs/#dns_failover_do_i_need_to_adjust),
    /// you cannot change this, therefore `ttl` has to be omitted in alias records.
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var main = new Aws.Elb.LoadBalancer("main", new Aws.Elb.LoadBalancerArgs
    ///         {
    ///             AvailabilityZones = 
    ///             {
    ///                 "us-east-1c",
    ///             },
    ///             Listeners = 
    ///             {
    ///                 new Aws.Elb.Inputs.LoadBalancerListenerArgs
    ///                 {
    ///                     InstancePort = 80,
    ///                     InstanceProtocol = "http",
    ///                     LbPort = 80,
    ///                     LbProtocol = "http",
    ///                 },
    ///             },
    ///         });
    ///         var www = new Aws.Route53.Record("www", new Aws.Route53.RecordArgs
    ///         {
    ///             ZoneId = aws_route53_zone.Primary.Zone_id,
    ///             Name = "example.com",
    ///             Type = "A",
    ///             Aliases = 
    ///             {
    ///                 new Aws.Route53.Inputs.RecordAliasArgs
    ///                 {
    ///                     Name = main.DnsName,
    ///                     ZoneId = main.ZoneId,
    ///                     EvaluateTargetHealth = true,
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ### NS and SOA Record Management
    /// 
    /// When creating Route 53 zones, the `NS` and `SOA` records for the zone are automatically created. Enabling the `allow_overwrite` argument will allow managing these records in a single deployment without the requirement for `import`.
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var exampleZone = new Aws.Route53.Zone("exampleZone", new Aws.Route53.ZoneArgs
    ///         {
    ///         });
    ///         var exampleRecord = new Aws.Route53.Record("exampleRecord", new Aws.Route53.RecordArgs
    ///         {
    ///             AllowOverwrite = true,
    ///             Name = "test.example.com",
    ///             Ttl = 30,
    ///             Type = "NS",
    ///             ZoneId = exampleZone.ZoneId,
    ///             Records = 
    ///             {
    ///                 exampleZone.NameServers.Apply(nameServers =&gt; nameServers[0]),
    ///                 exampleZone.NameServers.Apply(nameServers =&gt; nameServers[1]),
    ///                 exampleZone.NameServers.Apply(nameServers =&gt; nameServers[2]),
    ///                 exampleZone.NameServers.Apply(nameServers =&gt; nameServers[3]),
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class Record : Pulumi.CustomResource
    {
        /// <summary>
        /// An alias block. Conflicts with `ttl` &amp; `records`.
        /// Alias record documented below.
        /// </summary>
        [Output("aliases")]
        public Output<ImmutableArray<Outputs.RecordAlias>> Aliases { get; private set; } = null!;

        /// <summary>
        /// Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
        /// </summary>
        [Output("allowOverwrite")]
        public Output<bool> AllowOverwrite { get; private set; } = null!;

        /// <summary>
        /// A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
        /// </summary>
        [Output("failoverRoutingPolicies")]
        public Output<ImmutableArray<Outputs.RecordFailoverRoutingPolicy>> FailoverRoutingPolicies { get; private set; } = null!;

        /// <summary>
        /// [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
        /// </summary>
        [Output("fqdn")]
        public Output<string> Fqdn { get; private set; } = null!;

        /// <summary>
        /// A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
        /// </summary>
        [Output("geolocationRoutingPolicies")]
        public Output<ImmutableArray<Outputs.RecordGeolocationRoutingPolicy>> GeolocationRoutingPolicies { get; private set; } = null!;

        /// <summary>
        /// The health check the record should be associated with.
        /// </summary>
        [Output("healthCheckId")]
        public Output<string?> HealthCheckId { get; private set; } = null!;

        /// <summary>
        /// A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
        /// </summary>
        [Output("latencyRoutingPolicies")]
        public Output<ImmutableArray<Outputs.RecordLatencyRoutingPolicy>> LatencyRoutingPolicies { get; private set; } = null!;

        /// <summary>
        /// Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
        /// </summary>
        [Output("multivalueAnswerRoutingPolicy")]
        public Output<bool?> MultivalueAnswerRoutingPolicy { get; private set; } = null!;

        /// <summary>
        /// DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
        /// </summary>
        [Output("records")]
        public Output<ImmutableArray<string>> Records { get; private set; } = null!;

        /// <summary>
        /// Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
        /// </summary>
        [Output("setIdentifier")]
        public Output<string?> SetIdentifier { get; private set; } = null!;

        /// <summary>
        /// The TTL of the record.
        /// </summary>
        [Output("ttl")]
        public Output<int?> Ttl { get; private set; } = null!;

        /// <summary>
        /// `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;

        /// <summary>
        /// A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
        /// </summary>
        [Output("weightedRoutingPolicies")]
        public Output<ImmutableArray<Outputs.RecordWeightedRoutingPolicy>> WeightedRoutingPolicies { get; private set; } = null!;

        /// <summary>
        /// Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See `resource_elb.zone_id` for example.
        /// </summary>
        [Output("zoneId")]
        public Output<string> ZoneId { get; private set; } = null!;


        /// <summary>
        /// Create a Record resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Record(string name, RecordArgs args, CustomResourceOptions? options = null)
            : base("aws:route53/record:Record", name, args ?? new RecordArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Record(string name, Input<string> id, RecordState? state = null, CustomResourceOptions? options = null)
            : base("aws:route53/record:Record", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Record resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Record Get(string name, Input<string> id, RecordState? state = null, CustomResourceOptions? options = null)
        {
            return new Record(name, id, state, options);
        }
    }

    public sealed class RecordArgs : Pulumi.ResourceArgs
    {
        [Input("aliases")]
        private InputList<Inputs.RecordAliasArgs>? _aliases;

        /// <summary>
        /// An alias block. Conflicts with `ttl` &amp; `records`.
        /// Alias record documented below.
        /// </summary>
        public InputList<Inputs.RecordAliasArgs> Aliases
        {
            get => _aliases ?? (_aliases = new InputList<Inputs.RecordAliasArgs>());
            set => _aliases = value;
        }

        /// <summary>
        /// Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
        /// </summary>
        [Input("allowOverwrite")]
        public Input<bool>? AllowOverwrite { get; set; }

        [Input("failoverRoutingPolicies")]
        private InputList<Inputs.RecordFailoverRoutingPolicyArgs>? _failoverRoutingPolicies;

        /// <summary>
        /// A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
        /// </summary>
        public InputList<Inputs.RecordFailoverRoutingPolicyArgs> FailoverRoutingPolicies
        {
            get => _failoverRoutingPolicies ?? (_failoverRoutingPolicies = new InputList<Inputs.RecordFailoverRoutingPolicyArgs>());
            set => _failoverRoutingPolicies = value;
        }

        [Input("geolocationRoutingPolicies")]
        private InputList<Inputs.RecordGeolocationRoutingPolicyArgs>? _geolocationRoutingPolicies;

        /// <summary>
        /// A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
        /// </summary>
        public InputList<Inputs.RecordGeolocationRoutingPolicyArgs> GeolocationRoutingPolicies
        {
            get => _geolocationRoutingPolicies ?? (_geolocationRoutingPolicies = new InputList<Inputs.RecordGeolocationRoutingPolicyArgs>());
            set => _geolocationRoutingPolicies = value;
        }

        /// <summary>
        /// The health check the record should be associated with.
        /// </summary>
        [Input("healthCheckId")]
        public Input<string>? HealthCheckId { get; set; }

        [Input("latencyRoutingPolicies")]
        private InputList<Inputs.RecordLatencyRoutingPolicyArgs>? _latencyRoutingPolicies;

        /// <summary>
        /// A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
        /// </summary>
        public InputList<Inputs.RecordLatencyRoutingPolicyArgs> LatencyRoutingPolicies
        {
            get => _latencyRoutingPolicies ?? (_latencyRoutingPolicies = new InputList<Inputs.RecordLatencyRoutingPolicyArgs>());
            set => _latencyRoutingPolicies = value;
        }

        /// <summary>
        /// Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
        /// </summary>
        [Input("multivalueAnswerRoutingPolicy")]
        public Input<bool>? MultivalueAnswerRoutingPolicy { get; set; }

        /// <summary>
        /// DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("records")]
        private InputList<string>? _records;

        /// <summary>
        /// A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
        /// </summary>
        public InputList<string> Records
        {
            get => _records ?? (_records = new InputList<string>());
            set => _records = value;
        }

        /// <summary>
        /// Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
        /// </summary>
        [Input("setIdentifier")]
        public Input<string>? SetIdentifier { get; set; }

        /// <summary>
        /// The TTL of the record.
        /// </summary>
        [Input("ttl")]
        public Input<int>? Ttl { get; set; }

        /// <summary>
        /// `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        [Input("weightedRoutingPolicies")]
        private InputList<Inputs.RecordWeightedRoutingPolicyArgs>? _weightedRoutingPolicies;

        /// <summary>
        /// A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
        /// </summary>
        public InputList<Inputs.RecordWeightedRoutingPolicyArgs> WeightedRoutingPolicies
        {
            get => _weightedRoutingPolicies ?? (_weightedRoutingPolicies = new InputList<Inputs.RecordWeightedRoutingPolicyArgs>());
            set => _weightedRoutingPolicies = value;
        }

        /// <summary>
        /// Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See `resource_elb.zone_id` for example.
        /// </summary>
        [Input("zoneId", required: true)]
        public Input<string> ZoneId { get; set; } = null!;

        public RecordArgs()
        {
        }
    }

    public sealed class RecordState : Pulumi.ResourceArgs
    {
        [Input("aliases")]
        private InputList<Inputs.RecordAliasGetArgs>? _aliases;

        /// <summary>
        /// An alias block. Conflicts with `ttl` &amp; `records`.
        /// Alias record documented below.
        /// </summary>
        public InputList<Inputs.RecordAliasGetArgs> Aliases
        {
            get => _aliases ?? (_aliases = new InputList<Inputs.RecordAliasGetArgs>());
            set => _aliases = value;
        }

        /// <summary>
        /// Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
        /// </summary>
        [Input("allowOverwrite")]
        public Input<bool>? AllowOverwrite { get; set; }

        [Input("failoverRoutingPolicies")]
        private InputList<Inputs.RecordFailoverRoutingPolicyGetArgs>? _failoverRoutingPolicies;

        /// <summary>
        /// A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
        /// </summary>
        public InputList<Inputs.RecordFailoverRoutingPolicyGetArgs> FailoverRoutingPolicies
        {
            get => _failoverRoutingPolicies ?? (_failoverRoutingPolicies = new InputList<Inputs.RecordFailoverRoutingPolicyGetArgs>());
            set => _failoverRoutingPolicies = value;
        }

        /// <summary>
        /// [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
        /// </summary>
        [Input("fqdn")]
        public Input<string>? Fqdn { get; set; }

        [Input("geolocationRoutingPolicies")]
        private InputList<Inputs.RecordGeolocationRoutingPolicyGetArgs>? _geolocationRoutingPolicies;

        /// <summary>
        /// A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
        /// </summary>
        public InputList<Inputs.RecordGeolocationRoutingPolicyGetArgs> GeolocationRoutingPolicies
        {
            get => _geolocationRoutingPolicies ?? (_geolocationRoutingPolicies = new InputList<Inputs.RecordGeolocationRoutingPolicyGetArgs>());
            set => _geolocationRoutingPolicies = value;
        }

        /// <summary>
        /// The health check the record should be associated with.
        /// </summary>
        [Input("healthCheckId")]
        public Input<string>? HealthCheckId { get; set; }

        [Input("latencyRoutingPolicies")]
        private InputList<Inputs.RecordLatencyRoutingPolicyGetArgs>? _latencyRoutingPolicies;

        /// <summary>
        /// A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
        /// </summary>
        public InputList<Inputs.RecordLatencyRoutingPolicyGetArgs> LatencyRoutingPolicies
        {
            get => _latencyRoutingPolicies ?? (_latencyRoutingPolicies = new InputList<Inputs.RecordLatencyRoutingPolicyGetArgs>());
            set => _latencyRoutingPolicies = value;
        }

        /// <summary>
        /// Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
        /// </summary>
        [Input("multivalueAnswerRoutingPolicy")]
        public Input<bool>? MultivalueAnswerRoutingPolicy { get; set; }

        /// <summary>
        /// DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("records")]
        private InputList<string>? _records;

        /// <summary>
        /// A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
        /// </summary>
        public InputList<string> Records
        {
            get => _records ?? (_records = new InputList<string>());
            set => _records = value;
        }

        /// <summary>
        /// Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
        /// </summary>
        [Input("setIdentifier")]
        public Input<string>? SetIdentifier { get; set; }

        /// <summary>
        /// The TTL of the record.
        /// </summary>
        [Input("ttl")]
        public Input<int>? Ttl { get; set; }

        /// <summary>
        /// `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        [Input("weightedRoutingPolicies")]
        private InputList<Inputs.RecordWeightedRoutingPolicyGetArgs>? _weightedRoutingPolicies;

        /// <summary>
        /// A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
        /// </summary>
        public InputList<Inputs.RecordWeightedRoutingPolicyGetArgs> WeightedRoutingPolicies
        {
            get => _weightedRoutingPolicies ?? (_weightedRoutingPolicies = new InputList<Inputs.RecordWeightedRoutingPolicyGetArgs>());
            set => _weightedRoutingPolicies = value;
        }

        /// <summary>
        /// Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See `resource_elb.zone_id` for example.
        /// </summary>
        [Input("zoneId")]
        public Input<string>? ZoneId { get; set; }

        public RecordState()
        {
        }
    }
}
