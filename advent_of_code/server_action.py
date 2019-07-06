import requests
from .config_file import get_session_value
from .cache_file import check_if_downloaded, save_to_location

input_url = "https://adventofcode.com/{}/day/{}/input"
submit_url = "https://adventofcode.com/{}/day/{}/submit"


def download_input(year, day, session):
    """
        Download file from a advent of code server
    """
    session_value = get_session_value(session)
    if session_value is not None:
        if not check_if_downloaded(year, day, session):
            inputUrl = input_url.format(year, day)
            input = requests.get(inputUrl, cookies={"session": session_value})
            save_to_location(year, day, session, input.text)
    else:
        raise Exception("{} key is not present in config file".format(session))
