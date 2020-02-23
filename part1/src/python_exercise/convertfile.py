import os
import sys
import json
import yaml
from cfn_flip import flip, to_yaml, to_json
from cfn_tools import load_yaml, dump_json, load_json
from cfn_clean import clean

ROOT_DIR = os.path.dirname(__file__)

# function to convert yaml file to json file
def convert_yaml_to_json(yaml_file):
    converted_file = ROOT_DIR+'/../../../tacocat_cf.json'

    with open(yaml_file, 'r') as file_in:
        yaml_data = load_yaml(file_in)
        yaml_data = clean(yaml_data)

    with  open(converted_file, 'w') as file_out:
        json_data = dump_json(yaml_data)
        json_data = load_json(json_data)     
        json.dump(json_data, file_out, sort_keys=True, indent=4, separators=(',', ': '))
        print('#####--Converted successfully, please check the root folder with the name tacocat_cf.json--#####')
