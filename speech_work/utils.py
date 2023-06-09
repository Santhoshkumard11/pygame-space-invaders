from pyautogui import press, keyDown, keyUp
from typing import Callable
import logging
import asyncio
from constants import COMMANDS_AUDIO_MOVE_MAPPING


async def ahold(key, sleep_interval=0.07):
    keyDown(key)
    await asyncio.sleep(sleep_interval)
    keyUp(key)


async def apress(key, presses=2, interval=0.0):
    press(key, presses, interval)
    await asyncio.sleep(0)


async def move_ship_left(sleep_interval=0.07):
    await ahold("left", sleep_interval)


async def move_ship_right(sleep_interval=0.07):
    await ahold("right", sleep_interval)


async def move_ship_left_corner():
    await move_ship_left(sleep_interval=1.2)


async def move_ship_right_corner():
    await move_ship_right(sleep_interval=1.2)


async def shoot():
    await apress("space")


async def rapid_fire():
    await apress("space", presses=100, interval=0.1)


async def start_game():
    await shoot()


async def pause_game():
    await apress("esc", presses=1)


async def do_nothing():
    await asyncio.sleep(0)


def process_text(text: str):
    """Scan through the list of phrases and pick the best match

    Args:
        text (str): text from Azure Cognitive Service

    Returns:
        str: method name to the corresponding command
    """

    # if nothing matches call do_nothing
    default_method_name = "do_nothing"

    for action, method_name in COMMANDS_AUDIO_MOVE_MAPPING.items():
        if text.find(action) != -1:
            return method_name

    return default_method_name


async def make_move(text: str):
    """Get a single command name from the transcribed text and call the corresponding command

    Args:
        text (str): text from Azure Cognitive Service
    """

    callable_action_method_name = process_text(text)

    callable_action_method: Callable = globals()[callable_action_method_name]

    logging.info(f"Executing - {callable_action_method_name}")
    try:
        await callable_action_method()
    except Exception as e:
        logging.error(f"Error executing {callable_action_method_name} \n{e}")
    else:
        logging.info(f"Successfully Executed - {callable_action_method_name}")
