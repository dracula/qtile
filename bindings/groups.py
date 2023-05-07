# built in libs
from libqtile.config import Key
from libqtile.lazy import lazy

# Modules and Others Config files
from groups.names import init_groups


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
