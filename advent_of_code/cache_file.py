import appdirs
import os
import shutil
from pathlib import Path


def check_if_downloaded(year, day, session):
    """
    Check if really a input is downloaded or not and cached
    """
    cache_location = appdirs.user_cache_dir()
    cache_file = os.path.join(
        cache_location, str(session), str(year), str(day), "input.txt"
    )
    cache_file = Path(cache_file)
    return cache_file.exists()


def save_to_location(year, day, session, input):
    """
    Save a input to its location
    """
    cache_location = appdirs.user_cache_dir()
    cache_folder = os.path.join(
        cache_location, "advent_of_code", str(session), str(year), str(day)
    )
    Path(cache_folder).mkdir(parents=True, exist_ok=True)
    cache_file = os.path.join(cache_folder, "input.txt")
    with open(cache_file, "w+") as f:
        f.write(input)


def delete_input(year, day, session):
    """
    Delete input from a cache folders
    """
    cache_location = appdirs.user_cache_dir()
    cache_folder = os.path.join(
        cache_location, "advent_of_code", str(session), str(year), str(day)
    )
    if Path(cache_folder).exists():
        shutil.rmtree(cache_folder)
