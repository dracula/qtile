from libqtile import layout

# Define layouts
def init_layouts():
    layouts = [
        layout.MonadTall(),
        layout.MonadWide(),
        layout.Matrix(),
    ]
    return layouts
