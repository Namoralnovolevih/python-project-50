import json
import yaml


def parser(data: str, format: str) -> dict:
    extensions = {'json': parse_json,
                  'yml': parse_yaml,
                  'yaml': parse_yaml,
                  }

    return extensions[format](data)


def parse_json(data: str) -> dict:
    res = json.loads(data)

    return res if isinstance(res, dict) else {}


def parse_yaml(data: str) -> dict:
    res = yaml.load(data, Loader=yaml.SafeLoader)

    return res if isinstance(res, dict) else {}
