# Bioschemas.org map2model

map2model is a Python module developed to facilitate [Bioschemas Groups](http://bioschemas.org/groups/) in the specification proposal process.

## Run the module in your computer
1. Clone the repository: ```git clone https://github.com/BioSchemas/bioschemas-map2model.git```
1. Add the ![Bioschemas GDrive](https://drive.google.com/drive/folders/0B8yXU9SkT3ftaWJtTGYyTTJjck0?usp=sharing) to your Google Account Drive.
1. Go to ![Google's APIs Console](https://console.developers.google.com/iam-admin/projects) and make your own project.
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
1. Install Python 3.x using ![brew](https://brew.sh/) ```brew install python3```
1. Install Python dependencies with ```pip3 install -r requirements.txt```.
> If you get an error executing pip command, check if you have pip installed otherwise install with the following command ```python3 get-pip.py```
1. Run the map2model module with the command ```python3 run.py```.
1. Once the module succesfuly runned, create a pull request to update the folder ```docs\specification_md_files\```.
> Updates will be loaded to [bioschemas.github.io repository](https://github.com/BioSchemas/bioschemas.github.io) when the pull request is merged to the master branch.
