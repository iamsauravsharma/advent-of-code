from .cache_file import cache_file_data
from .server_action import submit_output
from .config_file import get_all_session


class _Puzzle:
    """
    Puzzle class for handling out a puzzle decorator
    """

    def __init__(self, function, operation_type, year, day, part, session=None):
        self.function = function
        self.year = year
        self.day = day
        self.part = part
        if self.session is None:
            self.session == get_all_session()
        else:
            self.session = session
        self.operation_type = operation_type

    def __call__(self):
        input = cache_file_data(self.year, self.day, self.session)
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


def submit(year, day, part, session=None):
    """
    Puzzle decorator used to submit a solution and provide a input data
    """

    def _cache(function):
        operation_type = "submit"
        return _Puzzle(function, operation_type, year, day, part, session)

    return _cache


def solve(year, day, part, session=None):
    """
    Puzzle decorator used to solve a solution instead of submiting a submiting it
    """

    def _cache(function):
        operation_type = "solve"
        return _Puzzle(function, operation_type, year, day, part, session)

    return _cache
