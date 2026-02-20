---
title: Validating Definitions
category: features
createdAt: '2021-07-29T13:48:58.963Z'
hidden: false
slug: validating-definitions
updatedAt: '2021-07-30T19:37:02.753Z'
---
The CloudZero CostFormation Toolkit extension provides two modes of validation: inline static validation and full semantic validation.

# Inline syntactic validation

When you are in the VSCode editor, inline validation will provide visual hints about problems in your definition file. This validation will catch syntactic problems like improperly formatted YAML, invalid keywords, missing keywords, and other problems that can be found through static analysis of the definitions file. Inline validation will not find problems like invalid sources or dependency cycles. These types of problems require the full compilation and validation provided by the CloudZero platform. Use the full semantic validation check for those types of problems.

As with other features of the extension, inline validation is applied only to files with the extension `.cz.yaml`. When you are in the editor window for a definition file, problems will be underlined with a red squiggly line.

<Image align="center" alt="Problem underlined" className="border" border="#222323" width="1432" src="https://files.readme.io/97c6872-Screen_Shot_2021-07-29_at_9.21.27_AM.png" />

To determine what the problem is, hold the mouse over the problem area and a popup will indicate what the problem is.

<Image align="center" alt="Popup with information about the problem" className="border" border="#232324" width="1976" src="https://files.readme.io/a251d06-Screen_Shot_2021-07-29_at_9.22.38_AM.png" />

<Callout icon="ℹ️" theme="info">
  Sometimes the problem will also show a lightbulb indicating a suggested fix. This feature is not supported and the suggested fix will only take you to the schema file used for validation.
</Callout>

<Image align="center" alt="Lightbulb indicating suggested fix" className="border" border="#222223" width="1702" src="https://files.readme.io/d120bd7-Screen_Shot_2021-07-29_at_9.25.35_AM.png" />

# Full semantic validation

Full semantic validation is provided by the CloudZero platform. This level of validation is performed whenever you save your definitions file locally as well as when publishing definitions. Any time you save the file locally, the definitions are sent to the CloudZero platform, which will return any errors. These errors are shown in the **Problem** output window as well as the CloudZero CostFormation Toolkit output.

<Image align="center" alt="Problem output window" className="border" border="#212324" width="2022" src="https://files.readme.io/b9910ba-Screen_Shot_2021-07-29_at_5.13.32_PM.png" />
