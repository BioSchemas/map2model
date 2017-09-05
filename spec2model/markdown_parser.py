import frontmatter
from io import BytesIO

def get_specification_post(path_to_json,spec_file):
    with open(path_to_json+spec_file) as data_file:
        spec_data = json.load(data_file)

    spec_metadata={}

    for spec_detail in spec_data:
        spec_metadata[spec_detail]=spec_data[spec_detail]

    spec_post=frontmatter.Post('')

    extended_props=[]
    new_props=[]



    spec_metadata['extended_props'] = extended_props
    spec_metadata['new_props'] = new_props

    spec_post.metadata=spec_metadata

    return spec_post


class FrontMatterParser:
    md_files_path=''

    def __init__(self):
        self.md_files_path='../specification_md_files/'


    def parse_front_matter(self, parsed_spec):

        for json_spec in self.json_specs:
            temp_spec_post=get_specification_post(self.path_to_json, json_spec)
            temp_spec_post.metadata['layout']= 'new_spec_detail'
            md_fm_bytes = BytesIO()
            frontmatter.dump(temp_spec_post, md_fm_bytes)
            with open(self.md_files_path+temp_spec_post.metadata['name']+'.md', 'w') as outfile:
                temp_str=str(md_fm_bytes.getvalue(),'utf-8')
                outfile.write(temp_str)
                outfile.close()

        print ('completed')
