import spec2model.file_manager as f_manager
import spec2model.mapping as mapper

bsc_file_manager = f_manager.FolderDigger()
bsc_spec_list = bsc_file_manager.get_specification_list()

bsc_parser = mapper.GSheetsParser()

spec_id = '1H12h5VpVNJFzNs2RQJWjXkauCEn3qEsVFzKRoiHHffY'
bsc_parser.set_gsheet_id(spec_id)
bsc_parser.set_spec_metadata(bsc_spec_list[spec_id])
bsc_parser.get_mapping_g_sheets()












