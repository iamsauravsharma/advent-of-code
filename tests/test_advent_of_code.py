import os
import pathlib
import subprocess

from advent_of_code import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_cli_main_output():
    assert subprocess.run(
        "advent-of-code", capture_output=True, text=True
    ).stdout == read_command_output("main.txt")


def test_cli_config_output():
    assert subprocess.run(
        ["advent-of-code", "config", "--help"], capture_output=True, text=True
    ).stdout == read_command_output("config.txt")


def test_cli_download_output():
    assert subprocess.run(
        ["advent-of-code", "download", "--help"], capture_output=True, text=True
    ).stdout == read_command_output("download.txt")


def test_cli_remove_output():
    assert subprocess.run(
        ["advent-of-code", "remove", "--help"], capture_output=True, text=True
    ).stdout == read_command_output("remove.txt")


def read_command_output(file: str) -> str:
    output_file = os.path.join(pathlib.Path.cwd(), "tests", "command_outputs", file)
    with open(output_file) as file_to_read:
        output_data = file_to_read.read()
    return output_data
