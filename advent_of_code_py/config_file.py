"""Module to perform config file related operation"""

import json
import os
from pathlib import Path
from typing import List

from platformdirs import user_config_dir


class Data:
    """Class to store data about a config file of advent-of-code"""

    def __init__(self, **kwargs: str):
        """Initialize Data class"""
        self.session_list = kwargs

    def to_json(self) -> str:
        """Convert Data to JSON type"""
        return json.dumps(self.__dict__, indent=4, sort_keys=True)

    @classmethod
    def from_json(cls, json_str: str):
        """Create Data type from JSON"""
        json_dict = json.loads(json_str)
        json_data = json_dict.get("session_list")
        return cls(**json_data)

    def add_session(self, **kwargs: str):
        """Add new session or update session in a config file Data type."""
        self.session_list.update(kwargs)

    def delete_session(self, session: str):
        """Delete Session from config files"""
        try:
            self.session_list.pop(session)
        except KeyError:
            raise Exception("Value with name {} not found over config".format(session))


def read_json_file(config_file: Path) -> Data:
    """Read JSON file to return Data type"""
    with config_file.open("a+") as opened_file:
        opened_file.seek(0)
        data = Data.from_json(opened_file.read())
    return data


def config_file_path() -> Path:
    """Get Config file location"""
    config_location = user_config_dir()
    config_file = os.path.join(config_location, "aoc-config.json")
    return Path(config_file)


def add_to_json(**kwargs: str):
    """Add new session to json config file"""
    config_file = config_file_path()
    data = read_json_file(config_file)
    data.add_session(**kwargs)
    with config_file.open("w") as opened_file:
        opened_file.write(data.to_json())


def delete_from_json(session: str):
    """Delete session from JSON config file"""
    config_file = config_file_path()
    data = read_json_file(config_file)
    data.delete_session(session)
    with open(config_file, "w") as opened_file:
        opened_file.write(data.to_json())


def print_all_session():
    """List all session from a JSON file along with value"""
    config_file = config_file_path()
    data = read_json_file(config_file)
    json_dict = json.loads(data.to_json())
    json_data = json_dict.get("session_list")
    for key, val in json_data.items():
        print("{} = {}".format(key, val))


def get_session_value(session_name: str) -> str:
    """Return session name value from JSON config file"""
    config_file = config_file_path()
    data = read_json_file(config_file)
    json_dict = json.loads(data.to_json())
    json_data = json_dict.get("session_list")
    session_value = json_data.get(session_name)
    if session_value is not None:
        return session_value
    raise Exception("{} key is not present in config file".format(session_name))


def get_all_session() -> List[str]:
    """Return all session name"""
    config_file = config_file_path()
    data = read_json_file(config_file)
    json_dict = json.loads(data.to_json())
    json_data = json_dict.get("session_list")
    session_list = list(json_data.keys())
    return session_list
