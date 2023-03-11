from libqtile.config import Group

# Define groups
def init_groups():
    group_names = [
        ("", {"layout": "bsp"}),
        ("", {"layout": "bsp"}),
        ("｡♪", {"layout": "bsp"}),
        ("", {"layout": "bsp"}),
        ("", {"layout": "bsp"}),
        ("", {"layout": "bsp"}),
    ]
    return group_names
 


# Making objects from each group member
def Groups_name_creator():
    return  [Group(name, **kwargs) for name, kwargs in init_groups()]


# Assign apps to specific groups
def init_group_mappings():
    return {
        "chromium": "1",
        "firefox": "1",
        "spotify": "3",
        "telegram-desktop": "6",
    }
