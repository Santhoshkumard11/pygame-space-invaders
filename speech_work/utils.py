from pyautogui import press
from constants import COMMANDS_AUDIO_MOVE_MAPPING
from typing import Callable
import logging


def move_ship_left():
    press("left")


def move_ship_right():
    press("right")


def do_nothing():
    pass


def process_text(text: str):
    """Scan through the list of phrases and pick the best match

    Args:
        text (str): text from Azure Cognitive Service

    Returns:
        str: method name to the corresponding command
    """

    for action, method_name in COMMANDS_AUDIO_MOVE_MAPPING.items():
        if text.find(action) != -1:
            return method_name

    # if nothing matches call do_nothing
    return "do_nothing"


def make_move(text):
    """Get a single command name from the transcribed text and call the corresponding command

    Args:
        text (str): text from Azure Cognitive Service
    """

    text: str = process_text(text)

    callable_action_method: Callable = globals()[text]
    callable_action_method_name = callable_action_method.__name__
    logging.info(f"Executing - {callable_action_method_name}")
    try:
        callable_action_method()
    except Exception as e:
        logging.error(f"Error executing {callable_action_method_name} \n{e}")
    else:
        logging.info(f"Successfully Executed - {callable_action_method_name}")
