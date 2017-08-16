from ruamel.yaml import YAML



class YamlIO:
    yml_path=''
    yaml= ''

    def __init__(self):
        self.yml_path = '../spec2model/configuration.yml'
        self.yaml = YAML()

    def set_yml_path(self, file_path):
        self.yml_path = file_path

    def read_yml_config(self):
        self.yaml.allow_duplicate_keys = True
        with open(self.yml_path) as f:
            stream = f.read()
        config_yml=self.yaml.load(stream)




all_specs_yml=config_yml['specifications']

for spec_yml in all_specs_yml:
    print(spec_yml['g_folder'])
    temp = spec_yml['name']


print(temp)