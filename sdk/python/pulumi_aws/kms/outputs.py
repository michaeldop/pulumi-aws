# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GrantConstraint',
    'GetSecretSecretResult',
    'GetSecretsSecretResult',
]

@pulumi.output_type
class GrantConstraint(dict):
    def __init__(__self__, *,
                 encryption_context_equals: Optional[Mapping[str, str]] = None,
                 encryption_context_subset: Optional[Mapping[str, str]] = None):
        """
        :param Mapping[str, str] encryption_context_equals: A list of key-value pairs that must match the encryption context in subsequent cryptographic operation requests. The grant allows the operation only when the encryption context in the request is the same as the encryption context specified in this constraint. Conflicts with `encryption_context_subset`.
        :param Mapping[str, str] encryption_context_subset: A list of key-value pairs that must be included in the encryption context of subsequent cryptographic operation requests. The grant allows the cryptographic operation only when the encryption context in the request includes the key-value pairs specified in this constraint, although it can include additional key-value pairs. Conflicts with `encryption_context_equals`.
        """
        if encryption_context_equals is not None:
            pulumi.set(__self__, "encryption_context_equals", encryption_context_equals)
        if encryption_context_subset is not None:
            pulumi.set(__self__, "encryption_context_subset", encryption_context_subset)

    @property
    @pulumi.getter(name="encryptionContextEquals")
    def encryption_context_equals(self) -> Optional[Mapping[str, str]]:
        """
        A list of key-value pairs that must match the encryption context in subsequent cryptographic operation requests. The grant allows the operation only when the encryption context in the request is the same as the encryption context specified in this constraint. Conflicts with `encryption_context_subset`.
        """
        return pulumi.get(self, "encryption_context_equals")

    @property
    @pulumi.getter(name="encryptionContextSubset")
    def encryption_context_subset(self) -> Optional[Mapping[str, str]]:
        """
        A list of key-value pairs that must be included in the encryption context of subsequent cryptographic operation requests. The grant allows the cryptographic operation only when the encryption context in the request includes the key-value pairs specified in this constraint, although it can include additional key-value pairs. Conflicts with `encryption_context_equals`.
        """
        return pulumi.get(self, "encryption_context_subset")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetSecretSecretResult(dict):
    def __init__(__self__, *,
                 name: str,
                 payload: str,
                 context: Optional[Mapping[str, str]] = None,
                 grant_tokens: Optional[List[str]] = None):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "payload", payload)
        if context is not None:
            pulumi.set(__self__, "context", context)
        if grant_tokens is not None:
            pulumi.set(__self__, "grant_tokens", grant_tokens)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def payload(self) -> str:
        return pulumi.get(self, "payload")

    @property
    @pulumi.getter
    def context(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "context")

    @property
    @pulumi.getter(name="grantTokens")
    def grant_tokens(self) -> Optional[List[str]]:
        return pulumi.get(self, "grant_tokens")


@pulumi.output_type
class GetSecretsSecretResult(dict):
    def __init__(__self__, *,
                 name: str,
                 payload: str,
                 context: Optional[Mapping[str, str]] = None,
                 grant_tokens: Optional[List[str]] = None):
        """
        :param str name: The name to export this secret under in the attributes.
        :param str payload: Base64 encoded payload, as returned from a KMS encrypt operation.
        :param Mapping[str, str] context: An optional mapping that makes up the Encryption Context for the secret.
        :param List[str] grant_tokens: An optional list of Grant Tokens for the secret.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "payload", payload)
        if context is not None:
            pulumi.set(__self__, "context", context)
        if grant_tokens is not None:
            pulumi.set(__self__, "grant_tokens", grant_tokens)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name to export this secret under in the attributes.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def payload(self) -> str:
        """
        Base64 encoded payload, as returned from a KMS encrypt operation.
        """
        return pulumi.get(self, "payload")

    @property
    @pulumi.getter
    def context(self) -> Optional[Mapping[str, str]]:
        """
        An optional mapping that makes up the Encryption Context for the secret.
        """
        return pulumi.get(self, "context")

    @property
    @pulumi.getter(name="grantTokens")
    def grant_tokens(self) -> Optional[List[str]]:
        """
        An optional list of Grant Tokens for the secret.
        """
        return pulumi.get(self, "grant_tokens")


