from libqtile import widget


def init_widgets(config: dict):
    widgets = [
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
        widget.Prompt(
            font=config["font"],
            fontsize=config["fontsize"],
            foreground=config["foreground"],
            background=config["background"],
            padding=5,
            prompt="Run: ",
            cursor_color=config["comment"],
        ),
        widget.WindowName(
            foreground=config["foreground"],
            background=config["background"],
            font=config["font"],
            fontsize=config["fontsize"],
            padding=5,
        ),
        widget.Wlan(
            interface="wlan0",
            format="[{ssid}] {quality:03.0f}%",
        ),
        widget.Systray(
            background=config["background"],
            padding=5,
            icon_size=config["fontsize"],
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
