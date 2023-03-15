# built in libs
from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy

# config files
from .groups import init_groups

# Set the super key
super = "mod4"
alt = "mod1"


# Define keybindings
def init_keys():
    keys = [
        # Switch between windows in current stack pane
        Key([super], "h", lazy.layout.left()),
        Key([super], "k", lazy.layout.down()),
        Key([super], "j", lazy.layout.up()),
        Key([super], "l", lazy.layout.right()),
        # Move windows posation in current stack
        Key([super, "Shift"], "h", lazy.layout.shuffle_left()),
        Key([super, "shift"], "k", lazy.layout.shuffle_down()),
        Key([super, "shift"], "j", lazy.layout.shuffle_up()),
        Key([super, "Shift"], "l", lazy.layout.shuffle_right()),
        # Flib windows tile desing
        Key([super, alt], "j", lazy.layout.flip_down()),
        Key([super, alt], "k", lazy.layout.flip_up()),
        Key([super, alt], "h", lazy.layout.flip_left()),
        Key([super, alt], "l", lazy.layout.flip_right()),
        # Switch window focus to other pane(s) of stack
        Key([super], "Tab", lazy.layout.next()),
        Key([super, "Shift"], "Tab", lazy.layout.previous()),
        # Swap panes of split stack
        Key([super, "Shift"], "space", lazy.layout.rotate()),
        # Switch Window Mode to Normalize
        Key([super, "shift"], "n", lazy.layout.normalize()),
        # Switch window Mode to FullScreen
        Key([super, "Shift"], "f", lazy.window.toggle_fullscreen()),
        # Switch between tiling mode and floating mode
        Key([super, "Shift"], "t", lazy.window.toggle_floating()),
        # resize fcuse window
        Key([super, "control"], "g", lazy.layout.grow()),
        Key([super, "control"], "s", lazy.layout.shrink()),
        Key([super, "control"], "j", lazy.layout.grow_down()),
        Key([super, "control"], "k", lazy.layout.grow_up()),
        Key([super, "control"], "h", lazy.layout.grow_left()),
        Key([super, "control"], "l", lazy.layout.grow_right()),
        # Toggle between different layouts as defined below
        Key([super], "space", lazy.next_layout()),
        # Kill focused window
        Key([super], "w", lazy.window.kill()),
        # Restart Qtile
        Key([super, "control"], "r", lazy.restart()),
        # Shutdown Qtile
        Key([super, "control"], "q", lazy.shutdown()),
    ]
    return keys


def init_apps_run():
    term = "kitty"
    browser = "firefox"

    keys = [
        Key([super], "Return", lazy.spawn(term)),
        Key([super], "b", lazy.spawn(browser)),
        Key([super], "d", lazy.spawn("dmenu_run")),
    ]

    return keys


def init_groups_keys():
    keys = []
    for i, (name, kwargs) in enumerate(init_groups(), 1):
        keys.append(
            Key([super], str(i), lazy.group[name].toscreen())
        )  # Switch to another group
        keys.append(
            Key([super, "shift"], str(i), lazy.window.togroup(name))
        )  # Send current window to another group
    return keys


def init_mouse_keys():
    mouse = [
        # other mouse bindings
        Drag(
            [super],
            "Button1",
            lazy.window.set_position_floating(),
            start=lazy.window.get_position(),
        ),
        Drag(
            [super],
            "Button3",
            lazy.window.set_size_floating(),
            start=lazy.window.get_size(),
        ),
        Click([super], "Button2", lazy.window.bring_to_front())
        # replace superkey with your preferred superifier key
    ]
    return mouse
