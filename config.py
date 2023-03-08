#  qtile built-in libraries
from libqtile import bar, hook
from libqtile.config import Screen
from libqtile.lazy import lazy

# Config files and other libraries
from cfg.bindings import init_app_run, init_keys
from cfg.groups import init_group_mappings, init_groups
from cfg.layouts import init_layouts
from cfg.widgets import init_widgets
from colors.dracula import Dracula

# Set the Vars objects
keys = init_keys()
apps = init_app_run()
keys.extend(apps)
widgets = init_widgets()
layouts = init_layouts()
groups = init_groups()
group_mappings = init_group_mappings()


# Set your default widget styles
colors = Dracula()
widget_defaults = dict(
    font="Fera Code Font Mono",
    fontsize=12,
    fontshadow=None,
)

# Merge the theme dictionary with the widget_defaults dictionary
widget_defaults.update(colors)


# Set up the hooks
@hook.subscribe.startup_once
def autostart():
    lazy.spawn("picom -b")


# Define the bar
def init_bar():
    return bar.Bar(
        widgets,
        24,
    )


# Set up the screens
screens = [Screen(top=init_bar())]

# Set the remaining attributes of the qtile object
def main(qtile):
    qtile.configured = False
    # Set the remaining attributes of the qtile object
    qtile.widget_defaults = widget_defaults
    qtile.keys = keys
    qtile.groups = groups
    qtile.group_mappings = group_mappings
    qtile.layouts = layouts
    qtile.screen = screens
    qtile.configured = True
