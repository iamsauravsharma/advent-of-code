import appdirs
import os
import json
from pathlib import Path


class Data:
    """
    Class to store data about a config file
    """

    def __init__(self, **kwargs):
        self.session_list = kwargs

    def to_json(self):
        """
        Convert Data to JSON type
        """
        return json.dumps(self.__dict__, indent=4, sort_keys=True)

    @classmethod
    def from_json(cls, json_str):
        """
        Create a Data type from json_str
        """
        json_dict = json.loads(json_str)
        json_data = json_dict.get("session_list")
        return cls(**json_data)

    def add_session(self, **kwargs):
        """
        Add new session or update session in a config file Data type
        """
        self.session_list.update(kwargs)

    def delete_session(self, session):
        """
        Delete Session from config file
        """
        try:
            self.session_list.pop(session)
        except KeyError:
            print("Value with name {} not found over config".format(session))


def __read_json_file(config_file):
    """
    Read JSON file to return Data type
    """
    if not config_file.exists():
        with open(config_file, "a+") as f:
            val = Data()
            f.write(val.to_json())
    with open(config_file) as f:
        val = f.read()
        data = Data.from_json(val)
    return data


def __config_file_data():
    """
    Get Config file location
    """
    config_location = appdirs.user_config_dir()
    config_file = os.path.join(config_location, "aoc-config.json")
    config_file = Path(config_file)
    return config_file


def add_to_json(**kwargs):
    """
    Add new session to json config file
    """
    config_file = __config_file_data()
    data = __read_json_file(config_file)
    data.add_session(**kwargs)
    with open(config_file, "w") as f:
        f.write(data.to_json())


def delete_from_json(session):
    """
    Delete session from JSON config file
    """
    config_file = __config_file_data()
    data = __read_json_file(config_file)
    data.delete_session(session)
    with open(config_file, "w") as f:
        f.write(data.to_json())


def list_from_json():
    """
    List all session from a JSON file along with value
    """
    config_file = __config_file_data()
    data = __read_json_file(config_file)
    json_dict = json.loads(data.to_json())
    json_data = json_dict.get("session_list")
    for key, val in json_data.items():
        print("{} = {}".format(key, val))


def get_session_value(session_name):
    """
    Return session name value from JSON config file
    """
    config_file = __config_file_data()
    data = __read_json_file(config_file)
    json_dict = json.loads(data.to_json())
    json_data = json_dict.get("session_list")
    return json_data.get(session_name)
