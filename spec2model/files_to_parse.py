from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

specs_id = '0Bw_p-HKWUjHoNThZOWNKbGhOODg'
specs_list={}

file_list=drive.ListFile({'q':"'"+specs_id+"' in parents and trashed =false"}).GetList();

for file in file_list:
    if (not(file['title']=='_commons_' or file['title']=='_templates_')):
        specs_list[file['title']]=file['id']


for spec_key in specs_list:

    files_bsc_spec={}
    spec_id=specs_list[spec_key]
    specs_files=drive.ListFile({'q':"'"+spec_key+"' in parents and trashed =false"}).GetList();

    files_bsc_spec['name']=current_file['title']
    files_bsc_spec['folder_id']=files_bsc_spec['name']

    j=0
    for current_file in specs_files:
        current_name=current_file['title']
        current_name=current_name.replace(spec_id,'')
        temp_name=current_name.strip()

        if(temp_name=='specification' or temp_name=='Specification'):
            files_bsc_spec['specification_id']=current_file['title']
        elif(temp_name=='mapping' or temp_name=='Mapping'):
            files_bsc_spec['mapping_id']=current_file['title']
        else:
            print('No Spec file')

    print(files_bsc_spec)






