from libqtile import widget


def init_widgets(config: dict):
    widgets = [
        widget.CurrentLayout(
            foreground=config["foreground"],
            font=config["font"],
            fontsize=16,
            markup=True,
        ),
        widget.CurrentLayoutIcon(
            background=config["background"],
            foreground=config["foreground"],
            scale=0.76,
        ),
        widget.Sep(padding=20),
        widget.GroupBox(
            font=config["font"],
            fontsize=config["fontsize"],
            margin_y=2,
            margin_x=2,
            padding_y=8,
            padding_x=5,
            borderwidth=2,
            active=config["green"],
            inactive=config["comment"],
            rounded=False,
            highlight_color=config["pink"],
            highlight_method="block",
            foreground=config["foreground"],
            background=config["background"],
        ),
        widget.Sep(padding=20),
        widget.WindowName(
            foreground=config["foreground"],
            background=config["background"],
            font=config["font"],
            fontsize=config["fontsize"],
            padding=5,
        ),
        widget.KeyboardLayout(
            font=config["font"], configured_keyboards=["us", "ir"], fmt="Keyboard: {}"
        ),
        widget.Sep(padding=20),
        widget.Net(),
        widget.Systray(
            background=config["background"],
            padding=5,
            icon_size=config["fontsize"],
        ),
        widget.PulseVolume(
            background=config["background"],
            foreground=config["foreground"],
            font=config["font"],
            emoji=True,
        ),
        widget.Notify(
            fontsize=16,
            background=config["background"],
            foreground=config["foreground"],
            default_timeout=5,
            markup=True,
            margin=5,
        ),
        widget.Clock(
            format=" %I:%M%p",
            update_interval=1,
            font=config["font"],
            fontsize=config["fontsize"],
            foreground=config["foreground"],
            background=config["background"],
        ),
    ]
    return widgets
