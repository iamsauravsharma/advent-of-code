from .cache_file import cache_file_data
from .server_action import submit_output
from .config_file import get_all_session


class _Puzzle:
    """
    Puzzle class for handling out a puzzle decorator
    """

    def __init__(
        self, function, operation_type, year, day, part, session=None, input_file=None
    ):
        self.function = function
        self.year = year
        self.day = day
        self.part = part
        if self.session is None:
            self.session == get_all_session()
        else:
            self.session = session
        self.operation_type = operation_type
        self.input_file = input_file

    def __call__(self):
        if self.input_file is None:
            input = cache_file_data(self.year, self.day, self.session)
        else:
            with open(self.input_file) as f:
                input = f.read()
        answer = self.function(input)
        if answer is not None:
            for session_list in self.session:
                if self.operation_type == "submit":
                    message = submit_output(
                        self.year, self.day, self.part, session_list, answer
                    )
                    if message.contains("Congratulation"):
                        print(
                            "{}:{}-{}-{}: {} {} {}".format(
                                session_list,
                                self.year,
                                self.day,
                                self.part,
                                answer,
                                u"\u2713",
                                message,
                            )
                        )
                    else:
                        print(
                            "{}:{}-{}-{}: {} {} {}".format(
                                session_list,
                                self.year,
                                self.day,
                                self.part,
                                answer,
                                u"\u274C",
                                message,
                            )
                        )
                elif self.operation_type == "solve":
                    print(
                        "{}:{}-{}-{}: {}".format(
                            session_list, self.year, self.day, self.part, answer
                        )
                    )


def submit(year, day, part, session=None, input_file=None):
    """
    Puzzle decorator used to submit a solution to advent_of_code server and
    provide result. If input_file is not present then it tries to download
    file and cache it for submiting solution else it will use input_file path
    """

    def _action(function):
        operation_type = "submit"
        return _Puzzle(function, operation_type, year, day, part, session, input_file)

    return _action


def solve(year, day, part, session=None, input_file=None):
    """
    Puzzle decorator used to solve a solution instead of submiting it to server its
    print output value. Puzzle can also be solved by using custom file location with
    help of input_file parameter while using input_file year, day, part are required
    even if they are not used for only reference purpose of printing output.
    """

    def _action(function):
        operation_type = "solve"
        return _Puzzle(function, operation_type, year, day, part, session, input_file)

    return _action
