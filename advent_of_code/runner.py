import click


def adventrunner(func):
    def create_command():
        initializer_defined = func()

        @click.group()
        def main():
            """
            CLI tool created from a provided Initializer Object
            """
            pass

        @main.command(help="run a certain function defined inside a run function")
        @click.argument("name")
        def run(name):
            initializer_defined.run(name)

        @main.command("list", help="list out all of the available function")
        def list_functions():
            initializer_defined.list_functions()

        return main()

    return create_command
