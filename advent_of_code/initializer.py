"""
initializer module which defines Initializer class for initializing advent of code
function runner
"""
import inspect


class Initializer:
    """
    Initialize class which is used to initialize an advent of code function runner.
    Initialize create out a basic class which is used for adding of different
    function of advent of code solution so all of functions can be easily run with
    one simple CLI tool.
    """

    function_list = {}

    def add(self, **kwargs):
        """Add a function to a Initializer class"""
        self.function_list.update(kwargs)

    def run(self, function_alias: str):
        """Run a certain function by their name/alias"""
        self.function_list.get(function_alias)()

    def run_all(self):
        """Run all functions which are added to `Initializer`"""
        for value in self.function_list.values():
            value()

    def list_functions(self):
        """List out all of the function and its location along with its alias"""
        for (keys, value) in self.function_list.items():
            print(
                "{:10} -> {}.{}".format(
                    keys, inspect.getmodule(value).__name__, value.__name__
                )
            )
