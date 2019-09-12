import requests
from .config_file import get_session_value
from .cache_file import (
    check_if_downloaded,
    save_input_to_location,
    check_if_answer_is_present,
    save_submitted_answer,
    save_last_submission_time,
    check_last_submission_time,
)

input_url = "https://adventofcode.com/{}/day/{}/input"
submit_url = "https://adventofcode.com/{}/day/{}/answer"


def download_input(year, day, session):
    """
    Download file from a advent of code server and save it for future reference and use
    """
    session_value = get_session_value(session)
    if not check_if_downloaded(year, day, session):
        inputUrl = input_url.format(year, day)
        input = requests.get(inputUrl, cookies={"session": session_value})
        save_input_to_location(year, day, session, input.text)


def submit_output(year, day, part, session, output):
    """
    Submit solution output to a advent of code server
    """
    session_value = get_session_value(session)
    submitUrl = submit_url.format(year, day)
    submitted_message = check_if_answer_is_present(year, day, part, session, output)
    if submitted_message is None:
        last_submitted_message = check_last_submission_time(year, day, session)
        if last_submitted_message is None:
            data = {"level": part, "answer": output}
            save_last_submission_time(year, day, session)
            response = requests.post(
                submitUrl, data, cookies={"session": session_value}
            )
            if response.status_code != 200:
                message = (
                    "Error Submiting a Solution Online doesn't got response code 200"
                )
            else:
                text_data = response.text
                if "too high" in text_data:
                    message = "Your answer is too high"
                    save_submitted_answer(year, day, part, session, output, message)
                elif "too low" in text_data:
                    message = "Your answer is too low"
                    save_submitted_answer(year, day, part, session, output, message)
                elif "That's not" in text_data:
                    message = "That's not the right answer"
                    save_submitted_answer(year, day, part, session, output, message)
                elif "You don't seem" in text_data:
                    message = "You don't seem to be solving right level"
                elif "You gave an answer" in text_data:
                    message = (
                        "You have to wait for 1 min before submitting next solution"
                    )
                elif "That's the right answer":
                    message = "Congratulation, you have solved question successfully"
                    save_submitted_answer(
                        year,
                        day,
                        part,
                        session,
                        output,
                        "Congratulation, you have solved question correctly",
                    )
            return message
        else:
            return last_submitted_message
    else:
        return submitted_message
