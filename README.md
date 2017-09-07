# Bioschemas.org map2model

map2model is a Python module developed to facilitate [Bioschemas Groups](http://bioschemas.org/groups/) in the specification proposal process.

## Run the module in your computer
1. Clone the repository: ```git clone https://github.com/BioSchemas/bioschemas-map2model.git```
1. Go to ![APIs Console](https://console.developers.google.com/iam-admin/projects) and make your own project.
1. Search for ‘Google Drive API’, select the entry, and click ‘Enable’.
1. Select ‘Credentials’ from the left menu, click ‘Create Credentials’, select ‘OAuth client ID’.
1. Now, the product name and consent screen need to be set -> click ‘Configure consent screen’ and follow the instructions. Once finished:
      - Select ‘Application type’ to be Web application.
      - Enter an appropriate name.
      - Input http://localhost:8080 for ‘Authorized JavaScript origins’.
      - Input http://localhost:8080/ for ‘Authorized redirect URIs’.
      - Click ‘Save’.
      - Click ‘Download JSON’ on the right side of Client ID to download client_secret_<really long ID>.json.
      - Rename the JSON to client_secrets.json and paste in the root of the cloned repository
1. Open the Terminal or Console application of your Operating System and go to the folder where you cloned the repository.
1. Execute the module ```python run.py```
1. Once the module runned succesfuly, create a pull request to update the folder ```docs\specification_md_files\```

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
    1. **Minimum Fields:** The template gives three options for the property specification of the new Bioschemas Type, Minimum, Recomended or Optional. 
    1. **Cardinalitry:**	The template gives you the two possible cardinalyties in a Bioschemas Specification (ONE or Many).
    1. **Controlled Vocabulary:** 
      + A list of words separated by comas (,) precedeed by the Word "LIST - " 
        > "<LIST - ONE, TWO, THREE...>"
  
      + A list of ontologies following the syntax <Ontology_Name>:<Ontology_URL>, if you need to put more than one separate eachontology with comas (,), the ontology list should be preceeded by the word "ONTOLOGY - ".
        > "<ONTOLOGY - ontologyname1:URL1, ontologyname2:URL2, ontologyname3:URL3...>"

    >  For the Tools Specification you would have something like this.
    ![Fill the Bioschemas Fields](../master/docs/img/bioschemas_mapping.png)

8. Go to the Bioschemas fields Sheet to view the summary of your mapping
      > For the Tools Specification you would have something like this.
      ![Mapping Summary](../master/docs/img/mapping_summary.png)
      > If you have fields without name is because you will add to the Schema.org you selected as basis, and you need to add the name in the specification Doc File.

## 3. SPECIFICATION
Now that we have done the **Specification Mapping** there are two ways for documenting the SPecification:

   1. G-DOCS SPECIFICATION
   1. MARKDOWN SPECIFICATION
      
The **G-DOCS Specification** is thought to be a way for having a realtime feedback from the **collaborators**, but you can just jump to do the **MarkDown Specification** to be published in the Bioschemas page.

### 3.1. G-DOCS SPECIFICATION

   1. Make a copy of the [specification template](https://drive.google.com/open?id=0Bw_p-HKWUjHoQ2RkUUthWVd3RG8) naming the file **<SPECIFICATION_NAME> specification** and locating it in the [Bioschemas Drive Folder](https://drive.google.com/open?id=0Bw_p-HKWUjHoNThZOWNKbGhOODg) whitin the **<SPECIFICATION_NAME> folder**.
      > Folder for Bioschemas Tool Specification
      ![Bioschemas Tool Folder](../master/docs/img/specification_folder.png)
      
   1. First Copy the 

### 3.2. MARKDOWN SPECIFICATION

> Section under construction.

## RDFa

> Section under construction.

> **Please take into account that this repository is under construction, so suggestions and comments are welcome.**



