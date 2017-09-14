import spec2model.file_manager as f_manager
import spec2model.mapping as mapper
import frontmatter
import os
from io import BytesIO


class FrontMatterParser:
    md_files_path = ''
    bsc_parser = ''
    bsc_spec_list = ''
    creds_file_path='spec2model/mycreds.txt'

    def __init__(self):
        self.md_files_path='docs/specifications_md_files/'
        self.bsc_file_manager = f_manager.FolderDigger()
        self.bsc_parser = mapper.GSheetsParser()

    def __get_all_specs_dic(self):
        all_specs =[]
        for bsc_spec in self.bsc_spec_list:
            self.bsc_parser.set_gsheet_id(bsc_spec)
            self.bsc_parser.set_spec_metadata(self.bsc_spec_list[bsc_spec])
            all_specs.append(self.bsc_parser.get_mapping_g_sheets())
        return all_specs

    def __get_specification_post(self, spec_dic):
        spec_metadata={}
        spec_post=frontmatter.Post('')
        for spec_field in spec_dic:
            spec_metadata[spec_field]=spec_dic[spec_field]
        spec_post.metadata=spec_metadata
        return spec_post

    def __create_spec_folder_struct(self, spec_name):
        spec_dir = self.md_files_path + spec_name + '/'
        if not os.path.exists(spec_dir):
            os.makedirs(spec_dir)

        spec_exp_dir = spec_dir + 'examples/'

        if not os.path.exists(spec_exp_dir):
            os.makedirs(spec_exp_dir)

        print("%s file structure created." % spec_name)

    def parse_front_matter(self):

        self.bsc_spec_list = self.bsc_file_manager.get_specification_list()
        all_specs_formatted=self.__get_all_specs_dic()

        for  formatted_spec in all_specs_formatted:
            temp_spec_post=self.__get_specification_post(formatted_spec)
            temp_spec_post.metadata['layout']= 'new_spec_detail'
            md_fm_bytes = BytesIO()
            frontmatter.dump(temp_spec_post, md_fm_bytes)
            spec_name=temp_spec_post.metadata['name']
            self.__create_spec_folder_struct(spec_name)
            spec_md_file_path=self.md_files_path + spec_name + '/' + spec_name + '.md'
            with open(spec_md_file_path, 'w') as outfile:
                temp_str=str(md_fm_bytes.getvalue(),'utf-8')
                outfile.write(temp_str)
                outfile.close()
            print ('%s MarkDown file generated.' % temp_spec_post.metadata['name'])
        os.remove(self.creds_file_path)
        print('Goggle Drive connection closed and credit file deleted.')
        print ('All Jekyll formatted MarkDown files generated.')


