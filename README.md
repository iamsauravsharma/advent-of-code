# Advent-of-code
(WIP) [Advent of Code][advent_of_code_link] helper CLI and library for python projects

**Status & Info:**

| Travis Build Status | Code style | License |
| :---: | :---: | :---: |
| [![Travis Build Status][build_badge]][build_link] | [![Code style][black_badge]][black_link] | [![License: MIT][license_badge]][license_link] |

## Usage

### Installation
To install out advent-of-code run out following command which install out advent-of-code cli and advent_of_code library.
```bash
poetry add --git=https://github.com/iamsauravsharma/advent-of-code
```

### Usage
Initially for advent-of-code to work out it need session value or session ID which you can obtain out by viewing out cookie while visiting advent of code server.
After collecting session cookie value you need to add those value in config using advent-of-code CLI
```bash
advent-of-code config add <session-name> <session-value>
```

Now you can import out library by using
```python
import advent_of_code
```

After importing a library you can now use out either two decorator solve or submit decorator for a function of puzzle

For example:-
```python
@advent_of_code.submit(2018,3,1,session="<session-name>")
def puzzle_2018_3_10(input):
    # do some calculation
    return final_output
```

Now after decorating out function now you can call out function
```python
puzzle_2018_3_10()
```
After calling out function `final_output` value will be submitted out to advent-of-code server for 2018 year day 3
problem then returns out whether submitted answer was correct or not. If session value is not provided then
solution will be submitted to all session value set out.

You can also use out advent-of-code builtin Initializer and runner to create out appropriate CLI
tool for problem so problem can be run easily
To set advent-of-code puzzle as CLI
```python
@advent_of_code.adventrunner()
def main_cli():
    initializer = advent_of_code.Initializer()
    initializer.add("<function_alias>"="<function>")
    # add other function
    return initializer
```
Now you can set out main_cli as entry points and it will create out CLI with appropriate name and function which was added.

[advent_of_code_link]: https://adventofcode.com

[build_badge]: https://img.shields.io/travis/com/iamsauravsharma/advent-of-code.svg?logo=travis
[build_link]: https://travis-ci.com/iamsauravsharma/advent-of-code

[black_badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black_link]: https://github.com/ambv/black

[license_badge]: https://img.shields.io/github/license/iamsauravsharma/advent-of-code.svg
[license_link]: LICENSE
