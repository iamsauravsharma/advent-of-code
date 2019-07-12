import inspect


class Initializer:
    function_list = {}

    def add(self, **kwargs):
        self.function_list.update(kwargs)

    def run(self, function_alias):
        self.function_list.get(function_alias)()

    def list_functions(self):
        for (keys, value) in self.function_list.items():
            print(
                "{:10} -> {}.{}".format(
                    keys, inspect.getmodule(value).__name__, value.__name__
                )
            )
