import os, json, pydash


path_to_json = '../json/'

json_specs=[pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('_spec.json')]


with open(path_to_json+json_specs[0]) as data_file:
    data = json.load(data_file)

for property in data['properties']:
    if property['domain_case']=="reu_sdo":
        print(property)




