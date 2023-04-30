# python libraries
import os
import subprocess

#  qtile built-in libraries
from libqtile import bar, hook, qtile
from libqtile.config import Screen

# Config files and other libraries
from cfg.bindings import (init_apps_run, init_groups_keys, init_keys,
                          init_mouse_keys)
from cfg.groups import Groups_name_creator, init_group_mappings
from cfg.layouts import init_layouts
from cfg.widgets import init_widgets
from colors.dracula import Dracula


# Set up the hooks
@hook.subscribe.startup_once
def autostart():
    subprocess.Popen("dunst")
    subprocess.Popen(["picom", "-b"])
    subprocess.Popen(["greenclip", "daemon"])
    os.environ["QT_QPA_PLATFORMTHEME"] = "qt5ct"
    subprocess.Popen("lxqt-policykit-agent")
    subprocess.Popen("nm-applet")


# Set your default widget styles
colors = Dracula()
widgets_themes = dict(
    font="FantasqueSansMono Nerd Font Mono",
    fontsize=18,
)

# Merge the theme dictionary with the widgets_themes dictionary
widgets_themes.update(colors)

layoutConfig = dict(
    margin=[5, 2, 2, 5],
    border_width=2,
    border_focus=colors["pink"],
    border_normal=colors["cyan"],
)

# Set the Vars objects
keys = init_keys()
mouse = init_mouse_keys()
apps = init_apps_run()
keys.extend(apps)
layouts = init_layouts(layoutConfig)
groups = Groups_name_creator()
groups_bind = init_groups_keys()
keys.extend(groups_bind)
group_mappings = init_group_mappings()


# Define the bar
def init_bar():
    return bar.Bar(
        init_widgets(widgets_themes),
        24,
        opacity=0.66,
        background=colors["background"],
        floating=True,  # allow the bar to have a shadow effect
        border_width=0,  # remove the default border
        margin=[0, 5, 5, 10],  # add some margin for the shadow effect
        draw_shadow=True,  # enable the shadow effect
        shadow_offset=[0, 3],  # set the shadow offset
    )


# Set up the screens
screens = [
    Screen(
        top=init_bar(),
        wallpaper="~/.config/qtile/wallpapers/dracula_qtile.png",
        wallpaper_mode="stretch",
    )
]

focus_on_window_activation = "smart"
drag = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
wmname = "qtile"


