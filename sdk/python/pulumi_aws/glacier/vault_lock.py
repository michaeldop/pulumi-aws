# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['VaultLock']


class VaultLock(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 complete_lock: Optional[pulumi.Input[bool]] = None,
                 ignore_deletion_error: Optional[pulumi.Input[bool]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 vault_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Glacier Vault Lock. You can refer to the [Glacier Developer Guide](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html) for a full explanation of the Glacier Vault Lock functionality.

        > **NOTE:** This resource allows you to test Glacier Vault Lock policies by setting the `complete_lock` argument to `false`. When testing policies in this manner, the Glacier Vault Lock automatically expires after 24 hours and this provider will show this resource as needing recreation after that time. To permanently apply the policy, set the `complete_lock` argument to `true`. When changing `complete_lock` to `true`, it is expected the resource will show as recreating.

        !> **WARNING:** Once a Glacier Vault Lock is completed, it is immutable. The deletion of the Glacier Vault Lock is not be possible and attempting to remove it from this provider will return an error. Set the `ignore_deletion_error` argument to `true` and apply this configuration before attempting to delete this resource via this provider or remove this resource from this provider's management.

        ## Example Usage
        ### Testing Glacier Vault Lock Policy

        ```python
        import pulumi
        import pulumi_aws as aws

        example_vault = aws.glacier.Vault("exampleVault")
        example_policy_document = example_vault.arn.apply(lambda arn: aws.iam.get_policy_document(statements=[aws.iam.GetPolicyDocumentStatementArgs(
            actions=["glacier:DeleteArchive"],
            effect="Deny",
            resources=[arn],
            conditions=[aws.iam.GetPolicyDocumentStatementConditionArgs(
                test="NumericLessThanEquals",
                variable="glacier:ArchiveAgeinDays",
                values=["365"],
            )],
        )]))
        example_vault_lock = aws.glacier.VaultLock("exampleVaultLock",
            complete_lock=False,
            policy=example_policy_document.json,
            vault_name=example_vault.name)
        ```
        ### Permanently Applying Glacier Vault Lock Policy

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glacier.VaultLock("example",
            complete_lock=True,
            policy=data["aws_iam_policy_document"]["example"]["json"],
            vault_name=aws_glacier_vault["example"]["name"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] complete_lock: Boolean whether to permanently apply this Glacier Lock Policy. Once completed, this cannot be undone. If set to `false`, the Glacier Lock Policy remains in a testing mode for 24 hours. After that time, the Glacier Lock Policy is automatically removed by Glacier and the this provider resource will show as needing recreation. Changing this from `false` to `true` will show as resource recreation, which is expected. Changing this from `true` to `false` is not possible unless the Glacier Vault is recreated at the same time.
        :param pulumi.Input[bool] ignore_deletion_error: Allow this provider to ignore the error returned when attempting to delete the Glacier Lock Policy. This can be used to delete or recreate the Glacier Vault via this provider, for example, if the Glacier Vault Lock policy permits that action. This should only be used in conjunction with `complete_lock` being set to `true`.
        :param pulumi.Input[str] policy: JSON string containing the IAM policy to apply as the Glacier Vault Lock policy.
        :param pulumi.Input[str] vault_name: The name of the Glacier Vault.
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

            if complete_lock is None:
                raise TypeError("Missing required property 'complete_lock'")
            __props__['complete_lock'] = complete_lock
            __props__['ignore_deletion_error'] = ignore_deletion_error
            if policy is None:
                raise TypeError("Missing required property 'policy'")
            __props__['policy'] = policy
            if vault_name is None:
                raise TypeError("Missing required property 'vault_name'")
            __props__['vault_name'] = vault_name
        super(VaultLock, __self__).__init__(
            'aws:glacier/vaultLock:VaultLock',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            complete_lock: Optional[pulumi.Input[bool]] = None,
            ignore_deletion_error: Optional[pulumi.Input[bool]] = None,
            policy: Optional[pulumi.Input[str]] = None,
            vault_name: Optional[pulumi.Input[str]] = None) -> 'VaultLock':
        """
        Get an existing VaultLock resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] complete_lock: Boolean whether to permanently apply this Glacier Lock Policy. Once completed, this cannot be undone. If set to `false`, the Glacier Lock Policy remains in a testing mode for 24 hours. After that time, the Glacier Lock Policy is automatically removed by Glacier and the this provider resource will show as needing recreation. Changing this from `false` to `true` will show as resource recreation, which is expected. Changing this from `true` to `false` is not possible unless the Glacier Vault is recreated at the same time.
        :param pulumi.Input[bool] ignore_deletion_error: Allow this provider to ignore the error returned when attempting to delete the Glacier Lock Policy. This can be used to delete or recreate the Glacier Vault via this provider, for example, if the Glacier Vault Lock policy permits that action. This should only be used in conjunction with `complete_lock` being set to `true`.
        :param pulumi.Input[str] policy: JSON string containing the IAM policy to apply as the Glacier Vault Lock policy.
        :param pulumi.Input[str] vault_name: The name of the Glacier Vault.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["complete_lock"] = complete_lock
        __props__["ignore_deletion_error"] = ignore_deletion_error
        __props__["policy"] = policy
        __props__["vault_name"] = vault_name
        return VaultLock(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="completeLock")
    def complete_lock(self) -> pulumi.Output[bool]:
        """
        Boolean whether to permanently apply this Glacier Lock Policy. Once completed, this cannot be undone. If set to `false`, the Glacier Lock Policy remains in a testing mode for 24 hours. After that time, the Glacier Lock Policy is automatically removed by Glacier and the this provider resource will show as needing recreation. Changing this from `false` to `true` will show as resource recreation, which is expected. Changing this from `true` to `false` is not possible unless the Glacier Vault is recreated at the same time.
        """
        return pulumi.get(self, "complete_lock")

    @property
    @pulumi.getter(name="ignoreDeletionError")
    def ignore_deletion_error(self) -> pulumi.Output[Optional[bool]]:
        """
        Allow this provider to ignore the error returned when attempting to delete the Glacier Lock Policy. This can be used to delete or recreate the Glacier Vault via this provider, for example, if the Glacier Vault Lock policy permits that action. This should only be used in conjunction with `complete_lock` being set to `true`.
        """
        return pulumi.get(self, "ignore_deletion_error")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[str]:
        """
        JSON string containing the IAM policy to apply as the Glacier Vault Lock policy.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="vaultName")
    def vault_name(self) -> pulumi.Output[str]:
        """
        The name of the Glacier Vault.
        """
        return pulumi.get(self, "vault_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

