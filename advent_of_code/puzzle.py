from .cache_file import cache_file_data
from .server_action import submit_output


class _Puzzle:
    """
    Puzzle class for handling out a puzzle decorator
    """

    def __init__(self, function, year, day, part, session="default"):
        self.function = function
        self.year = year
        self.day = day
        self.part = part
        self.session = session

    def __call__(self):
        input = cache_file_data(self.year, self.day, self.session)
        answer = self.function(input)
        if answer is not None:
            submit_output(self.year, self.day, self.part, self.session, answer)


def puzzle(year, day, part, session="default"):
    """
    Puzzle decorator used to submit a solution and provide a input data
    """

    def _cache(function):
        return _Puzzle(function, year, day, part, session)

    return _cache
