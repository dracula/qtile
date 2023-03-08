from libqtile.config import Group

# Define groups
def init_groups():
    groups = [Group(i) for i in "123456789"]
    return groups

# Assign apps to specific groups
def init_group_mappings():
    group_mappings = [
        ("Firefox", "1"),
        ("Emacs", "2"),
        ("Gnome-terminal", "3"),
        ("Nautilus", "4"),
    ]
    return group_mappings
