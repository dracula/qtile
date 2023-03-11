from libqtile import layout


# Define layouts
def init_layouts(layoutConfing:dict):

    layouts = [
        layout.Bsp(**layoutConfing),
        layout.MonadTall(**layoutConfing),
        layout.MonadWide(**layoutConfing),
        layout.Matrix(**layoutConfing),
    ]
    return layouts
