---
title: Restoring Previous Definitions
category: features
createdAt: '2023-01-30T13:55:55.369Z'
hidden: false
slug: restore-definitions
updatedAt: '2023-01-30T20:00:18.743Z'
---
If incorrect edits to your definitions were published to the CloudZero platform, you can restore them to a previous version.

To initiate a restore, open the VSCode command palette (⇧⌘P/Ctrl-Shift-P) and select the command **CloudZero: Restore CostFormation from an Older Version**

<Image align="center" alt="Restore.png" className="border" border="#000000" width="2048" src="https://files.readme.io/edaa1a5-Restore.png" />

After you press enter, a list of previous versions will be shown. The list will show the most recent changes first.

<Image align="center" alt="List of previous versions of CostFormation" className="border" border="#000000" width="2046" src="https://files.readme.io/420056f-olderversions.png" />

Select the version you would like to restore and press enter. You will then be asked if you want to restore to that version or save the file locally in order to make additional edits. If you choose to restore the file, that version will be published as the latest version. If you select to save the file locally, a file save dialog opens. Enter a file name for the the definitions and click **Save**. You can now make any necessary edits and then publish those changes as you would any other edits.

<Image align="center" alt="Confirm the restore" className="border" border="#000000" width="300px" src="https://files.readme.io/a449fce-ConfirmRestore.png" />

<Callout icon="ℹ️" theme="info">
  This operation is not a true rollback operation. Instead, it publishes the older version as a new set of changes. When you choose to restore older definitions, the current definitions that you are overwriting become the most recent older version.
</Callout>
