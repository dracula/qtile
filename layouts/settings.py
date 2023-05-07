from libqtile import layout


# Define layouts
def init_layouts(layoutConfing: dict):
    layouts = [
        layout.Bsp(
            **layoutConfing,
            border_on_single=True,
            fair=False,
            wrap_clients=True,
        ),
        layout.MonadTall(
            border_focus=layoutConfing["border_focus"],
            border_normal=layoutConfing["border_normal"],
            margin=10,
            align=0,
            change_ratio=0.5,
            change_size=20,
            single_margin=10,
        ),
        layout.MonadWide(
            border_focus=layoutConfing["border_focus"],
            border_normal=layoutConfing["border_normal"],
            margin=10,
            align=0,
            change_ratio=0.5,
            change_size=20,
            single_margin=10,
        ),
        layout.Floating(**layoutConfing),
        layout.Max(**layoutConfing),
    ]
    return layouts
