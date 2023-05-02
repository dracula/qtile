import os
# built in libs
from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy

# config files
from .groups import init_groups

# Set the varible key
super = "mod4"
alt = "mod1"
print_screen = "Print"
home = os.path.expanduser('~')



def resize(qtile, direction):
    layout = qtile.current_layout
    child = layout.current
    parent = child.parent

    while parent:
        if child in parent.children:
            layout_all = False

            if (direction == "left" and parent.split_horizontal) or (
                direction == "up" and not parent.split_horizontal
            ):
                parent.split_ratio = max(
                    5, parent.split_ratio - layout.grow_amount)
                layout_all = True
            elif (direction == "right" and parent.split_horizontal) or (
                direction == "down" and not parent.split_horizontal
            ):
                parent.split_ratio = min(
                    95, parent.split_ratio + layout.grow_amount)
                layout_all = True

            if layout_all:
                layout.group.layout_all()
                break

        child = parent
        parent = child.parent


@lazy.function
def resize_left(qtile):
    resize(qtile, "left")


@lazy.function
def resize_right(qtile):
    resize(qtile, "right")


@lazy.function
def resize_up(qtile):
    resize(qtile, "up")


@lazy.function
def resize_down(qtile):
    resize(qtile, "down")


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
        Key([super, "Shift"], "k", lazy.layout.shuffle_down()),
        Key([super, "Shift"], "j", lazy.layout.shuffle_up()),
        Key([super, "Shift"], "l", lazy.layout.shuffle_right()),
        # Flib windows tile desing
        Key([super, alt], "j", lazy.layout.flip_down()),
        Key([super, alt], "k", lazy.layout.flip_up()),
        Key([super, alt], "h", lazy.layout.flip_left()),
        Key([super, alt], "l", lazy.layout.flip_right()),
        # Switch window focus to other pane(s) of stack
        Key([alt], "Tab", lazy.layout.next()),
        Key([alt, "Shift"], "Tab", lazy.layout.previous()),
        # Swap panes of split stack
        Key([super, "Shift"], "Space", lazy.layout.rotate()),
        # Switch Window Mode to Normalize
        Key([super, "Shift"], "n", lazy.layout.normalize()),
        # Switch window Mode to FullScreen
        Key([super, "Shift"], "f", lazy.window.toggle_fullscreen()),
        # Switch between tiling mode and floating mode
        Key([super, "Shift"], "t", lazy.window.toggle_floating()),
        # resize fcuse window
        Key([super, "control"], "g", lazy.layout.grow()),
        Key([super, "control"], "s", lazy.layout.shrink()),
        Key([super, "control"], "j", resize_down),
        Key([super, "control"], "k", resize_up),
        Key([super, "control"], "h", resize_left),
        Key([super, "control"], "l", resize_right),
        # Toggle between different layouts as defined below
        Key([super], "Tab", lazy.next_layout()),
        # Switch KeyBoard language
        Key([super], "Space", lazy.widget["keyboardlayout"].next_keyboard()),
        # Kill focused window
        Key([super], "w", lazy.window.kill()),
        # Restart Qtile
        Key([super, "control"], "r", lazy.restart()),
        # Shutdown Qtile
        Key([super, "control"], "q", lazy.shutdown()),
    ]
    return keys


def init_apps_run():
    term = "alacritty"
    app_menu = "dmenu_run"
    clipboard = (
        'rofi -modi "clipboard:greenclip print" -show clipboard -run-command "{cmd}"'
    )
    browser = "firefox"
    file_manager = "pcmanfm-qt"
    qt5_config = "qt5ct"
    screenshot = f"{home}/.config/qtile/scripts/screenshot"

    keys = [
        Key([super], "Return", lazy.spawn(term)),
        Key([super], "b", lazy.spawn(browser)),
        Key([super], "d", lazy.spawn(app_menu)),
        Key([super], "v", lazy.spawn(clipboard)),
        Key([super], "e", lazy.spawn(file_manager)),
        Key([super], "q", lazy.spawn(qt5_config)),
        Key([], print_screen, lazy.spawn(
            f"{screenshot} -xcp {home}/Pictures/")),
        Key([super], print_screen, lazy.spawn(
            f'{screenshot} -xscp {home}/Pictures/'))
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
