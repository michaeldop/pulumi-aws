# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['SshKey']


class SshKey(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encoding: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Uploads an SSH public key and associates it with the specified IAM user.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        user_user = aws.iam.User("userUser", path="/")
        user_ssh_key = aws.iam.SshKey("userSshKey",
            username=user_user.name,
            encoding="SSH",
            public_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD3F6tyPEFEzV0LX3X8BsXdMsQz1x2cEikKDEY0aIj41qgxMCP/iteneqXSIFZBp5vizPvaoIR3Um9xK7PGoW8giupGn+EPuxIA4cDM4vzOqOkiMPhz5XK0whEjkVzTo4+S0puvDZuwIsdiW9mxhJc7tgBNL0cYlWSYVkz4G/fslNfRPW5mYAM49f4fhtxPb5ok4Q2Lg9dPKVHO/Bgeu5woMc7RY0p1ej6D4CKFE6lymSDJpW0YHX/wqE9+cfEauh7xZcG0q9t2ta6F6fmX0agvpFyZo8aFbXeUBr7osSCJNgvavWbM/06niWrOvYX2xwWdhXmXSrbX8ZbabVohBK41 mytest@mydomain.com")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] encoding: Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use `SSH`. To retrieve the public key in PEM format, use `PEM`.
        :param pulumi.Input[str] public_key: The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.
        :param pulumi.Input[str] status: The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is `active`.
        :param pulumi.Input[str] username: The name of the IAM user to associate the SSH public key with.
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

            if encoding is None:
                raise TypeError("Missing required property 'encoding'")
            __props__['encoding'] = encoding
            if public_key is None:
                raise TypeError("Missing required property 'public_key'")
            __props__['public_key'] = public_key
            __props__['status'] = status
            if username is None:
                raise TypeError("Missing required property 'username'")
            __props__['username'] = username
            __props__['fingerprint'] = None
            __props__['ssh_public_key_id'] = None
        super(SshKey, __self__).__init__(
            'aws:iam/sshKey:SshKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            encoding: Optional[pulumi.Input[str]] = None,
            fingerprint: Optional[pulumi.Input[str]] = None,
            public_key: Optional[pulumi.Input[str]] = None,
            ssh_public_key_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'SshKey':
        """
        Get an existing SshKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] encoding: Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use `SSH`. To retrieve the public key in PEM format, use `PEM`.
        :param pulumi.Input[str] fingerprint: The MD5 message digest of the SSH public key.
        :param pulumi.Input[str] public_key: The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.
        :param pulumi.Input[str] ssh_public_key_id: The unique identifier for the SSH public key.
        :param pulumi.Input[str] status: The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is `active`.
        :param pulumi.Input[str] username: The name of the IAM user to associate the SSH public key with.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["encoding"] = encoding
        __props__["fingerprint"] = fingerprint
        __props__["public_key"] = public_key
        __props__["ssh_public_key_id"] = ssh_public_key_id
        __props__["status"] = status
        __props__["username"] = username
        return SshKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def encoding(self) -> pulumi.Output[str]:
        """
        Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use `SSH`. To retrieve the public key in PEM format, use `PEM`.
        """
        return pulumi.get(self, "encoding")

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        """
        The MD5 message digest of the SSH public key.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[str]:
        """
        The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter(name="sshPublicKeyId")
    def ssh_public_key_id(self) -> pulumi.Output[str]:
        """
        The unique identifier for the SSH public key.
        """
        return pulumi.get(self, "ssh_public_key_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is `active`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        The name of the IAM user to associate the SSH public key with.
        """
        return pulumi.get(self, "username")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

