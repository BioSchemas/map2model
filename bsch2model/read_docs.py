import csv
import json
import oauth2client

store = oauth2client.file.Storage('sdo-bioschemas-client.json')
credentials = store.get()
http = credentials.authorize(httplib2.Http())
service = discovery.build('drive', 'v3', http=http)
