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


def __get_dic_from_sheet_row(prop_name, parent_type, c_property):

    property_as_dic = {}
    #Set Bioschemas attributes
    property_as_dic['bsc_dec'] = c_property['BSC Description'].strip().replace('\n', ' ')
    property_as_dic['marginality'] = c_property['Minimum Fields'].replace('\n', ' ')
    property_as_dic['cardinality'] = c_property['Cardinality'].strip().strip('\n').replace('\n', ' ')
    property_as_dic['controlled_vocab'] = c_property['Controlled Vocabulary'].strip().replace('\n', ' ')



    #Set schema.org attributes
    property_as_dic['name'] = c_property['Property'].strip().strip('\n')
    property_as_dic['expected_type'] = get_expected_type(c_property['Expected Type'])
    property_as_dic['sdo_desc'] = c_property['Description'].strip().replace('\n', ' ')

    property_as_dic['spec_type'] = ''


def get_mapping_properties(mapping_sheet, parent_type):
    list_of_hashes = mapping_sheet.get_all_records(head=5)
    type_properties = []

    for c_property in list_of_hashes:
        prop_name = c_property['Property'].strip().strip('\n')
        property_as_dic=__get_dic_from_sheet_row(prop_name, parent_type, c_property)
        type_properties.append(property_as_dic)
    return type_properties


class JSONParser:
    gsheet_id = ''
    cred_file = ''
    scope = []
    spec_metadata={}
    bsc_specification = {}

    def __init__(self):
        self.gsheet_id = '1h0-fgqnRe25-tVCmu2yWNQjthLzgkW4a1TVNMpCABlc'
        self.cred_file = '../spec2model/sdo-bioschemas-client.json'
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.spec_metadata={}
        self.bsc_specification = {}

    def set_gsheet_id(self, gsheet_id):
        self.gsheet_id = gsheet_id

    def set_spec_metadata(self, spec_metadata):
        self.spec_metadata=spec_metadata

    def __get_mapping_description(self, mapping_sheet):
        mapping_description = {}
        mapping_description['name']=self.spec_metadata['name']
        mapping_description['g_mapping_file']=self.spec_metadata['g_mapping_file']
        mapping_description['spec_mapping_url']=self.spec_metadata['spec_mapping_url']
        mapping_description['status']=self.spec_metadata['status']
        mapping_description['spec_type']=self.spec_metadata['spec_type']
        mapping_description['gh_folder']='https://github.com/BioSchemas/'+self.spec_metadata['name']
        mapping_description['gh_tasks']='https://github.com/BioSchemas/bioschemas/labels/type%3A%20'+self.spec_metadata['name']
        mapping_description['edit_url']='https://github.com/BioSchemas/bioschemas.github.io/edit/master/_newSpecs/'+self.spec_metadata['name']+'.md'
        mapping_description['version']=self.spec_metadata['version']
        mapping_description['subtitle'] = mapping_sheet.acell('B1').value
        mapping_description['description'] = mapping_sheet.acell('B2').value
        mapping_description['parent_type'] = mapping_sheet.acell('A6').value[8:].strip()
        return mapping_description

    def get_mapping_json(self):

        creds = ServiceAccountCredentials.from_json_keyfile_name(self.cred_file, self.scope)
        client = gspread.authorize(creds)
        mapping_sheet = client.open_by_key(self.gsheet_id).get_worksheet(0)

        spec_description = self.__get_mapping_description(mapping_sheet)
        self.bsc_specification['properties'] = get_mapping_properties(mapping_sheet)
        self.bsc_specification.update(spec_description)

        with open('../json/' + spec_description['name'] + '_spec.json', 'w') as outfile:
            json.dump(self.bsc_specification, outfile, indent=3)
            outfile.close()
        return self.bsc_specification
