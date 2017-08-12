import os, json, frontmatter
from io import BytesIO

def get_domain_case(spec_data, domain_case):
    use_case_props=[]
    for property in spec_data['properties']:
        if property['domain_case']==domain_case:
            use_case_props+=[property]
    return use_case_props

def get_json_dict(json_path):
    with open(json_path) as data_file:
        spec_data = json.load(data_file)

    return spec_data

def get_specification_post(path_to_json,spec_file, use_cases):
    with open(path_to_json+spec_file) as data_file:
        spec_data = json.load(data_file)

    spec_metadata={}

    spec_metadata['name']=spec_data['name']
    spec_metadata['version']=spec_data['version']
    spec_metadata['description']=spec_data['description']
    spec_post=frontmatter.Post('')

    for use_case in use_cases:
        spec_metadata[use_case] = get_domain_case(spec_data, use_case)

    spec_post.metadata=spec_metadata

    return spec_post

def get_spec_list(path_to_json):
    json_specs=[pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('_spec.json')]
    return json_specs


class FrontMatterParser:
    path_to_json = ''
    json_specs=[]
    md_files_path=''
    use_cases=[]

    def __init__(self):
        self.path_to_json = '../json/'
        self.json_specs=get_spec_list(self.path_to_json)
        self.md_files_path='../_newSpecs/'
        self.use_cases=['new_sdo','new_bsc','reu_sdo','reu_bsc']


    def parse_front_matter(self):

        for json_spec in self.json_specs:
            temp_spec_post=get_specification_post(self.path_to_json, json_spec,self.use_cases)
            md_fm_bytes = BytesIO()
            frontmatter.dump(temp_spec_post, md_fm_bytes)
            with open(self.md_files_path+temp_spec_post.metadata['name']+'.md', 'w') as outfile:
                temp_str=str(md_fm_bytes.getvalue(),'utf-8')
                outfile.write(temp_str)

        print ('completed')








