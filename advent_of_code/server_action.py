import requests
from .config_file import get_session_value
from .cache_file import check_if_downloaded, save_to_location

input_url = "https://adventofcode.com/{}/day/{}/input"
submit_url = "https://adventofcode.com/{}/day/{}/answer"


def download_input(year, day, session):
    """
        Download file from a advent of code server
    """
    session_value = get_session_value(session)
    if not check_if_downloaded(year, day, session):
        inputUrl = input_url.format(year, day)
        input = requests.get(inputUrl, cookies={"session": session_value})
        save_to_location(year, day, session, input.text)


def submit_output(year, day, part, session, output):
    """
    Submit solution to a advent of code server
    """
    session_value = get_session_value(session)
    submitUrl = submit_url.format(year, day)
    data = {"level": part, "answer": output}
    requests.post(submitUrl, data, cookies={"session": session_value})
