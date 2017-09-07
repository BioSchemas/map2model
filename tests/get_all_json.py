import spec2model.file_manager as f_manager
import spec2model.mapping as mapper

bsc_file_manager = f_manager.FolderDigger()
bsc_spec_list = bsc_file_manager.get_specification_list()

bsc_parser = mapper.GSheetsParser()

for bsc_spec in bsc_spec_list:
    mapping_file_id = bsc_spec
    bsc_parser.set_gsheet_id(bsc_spec)
    bsc_parser.set_spec_metadata(bsc_spec_list[bsc_spec])
    bsc_parser.get_mapping_g_sheets()
