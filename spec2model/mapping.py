import requests
import gspread
from pydrive.auth import GoogleAuth
from rdflib import ConjunctiveGraph


def __get_class_name(temp_uri):
    return temp_uri.replace("http://schema.org/","")


def __add_property(props_dic, prop_desc):
    sdo_uri="http://schema.org/"
    if prop_desc['prop_name'] in props_dic:
        t_prop_name = prop_desc['prop_name']
        props_dic[t_prop_name]['exp_type'].append(prop_desc['exp_type'].replace(sdo_uri,""))
    else:
        props_dic[prop_desc['prop_name']]=prop_desc
        props_dic[prop_desc['prop_name']]['exp_type'] = [prop_desc['exp_type'].replace(sdo_uri,"")]
    return props_dic


def __get_class_props(class_name, graph):
    print("Quering properties of  %s in Schema.org" % class_name)

    qres = graph.query("""prefix schema: <http://schema.org/>
                        select distinct * where {
                            ?property schema:domainIncludes  schema:%s .
                            ?property schema:rangeIncludes  ?exp_type .
                            ?property rdfs:label ?prop_name.
                            ?property rdfs:comment ?description
                        }""" % class_name)
    temp_dic = {}

    for row in qres:
        labels=row.labels.keys()
        labels_dic = {}
        print('Parsing %s property.' % row['prop_name'])
        for label in labels:
            labels_dic[label] = str(row[label]).replace('<a href=\"/docs/', '<a href=\"http://schema.org/docs/')
        temp_dic=__add_property(temp_dic, labels_dic)

    return temp_dic


def __get_parent_type(class_name, graph):

    print("Find parent type of %s in Schema.org" % class_name)

    qres = graph.query("""prefix schema: <http://schema.org/>
                          select ?supclass where{
                          ?class rdfs:label ?label .
                          ?class rdfs:subClassOf ?supclass .
                          filter (?label='%s')
                        }""" % class_name)
    resp_arr=[]

    for row in qres:
        resp_arr.append(str(row['supclass']))
    return resp_arr[0].replace('http://schema.org/', '')


def __get_properties(class_name, graph, properties):

    if(class_name=='Thing'):
        properties[class_name]=__get_class_props(class_name, graph)
        return properties
    else:
        temp_props = __get_class_props(class_name, graph)
        properties[class_name] = temp_props
        parent_type = __get_parent_type(class_name, graph)
        __get_properties(parent_type, graph, properties)


def get_properties_in_hierarchy(type_name):
    query_type = type_name
    g = ConjunctiveGraph()
    g.parse('http://schema.org/version/latest/schema.jsonld', format='json-ld')
    props_dic={}
    __get_properties(query_type, g, props_dic)
    return props_dic


def get_hierarchy(props_dic):
    type_hierarchy = []
    for h_type in props_dic:
        type_hierarchy.append(h_type)
    return type_hierarchy


# Function that receives an string with expected types and generates an array with each expected pype
def get_expected_type(expected_types):
    expected_types = expected_types.strip()
    expected_types = expected_types.replace('\n', '')
    expected_types = expected_types.replace(' OR ', ' ')
    expected_types = expected_types.replace(' or ', ' ')
    expected_types = expected_types.replace(',', '')
    list_of_types = []
    for type in expected_types.split(" "):
        temp_type = type.strip()
        if(temp_type != '' and temp_type != ' '):
            list_of_types.append(temp_type.strip())
    return list_of_types


def _parse_controlled_vocabulary(temp_cont_vocab):
    cv_parsed = {'terms':[] , 'ontologies':[]}
    if "LIST - " in temp_cont_vocab:
        temp_cont_vocab = temp_cont_vocab.replace('LIST - ', '').strip()
        element_list = temp_cont_vocab.split(',')
        for element in element_list:
            if element != '':
                temp_term = {}
                temp_term['name'] = element.strip()
                cv_parsed['terms'].append(temp_term)
    if "ONTOLOGY - " in temp_cont_vocab:
        temp_cont_vocab = temp_cont_vocab.replace('ONTOLOGY - ', '').strip()
        element_list = temp_cont_vocab.split(',')
        for element in element_list:
            if element != '':
                element = element.strip()
                temp_ont = element.split(":", 1)
                ontology = {}
                ontology['name'] = temp_ont[0].strip()
                ontology['url'] = temp_ont[1].strip()
                cv_parsed['ontologies'].append(ontology)
    return cv_parsed


def __get_dic_from_sheet_row(c_property):

    property_as_dic = {}

    # Set Bioschemas attributes

    property_as_dic['bsc_dec'] = c_property['BSC Description'].strip().replace('\n', ' ')
    property_as_dic['marginality'] = c_property['Marginality'].replace('\n', ' ')
    property_as_dic['cardinality'] = c_property['Cardinality'].strip().strip('\n').replace('\n', ' ')
    temp_cont_vocab = c_property['Controlled Vocabulary'].strip().replace('\n', ' ')
    property_as_dic['controlled_vocab'] = _parse_controlled_vocabulary(temp_cont_vocab)


    # Set schema.org attributes
    property_as_dic['name'] = c_property['Property'].strip().strip('\n')
    property_as_dic['expected_type'] = get_expected_type(c_property['Expected Type'])
    if('Property URL' in c_property and     c_property['Property URL'] != ''):
        property_as_dic['property_url'] = c_property['Property URL'].strip()
    if 'sdo_desc' not in property_as_dic:
        property_as_dic['sdo_desc'] = '';
    return property_as_dic


def get_property_in_hierarchy(sdo_props, mapping_property):
    prop_type="new_sdo"
    for hierarchy_level in sdo_props:
        if mapping_property['name'] in sdo_props[hierarchy_level].keys():
            prop_type = hierarchy_level
            mapping_property['sdo_desc']=sdo_props[hierarchy_level][mapping_property['name']]['description']
    return {'type':prop_type, 'property': mapping_property}


def get_formatted_props(sdo_props, mapping_props, spec_name, spec_type):
    all_props= []
    bsc_props = []

    # if type only get new properties from mapping file
    if(spec_type == "Type" or spec_type == "type"):
        for mapping_property in mapping_props:
            bsc_props.append(mapping_property['name'])
            temp_prop=get_property_in_hierarchy(sdo_props, mapping_property)
            if temp_prop['type'] == "new_sdo":
                temp_prop['property']['parent'] = spec_name
            all_props.append(temp_prop['property'])
        for sdo_prop in sdo_props:
            # now get all props from schema & make them such that _layout can use them
            for sdo_prop_prop in sdo_props[sdo_prop].keys():
                if sdo_props[sdo_prop][sdo_prop_prop]['prop_name'] not in bsc_props:
                    sdo_props[sdo_prop][sdo_prop_prop]['parent'] = sdo_prop
                    sdo_props[sdo_prop][sdo_prop_prop]['name'] = sdo_props[sdo_prop][sdo_prop_prop]['prop_name']
                    # sdo_props[sdo_prop][sdo_prop_prop]['bsc_dec'] = sdo_props[sdo_prop][sdo_prop_prop]['description']
                    sdo_props[sdo_prop][sdo_prop_prop]['sdo_desc'] = sdo_props[sdo_prop][sdo_prop_prop]['description']
                    sdo_props[sdo_prop][sdo_prop_prop]['expected_type'] = sdo_props[sdo_prop][sdo_prop_prop]['exp_type']
                    sdo_props[sdo_prop][sdo_prop_prop]['property_url'] = str("http://schema.org/"+sdo_props[sdo_prop][sdo_prop_prop]['prop_name'])
                    all_props.append(sdo_props[sdo_prop][sdo_prop_prop])
                else:
                    for i in all_props:
                        if i['name'] == sdo_props[sdo_prop][sdo_prop_prop]['prop_name']:
                            i['parent'] = sdo_prop
        return {'properties': all_props}

    # if profile
    for mapping_property in mapping_props:
        temp_prop=get_property_in_hierarchy(sdo_props, mapping_property)        
        if temp_prop['type'] == "new_sdo":
            temp_prop['property']['parent'] = spec_name
        else:
            temp_prop['property']['parent'] = temp_prop['type']
            temp_prop['property']['property_url'] = str("http://schema.org/"+temp_prop['property']['name'])
        all_props.append(temp_prop['property'])

    return {'properties': all_props}


def get_mapping_properties(mapping_sheet, spec_type):
    list_of_hashes = mapping_sheet.get_all_records(head=5)
    type_properties = []
    for c_property in list_of_hashes:
        if(c_property['Expected Type']!="" # and c_property['Description']!=""
           and c_property['Marginality']!="" and c_property['Cardinality']!=""):
            print("Parsing %s property from Google Sheets." % c_property['Property'])
            property_as_dic=__get_dic_from_sheet_row(c_property)
            type_properties.append(property_as_dic)
    return type_properties


class GSheetsParser:
    gsheet_id = ''
    cred_file = ''
    gauth = "This variable will have the Google Authorization file"
    scope = []
    spec_metadata={}
    bsc_specification = {}

    def __init__(self):
        self.gsheet_id = '1h0-fgqnRe25-tVCmu2yWNQjthLzgkW4a1TVNMpCABlc'
        #self.cred_file = 'client_secrets.json'
        #self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.spec_metadata={}
        self.bsc_specification = {}
        creds_path="spec2model/mycreds.txt"
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

    def set_gsheet_id(self, gsheet_id):
        self.gsheet_id = gsheet_id

    def set_spec_metadata(self, spec_metadata):
        self.spec_metadata=spec_metadata

    def check_url(self, spec_url):
        if spec_url==None: return "err_404"
        r=requests.get(spec_url)
        if r==404:
            return "err_404"
        else:
            return spec_url

    def __get_mapping_description(self, mapping_sheet):
        mapping_description = {}
        mapping_description['name']=self.spec_metadata['name']
        print("Parsing %s Google Sheet" % mapping_description['name'])
        mapping_description['g_mapping_file']=self.spec_metadata['g_mapping_file']
        mapping_description['spec_mapping_url']=self.spec_metadata['spec_mapping_url']
        mapping_description['status']=self.spec_metadata['status']
        mapping_description['spec_type']=self.spec_metadata['spec_type']
        mapping_description['gh_folder']='https://github.com/BioSchemas/specifications/tree/master/'+self.spec_metadata['name']
        mapping_description['gh_examples']='https://github.com/BioSchemas/specifications/tree/master/'+self.spec_metadata['name']+'/examples'
        mapping_description['gh_tasks']='https://github.com/BioSchemas/bioschemas/labels/type%3A%20'+self.spec_metadata['name']
        mapping_description['edit_url']='https://github.com/BioSchemas/specifications/tree/master/'+self.spec_metadata['name']+'/specification.html'
        mapping_description['use_cases_url']=self.check_url(self.spec_metadata['use_cases_url'])
        mapping_description['version']=self.spec_metadata['version']
        mapping_description['subtitle'] = mapping_sheet.acell('B1').value
        mapping_description['description'] = mapping_sheet.acell('B2').value
        mapping_description['parent_type'] = mapping_sheet.acell('A6').value[8:].strip()
        return mapping_description

    def get_mapping_g_sheets(self):

        client = gspread.authorize(self.gauth.credentials)

        print("Parsing %s file." % self.spec_metadata['g_mapping_file'])
        mapping_sheet = client.open_by_key(self.gsheet_id).get_worksheet(0)

        spec_description = self.__get_mapping_description(mapping_sheet)
        sdo_props = get_properties_in_hierarchy(spec_description['parent_type'])

        spec_description ['hierarchy']= get_hierarchy(sdo_props)
        print("Prepared schema.org properties for hierarchy %s" % str(spec_description ['hierarchy']))

        print("Classifing %s properties" % spec_description['name'])
        mapping_props = get_mapping_properties(mapping_sheet, spec_description['spec_type'])

        formatted_props = get_formatted_props(sdo_props, mapping_props, spec_description['name'], spec_description['spec_type'])
        spec_description.update(formatted_props)

        return spec_description
