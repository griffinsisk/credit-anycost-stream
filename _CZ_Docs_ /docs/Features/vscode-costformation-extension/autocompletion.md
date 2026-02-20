---
title: Autocompletion
category: features
createdAt: '2021-07-28T20:14:28.705Z'
hidden: false
slug: autocompletion
updatedAt: '2022-01-14T22:24:07.220Z'
---
As you write your Dimension definition, there are several places where autocompletion can help. Some autocompletion values act like templates for a particular definition section, such as rules and conditions, while others provide completion for a particular item, like a source.

For all autocomplete items, begin typing and the autocomplete possibilities will appear in a list. At any point you can select an item on the list and press enter to autocomplete the item.

<Callout icon="ℹ️">
  Some completion items are retrieved live from the CloudZero platform. Therefore you should authenticate with CloudZero for best results. See [Getting Started with the Toolkit](doc:getting-started-2) to learn how to authenticate the extension with the CloudZero platform.
</Callout>

# Autocomplete templates

For the different sections of a Dimension definition, autocomplete provides access to templates. These templates will add sections to your definition and then allow you to fill in the values for parts that can be customized.

For most templates you can begin typing the name of the section containing the template to see the templates available for that section. These special keywords are identified in the next sections.

## Dimension templates

When you start typing **dimension**, you will see the autocomplete templates for creating a Dimension definition under the dimension root.

<Image align="center" alt="List of Dimension definition templates" className="border" border="#242729" width="2700" src="https://files.readme.io/5eeb208-Screen_Shot_2021-07-28_at_3.53.34_PM.png" />

## Rule templates

When you start typing **rule**, you will see the autocomplete templates for the various types of rules you would add to the **Rules** section of a definition. These include rules for creating statically named groups, dynamically named groups, and dynamically named groups with a filter condition.

<Image align="center" alt="List of rule templates" className="border" border="#222426" width="2706" src="https://files.readme.io/1059ead-Screen_Shot_2021-07-28_at_3.58.20_PM.png" />

## Condition templates

When you start typing **condition** you will see the autocomplete templates for the supported conditions that can be added to the **Conditions** section. Each condition has two templates: one for using the source from the outer scope and one for defining a source scoped to that condition.

<Image align="center" alt="List of condition templates" className="border" border="#242527" width="2848" src="https://files.readme.io/0d5ad5d-Screen_Shot_2021-07-28_at_4.01.25_PM.png" />

## Source templates

When you start typing **source** you will see the autocomplete templates for the different ways you can specify a source. This includes single sources and multiple sources, as well as sources with and without transforms. These templates can be used in various sections depending on the scope of the source you want to create.

<Image align="center" alt="List of source templates" className="border" border="#232526" width="2858" src="https://files.readme.io/ac7a533-Screen_Shot_2021-07-28_at_4.08.34_PM.png" />

## Transform templates

When you start typing **transforms** you will see the autocomplete templates for creating the transforms section as well as those for creating the various transforms.

<Image align="center" alt="List of transforms templates" className="border" border="#232425" width="2994" src="https://files.readme.io/bbf5592-Screen_Shot_2021-07-28_at_4.11.05_PM.png" />

# Autocomplete sources

In addition to the autocomplete templates for sources, when you are in a source section, you will get autocomplete for the supported sources. When entering a source, you can either begin typing a source name, or press Ctrl-Space to see the list of possible sources.

<Image align="center" alt="List of possible sources" className="border" border="#242728" width="2144" src="https://files.readme.io/ad894a6-Screen_Shot_2021-07-28_at_5.57.55_PM.png" />

You can also do this when you are adding multiple sources.

<Image align="center" alt="Display source list for multiple sources" className="border" border="#232527" width="2272" src="https://files.readme.io/9b092ac-Screen_Shot_2021-07-28_at_5.58.53_PM.png" />

# Autocomplete streams

When you are in the **Streams** section of an Allocation Dimension the available stream names will autocomplete as you type. Streams that have been created but are not available for use in a Dimension definition, either because they are too new or are invalid, will not appear as autocomplete options.

<Image align="center" alt="Autocompletion of steam names" className="border" border="#060809" width="1077" src="https://files.readme.io/cead3a8-Screen_Shot_2022-01-14_at_11.19.10_AM.png" />
