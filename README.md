# Bioschemas.org map2model

**map2model** is a Python module that facilitates [Bioschemas Groups](http://bioschemas.org/groups/) in the specification definition process.

![Bioschemas Specification Process](../master/docs/img/specification_process.jpg)
      > If you want to modify the Flow Chart [Click here](https://drive.google.com/file/d/0B9lW_BhBep0Tay1XTndCaV9GSnc/view?usp=sharing) and store the result in img folder wiht the name **specification_process.jpg**.

**map2model** retreives properties and Bioschemas fields (Marginality, Cardinality and Controlled Vocabularries) from Bioschemas mapping **GDrive** files, classify properties in two groups:
      1. **Extended Properties:** Properties that are part of the extended schema.org Type. 
      2. **New Properties:** Properties that are new to schema.org vocabulary or are completely new to the schema.org
After Classifing the properties, it generates a Markdown file that can be interpreted by Bioschemas.org Jekyll implementation and are easy to visualize by end users.

Comments to each specifications should be done by github to keep track of them and execute the corrections to each specification.

## Run map2model in your computer
1. Clone the **bioschemas-map2model** repository: ```git clone https://github.com/BioSchemas/bioschemas-map2model.git```
1. Add the [Bioschemas GDrive Folder](https://drive.google.com/open?id=0B8yXU9SkT3ftaWJtTGYyTTJjck0) to your Google Account Drive.
      > In your Gooogle Drive Account go to **Shared with me**, right click the **Bioschemas.org** folder and select **Add to my Drive**)
1. Create a new Google's APIs Project and add Google Drive API Client:
      - Go to [Google's APIs Console](https://console.developers.google.com/iam-admin/projects) and make your own project.
      - In the **API & services** library, search for **Google Drive API**, add it to your services by clicking the link and select **Enable** option.
      - In the left meenu of Google APIs, click on **Credentials** and in the following screen click on **Create Credentials**, a dorpdown menu should appear, select the option **OAuth client ID**.
      - In the next screen click the **Configure consent screen** and in the OAuth consent screen, fill the Email address and Product name shown to users, optional fields are not necesary.
      - Click **Save** button to consent OAuth. 
      - In the Client ID screen select **Web application** radio buttton as the **Application type** and click create button.
      - In the next screen enter the Client ID you want to use in the API.
      - Input http://localhost:8080 for ‘Authorized JavaScript origins’.
      - Input http://localhost:8080/ for ‘Authorized redirect URIs’ and click **Save**.
      - In OAuth 2.0 client IDs click the down arrow icon of the client you just created on the right side of Client information to download **client_secret_<really long ID>.json**.
      - Rename the JSON to client_secrets.json and paste in the root of the **spec2model** cloned repository.
1. Open the Terminal or Console application of your Operating System and go to the folder where you cloned the **spec2model** repository.
1. Install Python 3.x. For example, using [brew](https://brew.sh/) ```brew install python3```.
1. Install Python dependencies using the command ```pip3 install -r requirements.txt```.
      > If you get an error executing pip command, check if you have pip installed, otherwise install it with the following command ```python3 get-pip.py```
1. Run the map2model module executing the command ```python3 run.py```.
1. Once the ```python3 run.py``` command finish, clone the **Bioschemas Specifications** repository using the command ```git clone ...``` 
1. Go to ```docs\specification_md_files\``` of your cloned spec2model repository, copy all the **.md files and paste them in your copy of **Bioschemas Specifications** repository.
1. Make a pull request of the **Bioschemas Specifications** repository.
      > Updates will be loaded to [bioschemas.github.io repository](https://github.com/BioSchemas/bioschemas.github.io) when the pull request is merged to the master branch.
