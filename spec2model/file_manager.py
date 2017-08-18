from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import spec2model.config_manager as yml_manager

class FolderDigger:

    gauth = "This variable will have the Google Authorization file"
    specs_id = '0Bw_p-HKWUjHoNThZOWNKbGhOODg'
    drive = "This variable will be the Google drive's object"
    yml_config = ''

    def __init__(self):
        creds_path="../spec2model/mycreds.txt"
        self.gauth = GoogleAuth()
        # Try to load saved client credentials
        self.gauth.LoadCredentialsFile(creds_path)
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
            self.gauth.SaveCredentialsFile(creds_path)

        self.drive = GoogleDrive(self.gauth)
        #This is the id of the folder Specification
        self.specs_id = '0Bw_p-HKWUjHoNThZOWNKbGhOODg'
        self.specs_list = {}
        self.yml_config = yml_manager.YamlIO()


    def set_spec_file_id(self, file_id):
        self.specs_id=file_id

    def get_spec_folder_files(self):
        file_list = self.drive.ListFile({'q':"'"+self.specs_id+"' in parents and trashed =false"}).GetList()
        return file_list

    def __get_gfile_or_foler_id(self, current_cfg_yml, spec_folder_files):
        current_spec_g_folder = current_cfg_yml['g_folder']
        for folder_file in spec_folder_files:
            if folder_file['title']==current_spec_g_folder:
                return folder_file
        return {}

    def __get_bsc_specs(self, spec_config, spec_folder_files):
        specs_list = {}
        for current_config in spec_config:
            spec_folder_dic = self.__get_gfile_or_foler_id(current_config, spec_folder_files)
            specs_list[spec_folder_dic['id']] = current_config[spec_folder_dic['title']]
        return specs_list

    def get_specification_list(self):
        self.yml_config.set_yml_path('../spec2model/configuration.yml')
        spec_config = self.yml_config.get_spec_yml_config()
        spec_folder_files = self.get_spec_folder_files()

        all_bsc_specs=self.__get_bsc_specs(spec_config,spec_folder_files)

        return all_bsc_specs

        # for file in file_list:
        #     if (not(file['title']=='_commons_' or file['title']=='_templates_' or '_*' in file['title'])):
        #         self.specs_list[file['title']]=file['id']

        # Gets the Specification file and de mapping file ids
        # for spec_key in self.specs_list:
        #
        #     spec_id=self.specs_list[spec_key]
        #     all_spec_files=self.drive.ListFile({'q':"'"+spec_id+"' in parents and trashed =false"}).GetList();
        #     spec_files={}
        #
        #     for current_file in all_spec_files:
        #
        #         current_name=current_file['title']
        #         current_name=current_name.replace(spec_key,'')
        #         temp_name=current_name.strip()
        #
        #         if(temp_name=='specification' or temp_name=='Specification'):
        #             spec_files['specification_id']=current_file['id']
        #         elif(temp_name=='mapping' or temp_name=='Mapping'):
        #             spec_files['mapping_id']=current_file['id']
        #
        #     # Writes a dictionary entry with key the name of the Type and it's content a dictionary with the specification and the mapping files id
        #     all_bsc_specs[spec_key]=spec_files
        #
        # return all_bsc_specs
