from ruamel.yaml import YAML

with open('../spec2model/configuration.yml') as f:
    stream = f.read()

yaml= YAML()
yaml.allow_duplicate_keys = True
config_yml=yaml.load(stream)

all_specs_yml=config_yml['specifications']

for spec_yml in all_specs_yml:
    print(spec_yml['g_folder'])
    temp = spec_yml['name']


print(temp)