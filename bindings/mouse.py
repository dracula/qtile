# built in libs
from libqtile.config import Click, Drag
from libqtile.lazy import lazy


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
