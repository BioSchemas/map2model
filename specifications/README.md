Here is the Specification Template, that should look like the page below the line.

Download the [_Specification Template_.md](_Specification Template_.md) and fill it **[canging the content in square brackets]**

============================

# **[type] specification [version]**
Bioschemas specification for describing [type] in the life-science
***
## Quick Description
[One paragraph description.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis rutrum nibh at lorem commodo, euismod iaculis ligula fringilla. Nunc ac vestibulum neque, non viverra dui. Pellentesque accumsan nulla sit amet dapibus vulputate. Nullam mollis risus nec velit molestie pellentesque. Suspendisse a orci ipsum. Aenean faucibus nisi in justo porttitor congue. Sed porttitor et eros quis feugiat.]

> [References to supporting information like “[use cases][bs]”, “[bioschemas mapping][bs]” and “[schema.org posted issues][bs]”].

## Properties
> Based on schema.org [[Schema dot org Type]][sch_type]

### Reused from Schema.org

| Property | Expected  Type    | Description                      | CN | MG | CV|
|---------|:------------------:|----------------------------------|:--:|:--:|:--:|
| [schema.org property name] | [schema.org property type] | [schema.org description] or [bioschemas clarification if needed]| [One or Many]| [M, R or O]| [Yes or No]|


### New Properties
| Property | Expected  Type    | Description                      | CN | MG | CV|
|---------|:------------------:|----------------------------------|:--:|:--:|:--:|
| [custom name or schema.org property name if present in other type] | [schema.org property type] | [bioschemas description] | [One or Many]| [M, R or O]| [Yes or No]|
>**Legend:**
+ _**CN:** Cardinality (one, many)_
+ _**MG:** Marginality (M: minimum; R: recommended; O: optional)_
+ _**CV**: Suggested controlled vocabularies (yes, no)_

## Example

>Schema.org suggests implementing metadata using JSON-LD, RDFa or Microdata. JSON-LD is the recommended format by Google, but any of these formats can be used for embedding information about tools in a web page or other online resource.

### Example 1 - [format: RDFa | JSON-LD | Microdata].  [Example description. Eg: Using minimum fields]
```html
      <div itemscope itemtype="http://schema.org/[type]">
            <div itemprop="id">[id]</div>
        <div itemprop="name">[name]</div>
        <div itemprop="description">[description]</div>
        ...
      </div>
```

## Controlled Vocabularies

>This section contains a list of fields that require a controlled vocabulary or enumeration and suggests what is acceptable for each.

### [Property]

[Please provide a list of suggested controlled vocabularies or a list of suggested enumerations. For controlled vocabularies include references or links to the vocabulary or branch within the vocabulary. Eg: EDAM Topic. For enumerations include values and value descriptions]


[//]: # (In this secction yo put the web page links so you can reuse them.)
[bs]: <http://bioschemas.org/>
[sch_type]:<http://schema.org/Event>
