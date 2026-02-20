---
title: Dimension Studio
deprecated: false
hidden: false
metadata:
  robots: index
---
<Callout icon="ℹ️" theme="info">
  This capability is in private preview. If you would like to use the Dimension Studio, contact your FinOps Account Manager. If you have any questions or feedback while using this capability, contact your FinOps Account Manager for assistance.
</Callout>

CloudZero provides a UI-based Dimension Studio, allowing users to create, update, or delete Dimension definitions directly within the CloudZero application. The YAML-based approach to creating Custom Dimensions is also available, and you can use YAML in the Dimension Studio. For details, see the section [YAML Dimension editing](/docs/dimensions-studio#/yaml-dimension-editing).

# Prerequisite

Each user must have a role with the `Modify Dimension Definitions` permission.

# Navigate to the Dimension Studio

1. Log in to CloudZero.
2. Click **Dimensions** in the top navigation.
3. When the Welcome screen opens, select an existing Dimension from the left navigation or select the option to create a new Dimension.

You can then use the features of the Dimension Studio to edit an existing Dimension or specify the name, type, rules, and transform for a new Dimension.

# Add a new Dimension

Follow these steps to create a new Dimension.

<Callout icon="ℹ️" theme="info">
  At any point, if you want to abandon your changes, select the option to **Discard Changes**. You will return to the left navigation on the Dimension editor screen and be able to create or edit a Dimension.
</Callout>

## Define the Dimension

1. Click **+ Add New Dimension**.
2. Enter the **Display Name** to be used for the Dimension in the UI.
3. Use the toggle to enable **Allocation** if you want your Dimension to support allocating by telemetry streams. See the section [Create an Allocation Dimension](/docs/dimensions-studio#/create-an-allocation-dimension) for information about the differences between these steps and what you must do to create an Allocation Dimension.
4. When the Dimension editing fields open, complete the fields to define the Dimension you are creating.
   1. **Dimensions Name**: The name is pre-populated from the **Display** **Name** you entered.
   2. **Default Value**: Optional. The category value that will be assigned to the spend if the spend does not match any of the `Group` or `GroupBy` rules that you configure.
   3. **Child**: A Dimension other than the one being defined. The Child Dimension will be the default by which you can drill down using the Explorer. A **Child** must be a logically connected grouping of spend. For example, if you are creating a `Product` Dimension to group spend by the products that are incurring that spend, you may want the **Child** dimension to be `Features`, so you can logically drill down from a particular Product Dimension to view cost for the Features associated with that product.
   4. **Hide**: Suppress display of this Dimension in the Explorer or Analytics. You may wish to hide a Dimension because it is used as a staging calculation or pass through, and your end users do not need to see the Dimension.
   5. **Disable**: De-activate this Dimension for data processing.

## Create rules to categorize spend

1. On the Dimension editing screen, click **+ Add Rule** to begin creating rules by which you will categorize spend.
2. By default, the UI loads a `Group` rule. If you wish, select **GroupBy**in the **Type** selector to change the rule type a `GroupBy` rule.
3. Using the rule form fields that open and the option to **Add Condition** or **Add Condition Group**, build rules by which to capture and categorize your spend. Your choices of options depend on whether you have selected building a `Group` or a `GroupBy` rule.

### Create a `Group` rule

To create a `Group` rule, enter the following in the rule form fields:

* **Name**: The name of the spend that matches what this Group rule will be called. For example if you are creating a Dimension called `Department`, you may name a particular group `Finance Department` or `Marketing Department`.
* **And/Or/Not rule selector**: Select the business logic by which to analyze your spend data:
  * **And**: All conditions within this rule must be true in order for spend to be categorized in this group. For example, if you want to create a `US - Storage` rule, you may set a rule where one source condition is `Region = US` AND the other source condition is `Service Category = Storage`.
  * **Or**: Any one condition within this rule must be true in order for spend to be categorized in this Group. For example, if you want to create an LLM Only rule, you may set a rule where either the source condition `AI Category = LLMs` OR the source condition `GenAI Model = gpt-4` must be true.
  * **Not**: Any spend not matching this condition will be categorized in the Group. For example, if you want to create a `Non-Azure Spend Group`, you may set a rule where the source condition `Cloud Provider` is NOT the value `Azure`.
* **Source**: A Dimension other than the one being defined that you wish to use as the first condition for the rule.
* **Value**: Value of the first condition you wish to use for the rule.
* When you select **And** or **Or** logic, you must select **Add Condition** or **Add Condition Group** and specify the **Source** and **Value** for each condition. If you want to delete a condition or a condition group, click the **trash icon** next to the rule you want to delete. These choices defined as follows:
  * **Add Condition**: Adds another condition to the rule being configured. For example, you may want to include `spend` from another `source` to be evaluated.
  * **Add Condition Group**: Adds an entirely new nested condition to be evaluated. This nested condition group will be evaluated in isolation, and then the outcome of that evaluation will be applied to the overall rule being configured. For more information, see the section [Condition Group](/docs/dimensions-studio#/condition-group).
* **Transforms**: For each condition, create a transform if you wish. For details, see the section [Transforms](/docs/dimensions-studio#/transforms).

### Create a GroupBy rule

To create a `GroupBy` rule, enter the following in the rule form fields:

* **Sources**: The source Dimensions of the spend that you are looking to include in the `GroupBy` rule. You can pick one or many different source Dimensions to include in the rule.
* **Coalesce**: For each condition, toggle this to `true` or `false`. See the table of source properties in the [CostFormation Language guide](/docs/costformation-definition-language-guide#/specifying-sources) for an overview of how Coalescing sources works.
* **Format**: Enter a format for the output of the `GroupBy` Rule. See the table of properties of a `GroupBy` rule in the [CostFormation Definition Language guide](/docs/costformation-definition-language-guide#/groupby-rules) for an overview of how formatting sources works.
* **Transforms**: You can choose to apply a Transform to the entire `GroupBy` rule or for any conditions that you set. For details, see the section [Transforms](/docs/dimensions-studio#/transforms).
* **And/Or/Not rule selector**: Select the business logic by which to analyze your spend data:
  * **And**: All conditions within this rule must be true in order for spend to be categorized in this Group. For example, if you want to create a `US - Storage` rule, you may set a rule where one source condition is `Region = US` AND the other source condition is `Service Category = Storage`.
  * **Or**: Any one condition within this rule must be true in order for spend to be categorized in this Group. For example, if you want to create an LLM Only rule, you may set a rule where either the source condition `AI Category = LLMs` OR the source condition `GenAI Model = gpt-4` must be true.
  * **Not**: Any spend not matching this condition will be categorized in the Group. For example, if you want to create a `Non-Azure Spend Group`, you may set a rule where the source condition `Cloud Provider` is NOT the value `Azure`.
* When you select **And** or **Or** logic, you must select **Add Condition** or **Add Condition Group** and specify the **Source** and **Value** for each condition. If you want to delete a condition or a condition group, click the **trash icon** next to the rule you want to delete. These choices defined as follows:
  * **Add Condition**: Adds another condition to the rule being configured. For example, you may want to include `spend` from another `source` to be evaluated.
  * **Add Condition Group**: Adds an entirely new nested condition to be evaluated. This nested condition group will be evaluated in isolation, and then the outcome of that evaluation will be applied to the overall rule being configured. For more information, see the section [Condition Group](/docs/dimensions-studio#/condition-group).

## Finish creating the rule and conditions

Continue to create as many rules and conditions needed to categorize spend under your Dimension.

## Save the Dimension

1. Click **Save Changes**. The system will now run an evaluation to determine if any underlying changes have been made to your company’s Dimension definitions while you have been working.
2. IF the system detects no conflicts, click **Publish Changes** to commit your work into the system and begin applying the Dimension to processing for your company.
3. IF the system detects conflicts, resolve those conflicts prior to publishing. For details, see the section [Handle conflicts identified when saving changes](/docs/dimensions-studio#/handle-problems-identified-when-saving-changes).

# Create an Allocation Dimension

For information about Allocation Dimensions, see the page [CostFormation: Allocating Shared Costs](/docs/costformation-allocating-shared-costs).

The Dimension Studio supports only creating allocations based on telemetry streams. The steps to create an Allocation Dimension follow.

1. Click **+ Add New Dimension**.
2. Enter the **Display Name** to be used for the Dimension in the UI.
3. Toggle **Allocation** on. The Dimension Studio will then load the option to **Allocate By Streams** rather than the options to specify conditions.
4. Click **Create Dimension.**
5. When the form opens, complete the fields to define the Dimension you are creating.
   1. **Dimensions Name**: The name is pre-populated from the **Display** **Name** you entered.
   2. **Default Value**: Optional. The category value that will be assigned to the spend if the spend does not match any of the `Group` or `GroupBy` rules that you configure.
   3. **Child**: A Dimension other than the one being defined. The Child Dimension will be the default by which you can drill down using the Explorer. A **Child** must be a logically connected grouping of spend. For example, if you are creating a `Product` Dimension to group spend by the products that are incurring that spend, you may want the **Child** dimension to be `Features`, so you can logically drill down from a particular Product Dimension to view cost for the Features associated with that product.
   4. **Hide**: Suppress display of this Dimension in the Explorer or Analytics. You may wish to hide a Dimension because it is used as a staging calculation or pass through, and your end users do not need to see the Dimension.
   5. **Disable**: De-activate this Dimension for data processing.
6. Select one or more streams by which to allocate spend.
7. Click **Save Changes**. For details, see the section [Save the Dimension](/docs/dimensions-studio#/save-the-dimension).

# Transforms

You may wish to transform the underlying data of a condition to make it uniform prior to applying the `and-or-not`. To do so, select **Transforms** and click **+ Add Transform**. Then select from the available transforms:

1. **Lower**: This makes all values lowercase prior to rules being evaluated. For example, `PROD`, `Prod`, `pRod` all will be changed to `prod`.
2. **Split**: This lets you split out values by a specific delimiter prior to evaluating the rule. For example, you may have a set of values that are `Tag-prod`, `Tagging-prod`, `Tags-prod`. Entering a split transformation of `-` and `1` means the rule will only run on the string `prod`.
3. **Normalize**: This transform will make all of the letters in the source value lowercase, and will also convert any instance of the characters `.,/#!$%^&*;:=_ ~()\'` to a dash (`-`).

If you want to delete a transform, click the trash icon next to the transform you want to delete.

Transforms can be applied to both `Group` and `GroupBy` rules, as well as any `condition` within these rule types.

# Condition Group

Adding a Condition Group adds an entirely new nested condition to be evaluated. This condition group will be evaluated in isolation, and then the outcome of that evaluation will be applied to the overall rule. An example nested rule follows:

<Image align="center" alt="Example of nested rule" border={true} src="https://files.readme.io/dae9609fb0de9a8f4de21e75daea84b3c3a194beee107ccb1336f3142fc3d6eb-nested-rule.png" className="border" />

In this example, we are creating a rule to categorize all of our spend to be `LLM Only`. To do this, due to the complexity of our environments, we set up a set of nested rule conditions. In the first condition, the `AI category` is `LLMs`. In this example, CloudZero will evaluate the rules as follows:

1. First, CloudZero will check to see if `Account Name` = `LLM-Playground` OR `Environment` = `LLM-Playground`.
2. If Cloud Spend matches either of these conditions, then this condition will evaluate as `TRUE`.
3. Then CloudZero will evaluate whether Cloud Spend fits into an `AI Category` = `LLMs`.
4. Because the top-level rule is an `AND` condition, only Cloud Spend where both checks have been evaluated as `TRUE` will pass the `LLM Only` rule.

This can also be written out in a formulaic statement:

`IF (Account Name = LLM-Playground OR Environment) = LLM-Playground AND AI-Category = LLMs`, then this rule passes.

# Edit an existing Dimension

1. To edit any existing Dimension, select it from the left navigation.
2. Click the **Dimension** you want to edit.
3. Make the needed updates.
4. Click **Save Changes**. For details, see the section [Save the Dimension](/docs/dimensions-studio#/save-the-dimension).

# Delete a Dimension

<Callout icon="ℹ️" theme="info">
  Deleting a Dimension can lead to downstream and upstream problems with other Dimensions. For example, if you have a **Product** > **Feature** > **Component** hierarchy built out, and delete the `Feature` Dimension, you must make updates to the `Product` and `Component` Dimensions for your CostFormation Definitions to properly function.
</Callout>

To delete any existing Dimension, follow these steps:

1. On the Dimensions screen, select the Dimension you want to delete using the left navigation menu.
2. Click **Delete Dimension**.
3. **Click Save Changes**. For details, see the section [Save the Dimension](/docs/dimensions-studio#/save-the-dimension).

# YAML Dimension editing

The Dimension Studio includes a **Code editor** tab with inYAML editing capabilities to create and update Dimensions.

<Image align="center" alt="Dimensions Studio code tab" border={true} src="https://files.readme.io/8d41ed1a2b5ec42ad5eb6c4dd7cc68ccd5e39990310e04b92b810727e5974122-Dimensions-Studio-code-tab.png" className="border" />

Changes that you make in the YAML Code Editor and the Visual Editor will synchronize automatically. For example, if you add a new `Group` rule to a Dimension through the UI, the rule will appear in the corresponding YAML automatically. If you add a new transform using YAML, the transform will be shown in the UI as well.

<Callout icon="ℹ️" theme="info">
  The Dimension Studio supports most of the YAML-based CostFormation capabilities. You may need to use the [VS Code CostFormation Toolkit](/docs/vscode-costformation-extension) to achieve outcomes for complex use cases and cost allocation requirements.
</Callout>

To open the YAML editor for an individual Dimension, follow these steps:

1. To edit or delete any existing Dimension, select it from the left navigation.
2. Select the **Code editor** tab.
3. Make the changes you want to this Dimension.
4. Click **Save Changes**. For details, see the section [Save the Dimension](/docs/dimensions-studio#/save-the-dimension).

To open a comprehensive YAML-based view of your entire CostFormation definition file, follow these steps:

1. To open the Dimension Studio, click **Dimension** in the top navigation of the CloudZero app.
2. Click **Edit YAML file.**

For more information about YAML-based editing, see the [CostFormation documentation](/docs/cost-formation-definition-language).

# Handle problems identified when saving changes

When you are saving changes to your CostFormation definitions, CloudZero will validate your changes to ensure that you are not committing breaking changes that will impact your end users and cost allocations.

Problems identified will largely be grouped into these major categories:

* **Versioning**: These problems can occur when another user has published changes to your CostFormation definitions while you have been using the visual editor.

  In these circumstances, it is recommended to revert any changes that you have made to make sure that you are working from the most recent version of your accounts definitions, and to not overwrite another user's work.

* **Formatting and syntax**: These problems occur mainly when you are using the Code editor to hand write CostFormation definitions. The Dimension Studio will highlight each area where there is a formatting or syntax error, and will require that each be fixed prior to publishing your changes into the platform.
