from libqtile.config import Group


# Define groups
def init_groups():
    group_names = [
        (""),
        (""),
        ("｡♪"),
        (""),
        (""),
        (""),
    ]

    groups = [Group(i) for i in group_names]
    return groups


# Assign apps to specific groups
def init_group_mappings():
    return {
        "chromium": "1",
        "firefox": "1",
        "spotify": "3",
        "telegram-desktop": "6",
    }
