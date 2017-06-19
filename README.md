# Bioschemas Specification Process
This repository will help people interested in defining a Bioschemas Specification. This process starts with the Use Case Study and finish with the RDFa generation.

![Bioschemas Specification Process](../master/img/specification_process.jpg)

Here you will find all the templates and documentation needed to be familiar with the Specification Process.
>Please take into account that this repository is under construction, so suggestions and comments are welcome.

In the following README you will have the process to create:
1. Use Case Study
1. Mapping
1. Specification
1. Markdown
1. RDFa

>These explanations will be supported by an example of the **Bioscheas Tools Specification**.

## USE CASE STUDY
> Section under construction.

## MAPPING

After Defining the properties, the Schema.org type and you will need to follow the steps bellow to get the new Specification Structure.

1. Make a copy of the [mapping template](https://drive.google.com/open?id=0Bw_p-HKWUjHoQ2RkUUthWVd3RG8) naming the file **<SPECIFICATION_NAME> mapping** and locating it in the [Bioschemas Drive Folder](https://drive.google.com/open?id=0Bw_p-HKWUjHoNThZOWNKbGhOODg) whitin the **<SPECIFICATION_NAME> folder**.
> Folder for Bioschemas Tool Specification

![Bioschemas Tool Folder](../master/img/specification_folder.png)

2. Open the Mapping template and you will find the following structure.

![Bioschemas Tools Mapping empty file](../master/img/mapping_empty_file.png)

+ **schema.org**: These columns are copy -pasted from the schema.org type definition page.
  1. **Property:** Name of the property from the selected schema.org type.
  1. **Expected Type:** Expectedd type for the property suggested by schema.org selected type.
  1. **Description:**: Description of the property from the schema.org vocabulary for the selected type.
+ **bioschemas:** These columns are defined for the properties that will be in the Bioschemas Specification file.
  1. **SubProperties:** The subproperties of an specific property, should be listed inn the following format <subProperty_Name>: <subProperty_Type> and if you have multiples subproperties they should be separated by coma (,) as in this example  <subProperty_Name1>: <subProperty_Type1>, <subProperty_Name2>: <subProperty_Type2>, <subProperty_Name3>: <subProperty_Type3>... and so on.
  1. **Minimum Fields:** The template gives three options for the property specification of the new Bioschemas Type, Minimum, Recomended or Optional. 
  1. **Cardinalitry:**	The template gives you the two possible cardinalyties in a Bioschemas Specification (ONE or Many)
  1. **Controlled Vocabulary:** A list of words separated by comas (,) or a list of ontologies following the syntax <Ontology_Name>:<Ontology_URL>, if you need to put more than one separate eachontology with comas (,).
+ **USE CASE**
  - **USE CASE NAME**
  - **USE CASE URL**
  - **CONTRIBUTOR1, CONTRIBUTOR2,...**: List of Contributors that worked in the description of this Use Case.
    1. Name: Name for the Use Case (This field is only needed to double check or compare the diferent names that this property has across the diffente Use Cases, and with this define the BioSchema property name).
    1. Content Example: Example of the Use Case.
    1. UseCase: Three possible options for the Specifications Mapping 
        - Match: If the use case matches with a Schema.org property.
        - jhjgjkg


3. Go to the schema.org and find the definition of the type you want to reuse in the Bioschemas Structure

4. Copy the entire Type definition table and paste into your mapping starting in **A6 Cell**.
5. Item 3b
## SPECIFICATION

## MARKDOWN

## RDFa



