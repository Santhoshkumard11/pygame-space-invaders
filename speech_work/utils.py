from pyautogui import press, keyDown, keyUp
from typing import Callable
import logging
from time import sleep
from constants import COMMANDS_AUDIO_MOVE_MAPPING


def move_ship_left(sleep_interval=0.07):
    keyDown("left")
    sleep(sleep_interval)
    keyUp("left")


def move_ship_right(sleep_interval=0.07):
    keyDown("right")
    sleep(sleep_interval)
    keyUp("right")


def move_ship_left_corner():
    move_ship_left(1)


def move_ship_right_corner():
    move_ship_right(1)


def shoot():
    press("space")


def rapid_fire():
    press("space", presses=100, interval=0.1)


def do_nothing():
    pass


def process_text(text: str):
    """Scan through the list of phrases and pick the best match

    Args:
        text (str): text from Azure Cognitive Service

    Returns:
        str: method name to the corresponding command
    """

    # if nothing matches call do_nothing
    method_name = "do_nothing"

    for action, method_name in COMMANDS_AUDIO_MOVE_MAPPING.items():
        if text.find(action) != -1:
            method_name = method_name
            break

    return method_name


def make_move(text: str):
    """Get a single command name from the transcribed text and call the corresponding command

    Args:
        text (str): text from Azure Cognitive Service
    """

    callable_action_method_name = process_text(text)

    callable_action_method: Callable = globals()[callable_action_method_name]

    logging.info(f"Executing - {callable_action_method_name}")
    try:
        callable_action_method()
    except Exception as e:
        logging.error(f"Error executing {callable_action_method_name} \n{e}")
    else:
        logging.info(f"Successfully Executed - {callable_action_method_name}")
