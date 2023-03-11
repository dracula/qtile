# built in libs
from libqtile.config import Key
from libqtile.lazy import lazy

# config files
from .groups import init_groups

# Set the mod key
mod = "mod4"


# Define keybindings
def init_keys():
    keys = [
        # Switch between windows in current stack pane
        Key([mod], "k", lazy.layout.down()),
        Key([mod], "j", lazy.layout.up()),
        # Move windows up or down in current stack
        Key([mod, "shift"], "k", lazy.layout.shuffle_down()),
        Key([mod, "shift"], "j", lazy.layout.shuffle_up()),
        # Switch window focus to other pane(s) of stack
        Key([mod], "space", lazy.layout.next()),
        # Swap panes of split stack
        Key([mod, "shift"], "space", lazy.layout.rotate()),
        # Toggle between different layouts as defined below
        Key([mod], "Tab", lazy.next_layout()),
        # Kill focused window
        Key([mod], "w", lazy.window.kill()),
        # Restart Qtile
        Key([mod, "control"], "r", lazy.restart()),
        # Shutdown Qtile
        Key([mod, "control"], "q", lazy.shutdown()),
    ]
    return keys


def init_apps_run():
    term = "kitty"
    browser = "firefox"

    keys = [
        Key([mod], "Return", lazy.spawn(term)),
        Key([mod], "b", lazy.spawn(browser)),
        Key([mod], "Space", lazy.spawn("dmenu_run")),
    ]

    return keys


def init_groups_keys():
    keys = []
    for i, (name, kwargs) in enumerate(init_groups(), 1):
        keys.append(
            Key([mod], str(i), lazy.group[name].toscreen())
        )  # Switch to another group
        keys.append(
            Key([mod, "shift"], str(i), lazy.window.togroup(name))
        )  # Send current window to another group
    return keys
