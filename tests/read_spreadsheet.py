import gspread
import json
from pydrive.auth import GoogleAuth
from oauth2client.service_account import ServiceAccountCredentials

creds_path="spec2model/mycreds.txt"
gauth = GoogleAuth()
gsheet_id=""
# Try to load saved client credentials
gauth.LoadCredentialsFile(creds_path)
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
    gauth.SaveCredentialsFile(creds_path)

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
#creds = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)
client = gspread.authorize(gauth.credentials)

sheet = client.open_by_key(gsheet_id).get_worksheet(0)
