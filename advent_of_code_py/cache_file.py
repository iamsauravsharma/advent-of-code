"""Module which performs cache file related operation stored over CACHE_DIR of OS"""
import importlib
import os
import time
from pathlib import Path

from platformdirs import user_cache_dir

from enum import Enum


class FileType(Enum):
    INPUT_FILE = "input.txt"
    SUBMISSION_FILE = "submission.txt"
    TIME_FILE = "time.txt"


def input_data_is_downloaded(year: int, day: int, session: str) -> bool:
    """Check if an input is downloaded and cached"""
    cache_file = cache_file_path(year, day, session, file_type="input_file")
    return cache_file.exists()


def save_input_to_cache(year: int, day: int, session: str, input_data: str):
    """Save a input to its cache location for future reference and use"""
    cache_file = cache_file_path(year, day, session, FileType.INPUT_FILE)
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    with cache_file.open("w") as opened_file:
        opened_file.write(input_data)


def delete_input(year: int, day: int, session: str):
    """Delete input from a cache folder"""
    cache_file = cache_file_path(year, day, session, FileType.INPUT_FILE)
    cache_file.unlink(missing_ok=True)


def get_cache_file_data(year: int, day: int, session: str) -> str:
    """Return cache file input data from cache folder for certain problem"""
    server_action = importlib.import_module(".server_action")
    server_action.download_input(year, day, session)
    cache_file = cache_file_path(year, day, session, FileType.INPUT_FILE)
    with cache_file.open() as opened_file:
        input_data = opened_file.read()
    return input_data


def save_submitted_answer(
    year: int, day: int, part: int, session: str, answer: str, message: str
):
    """Save submitted input to file of problem"""
    submitted_file = cache_file_path(year, day, session, FileType.SUBMISSION_FILE)
    with submitted_file.open("a") as opened_file:
        opened_file.write("{}!{}:{}\n".format(part, answer, message))


def last_submitted_answer_message(
    year: int, day: int, part: int, session: str, output: str
) -> str:
    """
    Check if answer is already submitted by user if submitted return message of last
    submission
    """
    submission_file = cache_file_path(year, day, session, FileType.SUBMISSION_FILE)
    last_answer_message = ""
    with submission_file.open() as opened_file:
        lines = opened_file.read()
        for line in lines:
            separate_part = line.split("!", 1)
            if separate_part[0] == part:
                separate_output = separate_part[1].split(":", 1)
                if separate_output == output:
                    last_answer_message = separate_output[1]
    return last_answer_message


def save_last_submission_time(year: int, day: int, session: str):
    """Save a time where a request is performed for last submission"""
    last_time_file = cache_file_path(year, day, session, FileType.TIME_FILE)
    with last_time_file.open("w") as opened_file:
        opened_file.write(str(time.time()))


def check_less_than_one_min_submission(year: int, day: int, session: str) -> bool:
    """
    Check last submission time for solution return true if time is less than 60 second
    """
    last_time_file = cache_file_path(year, day, session, FileType.TIME_FILE)
    with last_time_file.open() as opened_file:
        last_time = float(opened_file.read())
        current_time = time.time()
        early_submission = current_time - last_time < 60.0
    return early_submission


def cache_file_path(year: int, day: int, session: str, file_type: FileType) -> Path:
    """Return desire path for a cache folders or files"""
    cache_location = user_cache_dir(appname="advent-of-code")
    cache_file = os.path.join(
        cache_location, str(session), str(year), str(day), file_type.value
    )
    return Path(cache_file)
