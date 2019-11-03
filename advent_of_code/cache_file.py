""" Module which performs cache file related operation stored over CACHE_DIR of OS"""
import os
import time
from pathlib import Path

import appdirs


def check_if_downloaded(year: int, day: int, session: int) -> bool:
    """
    Check if an input is downloaded and cached or not in cache location

    ***Parameters***

    - `year`: *int*
    :   Year for which input download need to be checked out
    - `day`: *int*
    :    Day for which input download need to be checked out
    - `session`: *str*
    :    Session for which input download need to be checked out

    ***Returns***

    - *bool*
    :    Returns out whether input for problem is downloaded for not
    """
    cache_file = _join_path(year, day, session, input_file=True)
    cache_file = Path(cache_file)
    return cache_file.exists()


def save_input_to_location(year, day, session, input_data):
    """Save a input to its cache location for future reference and use"""
    cache_folder = _join_path(year, day, session)
    Path(cache_folder).mkdir(parents=True, exist_ok=True)
    cache_file = os.path.join(cache_folder, "input.txt")
    with open(cache_file, "w+") as opened_file:
        opened_file.write(input_data)


def delete_input(year, day, session):
    """Delete input from a cache folder"""
    cache_file = _join_path(year, day, session, input_file=True)
    if Path(cache_file).exists():
        os.remove(cache_file)


def cache_file_data(year, day, session):
    """Return cache file input data from cache folder for certain problem"""
    from .server_action import download_input

    download_input(year, day, session)
    cache_file = _join_path(year, day, session, input_file=True)
    with open(cache_file) as opened_file:
        input_data = opened_file.read()
    return input_data


def save_submitted_answer(year, day, part, session, output, message):
    """Save submitted input to file of problem"""
    submitted_file = _join_path(year, day, session, submission=True)
    with open(submitted_file, "a") as opened_file:
        opened_file.write("{}!{}:{}\n".format(part, output, message))


def last_submitted_answer_message(year, day, part, session, output):
    """
    Check if answer is already submitted by user if submitted return message of last
    submission
    """
    submission_file = _join_path(year, day, session, submission=True)
    last_answer_message = ""
    with open(submission_file, "r") as opened_file:
        lines = opened_file.read()
        for line in lines:
            seprate_part = line.split("!", 1)
            if seprate_part[0] == part:
                seprate_output = seprate_part[1].split(":", 1)
                if seprate_output == output:
                    last_answer_message = seprate_output[1]
    return last_answer_message


def save_last_submission_time(year, day, session):
    """Save a time where a request is performed for last submission"""
    last_time_file = _join_path(year, day, session, last_file=True)
    with open(last_time_file, "w") as opened_file:
        opened_file.write(str(time.time()))


def check_less_than_one_min_submission(year, day, session):
    """
    Check last submission time for solution return true if time is less than 60 second
    """
    last_time_file = _join_path(year, day, session, last_file=True)
    with open(last_time_file, "r") as opened_file:
        last_time = float(opened_file.read())
        current_time = time.time()
        early_submission = current_time - last_time < 60.0
    return early_submission


def _join_path(year, day, session, input_file=False, submission=False, last_file=False):
    """Return out desire path for a config folders and files"""
    cache_location = appdirs.user_cache_dir(appname="advent-of-code")
    cache_file = os.path.join(cache_location, str(session), str(year), str(day))
    if input_file:
        cache_file = os.path.join(cache_file, "input.txt")
    if submission:
        cache_file = os.path.join(cache_file, "submission.txt")
    if last_file:
        cache_file = os.path.join(cache_file, "time.txt")
    return cache_file
