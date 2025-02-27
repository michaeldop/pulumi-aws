// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package budgets

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a budgets budget resource. Budgets use the cost visualisation provided by Cost Explorer to show you the status of your budgets, to provide forecasts of your estimated costs, and to track your AWS usage, including your free tier usage.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/budgets"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := budgets.NewBudget(ctx, "ec2", &budgets.BudgetArgs{
// 			BudgetType: pulumi.String("COST"),
// 			CostFilters: pulumi.StringMap{
// 				"Service": pulumi.String("Amazon Elastic Compute Cloud - Compute"),
// 			},
// 			LimitAmount: pulumi.String("1200"),
// 			LimitUnit:   pulumi.String("USD"),
// 			Notifications: budgets.BudgetNotificationArray{
// 				&budgets.BudgetNotificationArgs{
// 					ComparisonOperator: pulumi.String("GREATER_THAN"),
// 					NotificationType:   pulumi.String("FORECASTED"),
// 					SubscriberEmailAddresses: pulumi.StringArray{
// 						pulumi.String("test@example.com"),
// 					},
// 					Threshold:     pulumi.Float64(100),
// 					ThresholdType: pulumi.String("PERCENTAGE"),
// 				},
// 			},
// 			TimePeriodEnd:   pulumi.String("2087-06-15_00:00"),
// 			TimePeriodStart: pulumi.String("2017-07-01_00:00"),
// 			TimeUnit:        pulumi.String("MONTHLY"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// Create a budget for *$100*.
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/budgets"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := budgets.NewBudget(ctx, "cost", &budgets.BudgetArgs{
// 			BudgetType:  pulumi.String("COST"),
// 			LimitAmount: pulumi.String("100"),
// 			LimitUnit:   pulumi.String("USD"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// Create a budget for s3 with a limit of *3 GB* of storage.
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/budgets"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := budgets.NewBudget(ctx, "s3", &budgets.BudgetArgs{
// 			BudgetType:  pulumi.String("USAGE"),
// 			LimitAmount: pulumi.String("3"),
// 			LimitUnit:   pulumi.String("GB"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// Create a Savings Plan Utilization Budget
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/budgets"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := budgets.NewBudget(ctx, "savingsPlanUtilization", &budgets.BudgetArgs{
// 			BudgetType: pulumi.String("SAVINGS_PLANS_UTILIZATION"),
// 			CostTypes: &budgets.BudgetCostTypesArgs{
// 				IncludeCredit:            pulumi.Bool(false),
// 				IncludeDiscount:          pulumi.Bool(false),
// 				IncludeOtherSubscription: pulumi.Bool(false),
// 				IncludeRecurring:         pulumi.Bool(false),
// 				IncludeRefund:            pulumi.Bool(false),
// 				IncludeSubscription:      pulumi.Bool(true),
// 				IncludeSupport:           pulumi.Bool(false),
// 				IncludeTax:               pulumi.Bool(false),
// 				IncludeUpfront:           pulumi.Bool(false),
// 				UseBlended:               pulumi.Bool(false),
// 			},
// 			LimitAmount: pulumi.String("100.0"),
// 			LimitUnit:   pulumi.String("PERCENTAGE"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// Create a RI Utilization Budget
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/budgets"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := budgets.NewBudget(ctx, "riUtilization", &budgets.BudgetArgs{
// 			BudgetType: pulumi.String("RI_UTILIZATION"),
// 			CostFilters: pulumi.StringMap{
// 				"Service": pulumi.String("Amazon Relational Database Service"),
// 			},
// 			CostTypes: &budgets.BudgetCostTypesArgs{
// 				IncludeCredit:            pulumi.Bool(false),
// 				IncludeDiscount:          pulumi.Bool(false),
// 				IncludeOtherSubscription: pulumi.Bool(false),
// 				IncludeRecurring:         pulumi.Bool(false),
// 				IncludeRefund:            pulumi.Bool(false),
// 				IncludeSubscription:      pulumi.Bool(true),
// 				IncludeSupport:           pulumi.Bool(false),
// 				IncludeTax:               pulumi.Bool(false),
// 				IncludeUpfront:           pulumi.Bool(false),
// 				UseBlended:               pulumi.Bool(false),
// 			},
// 			LimitAmount: pulumi.String("100.0"),
// 			LimitUnit:   pulumi.String("PERCENTAGE"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Budget struct {
	pulumi.CustomResourceState

	// The ID of the target account for budget. Will use current user's accountId by default if omitted.
	AccountId pulumi.StringOutput `pulumi:"accountId"`
	// Whether this budget tracks monetary cost or usage.
	BudgetType pulumi.StringOutput `pulumi:"budgetType"`
	// Map of CostFilters key/value pairs to apply to the budget.
	CostFilters pulumi.StringMapOutput `pulumi:"costFilters"`
	// Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..
	CostTypes BudgetCostTypesOutput `pulumi:"costTypes"`
	// The amount of cost or usage being measured for a budget.
	LimitAmount pulumi.StringOutput `pulumi:"limitAmount"`
	// The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.
	LimitUnit pulumi.StringOutput `pulumi:"limitUnit"`
	// The name of a budget. Unique within accounts.
	Name pulumi.StringOutput `pulumi:"name"`
	// The prefix of the name of a budget. Unique within accounts.
	NamePrefix pulumi.StringOutput `pulumi:"namePrefix"`
	// Object containing Budget Notifications. Can be used multiple times to define more than one budget notification
	Notifications BudgetNotificationArrayOutput `pulumi:"notifications"`
	// The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.
	TimePeriodEnd pulumi.StringPtrOutput `pulumi:"timePeriodEnd"`
	// The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.
	TimePeriodStart pulumi.StringOutput `pulumi:"timePeriodStart"`
	// The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.
	TimeUnit pulumi.StringOutput `pulumi:"timeUnit"`
}

// NewBudget registers a new resource with the given unique name, arguments, and options.
func NewBudget(ctx *pulumi.Context,
	name string, args *BudgetArgs, opts ...pulumi.ResourceOption) (*Budget, error) {
	if args == nil || args.BudgetType == nil {
		return nil, errors.New("missing required argument 'BudgetType'")
	}
	if args == nil || args.LimitAmount == nil {
		return nil, errors.New("missing required argument 'LimitAmount'")
	}
	if args == nil || args.LimitUnit == nil {
		return nil, errors.New("missing required argument 'LimitUnit'")
	}
	if args == nil || args.TimePeriodStart == nil {
		return nil, errors.New("missing required argument 'TimePeriodStart'")
	}
	if args == nil || args.TimeUnit == nil {
		return nil, errors.New("missing required argument 'TimeUnit'")
	}
	if args == nil {
		args = &BudgetArgs{}
	}
	var resource Budget
	err := ctx.RegisterResource("aws:budgets/budget:Budget", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBudget gets an existing Budget resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBudget(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BudgetState, opts ...pulumi.ResourceOption) (*Budget, error) {
	var resource Budget
	err := ctx.ReadResource("aws:budgets/budget:Budget", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Budget resources.
type budgetState struct {
	// The ID of the target account for budget. Will use current user's accountId by default if omitted.
	AccountId *string `pulumi:"accountId"`
	// Whether this budget tracks monetary cost or usage.
	BudgetType *string `pulumi:"budgetType"`
	// Map of CostFilters key/value pairs to apply to the budget.
	CostFilters map[string]string `pulumi:"costFilters"`
	// Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..
	CostTypes *BudgetCostTypes `pulumi:"costTypes"`
	// The amount of cost or usage being measured for a budget.
	LimitAmount *string `pulumi:"limitAmount"`
	// The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.
	LimitUnit *string `pulumi:"limitUnit"`
	// The name of a budget. Unique within accounts.
	Name *string `pulumi:"name"`
	// The prefix of the name of a budget. Unique within accounts.
	NamePrefix *string `pulumi:"namePrefix"`
	// Object containing Budget Notifications. Can be used multiple times to define more than one budget notification
	Notifications []BudgetNotification `pulumi:"notifications"`
	// The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.
	TimePeriodEnd *string `pulumi:"timePeriodEnd"`
	// The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.
	TimePeriodStart *string `pulumi:"timePeriodStart"`
	// The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.
	TimeUnit *string `pulumi:"timeUnit"`
}

type BudgetState struct {
	// The ID of the target account for budget. Will use current user's accountId by default if omitted.
	AccountId pulumi.StringPtrInput
	// Whether this budget tracks monetary cost or usage.
	BudgetType pulumi.StringPtrInput
	// Map of CostFilters key/value pairs to apply to the budget.
	CostFilters pulumi.StringMapInput
	// Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..
	CostTypes BudgetCostTypesPtrInput
	// The amount of cost or usage being measured for a budget.
	LimitAmount pulumi.StringPtrInput
	// The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.
	LimitUnit pulumi.StringPtrInput
	// The name of a budget. Unique within accounts.
	Name pulumi.StringPtrInput
	// The prefix of the name of a budget. Unique within accounts.
	NamePrefix pulumi.StringPtrInput
	// Object containing Budget Notifications. Can be used multiple times to define more than one budget notification
	Notifications BudgetNotificationArrayInput
	// The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.
	TimePeriodEnd pulumi.StringPtrInput
	// The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.
	TimePeriodStart pulumi.StringPtrInput
	// The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.
	TimeUnit pulumi.StringPtrInput
}

func (BudgetState) ElementType() reflect.Type {
	return reflect.TypeOf((*budgetState)(nil)).Elem()
}

type budgetArgs struct {
	// The ID of the target account for budget. Will use current user's accountId by default if omitted.
	AccountId *string `pulumi:"accountId"`
	// Whether this budget tracks monetary cost or usage.
	BudgetType string `pulumi:"budgetType"`
	// Map of CostFilters key/value pairs to apply to the budget.
	CostFilters map[string]string `pulumi:"costFilters"`
	// Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..
	CostTypes *BudgetCostTypes `pulumi:"costTypes"`
	// The amount of cost or usage being measured for a budget.
	LimitAmount string `pulumi:"limitAmount"`
	// The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.
	LimitUnit string `pulumi:"limitUnit"`
	// The name of a budget. Unique within accounts.
	Name *string `pulumi:"name"`
	// The prefix of the name of a budget. Unique within accounts.
	NamePrefix *string `pulumi:"namePrefix"`
	// Object containing Budget Notifications. Can be used multiple times to define more than one budget notification
	Notifications []BudgetNotification `pulumi:"notifications"`
	// The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.
	TimePeriodEnd *string `pulumi:"timePeriodEnd"`
	// The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.
	TimePeriodStart string `pulumi:"timePeriodStart"`
	// The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.
	TimeUnit string `pulumi:"timeUnit"`
}

// The set of arguments for constructing a Budget resource.
type BudgetArgs struct {
	// The ID of the target account for budget. Will use current user's accountId by default if omitted.
	AccountId pulumi.StringPtrInput
	// Whether this budget tracks monetary cost or usage.
	BudgetType pulumi.StringInput
	// Map of CostFilters key/value pairs to apply to the budget.
	CostFilters pulumi.StringMapInput
	// Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..
	CostTypes BudgetCostTypesPtrInput
	// The amount of cost or usage being measured for a budget.
	LimitAmount pulumi.StringInput
	// The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.
	LimitUnit pulumi.StringInput
	// The name of a budget. Unique within accounts.
	Name pulumi.StringPtrInput
	// The prefix of the name of a budget. Unique within accounts.
	NamePrefix pulumi.StringPtrInput
	// Object containing Budget Notifications. Can be used multiple times to define more than one budget notification
	Notifications BudgetNotificationArrayInput
	// The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.
	TimePeriodEnd pulumi.StringPtrInput
	// The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.
	TimePeriodStart pulumi.StringInput
	// The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.
	TimeUnit pulumi.StringInput
}

func (BudgetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*budgetArgs)(nil)).Elem()
}
