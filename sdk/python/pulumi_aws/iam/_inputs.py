# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetPolicyDocumentStatementArgs',
    'GetPolicyDocumentStatementConditionArgs',
    'GetPolicyDocumentStatementNotPrincipalArgs',
    'GetPolicyDocumentStatementPrincipalArgs',
]

@pulumi.input_type
class GetPolicyDocumentStatementArgs:
    def __init__(__self__, *,
                 actions: Optional[List[str]] = None,
                 conditions: Optional[List['GetPolicyDocumentStatementConditionArgs']] = None,
                 effect: Optional[str] = None,
                 not_actions: Optional[List[str]] = None,
                 not_principals: Optional[List['GetPolicyDocumentStatementNotPrincipalArgs']] = None,
                 not_resources: Optional[List[str]] = None,
                 principals: Optional[List['GetPolicyDocumentStatementPrincipalArgs']] = None,
                 resources: Optional[List[str]] = None,
                 sid: Optional[str] = None):
        """
        :param List[str] actions: A list of actions that this statement either allows
               or denies. For example, ``["ec2:RunInstances", "s3:*"]``.
        :param List['GetPolicyDocumentStatementConditionArgs'] conditions: A nested configuration block (described below)
               that defines a further, possibly-service-specific condition that constrains
               whether this statement applies.
        :param str effect: Either "Allow" or "Deny", to specify whether this
               statement allows or denies the given actions. The default is "Allow".
        :param List[str] not_actions: A list of actions that this statement does *not*
               apply to. Used to apply a policy statement to all actions *except* those
               listed.
        :param List['GetPolicyDocumentStatementNotPrincipalArgs'] not_principals: Like `principals` except gives principals that
               the statement does *not* apply to.
        :param List[str] not_resources: A list of resource ARNs that this statement
               does *not* apply to. Used to apply a policy statement to all resources
               *except* those listed.
        :param List['GetPolicyDocumentStatementPrincipalArgs'] principals: A nested configuration block (described below)
               specifying a principal (or principal pattern) to which this statement applies.
        :param List[str] resources: A list of resource ARNs that this statement applies
               to. This is required by AWS if used for an IAM policy.
        :param str sid: An ID for the policy statement.
        """
        if actions is not None:
            pulumi.set(__self__, "actions", actions)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if effect is not None:
            pulumi.set(__self__, "effect", effect)
        if not_actions is not None:
            pulumi.set(__self__, "not_actions", not_actions)
        if not_principals is not None:
            pulumi.set(__self__, "not_principals", not_principals)
        if not_resources is not None:
            pulumi.set(__self__, "not_resources", not_resources)
        if principals is not None:
            pulumi.set(__self__, "principals", principals)
        if resources is not None:
            pulumi.set(__self__, "resources", resources)
        if sid is not None:
            pulumi.set(__self__, "sid", sid)

    @property
    @pulumi.getter
    def actions(self) -> Optional[List[str]]:
        """
        A list of actions that this statement either allows
        or denies. For example, ``["ec2:RunInstances", "s3:*"]``.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: Optional[List[str]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def conditions(self) -> Optional[List['GetPolicyDocumentStatementConditionArgs']]:
        """
        A nested configuration block (described below)
        that defines a further, possibly-service-specific condition that constrains
        whether this statement applies.
        """
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: Optional[List['GetPolicyDocumentStatementConditionArgs']]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter
    def effect(self) -> Optional[str]:
        """
        Either "Allow" or "Deny", to specify whether this
        statement allows or denies the given actions. The default is "Allow".
        """
        return pulumi.get(self, "effect")

    @effect.setter
    def effect(self, value: Optional[str]):
        pulumi.set(self, "effect", value)

    @property
    @pulumi.getter(name="notActions")
    def not_actions(self) -> Optional[List[str]]:
        """
        A list of actions that this statement does *not*
        apply to. Used to apply a policy statement to all actions *except* those
        listed.
        """
        return pulumi.get(self, "not_actions")

    @not_actions.setter
    def not_actions(self, value: Optional[List[str]]):
        pulumi.set(self, "not_actions", value)

    @property
    @pulumi.getter(name="notPrincipals")
    def not_principals(self) -> Optional[List['GetPolicyDocumentStatementNotPrincipalArgs']]:
        """
        Like `principals` except gives principals that
        the statement does *not* apply to.
        """
        return pulumi.get(self, "not_principals")

    @not_principals.setter
    def not_principals(self, value: Optional[List['GetPolicyDocumentStatementNotPrincipalArgs']]):
        pulumi.set(self, "not_principals", value)

    @property
    @pulumi.getter(name="notResources")
    def not_resources(self) -> Optional[List[str]]:
        """
        A list of resource ARNs that this statement
        does *not* apply to. Used to apply a policy statement to all resources
        *except* those listed.
        """
        return pulumi.get(self, "not_resources")

    @not_resources.setter
    def not_resources(self, value: Optional[List[str]]):
        pulumi.set(self, "not_resources", value)

    @property
    @pulumi.getter
    def principals(self) -> Optional[List['GetPolicyDocumentStatementPrincipalArgs']]:
        """
        A nested configuration block (described below)
        specifying a principal (or principal pattern) to which this statement applies.
        """
        return pulumi.get(self, "principals")

    @principals.setter
    def principals(self, value: Optional[List['GetPolicyDocumentStatementPrincipalArgs']]):
        pulumi.set(self, "principals", value)

    @property
    @pulumi.getter
    def resources(self) -> Optional[List[str]]:
        """
        A list of resource ARNs that this statement applies
        to. This is required by AWS if used for an IAM policy.
        """
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: Optional[List[str]]):
        pulumi.set(self, "resources", value)

    @property
    @pulumi.getter
    def sid(self) -> Optional[str]:
        """
        An ID for the policy statement.
        """
        return pulumi.get(self, "sid")

    @sid.setter
    def sid(self, value: Optional[str]):
        pulumi.set(self, "sid", value)


@pulumi.input_type
class GetPolicyDocumentStatementConditionArgs:
    def __init__(__self__, *,
                 test: str,
                 values: List[str],
                 variable: str):
        """
        :param str test: The name of the
               [IAM condition operator](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html)
               to evaluate.
        :param List[str] values: The values to evaluate the condition against. If multiple
               values are provided, the condition matches if at least one of them applies.
               (That is, the tests are combined with the "OR" boolean operation.)
        :param str variable: The name of a
               [Context Variable](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys)
               to apply the condition to. Context variables may either be standard AWS
               variables starting with `aws:`, or service-specific variables prefixed with
               the service name.
        """
        pulumi.set(__self__, "test", test)
        pulumi.set(__self__, "values", values)
        pulumi.set(__self__, "variable", variable)

    @property
    @pulumi.getter
    def test(self) -> str:
        """
        The name of the
        [IAM condition operator](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html)
        to evaluate.
        """
        return pulumi.get(self, "test")

    @test.setter
    def test(self, value: str):
        pulumi.set(self, "test", value)

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        """
        The values to evaluate the condition against. If multiple
        values are provided, the condition matches if at least one of them applies.
        (That is, the tests are combined with the "OR" boolean operation.)
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: List[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def variable(self) -> str:
        """
        The name of a
        [Context Variable](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys)
        to apply the condition to. Context variables may either be standard AWS
        variables starting with `aws:`, or service-specific variables prefixed with
        the service name.
        """
        return pulumi.get(self, "variable")

    @variable.setter
    def variable(self, value: str):
        pulumi.set(self, "variable", value)


@pulumi.input_type
class GetPolicyDocumentStatementNotPrincipalArgs:
    def __init__(__self__, *,
                 identifiers: List[str],
                 type: str):
        """
        :param List[str] identifiers: List of identifiers for principals. When `type`
               is "AWS", these are IAM user or role ARNs.  When `type` is "Service", these are AWS Service roles e.g. `lambda.amazonaws.com`. When `type` is "Federated", these are web identity users or SAML provider ARNs.
        :param str type: The type of principal. For AWS ARNs this is "AWS".  For AWS services (e.g. Lambda), this is "Service". For Federated access the type is "Federated".
        """
        pulumi.set(__self__, "identifiers", identifiers)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def identifiers(self) -> List[str]:
        """
        List of identifiers for principals. When `type`
        is "AWS", these are IAM user or role ARNs.  When `type` is "Service", these are AWS Service roles e.g. `lambda.amazonaws.com`. When `type` is "Federated", these are web identity users or SAML provider ARNs.
        """
        return pulumi.get(self, "identifiers")

    @identifiers.setter
    def identifiers(self, value: List[str]):
        pulumi.set(self, "identifiers", value)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of principal. For AWS ARNs this is "AWS".  For AWS services (e.g. Lambda), this is "Service". For Federated access the type is "Federated".
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: str):
        pulumi.set(self, "type", value)


@pulumi.input_type
class GetPolicyDocumentStatementPrincipalArgs:
    def __init__(__self__, *,
                 identifiers: List[str],
                 type: str):
        """
        :param List[str] identifiers: List of identifiers for principals. When `type`
               is "AWS", these are IAM user or role ARNs.  When `type` is "Service", these are AWS Service roles e.g. `lambda.amazonaws.com`. When `type` is "Federated", these are web identity users or SAML provider ARNs.
        :param str type: The type of principal. For AWS ARNs this is "AWS".  For AWS services (e.g. Lambda), this is "Service". For Federated access the type is "Federated".
        """
        pulumi.set(__self__, "identifiers", identifiers)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def identifiers(self) -> List[str]:
        """
        List of identifiers for principals. When `type`
        is "AWS", these are IAM user or role ARNs.  When `type` is "Service", these are AWS Service roles e.g. `lambda.amazonaws.com`. When `type` is "Federated", these are web identity users or SAML provider ARNs.
        """
        return pulumi.get(self, "identifiers")

    @identifiers.setter
    def identifiers(self, value: List[str]):
        pulumi.set(self, "identifiers", value)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of principal. For AWS ARNs this is "AWS".  For AWS services (e.g. Lambda), this is "Service". For Federated access the type is "Federated".
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: str):
        pulumi.set(self, "type", value)


