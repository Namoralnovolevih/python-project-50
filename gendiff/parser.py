import json
import yaml


def parser(file):
    if file.endswith(".json"):
        with open(file) as f1:
            data1 = json.load(f1)
        return data1
    if file.endswith(".yaml") or file.endswith(".yml"):
        with open(file) as f2:
            data2 = yaml.safe_load(f2)
        return data2
