import gspread
import requests
import json

# import json
from oauth2client.service_account import ServiceAccountCredentials

gsheet_id = '1h0-fgqnRe25-tVCmu2yWNQjthLzgkW4a1TVNMpCABlc'
cred_file = 'sdo-bioschemas-client.json'
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(cred_file, scope)
client = gspread.authorize(creds)

spread_sheet_name = client.open_by_key(gsheet_id).title
spec_name = spread_sheet_name
spec_name = spec_name.replace(' mapping', '')
spec_name = spec_name.replace(' Mapping', '')



mapping_sheet = client.open_by_key(gsheet_id).get_worksheet(0)
list_of_hashes = mapping_sheet.get_all_records(head=4)
spec_version='0.0.1'
spec_description='Some description.'

bsc_specification = {'name':spec_name, 'version':spec_version, 'description':spec_description}

type_properties = []

def isSchemaorgType(current_url):
    request = requests.get(current_url)
    if(request.status_code == 404):
        return False
    return True


# Function sets property domain and property domain case based on the name of the Property field title
# returns an array with the propperty domain and the property type
def get_domain_and_case(property_field):
    prop_case = 'new_bsc'
    prop_domain=''

    if(property_field.find('New properties for') == 0):
        prop_domain=property_field[19:]
        if(isSchemaorgType('http://schema.org/'+prop_domain)):
            prop_case = 'new_sdo'
        else:
            prop_case = 'new_bsc'
    elif(property_field.find('Reused properties from') == 0):
        prop_domain=property_field[23:]
        if(isSchemaorgType('http://schema.org/'+prop_domain)):
            prop_case = 'reu_sdo'
        else:
            prop_case = 'reu_bsc'
    else: prop_domain='invalid domain type'

    return[prop_domain, prop_case]


prop_domain=''
domain_case=''
for c_property in list_of_hashes:
    property_as_dic={}
    # domain_case can have new_bsc (new property for Bioschema Type), new_sdo (New Property for Schema.org Type),
    # reu_bsc (reuse a property from Bioschema Type), reu_sdo (Reuse Schema.org Type)
    if(c_property['Expected Type']=='' and c_property['Description']=='' and c_property['Minimum Fields']==''):
        property_string=c_property['Property']
        domain_info = get_domain_and_case(property_string)
        prop_domain = domain_info[0]
        domain_case = domain_info[1]
    else:
       property_as_dic['name']=c_property['Property']
       property_as_dic['expected_type']=c_property['Expected Type']
       property_as_dic['sdo_desc']=c_property['Description']
       property_as_dic['bsc_dec']=c_property['SubProperties']
       property_as_dic['marginality']=c_property['Minimum Fields']
       property_as_dic['cardinality']=c_property['Cardinality']
       property_as_dic['controlled_vocab']=c_property['Controlled Vocabulary']
       property_as_dic['domain']=prop_domain
       property_as_dic['domain_case']=domain_case
       type_properties.append(property_as_dic)

bsc_specification['properties']=type_properties

with open('temp_spec.json', 'w') as outfile:
    json.dump(bsc_specification, outfile, indent=3)

