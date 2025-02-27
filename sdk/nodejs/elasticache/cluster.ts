// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides an ElastiCache Cluster resource, which manages a Memcached cluster or Redis instance.
 * For working with Redis (Cluster Mode Enabled) replication groups, see the
 * `aws.elasticache.ReplicationGroup` resource.
 *
 * > **Note:** When you change an attribute, such as `nodeType`, by default
 * it is applied in the next maintenance window. Because of this, this provider may report
 * a difference in its planning phase because the actual modification has not yet taken
 * place. You can use the `applyImmediately` flag to instruct the service to apply the
 * change immediately. Using `applyImmediately` can result in a brief downtime as the server reboots.
 * See the AWS Docs on [Modifying an ElastiCache Cache Cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Clusters.Modify.html) for more information.
 *
 * ## Example Usage
 * ### Memcached Cluster
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const example = new aws.elasticache.Cluster("example", {
 *     engine: "memcached",
 *     nodeType: "cache.m4.large",
 *     numCacheNodes: 2,
 *     parameterGroupName: "default.memcached1.4",
 *     port: 11211,
 * });
 * ```
 * ### Redis Instance
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const example = new aws.elasticache.Cluster("example", {
 *     engine: "redis",
 *     engineVersion: "3.2.10",
 *     nodeType: "cache.m4.large",
 *     numCacheNodes: 1,
 *     parameterGroupName: "default.redis3.2",
 *     port: 6379,
 * });
 * ```
 * ### Redis Cluster Mode Disabled Read Replica Instance
 *
 * These inherit their settings from the replication group.
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const replica = new aws.elasticache.Cluster("replica", {replicationGroupId: aws_elasticache_replication_group.example.id});
 * ```
 */
export class Cluster extends pulumi.CustomResource {
    /**
     * Get an existing Cluster resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterState, opts?: pulumi.CustomResourceOptions): Cluster {
        return new Cluster(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:elasticache/cluster:Cluster';

    /**
     * Returns true if the given object is an instance of Cluster.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Cluster {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Cluster.__pulumiType;
    }

    /**
     * Specifies whether any database modifications
     * are applied immediately, or during the next maintenance window. Default is
     * `false`. See [Amazon ElastiCache Documentation for more information.](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheCluster.html)
     * (Available since v0.6.0)
     */
    public readonly applyImmediately!: pulumi.Output<boolean>;
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferredAvailabilityZones` instead. Default: System chosen Availability Zone.
     */
    public readonly availabilityZone!: pulumi.Output<string>;
    /**
     * Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `numCacheNodes` must be greater than `1`
     */
    public readonly azMode!: pulumi.Output<string>;
    /**
     * List of node objects including `id`, `address`, `port` and `availabilityZone`.
     * Referenceable e.g. as `${aws_elasticache_cluster.bar.cache_nodes.0.address}`
     */
    public /*out*/ readonly cacheNodes!: pulumi.Output<outputs.elasticache.ClusterCacheNode[]>;
    /**
     * (Memcached only) The DNS name of the cache cluster without the port appended.
     */
    public /*out*/ readonly clusterAddress!: pulumi.Output<string>;
    /**
     * Group identifier. ElastiCache converts
     * this name to lowercase
     */
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * (Memcached only) The configuration endpoint to allow host discovery.
     */
    public /*out*/ readonly configurationEndpoint!: pulumi.Output<string>;
    /**
     * Name of the cache engine to be used for this cache cluster.
     * Valid values for this parameter are `memcached` or `redis`
     */
    public readonly engine!: pulumi.Output<string>;
    /**
     * Version number of the cache engine to be used.
     * See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
     * in the AWS Documentation center for supported versions
     */
    public readonly engineVersion!: pulumi.Output<string>;
    /**
     * Specifies the weekly time range for when maintenance
     * on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
     * The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
     */
    public readonly maintenanceWindow!: pulumi.Output<string>;
    /**
     * The compute and memory capacity of the nodes. See
     * [Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
     * supported node types
     */
    public readonly nodeType!: pulumi.Output<string>;
    /**
     * An Amazon Resource Name (ARN) of an
     * SNS topic to send ElastiCache notifications to. Example:
     * `arn:aws:sns:us-east-1:012345678999:my_sns_topic`
     */
    public readonly notificationTopicArn!: pulumi.Output<string | undefined>;
    /**
     * The initial number of cache nodes that the
     * cache cluster will have. For Redis, this value must be 1. For Memcache, this
     * value must be between 1 and 20. If this number is reduced on subsequent runs,
     * the highest numbered nodes will be removed.
     */
    public readonly numCacheNodes!: pulumi.Output<number>;
    /**
     * Name of the parameter group to associate
     * with this cache cluster
     */
    public readonly parameterGroupName!: pulumi.Output<string>;
    /**
     * The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replicationGroupId`.
     */
    public readonly port!: pulumi.Output<number>;
    /**
     * A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `numCacheNodes`. If you want all the nodes in the same Availability Zone, use `availabilityZone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
     */
    public readonly preferredAvailabilityZones!: pulumi.Output<string[] | undefined>;
    /**
     * The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
     */
    public readonly replicationGroupId!: pulumi.Output<string>;
    /**
     * One or more VPC security groups associated
     * with the cache cluster
     */
    public readonly securityGroupIds!: pulumi.Output<string[]>;
    /**
     * List of security group
     * names to associate with this cache cluster
     */
    public readonly securityGroupNames!: pulumi.Output<string[]>;
    /**
     * A single-element string list containing an
     * Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
     * Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
     */
    public readonly snapshotArns!: pulumi.Output<string[] | undefined>;
    /**
     * The name of a snapshot from which to restore data into the new node group.  Changing the `snapshotName` forces a new resource.
     */
    public readonly snapshotName!: pulumi.Output<string | undefined>;
    /**
     * The number of days for which ElastiCache will
     * retain automatic cache cluster snapshots before deleting them. For example, if you set
     * SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
     * before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
     * Please note that setting a `snapshotRetentionLimit` is not supported on cache.t1.micro or cache.t2.* cache nodes
     */
    public readonly snapshotRetentionLimit!: pulumi.Output<number | undefined>;
    /**
     * The daily time range (in UTC) during which ElastiCache will
     * begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
     */
    public readonly snapshotWindow!: pulumi.Output<string>;
    /**
     * Name of the subnet group to be used
     * for the cache cluster.
     */
    public readonly subnetGroupName!: pulumi.Output<string>;
    /**
     * A map of tags to assign to the resource
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;

    /**
     * Create a Cluster resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ClusterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ClusterArgs | ClusterState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ClusterState | undefined;
            inputs["applyImmediately"] = state ? state.applyImmediately : undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["availabilityZone"] = state ? state.availabilityZone : undefined;
            inputs["azMode"] = state ? state.azMode : undefined;
            inputs["cacheNodes"] = state ? state.cacheNodes : undefined;
            inputs["clusterAddress"] = state ? state.clusterAddress : undefined;
            inputs["clusterId"] = state ? state.clusterId : undefined;
            inputs["configurationEndpoint"] = state ? state.configurationEndpoint : undefined;
            inputs["engine"] = state ? state.engine : undefined;
            inputs["engineVersion"] = state ? state.engineVersion : undefined;
            inputs["maintenanceWindow"] = state ? state.maintenanceWindow : undefined;
            inputs["nodeType"] = state ? state.nodeType : undefined;
            inputs["notificationTopicArn"] = state ? state.notificationTopicArn : undefined;
            inputs["numCacheNodes"] = state ? state.numCacheNodes : undefined;
            inputs["parameterGroupName"] = state ? state.parameterGroupName : undefined;
            inputs["port"] = state ? state.port : undefined;
            inputs["preferredAvailabilityZones"] = state ? state.preferredAvailabilityZones : undefined;
            inputs["replicationGroupId"] = state ? state.replicationGroupId : undefined;
            inputs["securityGroupIds"] = state ? state.securityGroupIds : undefined;
            inputs["securityGroupNames"] = state ? state.securityGroupNames : undefined;
            inputs["snapshotArns"] = state ? state.snapshotArns : undefined;
            inputs["snapshotName"] = state ? state.snapshotName : undefined;
            inputs["snapshotRetentionLimit"] = state ? state.snapshotRetentionLimit : undefined;
            inputs["snapshotWindow"] = state ? state.snapshotWindow : undefined;
            inputs["subnetGroupName"] = state ? state.subnetGroupName : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as ClusterArgs | undefined;
            inputs["applyImmediately"] = args ? args.applyImmediately : undefined;
            inputs["availabilityZone"] = args ? args.availabilityZone : undefined;
            inputs["azMode"] = args ? args.azMode : undefined;
            inputs["clusterId"] = args ? args.clusterId : undefined;
            inputs["engine"] = args ? args.engine : undefined;
            inputs["engineVersion"] = args ? args.engineVersion : undefined;
            inputs["maintenanceWindow"] = args ? args.maintenanceWindow : undefined;
            inputs["nodeType"] = args ? args.nodeType : undefined;
            inputs["notificationTopicArn"] = args ? args.notificationTopicArn : undefined;
            inputs["numCacheNodes"] = args ? args.numCacheNodes : undefined;
            inputs["parameterGroupName"] = args ? args.parameterGroupName : undefined;
            inputs["port"] = args ? args.port : undefined;
            inputs["preferredAvailabilityZones"] = args ? args.preferredAvailabilityZones : undefined;
            inputs["replicationGroupId"] = args ? args.replicationGroupId : undefined;
            inputs["securityGroupIds"] = args ? args.securityGroupIds : undefined;
            inputs["securityGroupNames"] = args ? args.securityGroupNames : undefined;
            inputs["snapshotArns"] = args ? args.snapshotArns : undefined;
            inputs["snapshotName"] = args ? args.snapshotName : undefined;
            inputs["snapshotRetentionLimit"] = args ? args.snapshotRetentionLimit : undefined;
            inputs["snapshotWindow"] = args ? args.snapshotWindow : undefined;
            inputs["subnetGroupName"] = args ? args.subnetGroupName : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["cacheNodes"] = undefined /*out*/;
            inputs["clusterAddress"] = undefined /*out*/;
            inputs["configurationEndpoint"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Cluster.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Cluster resources.
 */
export interface ClusterState {
    /**
     * Specifies whether any database modifications
     * are applied immediately, or during the next maintenance window. Default is
     * `false`. See [Amazon ElastiCache Documentation for more information.](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheCluster.html)
     * (Available since v0.6.0)
     */
    readonly applyImmediately?: pulumi.Input<boolean>;
    readonly arn?: pulumi.Input<string>;
    /**
     * The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferredAvailabilityZones` instead. Default: System chosen Availability Zone.
     */
    readonly availabilityZone?: pulumi.Input<string>;
    /**
     * Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `numCacheNodes` must be greater than `1`
     */
    readonly azMode?: pulumi.Input<string>;
    /**
     * List of node objects including `id`, `address`, `port` and `availabilityZone`.
     * Referenceable e.g. as `${aws_elasticache_cluster.bar.cache_nodes.0.address}`
     */
    readonly cacheNodes?: pulumi.Input<pulumi.Input<inputs.elasticache.ClusterCacheNode>[]>;
    /**
     * (Memcached only) The DNS name of the cache cluster without the port appended.
     */
    readonly clusterAddress?: pulumi.Input<string>;
    /**
     * Group identifier. ElastiCache converts
     * this name to lowercase
     */
    readonly clusterId?: pulumi.Input<string>;
    /**
     * (Memcached only) The configuration endpoint to allow host discovery.
     */
    readonly configurationEndpoint?: pulumi.Input<string>;
    /**
     * Name of the cache engine to be used for this cache cluster.
     * Valid values for this parameter are `memcached` or `redis`
     */
    readonly engine?: pulumi.Input<string>;
    /**
     * Version number of the cache engine to be used.
     * See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
     * in the AWS Documentation center for supported versions
     */
    readonly engineVersion?: pulumi.Input<string>;
    /**
     * Specifies the weekly time range for when maintenance
     * on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
     * The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
     */
    readonly maintenanceWindow?: pulumi.Input<string>;
    /**
     * The compute and memory capacity of the nodes. See
     * [Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
     * supported node types
     */
    readonly nodeType?: pulumi.Input<string>;
    /**
     * An Amazon Resource Name (ARN) of an
     * SNS topic to send ElastiCache notifications to. Example:
     * `arn:aws:sns:us-east-1:012345678999:my_sns_topic`
     */
    readonly notificationTopicArn?: pulumi.Input<string>;
    /**
     * The initial number of cache nodes that the
     * cache cluster will have. For Redis, this value must be 1. For Memcache, this
     * value must be between 1 and 20. If this number is reduced on subsequent runs,
     * the highest numbered nodes will be removed.
     */
    readonly numCacheNodes?: pulumi.Input<number>;
    /**
     * Name of the parameter group to associate
     * with this cache cluster
     */
    readonly parameterGroupName?: pulumi.Input<string>;
    /**
     * The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replicationGroupId`.
     */
    readonly port?: pulumi.Input<number>;
    /**
     * A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `numCacheNodes`. If you want all the nodes in the same Availability Zone, use `availabilityZone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
     */
    readonly preferredAvailabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
     */
    readonly replicationGroupId?: pulumi.Input<string>;
    /**
     * One or more VPC security groups associated
     * with the cache cluster
     */
    readonly securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * List of security group
     * names to associate with this cache cluster
     */
    readonly securityGroupNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A single-element string list containing an
     * Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
     * Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
     */
    readonly snapshotArns?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of a snapshot from which to restore data into the new node group.  Changing the `snapshotName` forces a new resource.
     */
    readonly snapshotName?: pulumi.Input<string>;
    /**
     * The number of days for which ElastiCache will
     * retain automatic cache cluster snapshots before deleting them. For example, if you set
     * SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
     * before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
     * Please note that setting a `snapshotRetentionLimit` is not supported on cache.t1.micro or cache.t2.* cache nodes
     */
    readonly snapshotRetentionLimit?: pulumi.Input<number>;
    /**
     * The daily time range (in UTC) during which ElastiCache will
     * begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
     */
    readonly snapshotWindow?: pulumi.Input<string>;
    /**
     * Name of the subnet group to be used
     * for the cache cluster.
     */
    readonly subnetGroupName?: pulumi.Input<string>;
    /**
     * A map of tags to assign to the resource
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The set of arguments for constructing a Cluster resource.
 */
export interface ClusterArgs {
    /**
     * Specifies whether any database modifications
     * are applied immediately, or during the next maintenance window. Default is
     * `false`. See [Amazon ElastiCache Documentation for more information.](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheCluster.html)
     * (Available since v0.6.0)
     */
    readonly applyImmediately?: pulumi.Input<boolean>;
    /**
     * The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferredAvailabilityZones` instead. Default: System chosen Availability Zone.
     */
    readonly availabilityZone?: pulumi.Input<string>;
    /**
     * Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `numCacheNodes` must be greater than `1`
     */
    readonly azMode?: pulumi.Input<string>;
    /**
     * Group identifier. ElastiCache converts
     * this name to lowercase
     */
    readonly clusterId?: pulumi.Input<string>;
    /**
     * Name of the cache engine to be used for this cache cluster.
     * Valid values for this parameter are `memcached` or `redis`
     */
    readonly engine?: pulumi.Input<string>;
    /**
     * Version number of the cache engine to be used.
     * See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
     * in the AWS Documentation center for supported versions
     */
    readonly engineVersion?: pulumi.Input<string>;
    /**
     * Specifies the weekly time range for when maintenance
     * on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
     * The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
     */
    readonly maintenanceWindow?: pulumi.Input<string>;
    /**
     * The compute and memory capacity of the nodes. See
     * [Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
     * supported node types
     */
    readonly nodeType?: pulumi.Input<string>;
    /**
     * An Amazon Resource Name (ARN) of an
     * SNS topic to send ElastiCache notifications to. Example:
     * `arn:aws:sns:us-east-1:012345678999:my_sns_topic`
     */
    readonly notificationTopicArn?: pulumi.Input<string>;
    /**
     * The initial number of cache nodes that the
     * cache cluster will have. For Redis, this value must be 1. For Memcache, this
     * value must be between 1 and 20. If this number is reduced on subsequent runs,
     * the highest numbered nodes will be removed.
     */
    readonly numCacheNodes?: pulumi.Input<number>;
    /**
     * Name of the parameter group to associate
     * with this cache cluster
     */
    readonly parameterGroupName?: pulumi.Input<string>;
    /**
     * The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replicationGroupId`.
     */
    readonly port?: pulumi.Input<number>;
    /**
     * A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `numCacheNodes`. If you want all the nodes in the same Availability Zone, use `availabilityZone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
     */
    readonly preferredAvailabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
     */
    readonly replicationGroupId?: pulumi.Input<string>;
    /**
     * One or more VPC security groups associated
     * with the cache cluster
     */
    readonly securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * List of security group
     * names to associate with this cache cluster
     */
    readonly securityGroupNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A single-element string list containing an
     * Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
     * Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
     */
    readonly snapshotArns?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of a snapshot from which to restore data into the new node group.  Changing the `snapshotName` forces a new resource.
     */
    readonly snapshotName?: pulumi.Input<string>;
    /**
     * The number of days for which ElastiCache will
     * retain automatic cache cluster snapshots before deleting them. For example, if you set
     * SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
     * before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
     * Please note that setting a `snapshotRetentionLimit` is not supported on cache.t1.micro or cache.t2.* cache nodes
     */
    readonly snapshotRetentionLimit?: pulumi.Input<number>;
    /**
     * The daily time range (in UTC) during which ElastiCache will
     * begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
     */
    readonly snapshotWindow?: pulumi.Input<string>;
    /**
     * Name of the subnet group to be used
     * for the cache cluster.
     */
    readonly subnetGroupName?: pulumi.Input<string>;
    /**
     * A map of tags to assign to the resource
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
