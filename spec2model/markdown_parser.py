import os, json
import pandas as pd

path_to_json = '../json/'

json_specs=[pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('_spec.json')]

print(json_specs)

