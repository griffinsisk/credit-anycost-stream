---
title: Overview of Toolkit Features
category: features
createdAt: '2021-07-28T14:31:16.485Z'
hidden: false
slug: overview-of-features
updatedAt: '2022-01-14T23:21:51.683Z'
---
The CostFormation Toolkit extension for VS Code supports all aspects of authoring custom CloudZero Dimensions, including downloading, validating, and publishing of your custom definitions.

The following describes the available features. More in-depth information on how to use these features is provided on the remaining pages in this section.

# Autocompletion

Several of the definition language constructs can be automatically completed with VSCode autocomplete functionality. Autocomplete provides templates for things like rules and transforms, as well as dynamic source information such as resource tags or Kubernetes labels, by using live data from the CloudZero platform.

# &#x20;Inline Static Validation

While you are editing your definition files, the extension provides inline static validation as you type. This validation will immediately alert you with visual cues when you have ill-formatted YAML or have structural and syntactic errors in your definitions.

# Definition Downloading

The extension can retrieve the current live definitions so you can be sure you are editing the latest definitions. The extension can also download older versions of the definitions to allow you to view previous versions or even rollback some definitions.

# Line-by-Line Diff

When you are editing your definitions, you can review your changes with a line-by-line diff of your current edits against the currently published definitions.

# Telemetry Code Lens

To provide more context when you are editing dimensions, this feature will display an annotation above the definition of any Dimension that is referenced by a telemetry stream.

<Image align="center" alt="Annotation designating telemetry stream reference" className="border" border="#080909" width="1174" src="https://files.readme.io/5779e51-Screen_Shot_2022-01-14_at_2.53.22_PM.png" />

A telemetry stream tracks usage for the elements of one or more Dimensions. If one of those referenced Dimensions is removed, it will render the stream invalid and unavailable for use in authoring Allocation Dimensions. Clicking on the inline annotation will open the Telemetry Streams page for your organization, where you can see detailed information about each telemetry stream.

The code lens can be toggled on and off. To do so, open the settings UI (**Code** › **Settings** › **Settings**) and uncheck the **Code Lens** › **Telemetry: Enable** setting.

<Image align="center" alt="Toggle Telemetry Code LEns" className="border" border="#1a1c1c" width="1244" src="https://files.readme.io/59471d5-Screen_Shot_2022-01-14_at_2.36.21_PM.png" />

# Full Validation

While the inline static validation provides immediate feedback as you type, when you save a definitions file locally, the CloudZero platform provides full validation, including validation of sources, cycles in your dependencies, and so on.

# Publishing

When you have finished creating your definitions, you can publish them directly to the CloudZero platform, making your definitions available to all of your CloudZero users through the CloudZero Cost Explorer.

# Restoring Older Definitions

If you have published a set of definitions and discover a problem, you can back out of your changes by restoring your definitions to a previous version.
