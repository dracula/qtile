# built in libs
from libqtile.config import Key
from libqtile.lazy import lazy

# Modules and Others Config files
from .vars import (app_menu, browser, clipboard, file_manager, home,
                   print_screen, qt5_config, screenshot, shell_menu, super,
                   term, win_selector)


def init_apps_run():
    keys = [
        Key([super], "Return", lazy.spawn(term)),
        Key([super], "b", lazy.spawn(browser)),
        Key([super], "d", lazy.spawn(app_menu)),
        Key([super], "r", lazy.spawn(shell_menu)),
        Key([super], "w", lazy.spawn(win_selector)),
        Key([super], "v", lazy.spawn(clipboard)),
        Key([super], "e", lazy.spawn(file_manager)),
        Key([super], "q", lazy.spawn(qt5_config)),
        Key([], print_screen, lazy.spawn(f"{screenshot} -xc {home}/Pictures/")),
        Key([super], print_screen, lazy.spawn(f"{screenshot} -xsc {home}/Pictures/")),
    ]

    return keys
