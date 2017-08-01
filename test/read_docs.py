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

#List all the files in Bioschemas.org/Templates folders
'''
file_list = drive.ListFile({'q': "'0Bw_p-HKWUjHoNThZOWNKbGhOODg' in parents and trashed=false"}).GetList()
for file1 in file_list:
  p[rint('title: %s, id: %s' % (file1['title'], file1['id']))
'''

#List all the files in Bioschemas.org/Templates/Biological Entity folders

file_list = drive.ListFile({'q': "'0B7X2x2IPBve7R3Uza1d6MGpuYVE' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))

specDocsFile = drive.CreateFile({'id': '1XASuESIHU3bi1aXMxQS5-rCOQX0ugjMNkh68VF4co4Q'})
specDocsFile.GetContentFile('specificationInHtml.html',mimetype='text/html')

'''
Specifications, id: 0Bw_p-HKWUjHoNThZOWNKbGhOODg
title: Beacon Mapping, id: 1wLJa4LkCM8oIvBPTFS1IBcygRGBpSrAgNfRSEadVICo
'''
