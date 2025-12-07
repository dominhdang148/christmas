from colorama import Fore, Style

import random

from utils.screen_clearer import clear_screen


def print_random_color_text(text: str):

    colors = [
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE,
        Fore.LIGHTBLACK_EX,
        Fore.LIGHTBLUE_EX,
        Fore.LIGHTRED_EX,
        Fore.LIGHTYELLOW_EX,
        Fore.LIGHTCYAN_EX,
        Fore.LIGHTGREEN_EX,
        Fore.LIGHTWHITE_EX,
        Fore.LIGHTMAGENTA_EX
    ]

    colored_chars = []

    for char in text:
        random_color = random.choice(colors)
        colored_chars.append(random_color+char)

    print("".join(colored_chars) + Style.RESET_ALL)


def play_christmas_tree_animation():
    clear_screen()
    print_random_color_text("       *       ")
    print_random_color_text("      ***      ")
    print_random_color_text("     *****     ")
    print_random_color_text("    *******    ")
    print_random_color_text("   *********   ")
