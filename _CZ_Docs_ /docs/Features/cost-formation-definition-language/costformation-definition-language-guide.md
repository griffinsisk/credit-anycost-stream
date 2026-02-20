---
title: Guide to Using the CostFormation Definition Language
category: features
createdAt: '2021-08-27T21:07:34.097Z'
hidden: false
metadata:
  title: Guide
slug: costformation-definition-language-guide
updatedAt: '2022-01-25T17:41:18.306Z'
---
This section will help you understand how to create Custom Dimensions using the CostFormation language to build Dimension definitions. CostFormation defines a syntax which is based on  [YAML](https://en.wikipedia.org/wiki/YAML) and is used to define the properties of a **Custom Dimension**, the rules that define the **Elements** of the dimension, and the **conditions** under which **charges** are placed into the element. For more information, see [Allocation Short Form Rules](/docs/allocation-short-form-rules).

<Callout icon="ℹ️" theme="info">
  The following defines key terms:

  **Dimension**: A way of viewing your cloud costs broken down into different groups or **Elements**.

  **Custom Dimension**:  A Dimension created with custom logic specific to your organization that allows you to view your cloud costs in the context of your business or engineering needs.

  **Element**: A group of related charges within a Dimension.

  **Charge**: A single line item of cloud cost or collection of cloud costs.
</Callout>

# YAML syntax

YAML is a human friendly data serialization language that works well with other programmatic languages. If you are not familiar with YAML, you can do a simple search for `YAML Tutorial` using your favorite search engine and find many sites and videos that can teach you the basics of YAML. For some quick information and links, you can visit the [YAML Wikipedia](https://en.wikipedia.org/wiki/YAML) page.

YAML relies on white space (spaces, indexes, and newlines) to create structure within a YAML document. Any line or lines that are indented using one or more spaces from a previous line are considered to be part of the structure of the previous line. For example:

```yaml
Root:
  Property1: Value1
  Property2:
    Property2-A: Value2-A
    Property2-B: Value2-B
  Property3:
    Property3-A: Value3-A
```

In the preceding example, `Root` is an object that contains the properties `Property1`, `Property2`, and `Property3` as they are indented by two spaces in from `Root`. `Property1` is assigned the value `Value1` while `Property2` is another object containing the properties `Property2-A` and `Property2-B`. The end of `Property2` is indicated by `Property3` as it is indented at the same level as `Property1` and `Property2` and is therefore a part of the object `Root`.

For CostFormation, you must be familiar with these key YAML constructs: key/value pairs, lists, and objects.

## Key/value pairs

Key/value pairs are used to create properties and assign them values. For example:

```yaml
Animal: Dog
Breed: Pug
Age: 5
```

In the preceding example, the keys are `Animal`, `Breed`, and `Age`. Their respective values are `Dog`, `Pug`, and `5`. Keys must be a string, while property values can be strings, integers, boolean values (that is, True or False), lists, and objects.

## Lists

In YAML, the value in the Key/Value pair can be a list. Lists can be denoted in the following ways: with indented lines that start with dashes:

```yaml
Toys:
  - Car
  - Ball
  - Doll
```

OR as a comma delimited list within square brackets:

```yaml
Toys: [Car, Ball, Doll]
```

The preceding examples are equivalent.

## Objects

In YAML, the value in the Key/Value pair can be another object with its own key/value pair. For example:

```yaml
Ball1:
  Sport: Soccer
  Color: Black and White
  Material: Leather
Ball2:
  Sport: Football
  Color: Brown
  Material: Leather
```

The preceding example shows `Ball1` and `Ball2` as objects with properties defining attributes of each ball.

# CostFormation Definition File

All Custom Dimension definitions are placed in a single CostFormation Definition File which can be downloaded from CloudZero, edited to add, remove, or modify your Custom Dimensions, and then uploaded to publish the new Custom Dimensions. This file contains the YAML based definitions for one or more Custom Dimensions.

The CostFormation Definition File must contain the root key `Dimensions` followed by one or more Custom Dimension definitions. Each definition comprises a key, which is the Dimension's ID, and a set of properties which define the attributes of the Custom Dimension. The basic structure will look as follows:

```yaml
Dimensions:
  <Dimension 1 Id>:
    <Dimension 1 Properties>
  <Dimension 2 Id>:
    <Dimension 2 Properties>
  ...
  <Dimension N Id>:
    <Dimension N Properties>
```

For example:

```yaml
Dimensions:
  Country:
    Name: Custom Country Dimension
    DefaultValue: global
    Child: Region
    Rules:
      - Type: GroupBy
        Source: Region
        Transforms:
          - Type: Split. # This transform splits a string on '-' and takes the first item
            Delimiter: '-'  # For example, if the source value is "us-east-1" it would be transformed to "us"
            Index: 1
          - Type: Lower # Lowercases the string; for example "US" would become "us"

  AccountName:
    Name: Account Name
    Disable: true
    Source: Account
    Groups:
        Prod Feature A:
          - Equals: 0123456789010  # Any account with id 0123456789010 will be grouped under "Prod Feature A"
        Prod Feature B:
          - Equals: 0123456789011
        Dev Feature A:
          -Equals:
            - 0123456789012  # Any account with either id 0123456789012 or 0123456789013 will be grouped under "Dev Feature A"
            - 0123456789013
        Dev Feature B:
          - Equals:
            - 0123456789014
            - 0123456789015
```

The preceding definitions file declares two new dimensions: `Country` and `AccountName`.

# Defining a Custom Dimension

A Custom Dimension definition consists of a unique ID and a set of properties that define attributes of the Dimension, such as its name or whether it should be made visible to users in CloudZero or not, as well as the rules that define the dimension. A Custom Dimension may also optionally specify a default source to be used in the rules and conditions for the definition.

A Custom Dimension definition has the following structure:

```yaml
  <DimensionId>:
    Name: <Dimension Name>
    Hide: <True|False>
    Disable: <True|False>
    Child: <Another Dimension>
    DefaultValue: <Default Element Name>

    <Source Properties>
    <Rules> | <AllocateByStreams> | <AllocateByRules>
```

The `DimensionId` is a unique identifier that can be used when referencing this Custom Dimension as a source value in other Custom Dimensions. The `DimensionId`will also be used as the visible name of the Dimension if the `Name` property is not specified.

The following are the properties of a dimension definition.

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Required?</th>
      <th>Available For</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><p>Name</p></td>
      <td><p>String</p></td>
      <td><p>No</p></td>
      <td><p>All</p></td>
      <td><p>This property provides a user visible name for the custom dimension. This is the name that will be visible in areas such as the Explorer. If not present, the ID will be used as the name.</p></td>
    </tr>

    <tr>
      <td><p>Hide</p></td>
      <td><p>Boolean</p></td>
      <td><p>No</p></td>
      <td><p>All</p></td>
      <td><p>If set to <em>True</em>, the dimension will not be visible in CloudZero, but the dimension can be used as a source for other dimensions. Otherwise the dimension will be visible to all users. This allows you to create some dimensions that are not meant to be used directly by your users, but rather are meant to be building blocks for other dimensions.</p></td>
    </tr>

    <tr>
      <td><p>Disable</p></td>
      <td><p>Boolean</p></td>
      <td><p>No</p></td>
      <td><p>All</p></td>
      <td><p>If set to <em>True</em> this dimension will not be compiled and will not be visible in CloudZero and cannot be used as a source for other dimensions. It allows you to remove the dimension without fully deleting it. If this is not set, it will default to <em>False</em>.</p></td>
    </tr>

    <tr>
      <td><p>Child</p></td>
      <td><p>String</p></td>
      <td><p>No</p></td>
      <td><p>All</p></td>
      <td><p>This property identifies the next logical dimension in the hierarchy. Currently, this field's value is used to determine the next GroupBy value when drilling down in the Explorer. Any valid Source is a valid Child. For example, the Child of <code>PaymentOption</code> is <code>Service</code>, meaning when viewing data grouped by <code>PaymentOption</code> the next logical grouping is <code>Service</code>.</p></td>
    </tr>

    <tr>
      <td><p>Override</p></td>
      <td><p>String</p></td>
      <td><p>No</p></td>
      <td><p>Group dimensions only</p></td>

      <td />
    </tr>

    <tr>
      <td><p>DefaultValue</p></td>
      <td><p>String</p></td>
      <td><p>No</p></td>
      <td><p>All</p></td>
      <td><p>This property indicates the name of the <em>Element</em> to place any charge that does not match any rules in the definition.</p>
      <p>See <a href="#applying-rules">Applying Rules</a> for more information on how this property is used.</p></td>
    </tr>

    <tr>
      <td><p>\<Source Properties></p></td>
      <td><p>Collection of properties</p></td>
      <td><p>No</p></td>
      <td><p>All</p></td>
      <td><p>This is a collection of properties that identify source dimensions as well as ways to manipulate the incoming data before rules and conditions are applied.</p>
      <p>See <a href="#specifying-sources">Specifying Sources</a> for more information on the source properties.</p></td>
    </tr>

    <tr>
      <td><p>Type</p></td>
      <td><p>String</p></td>
      <td><p>No</p></td>
      <td><p>All</p></td>
      <td><p>This defines the type of custom dimension. Possible values are "Allocation" or "Grouping". If omitted, it will default to "Grouping"</p></td>
    </tr>

    <tr>
      <td><p>\<Rules></p></td>
      <td><p>Object or list of objects</p></td>
      <td><p>Yes</p></td>
      <td><p>Group dimensions only</p></td>
      <td><p>This section contains the rules and conditions for grouping the sources into elements.</p>
      <p>See <a href="#adding-rules">Adding Rules</a> for the different rule structures.</p></td>
    </tr>

    <tr>
      <td><p>AllocateByStreams | AllocateByRules</p></td>
      <td><p>Object or list of objects</p></td>
      <td><p>Yes</p></td>
      <td><p>Allocation dimensions only</p></td>
      <td><p>This section defines how the cost allocations will be split. See <a href="#adding-allocations">Adding Allocations</a> for more information on creating allocations.</p></td>
    </tr>
  </tbody>
</table>

# Overriding default Dimensions

There are a number of Custom Dimensions that are provided by default to all customers. The definitions for these Dimensions are maintained by CloudZero. If for some reason the default definition of a particular Dimension does not suit your particular needs, you may override the it with your own definition in your custom definition file. You can do this by setting the `Override` field in your custom dimension to reference the default Dimension you wish to override.

For example:

```yaml
  Elasticity:
    Name: Elasticity
    Override: CZ:Defined:Elasticity
    ....
```

The `Override` field is required in order to override the default Dimension. Without this field, the preceding definition would fail validation because the name `Elasticity` collides with the name of the default Dimension `CZ:Defined:Elasticity`. However, by adding the `Override` field and the ID of the default Dimension, `CZ:Defined:Elasticity`, you are explicitly specifying that you want this definition to be used in place of the default Definition.

Any other Dimensions, whether in the default Ddimensions definitions or in your own custom definitions, that reference the overridden default Dimension, will be automatically adjusted to reference the new dimension in your custom definitions.

<Callout icon="ℹ️" theme="info">
  The following capabilities and restrictions apply when overriding default Dimensions:

  * Only default Dimensions can be overridden. You cannot specify another Custom Dimension from the `User:Defined` namespace as the override target.
  * A default Dimension can only be overridden by one custom Dimension.
  * All Dimension names, whether a default Dimension or a custom Dimension, must be unique, unless the matching names are from a Custom Dimension and the default Dimension it is overriding.
  * When you are specifying that a Custom Dimension overrides a default Dimension, neither the ID nor the name of the Custom Dimension needs to match those of the overridden default Dimension. Either or both may be different.
</Callout>

See [Additional Cloud Provider Dimensions](doc:dimensions#additional-cloud-provider-dimensions) for a list of default dimensions or [Default Dimension Definitions](doc:default-dimension-definitions) for their current definitions.

# Specifying sources

When you are defining a Custom Dimension, you must designate the source of the data against which the rules and conditions are applied. Any other dimension can be used as a source, including Core Dimensions, Tag Dimensions, Kubernetes Dimensions, CloudZero-provided Dimensions, and other Custom Dimensions. For a full list of Dimensions and their source IDs, see the [reference documentation](doc:cfdl-reference#sources).

Sources can be specified in different locations of a Custom Dimension definition. They can be defined in the root of the definition as well as in a rule or in a condition. Source properties are inherited but can be overridden. This means that any sources specified at the root level of the definition will be applied to any rules and conditions that do not have a source specified within the rule or condition. Likewise, a source specified at the rule level will be applied to all conditions within the rule unless a source is specified within the condition. Any rule or condition that specifies its own source properties will use those source properties and ignore any inherited source properties.

For example:

```yaml
  Environment:
    Name: Environment
    Source: Account
    Rules:
      - Type: Group
        Name: Production
        Conditions:
          - Equals:
              - 123456789010
              - 123456789011
              - 123456789012
      - Type: Group
        Name: DevOps
        Conditions:
          - Source: CZ:Defined:Category
            Equals: Cloud Management
          - Source: Service
            Contains: Support
      - Type: Group
        Name: Development
        Conditions:
          - Equals:
            - 123456789013
            - 123456789014
```

In the preceding example, the source dimension, `Account`, is specified in the root of the definition and is used by default for any rule or condition that does not specify its own source. So in the first rule (`Name: Production`) the condition checks if `Account` is equal to `123456789010`, `123456789011`, or `123456789012`. However, in the second rule (`Name: DevOps`) the conditions both specify a source. So the first condition in that second rule checks if the source `CZ:Defined:Category` equals `Cloud Management` or if the source `Service` equals `Support`. The third rule (`Name: Development`) uses the `Account` as its source.

Sources can always be specified using a collection of properties.

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Required</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><p>Source (or Sources)</p></td>
      <td><p>String or a list of strings.</p></td>
      <td><p>Yes</p></td>
      <td><p>This property identifies one or more source dimensions. It specifies a single dimension as a string or multiple sources as a list of strings. </p>
      <p>If this property is not specified, then any of the other properties are ignored. </p>
      <p>See <a href="#single-versus-multiple-sources">Single versus Multiple Sources</a> for more information on single versus multiple sources.</p></td>
    </tr>

    <tr>
      <td><p>CoalesceSources</p></td>
      <td><p>Boolean</p></td>
      <td><p>No</p></td>
      <td><p>This property determines how multiple sources are handled. If it is set to true, then all specified sources are coalesced and treated as a single source. If set to false, then the sources are treated individually. If it is omitted, then it is set to <code>False</code>.</p>
      <p>See <a href="#handling-multiple-sources">Handling Multiple Sources</a> for information on the affects of coalescing sources.</p></td>
    </tr>

    <tr>
      <td><p>Transforms</p></td>
      <td><p>List of one or more transforms</p></td>
      <td><p>No</p></td>
      <td><p>This property specifies one or more transforms to apply to the sources. Transforms are applied in the order they are specified in this list.</p>
      <p>See <a href="#transforms">Transforms</a> for more information on transformations.</p></td>
    </tr>
  </tbody>
</table>

<Callout icon="ℹ️" theme="info">
  CloudZero-defined Dimensions differ from user-defined Dimensions.
  CloudZero defines [many useful Dimensions for you](cfdl-reference#additional-cloud-provider-dimensions) in addition to the Custom Dimensions you will define in CostFormation. Note the `Sources:` syntax difference between CloudZero-defined dimensions and your own defined dimensions:

  CloudZero defined dimensions: `Source: CZ:Defined:<DimensionId>`
  User defined dimensions: `Source: User:Defined:<DimensionId>`

  In addition, it is important to note that inheriting source properties differs from overriding source properties.

  Source properties are either inherited or overridden as a whole set. Therefore when a rule or a condition inherits a source, it inherits all of the properties, including transforms and whether to coalesce or not.

  However, if the `Source` or `Sources` property is specified in the rule or condition, then all source properties are overridden. If a condition or rule specifies the `Source` property, but the property `Transforms` is not specified, the transforms from the outer source are not inherited. In that case, no transforms would be applied to the source specified in the override.

  Also, to override the source, the `Source` or `Sources` property must be specified. If `Transforms` is specified but `Source` or `Sources` is not, then `Transforms` is ignored.
</Callout>

## Single versus multiple sources

When you are specifying sources, you can specify either a single source as a string, or multiple sources as a list of strings.

For example:

```
Source: Account
```

This specifies the dimension `Account` as a single source, whereas:

```
Sources:
  - Tag:Name
  - Resource
```

specifies `Tag:Name` and `Resources` as multiple sources.

<Callout icon="ℹ️" theme="info">
  The property name `Source` and `Sources` are aliases of each other and are completely interchangeable. There is no requirement to use one or the other when specifying single or multiple sources.
</Callout>

## Handling multiple sources

When multiple sources are specified, you can specify whether they should be coalesced or handled as individual sources. This impacts both how conditions are applied to the sources as well as the element names of dynamic elements when multiple sources are used in [_GroupBy_](doc:costformation-definition-language-guide#rule-types) rules.

Coalescing sources means that the value used will be the value of the first source in the list of sources that has an actual value, that is, is not null. For example:

```yaml
  Sources:
    - Tag:Environment
    - Tag:Env
    - Tag:environment
```

If `Tag:Environment` has a value, it will be used as the source value and the values in `Tag:Env` and `Tag:environment` will be ignored. However, if `Tag:Environment` does not have a value but `Tag:Env` does, then the value from `Tag:Env` is used. This feature is useful for situations like inconsistent tag names. As in the preceding example, the feature allows the three different tags to be treated as a single tag.

How multiple sources are handled is determined by the `CoalesceSources` property. If the `CoalesceSources` property is omitted or set to `False`, then the sources are treated individually. Not coalescing multiple sources has the following effect:

* Any conditions applied to the sources are applied as an `Or` of the individual sources. For example, the following evaluates to `True` if either `Tag:Name` or `Resource` contains the text `development`.

```yaml
- Sources:
    - Tag:Name
    - Resource
  CoalesceSources: False
  Contains: development
```

* In a _GroupBy_ rule the dynamic element names will be comprised from concatenating the values from each source. Because each source value is used, all source values must be present for any charge to match the rule. If any one of the sources for a charge does not have a value, then the rule evaluates to `False`.

If `CoalesceSources` is set to `True`, then the sources are coalesced and treated as a single source, using the first source that has a value. Sources are checked in the order they are specified. Consider the following example:

```yaml
- Sources
  - Tag:Name
  - Resource
  CoalesceSources: True
  Contains: development
```

For any charge checked against the condition, the source value will be the value of `Tag:Name` if it has a value. Otherwise, the source value will be the value of `Resource`. Therefore the preceding example will evaluate to `True` if the first non-null value of `Tag:Name` or `Resource` contains the text `development`.

The following table shows the differences between applying the condition using the preceding examples:

<table>
  <thead>
    <tr>
      <th>Tag:Name</th>
      <th>Resource</th>
      <th>Result if CoalesceSource=False</th>
      <th>Result if CoalesceSource=True</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><p>frontend-development</p></td>
      <td><p>gateway</p></td>
      <td><p>True</p></td>
      <td><p>True</p></td>
    </tr>

    <tr>
      <td><p>frontend</p></td>
      <td><p>gateway-development</p></td>
      <td><p>True</p></td>
      <td><p>False (condition applied to value <code>frontend</code>)</p></td>
    </tr>

    <tr>
      <td><p>null</p></td>
      <td><p>gateway-development</p></td>
      <td><p>True</p></td>
      <td><p>True (condition applied to value <code>gateway-development</code>)</p></td>
    </tr>
  </tbody>
</table>

In addition. when `CoalesceSources` is set to `True` in a _GroupBy_ rule, the dynamic element names will contain the single coalesced value. Based on the preceding table, the dynamic element names would be: `frontend-development`, `frontend`, and `gateway-development`.

## Transforms

When you are specifying sources, you can optionally specify a list of one or more transformations to apply to the sources. Transforms are ways to modify the source values to do things like lowercase them or extract substrings. Transforms are applied to the sources after coalescing (if coalescing is applied), but before conditions are applied. The result of the transforms is also used when the source data is generating dynamic element names.

Transforms are useful for cleaning your source data before applying conditions or generating dynamic element names to handle problems like inconsistent capitalization or inconsistent use of special characters. They are also useful for extracting substrings out of complex sources for better consistency in applying conditions, or better groupings of dynamic elements.

Transforms have the following structure:

```yaml
  Transforms:
    - Type: <Transform 1 Name>
      <Transform 1 Parameters>
    - Type: <Transform 2 Name>
      <Transform Parameters>
    ...
    - Type: <Transform N Name>
      <Transform N Parameters>
```

Transforms are applied in the order they are specified. The input for the first transform is the raw source value, while the input for the second transform would be the result of the first transform, and so on. The final value would be the result of the last transform.

For example:

```yaml
  Transforms:
    - Type: Split
      Delimiter: '-'
      Index: 1
    - Type: Lower
```

In the preceding example, the source is split into substrings using the dash (-) character and the first index is taken (the index is one-based) and the result is then made lowercase. Thus, if the source was `Gateway-Development`, the result of the transform would be `gateway`.

For the list of available transforms and their parameters, see the [reference page](doc:cfdl-reference#transforms).

# Adding rules

Each dimension definition contains a list of one or more CostFormation rules that determine how charges are grouped in elements. Rules tie together sources and conditions to create either statically named elements or dynamically named elements.

Rules are specified as follows:

```yaml
  <DimensionId>:
    Name: <Name>
    ...
    Rules:
      - Type: <Rule 1 Type>
        <Rule 1 Properties>
      - Type: <Rule 2 Type>
        <Rule 2 Properties>
      ...
      - Type: <Rule N Type>
        <Rule N Properties>
```

## Rule types

The types of rules are `Group`, `GroupBy`, and `Metadata`.

### `Group` rules

`Group` rules are used to create statically named elements. These rules are specified as follows:

```yaml
  - Type: Group
    Name: <Element Name>
    <Source Properties>
    Conditions:
       - <List of conditions>
```

The properties for a `Group` rule are:

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Required</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><p>Type</p></td>
      <td><p>String</p></td>
      <td><p>Yes (must be set to <code>Group</code>)</p></td>
      <td><p>This property indicates that the rule is a <em>Group</em> rule.</p></td>
    </tr>

    <tr>
      <td><p>Name</p></td>
      <td><p>String</p></td>
      <td><p>Yes</p></td>
      <td><p>This property specifies the name of the element.</p></td>
    </tr>

    <tr>
      <td><p>\<Source Properties></p></td>
      <td><p>Collection of properties</p></td>
      <td><p>No</p></td>
      <td><p>These properties indicate the default source to use for any conditions within this rule. If not specified, then the source specified for the dimension will be used.</p>
      <p>See <a href="#specifying-sources">Specifying Sources</a> for more information.</p></td>
    </tr>

    <tr>
      <td><p>Conditions</p></td>
      <td><p>List of conditions</p></td>
      <td><p>Yes</p></td>
      <td><p>This property specifies a list of one or more conditions that must evaluate to <code>True</code> for charges to be grouped in the specified element.</p>
      <p>See <a href="#adding-conditions-to-a-rule">Adding Conditions to a Rule</a> for more information.</p></td>
    </tr>
  </tbody>
</table>

For example:

```yaml
  - Type: Group
    Name: Test
    Source: Account
    Conditions:
      - Equals: 123456789010
```

With this rule any charges where the `Account` is equal to `123456789010` are placed in the `Test` element.

### `GroupBy` rules

GroupBy rules are used to create dynamic elements based on values from the sources. These rules are specified as follows:

```yaml
  - Type: GroupBy
    Format: <Element Name>
    <Source Properties>
    Conditions:
       <List of conditions>
```

The properties for a _GroupBy_ rule are:

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Required</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><p>Type</p></td>
      <td><p>String</p></td>
      <td><p>Yes (must be set to <code>GroupBy</code>)</p></td>
      <td><p>This property indicates that the rule is a <em>GroupBy</em> rule.</p></td>
    </tr>

    <tr>
      <td><p>Format</p></td>
      <td><p>String</p></td>
      <td><p>No</p></td>
      <td><p>This property specifies how to output the source values into dynamic element names. The contents of this property depend on whether the sources are coalesced or not. If not specified the source values will be concatenated with a space between each source.</p>
      <p>See the note that follows this table on formatting elements for more information on how to format element names.</p></td>
    </tr>

    <tr>
      <td><p>\<Source Properties></p></td>
      <td><p>Collection of properties</p></td>
      <td><p>Yes</p></td>
      <td><p>These properties indicate the source to use for generating element names. It will also be used for any conditions within this rule that do not specify a separate source.</p>
      <p>The source values must be non-null for charges to match this rule.</p>
      <p>See <a href="#specifying-sources">Specifying Sources</a> for more information.</p></td>
    </tr>

    <tr>
      <td><p>Conditions</p></td>
      <td><p>List of conditions</p></td>
      <td><p>No</p></td>
      <td><p>This property specifies a list of one or more conditions that must evaluate to <code>True</code> for charges to be grouped in the specified element.</p>
      <p>See <a href="#adding-conditions-to-a-rule">Adding Conditions to a Rule</a> for more information.</p></td>
    </tr>
  </tbody>
</table>

For example:[https://docs.cloudzero.com/docs/costformation-definition-language-guide#/groupby-rulesver](https://docs.cloudzero.com/docs/costformation-definition-language-guide#/groupby-rulesver)

```yaml
  - Type: GroupBy
    Format: 'Service {0} -- Region {1}'
    Source:
      - Service
      - Region
    Conditions:
      - Source: Account
        Equals: 123456789010
```

In this example elements will be created by combining the sources `Service` and `Region` using the format string, but only for line items where `Account` equals `123456789010`.

<Callout icon="ℹ️" theme="info">
  When you are specifying the format for elements in a `GroupBy` rule, the format string uses zero-based indexes to match to the sources. In the example `'Service {0} -- Region {1}'`, the `{0}` is replaced with the first source, `Service`, while `{1}` is replaced with the second source `Region`.

  The format string must include indexes for each source and only for each source. For example, `'Service {0}'` would be invalid because there is no index for `Region` while `'Service {0} -- Region {1} -- Country {2}'` would be invalid because there is no source to match with `{2}`.

  If the `Format` property is omitted, the sources are concatenated with a space in-between them. In the preceding example the default `Format` would have been `'{0} {1}'`.

  If sources are specified to be coalesced, then the format string should only indicate a single index  (i.e. `{0}`). When sources are coalesced, it is the equivalent of specifying a single source.
</Callout>

### `Metadata` Rules

`Metadata` rules are a type of static grouping rule where the element name and the condition are related. These rules are useful to group elements based on substrings within another dimension such as tags or resource names. When specifying a metadata matching rule, a list of metadata values are provided. The rule will check each of the sources to see if they contain that metadata value or any of its alternatives. When a match is found, the charges are grouped into an element name generated using the specified format and the matching metadata value.

These rules are specified as follows:

```yaml
  - Type: Metadata
    Format: <Element Name>
    <Source or Sources>
    Conditions:
       <List of conditions>
    Values:
       <List of metadata values>
```

The properties for a _Metadata_ rule are:

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Required</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><p>Type</p></td>
      <td><p>String</p></td>
      <td><p>Yes (must be set to <em>Metadata</em>)</p></td>
      <td><p>This property indicates that the rule is a <em>Metadata</em> rule.</p></td>
    </tr>

    <tr>
      <td><p>Format</p></td>
      <td><p>String</p></td>
      <td><p>No</p></td>
      <td><p>This property specifies how to output the metadata values into element names. The  format string must be written for a single source and therefore must have one placeholder.</p>
      <p>See the note below on <strong>Formatting Elements</strong> for more information on how to format element names.</p></td>
    </tr>

    <tr>
      <td><p>\<Source or Sources></p></td>
      <td><p>Property</p></td>
      <td><p>Yes</p></td>
      <td><p>These properties indicate a single source or multiple sources to use for the metadata matching. It will also be used for any conditions within this rule that do not specify a separate source.</p>
      <p>The source values must be non-null for charges to match this rule.</p>
      <p>See <a href="#specifying-sources">Specifying Sources</a> for more information.</p>
      <p>Unlike other rules, <em>Transforms</em> are not supported along with these sources.</p></td>
    </tr>

    <tr>
      <td><p>Conditions</p></td>
      <td><p>List of conditions</p></td>
      <td><p>No</p></td>
      <td><p>This property specifies a list of one or more conditions that must evaluate to <code>True</code> before the metadata matches are applied.</p>
      <p>See <a href="#adding-conditions-to-a-rule">Adding Conditions to a Rule</a> for more information.</p></td>
    </tr>

    <tr>
      <td><p>Values</p></td>
      <td><p>List of strings or string and arrays of strings.</p></td>
      <td><p>Yes</p></td>
      <td><p>This property specifies the metadata to match and element names to generate. Charges will be checked to see if the the source contains the metadata value, and if so, it will be grouped in an element named after that metadata value.</p></td>
    </tr>
  </tbody>
</table>

For example:

```yaml
  - Type: Metadata
    Format: 'Metadata Match: {0}'
    Source:
      - Tag:Name
      - Resource
    Conditions:
      - Source: Account
        Equals: 123456789010
    Values:
       - -Web-:
          - -UI-
          - Frontend
       - Order-Processing
       - Order-Staging:
          - WebOrderStaging
       - Order-Fulfillment
```

In this example, only charges from account `123456789010` will be checked. For all those charges, the `Tag:Name` and `Resource` dimensions will be checked to see if they contain any of the specified metadata values in the order they are presented in the `Values` property. The element names will be generated using the specified format so that there would be elements named `Metadata Match: Web`, `Metadata Match: Order-Processing`, `Metadata Match: Order-Staging`, or `Metadata Match: Order-Fulfillment`.

### Metadata value requirements and element names

The sources specified for metadata rules are always normalized, which turns any special characters into a dash (`-`) and uses a case insensitive comparison. Therefore, metadata values may only contain letters, numbers, and dashes (`-`). If any other characters are specified, a validation failure will occur.

Element names generated from the specified metadata values will have their case preserved. Using the preceding example, a charge with `order-staging` in `Tag:Name` will be placed in an element name `Metadata Match: Order-Staging`.

Any metadata values that contain a leading or trailing dash (`-`) will only use those characters during matching. The element name will have the leading or trailing dash or both removed.

Using the preceding example, any charges containing the text `-web-` will be grouped in the element `Metadata Match: Web`.

### Specifying alternatives

Sometimes you may want to specify alternatives to a metadata value. This can be useful when non-uniform tagging has occurred. Alternatives are specified by an array of alternatives after the metadata value. If any of those alternatives are found in the source, the charges will be grouped with the first specified metadata value.

Using the preceding example, the metadata values `-Web-` and `Order-Staging` have alternatives specified. Any charges containing either `-ui-` or `frontend` will be grouped along with any containing `-Web-` while charges containing `WebOrderStaging` will be grouped with any containing `Order-Staging`.

## Applying rules

Rules are applied in a top-down fashion based on the order the rule is specified. This means that for all charges, the conditions for the first rule in the definition are evaluated before the second rule, and so on. Therefore, the order in which rules appear in your definitions is important and can affect how charges are broken down into elements.

Using the following example:

```yaml
  Environment:
    Name: Environment
    Source: Account
    Rules:
      - Type: Group
        Name: Alfa
        Conditions:
          - Equals: 123456789010
      - Type: Group
        Name: R&D
        Conditions:
          - Source: CZ:Defined:Category
            Equals: Cloud Management
          - Source: Service
            Contains: Support
      - Type: Group
        Name: Production
        Conditions:
          - Equals:
            - 123456789011
            - 123456789012
          - And:
            - Equals: snowflake1234
            - Source: ProductFamily
              Equals: warehouse
            - Source: Resource
              Contains: prod
          - And:
            - Equals: snowflake1234
            - Source: ProductFamily
              Equals: database
            - Source: Resource
              Equals: live_billing
```

the conditions of the first rule (`Name: Alfa`) are checked before the conditions for the second rule (`Name: R&D`). Using these rules, all charges where the `Account` is equal to `123456789010` are placed in the `Alfa` element. For any charge whose `Account` is not equal to `123456789010` the charge will next be checked to see if `CZ:Defined:Category` is equal to `Cloud Management` or `Service` contains `Support`.

If all rules evaluate to `False`, then the charge will be grouped with other charges that do not match any rules. If a `DefaultValue` is specified, then the charges are grouped under that element. Otherwise they will be considered `unallocated` and will not be considered part of this Dimension.

### Default value versus unallocated

When charges do not match any rule, there is a distinct difference between having a `DefaultValue` property for a Dimension or not. When no `DefaultValue` is specified, all charges not matching any rules are considered *`unallocated`. However, if `DefaultValue` is specified, then all charges not matching any rule will be placed in the element defined by `DefaultValue'.

When you are filtering in the Explorer, if you choose to filter all charges where the Dimension **Does Not Have a Value**, the Explorer will only show **unallocated** charges. If a `DefaultValue` was specified, those charges are considered **allocated** to the element named in `DefaultValue` and therefore would not show up when this filter is applied.

### Combining rule types

When you are creating a Custom Dimension definition, you can combine rule types such that that some elements are statically defined while others are dynamically defined. Consider the earlier environment Dimension example. Perhaps there are some resources that are not in any of the defined accounts, but are tagged with a special environment tag. You could define the dimension as follows:

```yaml
  Environment:
    Name: Environment
    Source: Account
    Rules:
      - Type: Group
        Name: Alfa
        Conditions:
          - Equals: 123456789010
      - Type: Group
        Name: R&D
        Conditions:
          - Source: CZ:Defined:Category
            Equals: Cloud Management
          - Source: Service
            Contains: Support
      - Type: Group
        Name: Production
        Conditions:
          - Equals:
            - 123456789011
            - 123456789012
          - And:
            - Equals: snowflake1234
            - Source: ProductFamily
              Equals: warehouse
            - Source: Resource
              Contains: prod
          - And:
            - Equals: snowflake1234
            - Source: ProductFamily
              Equals: database
            - Source: Resource
              Equals: live_billing
      - Type: GroupBy
        Source: Tag:Environment
```

In the preceding definition, the addition of the last `GroupBy` rule will capture any charges that did not match the previous rules and check whether the associated resource has a value in the `Tag:Environment`. For those charges that have a value in `Tag:Environment`, the rule will create elements based on the values in that tag. If the tag values include the values `Alfa`, `R&D`, or `Production`, those charges will be grouped into the same element as the ones defined with the `Group` rule.

## Adding conditions to a rule

Conditions are the logic operations that are applied to sources to determine whether a charge should be included in a given rule. Conditions are structured as follows:

```yaml
  Conditions:
    - <Condition 1 Name>: <Condition 1 Values>
    - <Condition 2 Name>: <Condition 2 Values>
    ...
    - <Condition N Name>: <Condition N Values>
```

### Condition types

There are a few different types of conditions which allow you to compare source values against one or move values, compare whether sources have a value or not, or perform a logical operation that combines other conditions in a logical `And` or `Or` to create more complex conditions. Each condition type has a different structure.

### String comparison operations

String comparison operations compare the source value against one or more provided values. These operations are used to evaluate things like whether a given source equals one or more values, or a source contains one or more values as a substring.

Comparison can take either a single value. They have one of the following structures:

```yaml
  - <Condition Name>: <Value>
    <Source Properties>
```

Or:

```yaml
  - <Condition Name>:
      - <Value 1>
      - <Value 2>
      ...
      - <Value N>
    <Source Properties>
```

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Required</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><p>\<Condition Name></p></td>
      <td><p>String or list of strings</p></td>
      <td><p>Yes</p></td>
      <td><p>This specifies the name of the condition to apply. It must be one of the following: BeginsWith, Contains, or Equals. </p>
      <p>If a single string specified, then the source is compared against this single value. Otherwise, if a list is specified, then the condition is applied to each value as an <code>Or</code> in the order the values are specified. For example if the condition is <code>Equals</code> then it will evaluate to true if the source equals any one of the specified values.</p></td>
    </tr>

    <tr>
      <td><p>\<Source Properties></p></td>
      <td><p>Collection of properties</p></td>
      <td><p>No</p></td>
      <td><p>If specified, the condition will be applied to the specified sources along with any coalescing and/or transforms specified. If not specified, then the source from either the enclosing rule or dimension definition will be used.</p>
      <p>See <a href="#specifying-sources">Specifying Sources</a> for more information.</p></td>
    </tr>
  </tbody>
</table>

### HasValue condition

The `HasValue` condition allows you to evaluate whether a source is has an actual value or is null. It has the following structure:

```yaml
  - HasValue: <True|False>
    <Source Properties>
```

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Type</th>
      <th>Required</th>
      <th>Desccription</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><p>HasValue</p></td>
      <td><p>Boolean</p></td>
      <td><p>Yes</p></td>
      <td><p>This applies the <code>HasValue</code> operation to the source. If it is set to <code>True</code>, then the condition evaluates to <code>True</code> if the source has a value. If set to <code>False</code> then the condition evaluates to <code>True</code> if the source does <strong>not</strong> have a value.</p></td>
    </tr>

    <tr>
      <td><p>\<Source Properties></p></td>
      <td><p>Collection of properties</p></td>
      <td><p>No</p></td>
      <td><p>If specified, the condition will be applied to the specified sources along with any coalescing and/or transforms specified. If not specified, then the source from either the enclosing rule or dimension definition will be used.</p>
      <p>See <a href="#specifying-sources">Specifying Sources</a> for more information.</p></td>
    </tr>
  </tbody>
</table>

### Boolean logic operations

There are three Boolean logic operations that can be applied in conditions: `And`, `Or`, and `Not`. Each of these operations has the following format:

```yaml
  - <Logical Operator>
    - <Condition 1>
    - <Condition 2>
    ...
    - <Condition N>
```

The logical operations are applied as follows:

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><p>And</p></td>
      <td><p>All of the conditions in the list must evaluate to <code>True</code> for this condition to evaluate to <code>True</code>. If even one condition evaluates to <code>False</code>, then the whole condition evaluates to <code>False</code>.</p></td>
    </tr>

    <tr>
      <td><p>Or</p></td>
      <td><p>Only one condition in the list must evaluate to <code>True</code> for the entire condition to evaluate to <code>True</code>. Only when all conditions evaluate to <code>False</code> will the whole condition evaluate to <code>False</code>.</p></td>
    </tr>

    <tr>
      <td><p>Not</p></td>
      <td><p>The list of conditions are evaluated like an <code>Or</code>, but the final result is reversed. So if a single condition evaluates to <code>True</code>, then the whole condition evaluates to <code>False</code>. This condition only evaluates to <code>True</code> if all conditions in the list evaluate to <code>False</code>.</p></td>
    </tr>
  </tbody>
</table>

Logic operations can be nested. For example:

```yaml
  - And:
    - Or:
      - <condition 1>
      - <condition 2>
    - Not:
      - And:
        - <condition 3>
        - <condition 4>
```

This condition will evaluate to `True` only if either `condition 1`  or `condition 2` is `True` _and_ either `condition 3` or `condition 4` are `False`.

## Applying conditions

As with rules, the order conditions are listed is important. Conditions are evaluated top-down in the order presented in the list. If the first condition of a rule evaluates to `True`, then the whole condition evaluates to `True` and remaining conditions are not evaluated. If the first condition evaluates to `False` then second condition will be evaluated, and so on. If all conditions within a rule evaluate to `False`, then the rule itself evaluates to `False`. This effectively means that all of the conditions in a list are evaluated as a logical `Or` with the exception of when the list is part of the `And` logical operation.

for the list of available conditions and their parameters, see the [reference page](doc:cfdl-reference#conditions).

# Adding allocations

Allocation rules are used for an Allocation Dimension and define how shared resource costs should be split. They are defined under the `AllocateByStreams` key.

<Callout icon="ℹ️" theme="info">
  A stream must already exist within CloudZero in order to be used in a Dimension definition. You can view a  list of available telemetry streams within the application.
</Callout>

## Allocate by streams, simple telemetry allocation

An explicit allocation must be composed of a list of telemetry streams.

```yaml
Dimensions:
  Customer:
    Type: Allocation
    Name: Cost per Customer
    Hide: False
    Disable: False
    AllocateByStreams:
    Streams:
      - widget-processing-time
      - another-stream
      - active-organizations
```

A telemetry stream is comprised of utilization data sent by a customer organization to CloudZero. This data allows shared resource costs to be de-aggregated and precisely allocated. For more information on creating telemetry streams, see the [CostFormation: Allocating Shared Costs](doc:costformation-allocating-shared-costs) and [Unit Cost Analytics](doc:unit-cost-analytics) documentation.

Streams are listed in priority order and it is perfectly fine and expected that stream targets within a dimension will overlap at times. If a particular resource is targeted by multiple streams for the same time period, the higher priority stream will take precedence.

Priority order is determined top to bottom, with the first stream taking highest priority. In the preceding example, `widget-processing-time` is the highest priority stream, while `active-organizations` is the lowest.

## Allocate by streams, rate-based allocation

Rate-based allocation by streams allows the configuration of a manual allocation rate for a telemetry allocation Dimension in CostFormation. Using this feature results in a cost that depends only on provided usage and not the cost of the underlying resource within a given month.

For simple telemetry allocation by streams, the syntax is:

```yaml
 AllocateByStreams:
    Streams:
      - stream-1
      - stream-2
```

With simple telemetry allocation by streams, a Telemetry Allocation Dimension is specified by setting the AllocateByStreams property of an Allocation Dimension. This uses a single property, `Streams`, which is a list of one or more telemetry streams to use. Cost is proportionally split based on the values specified in the telemetry streams.

To use rate-based telemetry, add the optional property `Rate`:

```yaml
RateBasedAllocation:
    Type: Allocation
    AllocateByStreams:
      Rate:
        Type: Fixed
        Value: 1.23
        DefaultElement: 'Unallocated Cost' 
      Streams:
        - stream-1
        - stream-2
```

Only the `Type` value `Fixed` is supported. This specifies a fixed rate Allocation Dimension.

The cost for each line item will be determined by multiplying the rate value by the usage values specified in the telemetry stream.  To ensure the total cost is unchanged, an additional line item will be added and assigned the value specified by `DefaultElement`.

The required properties are `Type`, `Value`, and `DefaultElement`.

## Restrictions on allocations

To enforce best practices and prevent overly complex definitions that could impair your experience, CloudZero has applied several restrictions to authoring Dimensions. Each restriction has a threshold that can be adjusted by your customer success team.

These are the areas of restriction:

* The number of streams used within a single dimension definition
* The number of Allocation Dimensions that can be combined as sources
* The number of Dimensions that can combine the Resource Dimension and Allocation Dimensions as sources

Publishing an edit that violates one or more restrictions will result in a validation error along with a helpful error message.
