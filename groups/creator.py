from libqtile.config import Group

from .names import init_names


# Making objects from each group member
def init_name_creator():
    return [Group(name, **kwargs) for name, kwargs in init_names()]
