from libqtile.config import Group
from .groups.names import init_groups

# Making objects from each group member
def Groups_name_creator():
    return [Group(name, **kwargs) for name, kwargs in init_groups()]

