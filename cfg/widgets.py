from libqtile import widget


def init_widgets():
    widgets = [
        widget.GroupBox(),
        widget.Prompt(),
        widget.WindowName(),
        widget.TextBox("default config", name="default"),
        widget.Systray(),
        widget.Clock(format="&#x27;%Y-%m-%d %a %I:%M %p&#x27;"),
    ]
    return widgets
