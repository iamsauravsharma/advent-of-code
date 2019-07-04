import click
from .config_file import add_to_json, delete_from_json, list_from_json
from .server_action import download_input


@click.group()
def main():
    """
    CLI tool to perform action related to advent-of-code
    """
    pass


@main.group(help="Perform action related to config file")
def config():
    pass


@config.command(help="add session to config")
@click.argument("name")
@click.argument("session_value")
def add(name, session_value):
    data_list = {name: session_value}
    add_to_json(**data_list)


@config.command(help="list out all session present in config")
def list():
    list_from_json()


@config.command(help="remove session from config")
@click.argument("name")
def remove(name):
    delete_from_json(name)


@main.command(help="download solution form advent-of-code server")
@click.option("--year", "-y", multiple=True)
@click.option("--day", "-d", multiple=True)
@click.option("--session", "-s", multiple=True)
def download(year, day, session):
    for y in year:
        for d in day:
            for s in session:
                download_input(y, d, s)
