"""
initializer module which defines Initializer class which initialize advent of code
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
        """
        Add a function to a Initializer class.
        To add function to Initializer list pass `alias_of_function=function`
        as kwargs value. \n
        For example:-\n
        `initializer_name.add("solve1"=day1)`\n
        will add function day1 and alias
        it as solve1
        """
        self.function_list.update(kwargs)

    def run(self, function_alias):
        """
        Run a certain function by their name/alias \n
        For example:-\n
        `initializer_name.run("solve1")`\n
        will run any function which is aliased as solve1
        """
        self.function_list.get(function_alias)()

    def run_all(self):
        """
        Run all functions which are added to `Initializer`
        """
        for value in self.function_list.values():
            value()

    def list_functions(self):
        """
        List out all of the function and its location along with its alias
        """
        for (keys, value) in self.function_list.items():
            print(
                "{:10} -> {}.{}".format(
                    keys, inspect.getmodule(value).__name__, value.__name__
                )
            )
