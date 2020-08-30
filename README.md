# Advent-of-code-py
[Advent of Code][advent_of_code_link] helper CLI and library for python projects.

**Note:**
Currently it is still in beta stage which may have lots of bug please report bugs if you find any within library

**Status & Info:**

| Travis Build Status | Code style | License | Project Version |
| :---: | :---: | :---: | :---: |
| [![Travis Build Status][build_badge]][build_link] | [![Code style][black_badge]][black_link] | [![License: MIT][license_badge]][license_link] | [![PyPI][project_badge]][project_link] |

## Usage

### Installation
To install advent-of-code-py run following command which installs advent-of-code-py cli and advent_of_code_py library.
```bash
pip install advent-of-code-py
```

__OR__

```bash
poetry add advent-of-code-py
```

### Usage
Initially for advent-of-code-py to work it need session value or session ID which you can obtain by viewing cookie while visiting advent of code server.
After collecting session cookie value you need to add those values in config using advent-of-code-py CLI
```bash
advent-of-code-py config add <session-name> <session-value>
```

Now you can import library by using
```python
import advent_of_code_py
```

After importing a library you can use either two decorator present which are solve or submit decorator for a function of puzzle

For example:-
```python
@advent_of_code_py.submit(2018,3,1,session_list="<session-name>")
def puzzle_2018_3_1(data=None):
    # do some calculation with data and return final output
    return final_output
```

Now after decorating function now you can call function like regular function call
```python
puzzle_2018_3_1()
```
After calling function `final_output` value will be submitted by library to Advent of Code server for 2018 year day 3
problem, then returns whether the submitted answer was correct or not. If session value is not provided then
the solution will be submitted to all session value present in config file.

You can also use advent-of-code-py builtin Initializer and runner to create appropriate CLI tool for problem so
problem can be run easily from CLI instead of modifying python file every time to all appropriate function
To set advent-of-code-py puzzle as CLI
```python
@advent_of_code_py.advent_runner()
def main_cli():
    initializer = advent_of_code_py.Initializer()
    initializer.add("<function_alias>"="<function>")
    # for example to run above function you can write
    initializer.add(p_3_1=puzzle_2018_3_1)
    # add other function
    return initializer
```
Now you can set main_cli as entry points and it will create CLI with appropriate name and function which was added.
So for example to run function puzzle_2018_3_1() you have to run command as `entry-point-name run p_3_1` which
will run appropriate function as well as submit as desired if function was decorated by submit decorator or else only
prints its output.

[advent_of_code_link]: https://adventofcode.com

[build_badge]: https://img.shields.io/travis/com/iamsauravsharma/advent-of-code-py.svg?logo=travis
[build_link]: https://travis-ci.com/iamsauravsharma/advent-of-code-py

[black_badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black_link]: https://github.com/ambv/black

[license_badge]: https://img.shields.io/github/license/iamsauravsharma/advent-of-code-py.svg
[license_link]: LICENSE

[project_badge]: https://img.shields.io/pypi/v/advent-of-code-py?color=blue&logo=python
[project_link]: https://pypi.org/project/advent-of-code-py