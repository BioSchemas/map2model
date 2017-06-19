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
    1. **Cardinalitry:**	The template gives you the two possible cardinalyties in a Bioschemas Specification (ONE or Many).
    1. **Controlled Vocabulary:** 
      + A list of words separated by comas (,) precedeed by the Word "LIST - " 
        > "<LIST - ONE, TWO, THREE...>"
  
      + A list of ontologies following the syntax <Ontology_Name>:<Ontology_URL>, if you need to put more than one separate eachontology with comas (,), the ontology list should be preceeded by the word "ONTOLOGY - ".
        > "<ONTOLOGY - ontologyname1:URL1, ontologyname2:URL2, ontologyname3:URL3...>"
   
  + **USE CASE**
    - **USE CASE NAME**
    - **USE CASE URL**
    - **CONTRIBUTOR1, CONTRIBUTOR2,...**: List of Contributors that worked in the description of this Use Case.
      1. **Name:** Name for the Use Case (This field is only needed to double check or compare the diferent names that this property has across the diffente Use Cases, and with this define the BioSchema property name).
      1. **Content Example:** Example of the Use Case.
      1. **UseCase:** Three possible options for the Specifications Mapping 
          - **Match:** If the use case matches with a Schema.org property.
          - **No Match:** If the property doesn't match with the Schema.org Property.
          - **Partial Match**: If the Use Case Property doesn't match perfectly but is a close connection with the Schema.org property.
          
> Now that all the columns of the spread sheet are explained, lets follow the next step usisng the Bioschemas Tools Specification Example.

3. Go to the schema.org and find the definition of the type you want to reuse in the Bioschemas Structure

      > For the Tools Specificationin the Use Case Study was identified that the Schema.or Type [SoftwareApplication](http://schema.org/SoftwareApplication) is the one that fits the most with all the Use Cases.
      ![Schema.org Type Definition](../master/img/schema_org_type.png)

4. Copy the Type definition table, starting from the firts Property, don't copy the table headers.

    > For the SoftwareApplication example it should look like this.
    ![Copy Schema.org Type Definition](../master/img/schema_org_type_copy.png)

5. Then paste into your mapping Spreadsheet starting in **A6 Cell**.

    >  For the Tools Specification you would have something like this.
    ![Pasting Schema.org Type Definition to the mapping Template](../master/img/schema_org_paste_template.png)


6. Fill all the Use Cases for this Specification

    >  For the Tools Specification you would have something like this. The template gives you diferent colors for the Use Case Matching (Dark blue for Match, light blue for Partial Match and light ornge for No Match).
    ![Filling the Use Cases in the Mapping Template](../master/img/fill_mapping_template_UC.png)

7. Fill the Bioschemas Fields
  + **schema.org**: These columns are copy -pasted from the schema.org type definition page.
    1. **Property:** Name of the property from the selected schema.org type.
    1. **Expected Type:** Expectedd type for the property suggested by schema.org selected type.
    1. **Description:**: Description of the property from the schema.org vocabulary for the selected type.
  + **bioschemas:** These columns are defined for the properties that will be in the Bioschemas Specification file.
    1. **SubProperties:** The subproperties of an specific property, should be listed inn the following format <subProperty_Name>: <subProperty_Type> and if you have multiples subproperties they should be separated by coma (,) as in this example  <subProperty_Name1>: <subProperty_Type1>, <subProperty_Name2>: <subProperty_Type2>, <subProperty_Name3>: <subProperty_Type3>... and so on.
    1. **Minimum Fields:** The template gives three options for the property specification of the new Bioschemas Type, Minimum, Recomended or Optional. 
    1. **Cardinalitry:**	The template gives you the two possible cardinalyties in a Bioschemas Specification (ONE or Many).
    1. **Controlled Vocabulary:** 
      + A list of words separated by comas (,) precedeed by the Word "LIST - " 
        > "<LIST - ONE, TWO, THREE...>"
  
      + A list of ontologies following the syntax <Ontology_Name>:<Ontology_URL>, if you need to put more than one separate eachontology with comas (,), the ontology list should be preceeded by the word "ONTOLOGY - ".
        > "<ONTOLOGY - ontologyname1:URL1, ontologyname2:URL2, ontologyname3:URL3...>"

    >  For the Tools Specification you would have something like this.
    ![Fill the Bioschemas Fields](../master/img/bioschemas_mapping.png)

8. Go to the Bioschemas fields Sheet to view the summary of your mapping

        > For the Tools Specification you would have something like this.
        ![Mapping Summary](../master/img/mapping_summary.png)
        > If you have fields without name is because you will add to the Schema.org you selected as basis, and you need to add the name in the specification Doc File.

## SPECIFICATION

## MARKDOWN

## RDFa



