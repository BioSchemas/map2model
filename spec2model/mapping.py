import gspread
import requests
import json
from oauth2client.service_account import ServiceAccountCredentials


# Function that checks if a Specification Type belongs to shema.org
def isSchemaorgType(current_url):
    request = requests.get(current_url)
    if (request.status_code == 404):
        return False
    return True


# Function sets property domain and property domain case based on the name of the Property field title
# returns an array with the propperty domain and the property type
def get_domain_and_case(property_field):
    prop_case = 'new_bsc'
    prop_domain = ''

    if (property_field.find('New properties for') == 0):
        prop_domain = property_field[19:]
        if (isSchemaorgType('http://schema.org/' + prop_domain)):
            prop_case = 'new_sdo'
        else:
            prop_case = 'new_bsc'
    elif (property_field.find('Reused properties from') == 0):
        prop_domain = property_field[23:]
        if (isSchemaorgType('http://schema.org/' + prop_domain)):
            prop_case = 'reu_sdo'
        else:
            prop_case = 'reu_bsc'
    else:
        prop_domain = 'invalid domain type'

    return [prop_domain, prop_case]


# Function that receives an string with expected types and generates an array with each expected pype
def get_expected_type(expected_types):
    expected_types = expected_types.strip()
    expected_types = expected_types.replace('\n', '')
    expected_types = expected_types.replace(' OR ', ' or ')
    list_of_types = expected_types.split(' or ')
    i = 0

    for type in list_of_types:
        list_of_types[i] = type.strip()
        i += 1

    return list_of_types


def get_mapping_description(mapping_sheet):
    mapping_description = {}
    mapping_description['subtitle'] = mapping_sheet.acell('B1').value
    mapping_description['description'] = mapping_sheet.acell('B2').value
    mapping_description['version']='0.0.1'
    return mapping_description


def get_mapping_properties(mapping_sheet):
    list_of_hashes = mapping_sheet.get_all_records(head=5)

    type_properties = []

    prop_domain = ''
    domain_case = ''
    for c_property in list_of_hashes:
        property_as_dic = {}
        marg_value = c_property['Minimum Fields']
        # domain_case can have new_bsc (new property for Bioschema Type), new_sdo (New Property for Schema.org Type),
        # reu_bsc (reuse a property from Bioschema Type), reu_sdo (Reuse Schema.org Type)
        if (c_property['Expected Type'] == '' and c_property['Description'] == '' and c_property[
            'Minimum Fields'] == ''):
            property_string = c_property['Property']
            domain_info = get_domain_and_case(property_string)
            prop_domain = domain_info[0]
            domain_case = domain_info[1]
        elif (marg_value == "Minimum" or marg_value == "Recommended" or marg_value == "Optional"):
            property_as_dic['name'] = c_property['Property'].strip().strip('\n')
            property_as_dic['expected_type'] = get_expected_type(c_property['Expected Type'])
            property_as_dic['sdo_desc'] = c_property['Description'].strip().replace('\n', ' ')
            property_as_dic['bsc_dec'] = c_property['SubProperties'].strip().replace('\n', ' ')
            property_as_dic['marginality'] = c_property['Minimum Fields'].replace('\n', ' ')
            property_as_dic['cardinality'] = c_property['Cardinality'].strip().strip('\n').replace('\n', ' ')
            property_as_dic['controlled_vocab'] = c_property['Controlled Vocabulary'].strip().replace('\n', ' ')
            property_as_dic['domain'] = prop_domain.strip().replace('\n', ' ')
            property_as_dic['domain_case'] = domain_case.strip().replace('\n', ' ')
            type_properties.append(property_as_dic)

    return type_properties


class JSONParser:
    gsheet_id = '1h0-fgqnRe25-tVCmu2yWNQjthLzgkW4a1TVNMpCABlc'
    cred_file = 'sdo-bioschemas-client.json'
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    bsc_specification = {}

    def __init__(self):
        self.gsheet_id = '1h0-fgqnRe25-tVCmu2yWNQjthLzgkW4a1TVNMpCABlc'
        self.cred_file = 'sdo-bioschemas-client.json'
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.bsc_specification = {}

    def set_gsheet_id(self, gsheet_id):
        self.gsheet_id = gsheet_id

    def get_mapping_json(self):

        creds = ServiceAccountCredentials.from_json_keyfile_name(self.cred_file, self.scope)
        client = gspread.authorize(creds)
        spread_sheet_name = client.open_by_key(self.gsheet_id).title
        spec_name = spread_sheet_name
        spec_name = spec_name.replace(' mapping', '')
        spec_name = spec_name.replace(' Mapping', '')
        mapping_sheet = client.open_by_key(self.gsheet_id).get_worksheet(0)

        self.bsc_specification['name']=spec_name
        spec_description = get_mapping_description(mapping_sheet)
        self.bsc_specification['properties'] = get_mapping_properties(mapping_sheet)
        self.bsc_specification.update(spec_description)

        with open('../json/' + spec_name + '_spec.json', 'w') as outfile:
            json.dump(self.bsc_specification, outfile, indent=3)
            outfile.close()
        return self.bsc_specification