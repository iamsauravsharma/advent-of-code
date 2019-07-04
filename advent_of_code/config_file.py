import appdirs
import os
import json
from pathlib import Path


class Data:
    def __init__(self, **kwargs):
        self.session_list = kwargs

    def to_json(self):
        return json.dumps(self.__dict__, indent=4, sort_keys=True)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        json_data = json_dict.get("session_list")
        return cls(**json_data)

    def add_session(self, **kwargs):
        self.session_list.update(kwargs)

    def delete_session(self, session):
        try:
            self.session_list.pop(session)
        except KeyError:
            print("Value with name {} not found over config".format(session))


def __read_json_file(config_file):
    if not config_file.exists():
        with open(config_file, "a+") as f:
            val = Data()
            f.write(val.to_json())
    with open(config_file) as f:
        val = f.read()
        data = Data.from_json(val)
    return data


def __config_file_data():
    config_location = appdirs.user_config_dir()
    config_file = os.path.join(config_location, "aoc-config.json")
    config_file = Path(config_file)
    return config_file


def add_to_json(**kwargs):
    config_file = __config_file_data()
    data = __read_json_file(config_file)
    data.add_session(**kwargs)
    with open(config_file, "w") as f:
        f.write(data.to_json())


def delete_from_json(session):
    config_file = __config_file_data()
    data = __read_json_file(config_file)
    data.delete_session(session)
    with open(config_file, "w") as f:
        f.write(data.to_json())


def list_from_json():
    config_file = __config_file_data()
    data = __read_json_file(config_file)
    json_dict = json.loads(data.to_json())
    json_data = json_dict.get("session_list")
    for key, val in json_data.items():
        print("{} = {}".format(key, val))


def get_session_value(session_name):
    config_file = __config_file_data()
    data = __read_json_file(config_file)
    json_dict = json.loads(data.to_json())
    json_data = json_dict.get("session_list")
    return json_data.get(session_name)
