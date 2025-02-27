# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['VpcDhcpOptions']


class VpcDhcpOptions(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_name_servers: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 netbios_name_servers: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 netbios_node_type: Optional[pulumi.Input[str]] = None,
                 ntp_servers: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a VPC DHCP Options resource.

        ## Example Usage

        Basic usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        dns_resolver = aws.ec2.VpcDhcpOptions("dnsResolver", domain_name_servers=[
            "8.8.8.8",
            "8.8.4.4",
        ])
        ```

        Full usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        foo = aws.ec2.VpcDhcpOptions("foo",
            domain_name="service.consul",
            domain_name_servers=[
                "127.0.0.1",
                "10.0.0.2",
            ],
            netbios_name_servers=["127.0.0.1"],
            netbios_node_type="2",
            ntp_servers=["127.0.0.1"],
            tags={
                "Name": "foo-name",
            })
        ```
        ## Remarks

        * Notice that all arguments are optional but you have to specify at least one argument.
        * `domain_name_servers`, `netbios_name_servers`, `ntp_servers` are limited by AWS to maximum four servers only.
        * To actually use the DHCP Options Set you need to associate it to a VPC using `ec2.VpcDhcpOptionsAssociation`.
        * If you delete a DHCP Options Set, all VPCs using it will be associated to AWS's `default` DHCP Option Set.
        * In most cases unless you're configuring your own DNS you'll want to set `domain_name_servers` to `AmazonProvidedDNS`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: the suffix domain name to use by default when resolving non Fully Qualified Domain Names. In other words, this is what ends up being the `search` value in the `/etc/resolv.conf` file.
        :param pulumi.Input[List[pulumi.Input[str]]] domain_name_servers: List of name servers to configure in `/etc/resolv.conf`. If you want to use the default AWS nameservers you should set this to `AmazonProvidedDNS`.
        :param pulumi.Input[List[pulumi.Input[str]]] netbios_name_servers: List of NETBIOS name servers.
        :param pulumi.Input[str] netbios_node_type: The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).
        :param pulumi.Input[List[pulumi.Input[str]]] ntp_servers: List of NTP servers to configure.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['domain_name'] = domain_name
            __props__['domain_name_servers'] = domain_name_servers
            __props__['netbios_name_servers'] = netbios_name_servers
            __props__['netbios_node_type'] = netbios_node_type
            __props__['ntp_servers'] = ntp_servers
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['owner_id'] = None
        super(VpcDhcpOptions, __self__).__init__(
            'aws:ec2/vpcDhcpOptions:VpcDhcpOptions',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            domain_name_servers: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            netbios_name_servers: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            netbios_node_type: Optional[pulumi.Input[str]] = None,
            ntp_servers: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            owner_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'VpcDhcpOptions':
        """
        Get an existing VpcDhcpOptions resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the DHCP Options Set.
        :param pulumi.Input[str] domain_name: the suffix domain name to use by default when resolving non Fully Qualified Domain Names. In other words, this is what ends up being the `search` value in the `/etc/resolv.conf` file.
        :param pulumi.Input[List[pulumi.Input[str]]] domain_name_servers: List of name servers to configure in `/etc/resolv.conf`. If you want to use the default AWS nameservers you should set this to `AmazonProvidedDNS`.
        :param pulumi.Input[List[pulumi.Input[str]]] netbios_name_servers: List of NETBIOS name servers.
        :param pulumi.Input[str] netbios_node_type: The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).
        :param pulumi.Input[List[pulumi.Input[str]]] ntp_servers: List of NTP servers to configure.
        :param pulumi.Input[str] owner_id: The ID of the AWS account that owns the DHCP options set.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["domain_name"] = domain_name
        __props__["domain_name_servers"] = domain_name_servers
        __props__["netbios_name_servers"] = netbios_name_servers
        __props__["netbios_node_type"] = netbios_node_type
        __props__["ntp_servers"] = ntp_servers
        __props__["owner_id"] = owner_id
        __props__["tags"] = tags
        return VpcDhcpOptions(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the DHCP Options Set.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[Optional[str]]:
        """
        the suffix domain name to use by default when resolving non Fully Qualified Domain Names. In other words, this is what ends up being the `search` value in the `/etc/resolv.conf` file.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="domainNameServers")
    def domain_name_servers(self) -> pulumi.Output[Optional[List[str]]]:
        """
        List of name servers to configure in `/etc/resolv.conf`. If you want to use the default AWS nameservers you should set this to `AmazonProvidedDNS`.
        """
        return pulumi.get(self, "domain_name_servers")

    @property
    @pulumi.getter(name="netbiosNameServers")
    def netbios_name_servers(self) -> pulumi.Output[Optional[List[str]]]:
        """
        List of NETBIOS name servers.
        """
        return pulumi.get(self, "netbios_name_servers")

    @property
    @pulumi.getter(name="netbiosNodeType")
    def netbios_node_type(self) -> pulumi.Output[Optional[str]]:
        """
        The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).
        """
        return pulumi.get(self, "netbios_node_type")

    @property
    @pulumi.getter(name="ntpServers")
    def ntp_servers(self) -> pulumi.Output[Optional[List[str]]]:
        """
        List of NTP servers to configure.
        """
        return pulumi.get(self, "ntp_servers")

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[str]:
        """
        The ID of the AWS account that owns the DHCP options set.
        """
        return pulumi.get(self, "owner_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

