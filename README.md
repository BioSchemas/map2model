# Bioschemas.org map2model

**map2model** is a Python module that facilitates [Bioschemas Groups](http://bioschemas.org/groups/) in the specification definition process.

![Bioschemas Specification Process](../master/docs/img/specification_process.jpg)
> If you want to modify the Flow Chart [Click here](https://drive.google.com/file/d/0B9lW_BhBep0Tay1XTndCaV9GSnc/view?usp=sharing) and store the result in img folder with the name **specification_process.jpg**.

**map2model** retrieves properties and Bioschemas fields (Marginality, Cardinality and Controlled Vocabularies) from Bioschemas mapping **GDrive** files, then classifies properties into two groups:
1. **Extended properties:** Properties that are part of the extended schema.org Type. 
1. **New properties:** Properties that are new to the schema.org vocabulary or are completely new to schema.org.
      
After classifing the properties, **map2model** generates a Markdown file that can be interpreted by Bioschemas.org's Jekyll implementation thereby updating the Bioschemas.org web pages.

Comments on each specifications should be done through github enabling tracking and execution of corrections.

## Run map2model in your computer

### Requirements
Before starting, please ensure:
1. You have Git installed [https://git-scm.com/downloads](https://git-scm.com/downloads)
1. You have Python 3 installed [https://www.python.org/downloads/](https://www.python.org/downloads/)
1. You have Pip installed [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/)


### Steps

1. Clone the **bioschemas-map2model** repository: ```git clone https://github.com/BioSchemas/bioschemas-map2model.git```
1. Add the [Bioschemas GDrive Folder](https://drive.google.com/open?id=0B8yXU9SkT3ftaWJtTGYyTTJjck0) to your Google Account Drive.
      > In your Gooogle Drive Account go to **Shared with me**, right click the **Bioschemas.org** folder and select **Add to my Drive**)
      
1. Create a new Google's APIs Project and add Google Drive API Client:
      - Go to [Google's APIs Console](https://console.developers.google.com/iam-admin/projects) and create your own project. Call it whatever you want.
      - You will need to wait for a few moments while Google creates the project. Refresh the page and you should see your new project listed.
      - Click on the **Google APIs** logo (top left of screen). If you have existing projects, select the new one in the dropdown box next to the Google APIs logo.
      - Under **G Suite APIs** you will see **Drive API**. Click on it.
      - On the next page, click on **Enable**
      - You should see a yellow warning at the top of the page informing you of the need for credentials. Do **not** click the create credentials button at the right of this warning. Instead click the **key icon** in the left menu bar.
      - In the new dialog box there is a dropdown called **create credentials**... choose **OAuth client ID**. 
      - A form with radio buttons will appear, but it is greyed out and you cannot select anything. Instead click the blue  **Configure consent screen** button on the right.
      - In the new form enter whatever **product name** you wish and click **save**.
      - You will be returned to the form with radio buttons; select **Web application**.
      - In the text box called 'Authorised Javascript origins' type http://localhost:8080 (notice the lack of a trailing slash)
      - In the text box called 'Authorised redirect URIs' type http://localhost:8080/ (notice the trailing slash)
      - Click **create** then **OK**.
      - You will be on a page called 'Credentials' which has a table with the name of your new app. At the far right you will see a download icon (an arrow pointing down, above a line). Clicking on this allows you to download your credentials.
      - The downloaded file will have a very long name, e.g., *client_secret_896441073116-l0karljg25m6uvss45t48ufb9d7u3kku.apps.googleusercontent.com*. Change the name to **client_secrets.json** and move it to the top level of your cloned **bioschemas-map2model** repository.
1. Open the Terminal or Console application of your Operating System and go to the folder where you cloned the **bioschemas-map2model** repository.
1. Install Python dependencies using the command ```pip3 install -r requirements.txt```.
1. Run the map2model module executing the command ```python3 run.py```.
1. Once the ```python3 run.py``` command finish, clone the **Bioschemas Specifications** repository using the command ```git clone ...``` 
1. Go to ```docs\specification_md_files\``` of your cloned spec2model repository, copy all the **.md files and paste them in your copy of **Bioschemas Specifications** repository.
1. Make a pull request of the **Bioschemas Specifications** repository.
      > Updates will be loaded to [bioschemas.github.io repository](https://github.com/BioSchemas/bioschemas.github.io) when the pull request is merged to the master branch.
