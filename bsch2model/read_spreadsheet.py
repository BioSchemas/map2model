import gspread
import csv
import json
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('sdo-bioschemas-client.json', scope)
client = gspread.authorize(creds)

sheet = client.open("BiologicalEntity mapping").get_worksheet(0)

list_of_hashes = sheet.get_all_records(head=4)


with open('mapping_convertion.json','w') as fp:
    json.dump(list_of_hashes, fp)
