import gspread
import csv
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('sdo-bioschemas-client.json', scope)
client = gspread.authorize(creds)

sheet = client.open("BiologicalEntity mapping").get_worksheet(0)

list_of_hashes = sheet.get_all_records()

with open("full_specification_output.csv", "wb") as f_out:
    writer = csv.writer(f_out)
    writer.writerows(list_of_hashes)
