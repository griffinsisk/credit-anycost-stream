---
title: Reviewing and Publishing Definitions
category: features
createdAt: '2021-07-29T13:55:55.369Z'
hidden: false
slug: publish-definitions
updatedAt: '2021-08-11T20:00:18.743Z'
---
When you have completed your Dimension definitions, you can publish them to CloudZero to make them available for everyone in your organization. When you publish your definitions, they will be fully validated, and any validation failures will prevent the new definitions from being published.

# Review your changes

When you have modified your existing definitions, you may want to review the changes before publishing them. The CloudZero CostFormation Toolkit extension allows you to review a line-by-line diff between your current definitions with the latest version in the cloud.

To view the line-by-line diff, verify that you are in the file containing your latest edits, open the VSCode command palette (⇧⌘P/Ctrl-Shift-P), and select the command **CloudZero: Review CostFormation Changes**.

<Image align="center" alt="Select CloudZero: Review CostFormation Changes command" className="border" border="#000000" width="2046" src="https://files.readme.io/3325869-Review.png" />

After you press enter, a new tab opens with a side-by-side diff. This view is read-only and is only for reviewing changes. It does not provide any functionality to resolve or undo differences.

<Image align="center" alt="Diff view" className="border" border="#2a2b25" width="4704" src="https://files.readme.io/d70e292-Screen_Shot_2021-07-30_at_8.35.22_AM.png" />

# Publish your definitions

When you are ready to publish your new Definitions, go back to the tab containing your definitions, open the VSCode command palette (⇧⌘P/Ctrl-Shift-P), and select **CloudZero: Publish CostFormation**.

<Image align="center" alt="Select CloudZero: Publish CostFormation command" className="border" border="#000000" width="2072" src="https://files.readme.io/d012c96-publish.png" />

After you select the command, the Definitions will be uploaded, validated, and then published.

<Callout icon="ℹ️" theme="info">
  When definitions are published, there may be a delay of 15 to 30 minutes before the changes are visible in the Explorer.
</Callout>

# Conflicts when publishing

After you download the latest CostFormation definitions and make edits in VSCode, it is possible that a newer version of the CostFormation has been uploaded to the CloudZero platform by someone else. The CostFormation Toolkit will detect this and warn you that you may potentially overwrite changes that were uploaded since you downloaded the version you started your edits with.

<Image align="center" alt="Conflict notice" className="border" border="#000000" width="334" src="https://files.readme.io/323390d-ResolveConflicts.png" />

Click **Resolve Conflicts** to open a merge conflict editor, which merges the changes you have made with changes uploaded after you downloaded.

<Callout icon="⚠️" theme="warn">
  You can choose to click on **Overwrite Latest** to publish without merging with the other changes. However, you risk losing important changes.
</Callout>

If there are any conflicting changes, those conflicts will be highlighted using a conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

<Image align="center" alt="Conflict markers in the editor" className="border" border="#000000" width="1256" src="https://files.readme.io/2c7b4b5-threwaydiff.png" />

You can use the editor to resolve the conflicts. For any conflict highlighted in the editor, choose to accept the `current change` (which you made) or the `incoming change` that was uploaded after your last download. Alternatively, you can delete both sets of changes and put in new ones. All conflicts must be resolved before you can attempt to publish the merged changes.

<Callout icon="ℹ️" theme="info">
  It is very possible that your changes and the newly downloaded changes do not conflict in any way. In that case, the editor will contain the latest downloaded changes merged in with your changes and you will not find any occurrences of the conflict markers.
</Callout>

After you have resolved all conflicts and there are no more conflict markers, you can choose again to publish your definitions. The Toolkit will ask you if you have resolved all conflicts.

<Image align="center" alt="Confirming conflicts are resolved" className="border" border="#000000" width="326" src="https://files.readme.io/e30cfda-CompleteConflictResolve.png" />

Click **Conflicts are Resolved** and your Definitions will be published.

# Recommended workflow

The recommended workflow when you are using the CloudZero CostFormation Toolkit is to download the latest CostFormation definitions for your organization, make edits, and then publish the changes. This enables the extension to track important information about your CostFormation definition file, including the version downloaded. Working outside of this workflow may cause the extension to be unable to track this information.

The following actions can cause this:

* Moving or renaming files outside of VSCode, such as using terminal commands or other text editors.
* Downloading definitions files from other sources, like GitHub or other source control systems.
* Creating a new definition file using `Save As` command.

If the CostFormation Toolkit is unable to track this information or is otherwise unable to determine what version of the definitions your edits are based on, then any time you publish, a warning will be shown recommending that you review your changes to ensure you are not undoing changes that may have been uploaded after the version you began editing.

<Image align="center" alt="Review changes notice" className="border" border="#000000" width="356" src="https://files.readme.io/54f7867-ReviewChanges.png" />

You can select **Overwrite Latest** to publish your changes, or select **Review Changes** to bring up a line-by-line comparison of your definitions with the last published definitions.
