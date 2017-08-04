from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class FolderDigger:

    gauth = "This variable will have the Google Authorization file"
    specs_id = '0Bw_p-HKWUjHoNThZOWNKbGhOODg'
    specs_list={}
    drive= "This variable will be the Google drive's object"

    def __init__(self):
        self.gauth = GoogleAuth()
        # Try to load saved client credentials
        self.gauth.LoadCredentialsFile("spec2model/mycreds.txt")
        if self.gauth.credentials is None:
            # Authenticate if they're not there
            self.gauth.LocalWebserverAuth()
        elif self.gauth.access_token_expired:
            # Refresh them if expired
            self.gauth.Refresh()
        else:
            # Initialize the saved creds
            self.gauth.Authorize()
            # Save the current credentials to a file
            self.gauth.SaveCredentialsFile("spec2model/mycreds.txt")

        self.drive = GoogleDrive(self.gauth)
        #This is the id of the folder Specification
        self.specs_id = '0Bw_p-HKWUjHoNThZOWNKbGhOODg'
        self.specs_list={}

    def set_spec_file_id(self, file_id):
        self.specs_id=file_id

    def get_specification_list(self):

        file_list=self.drive.ListFile({'q':"'"+self.specs_id+"' in parents and trashed =false"}).GetList();

        # Gets a dictionary of all the specification with a folder
        for file in file_list:
            if (not(file['title']=='_commons_' or file['title']=='_templates_' or '_*' in file['title'])):
                self.specs_list[file['title']]=file['id']

        all_bsc_specs={}

        # Gets the Specification file and de mapping file ids
        for spec_key in self.specs_list:

            spec_id=self.specs_list[spec_key]
            all_spec_files=self.drive.ListFile({'q':"'"+spec_id+"' in parents and trashed =false"}).GetList();
            spec_files={}

            for current_file in all_spec_files:

                current_name=current_file['title']
                current_name=current_name.replace(spec_key,'')
                temp_name=current_name.strip()

                if(temp_name=='specification' or temp_name=='Specification'):
                    spec_files['specification_id']=current_file['id']
                elif(temp_name=='mapping' or temp_name=='Mapping'):
                    spec_files['mapping_id']=current_file['id']

            # Writes a dictionary entry with key the name of the Type and it's content a dictionary with the specification and the mapping files id
            all_bsc_specs[spec_key]=spec_files

        return all_bsc_specs







