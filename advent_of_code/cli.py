import click

from .cache_file import delete_input
from .config_file import add_to_json, delete_from_json, get_all_session, list_from_json
from .server_action import download_input
from .utils import get_current_year, get_day


@click.group()
def main():
    """
    CLI tool to perform action related to advent-of-code
    """
    pass


@main.group(help="perform action related to config file")
def config():
    pass


@config.command(help="add session to config")
@click.argument("name")
@click.argument("session_value")
def add(name, session_value):
    data_list = {name: session_value}
    add_to_json(**data_list)


@config.command("list", help="list out all session present in config")
def list_config_session():
    list_from_json()


@config.command("remove", help="remove session from config")
@click.argument("name")
def remove_config_data(name):
    delete_from_json(name)


@main.command(help="download solution from advent-of-code server")
@click.option(
    "--year",
    "-y",
    multiple=True,
    help="Pass input download year [default: latest year]",
)
@click.option(
    "--day",
    "-d",
    multiple=True,
    help="Pass input download day [default: latest day or day 1 of old year]",
)
@click.option(
    "--session",
    "-s",
    multiple=True,
    help="Pass session name or use all session as default",
)
def download(year, day, session):
    if year == ():
        year = [get_current_year()]
    if day == ():
        day = [get_day()]
    if session == ():
        session = get_all_session()
    for y in year:
        for d in day:
            for s in session:
                download_input(y, d, s)


@main.command("remove", help="delete a input file from cache folder")
@click.option(
    "--year",
    "-y",
    multiple=True,
    help="Year from which input is to be delete default all",
)
@click.option(
    "--day",
    "-d",
    multiple=True,
    help="Day from which input file is to be delete default all day",
)
@click.option(
    "--session",
    "-s",
    multiple=True,
    help="Session from which input file is to be deleted default all session",
)
def remove_cache(year, day, session):
    if year == ():
        year = list(range(2015, get_current_year() + 1))
    if day == ():
        day = list(range(1, 26))
    if session == ():
        session = get_all_session()
    print(year, day, session)
    for y in year:
        for d in day:
            for s in session:
                delete_input(y, d, s)
