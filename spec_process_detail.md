# Bioschemas Specification Process
This repository will help people interested in defining a Bioschemas Specification. This process starts with the Use Case Study and finish with the RDFa generation.

![Bioschemas Specification Process](../master/docs/img/specification_process.jpg)
> If you want to modify the Flow Chart [Click here](https://drive.google.com/file/d/0B9lW_BhBep0Tay1XTndCaV9GSnc/view?usp=sharing) and store the result in img folder wiht the name **specification_process.jpg**.

Here you will find all the templates and documentation needed to be familiar with the Specification Process.

In the following README you have the process needed to create a Bioschemas Specification:
1. Use Case Study
1. Mapping
1. Specification
1. Markdown
1. RDFa

> For this expalantion, the **Bioscheas Tool Specification** will be used as the specification sample.

## 1. USE CASE STUDY
> Section under construction.

## 2. MAPPING

After Defining the properties, the Schema.org type and you will need to follow the steps bellow to get the new Specification Structure.

1. Make a copy of the [mapping template](https://drive.google.com/open?id=0Bw_p-HKWUjHoQ2RkUUthWVd3RG8) naming the file **<SPECIFICATION_NAME> mapping** and locating it in the [Bioschemas Drive Folder](https://drive.google.com/open?id=0Bw_p-HKWUjHoNThZOWNKbGhOODg) whitin the **<SPECIFICATION_NAME> folder**.
      > Folder for Bioschemas Tool Specification
      ![Bioschemas Tool Folder](../master/docs/img/specification_folder.png)

2. Open the Mapping template and you will find the following structure.

    ![Bioschemas Tools Mapping empty file](../master/docs/img/mapping_empty_file.png)

  + **schema.org**: These columns are copy -pasted from the schema.org type definition page.
    1. **Property:** Name of the property from the selected schema.org type.
    1. **Expected Type:** Expectedd type for the property suggested by schema.org selected type.
    1. **Description:**: Description of the property from the schema.org vocabulary for the selected type.
  + **bioschemas:** These columns are defined for the properties that will be in the Bioschemas Specification file.
    1. **BSC Description:** If is considered an additional description for the property, here can be aded an additional text that complements the schema.org description.
    1. **Marginality:** The template gives three options for the property specification of the new Bioschemas Type, Minimum, Recomended or Optional. 
    1. **Cardinalitry:**	The template gives you the two possible cardinalyties in a Bioschemas Specification (ONE or Many).
    1. **Controlled Vocabulary:** 
      + This field contains a list of terms or ontologies, terms are words, that are separated by a coma, and an onlology is composed by a name_space:url.
      > This are three possible accepted values:
      > 1. red, green, blue, pallete3:htt://ontlology.pallete3.org
      > 1. pallete1:htt://ontlology.pallete1.org, pallete2:htt://ontlology.pallete2.org, pallete3:htt://ontlology.pallete3.org
      > 1. red, green, blue, white
   
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
      ![Schema.org Type Definition](../master/docs/img/schema_org_type.png)

4. Copy the Type definition table, starting from the firts Property, don't copy the table headers.

    > For the SoftwareApplication example it should look like this.
    ![Copy Schema.org Type Definition](../master/docs/img/schema_org_type_copy.png)

5. Then paste into your mapping Spreadsheet starting in **A6 Cell**.

    >  For the Tools Specification you would have something like this.
    ![Pasting Schema.org Type Definition to the mapping Template](../master/docs/img/schema_org_paste_template.png)


6. Fill all the Use Cases for this Specification

    >  For the Tools Specification you would have something like this. The template gives you diferent colors for the Use Case Matching (Dark blue for Match, light blue for Partial Match and light ornge for No Match).
    ![Filling the Use Cases in the Mapping Template](../master/docs/img/fill_mapping_template_UC.png)

7. Fill the Bioschemas Fields
  + **schema.org**: These columns are copy -pasted from the schema.org type definition page.
    1. **Property:** Name of the property from the selected schema.org type.
    1. **Expected Type:** Expectedd type for the property suggested by schema.org selected type.
    1. **Description:**: Description of the property from the schema.org vocabulary for the selected type.
  + **bioschemas:** These columns are defined for the properties that will be in the Bioschemas Specification file.
    1. **SubProperties:** The subproperties of an specific property, should be listed inn the following format <subProperty_Name>: <subProperty_Type> and if you have multiples subproperties they should be separated by coma (,) as in this example  <subProperty_Name1>: <subProperty_Type1>, <subProperty_Name2>: <subProperty_Type2>, <subProperty_Name3>: <subProperty_Type3>... and so on.
    1. **Marginality:** The template gives three options for the property specification of the new Bioschemas Type, Minimum, Recomended or Optional. 
    1. **Cardinalitry:**	The template gives you the two possible cardinalyties in a Bioschemas Specification (ONE or Many).
    1. **Controlled Vocabulary (CV):** 
**CV** means Controlled Vocabulary, this field contains a list term/ontology. A term is just a text that represent the value expected and an ontology is a namespace that contains ontology name colon (:) the ontology URL.

      **Examples:**

      - **Term list**
            ```term1, term2, ter3```

      - **Ontology list**
            ```onto1: http://onto1.com, onto2: http: //onto2.com, onto3: http://onto1.com```

      - **Mixed list**
            ```onto1:http://onto1.com, term1, onto2:http: //onto2.com, term2, term3, onto3:http://onto1.com```

    >  For the Tools Specification you would have something like this.
    ![Fill the Bioschemas Fields](../master/docs/img/bioschemas_mapping.png)

8. Go to the Bioschemas fields Sheet to view the summary of your mapping
      > For the Tools Specification you would have something like this.
      ![Mapping Summary](../master/docs/img/mapping_summary.png)
      > If you have fields without name is because you will add to the Schema.org you selected as basis, and you need to add the name in the specification Doc File.

## 3. SPECIFICATION
Specifications are generated following the **Use Cases** > **Mapping** > **map2model** process.
>Find a detailed description of this process in [Specifications Repository](https://github.com/BioSchemas/specifications).

### 3.1. map2model (Python Module)

1. Clone [map2model repository](https://github.com/BioSchemas/specifications).
1. Modify ```configuration.yml```in your forked repository (configuration.yml file tells map2model which **Types/Profiles** mapping spreadsheets parse to a specification.
1. Execute ```python3 run.py```
1. Fork [Bioschemas specification repository](https://github.com/BioSchemas/specifications)
1. Upload all ```specification.html``` files generated by **map2model** to the respective folder in your forked specifications repository.
      > If it is the first time you generate the specification **copy all the files** to the root of your forked repository.
1. Check everthing is OK.
1. Make a **Pull Request** of your specifications repository fork
1. Wait until your **Pull Request** is merged to [Bioschemas Web](https://github.com/BioSchemas/bioschemas.github.io)
1. Check your changes at [Specifications Bioschemas Web section](htt://bioschemas.org/bsc_specs)
>Find a detailed description of this section in [map2model repository](https://github.com/BioSchemas/map2model)
