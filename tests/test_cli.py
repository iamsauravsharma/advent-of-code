from click.testing import CliRunner

from advent_of_code_py import cli


def test_click_main():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0


def test_click_config():
    runner = CliRunner()
    result = runner.invoke(cli.config)
    assert result.exit_code == 0
