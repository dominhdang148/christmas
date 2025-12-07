from utils.christmas_tree import play_christmas_tree_animation
from utils.screen_clearer import clear_screen

import select
import time
import sys

from colorama import init


stop_flag = False
init()


def user_pressed_enter():
    if select.select([sys.stdin], [], [], 0)[0]:
        return sys.stdin.readline().strip() == ""
    return False


while not stop_flag:
    play_christmas_tree_animation()
    for _ in range(5):
        time.sleep(0.1)
        if user_pressed_enter():
            clear_screen()
            print("Merry Christmas!")
            sys.exit()
