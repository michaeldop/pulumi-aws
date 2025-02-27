// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.GuardDuty
{
    /// <summary>
    /// Provides a resource to manage a GuardDuty member. To accept invitations in member accounts, see the `aws.guardduty.InviteAccepter` resource.
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
    ///         var primary = new Aws.GuardDuty.Detector("primary", new Aws.GuardDuty.DetectorArgs
    ///         {
    ///             Enable = true,
    ///         });
    ///         var memberDetector = new Aws.GuardDuty.Detector("memberDetector", new Aws.GuardDuty.DetectorArgs
    ///         {
    ///             Enable = true,
    ///         }, new CustomResourceOptions
    ///         {
    ///             Provider = aws.Dev,
    ///         });
    ///         var memberMember = new Aws.GuardDuty.Member("memberMember", new Aws.GuardDuty.MemberArgs
    ///         {
    ///             AccountId = memberDetector.AccountId,
    ///             DetectorId = primary.Id,
    ///             Email = "required@example.com",
    ///             Invite = true,
    ///             InvitationMessage = "please accept guardduty invitation",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class Member : Pulumi.CustomResource
    {
        /// <summary>
        /// AWS account ID for member account.
        /// </summary>
        [Output("accountId")]
        public Output<string> AccountId { get; private set; } = null!;

        /// <summary>
        /// The detector ID of the GuardDuty account where you want to create member accounts.
        /// </summary>
        [Output("detectorId")]
        public Output<string> DetectorId { get; private set; } = null!;

        /// <summary>
        /// Boolean whether an email notification is sent to the accounts. Defaults to `false`.
        /// </summary>
        [Output("disableEmailNotification")]
        public Output<bool?> DisableEmailNotification { get; private set; } = null!;

        /// <summary>
        /// Email address for member account.
        /// </summary>
        [Output("email")]
        public Output<string> Email { get; private set; } = null!;

        /// <summary>
        /// Message for invitation.
        /// </summary>
        [Output("invitationMessage")]
        public Output<string?> InvitationMessage { get; private set; } = null!;

        /// <summary>
        /// Boolean whether to invite the account to GuardDuty as a member. Defaults to `false`. To detect if an invitation needs to be (re-)sent, the this provider state value is `true` based on a `relationship_status` of `Disabled`, `Enabled`, `Invited`, or `EmailVerificationInProgress`.
        /// </summary>
        [Output("invite")]
        public Output<bool?> Invite { get; private set; } = null!;

        /// <summary>
        /// The status of the relationship between the member account and its primary account. More information can be found in [Amazon GuardDuty API Reference](https://docs.aws.amazon.com/guardduty/latest/ug/get-members.html).
        /// </summary>
        [Output("relationshipStatus")]
        public Output<string> RelationshipStatus { get; private set; } = null!;


        /// <summary>
        /// Create a Member resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Member(string name, MemberArgs args, CustomResourceOptions? options = null)
            : base("aws:guardduty/member:Member", name, args ?? new MemberArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Member(string name, Input<string> id, MemberState? state = null, CustomResourceOptions? options = null)
            : base("aws:guardduty/member:Member", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Member resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Member Get(string name, Input<string> id, MemberState? state = null, CustomResourceOptions? options = null)
        {
            return new Member(name, id, state, options);
        }
    }

    public sealed class MemberArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// AWS account ID for member account.
        /// </summary>
        [Input("accountId", required: true)]
        public Input<string> AccountId { get; set; } = null!;

        /// <summary>
        /// The detector ID of the GuardDuty account where you want to create member accounts.
        /// </summary>
        [Input("detectorId", required: true)]
        public Input<string> DetectorId { get; set; } = null!;

        /// <summary>
        /// Boolean whether an email notification is sent to the accounts. Defaults to `false`.
        /// </summary>
        [Input("disableEmailNotification")]
        public Input<bool>? DisableEmailNotification { get; set; }

        /// <summary>
        /// Email address for member account.
        /// </summary>
        [Input("email", required: true)]
        public Input<string> Email { get; set; } = null!;

        /// <summary>
        /// Message for invitation.
        /// </summary>
        [Input("invitationMessage")]
        public Input<string>? InvitationMessage { get; set; }

        /// <summary>
        /// Boolean whether to invite the account to GuardDuty as a member. Defaults to `false`. To detect if an invitation needs to be (re-)sent, the this provider state value is `true` based on a `relationship_status` of `Disabled`, `Enabled`, `Invited`, or `EmailVerificationInProgress`.
        /// </summary>
        [Input("invite")]
        public Input<bool>? Invite { get; set; }

        public MemberArgs()
        {
        }
    }

    public sealed class MemberState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// AWS account ID for member account.
        /// </summary>
        [Input("accountId")]
        public Input<string>? AccountId { get; set; }

        /// <summary>
        /// The detector ID of the GuardDuty account where you want to create member accounts.
        /// </summary>
        [Input("detectorId")]
        public Input<string>? DetectorId { get; set; }

        /// <summary>
        /// Boolean whether an email notification is sent to the accounts. Defaults to `false`.
        /// </summary>
        [Input("disableEmailNotification")]
        public Input<bool>? DisableEmailNotification { get; set; }

        /// <summary>
        /// Email address for member account.
        /// </summary>
        [Input("email")]
        public Input<string>? Email { get; set; }

        /// <summary>
        /// Message for invitation.
        /// </summary>
        [Input("invitationMessage")]
        public Input<string>? InvitationMessage { get; set; }

        /// <summary>
        /// Boolean whether to invite the account to GuardDuty as a member. Defaults to `false`. To detect if an invitation needs to be (re-)sent, the this provider state value is `true` based on a `relationship_status` of `Disabled`, `Enabled`, `Invited`, or `EmailVerificationInProgress`.
        /// </summary>
        [Input("invite")]
        public Input<bool>? Invite { get; set; }

        /// <summary>
        /// The status of the relationship between the member account and its primary account. More information can be found in [Amazon GuardDuty API Reference](https://docs.aws.amazon.com/guardduty/latest/ug/get-members.html).
        /// </summary>
        [Input("relationshipStatus")]
        public Input<string>? RelationshipStatus { get; set; }

        public MemberState()
        {
        }
    }
}
