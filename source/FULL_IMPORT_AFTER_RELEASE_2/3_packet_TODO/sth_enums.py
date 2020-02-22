
from enum import Enum as _Enum


class ScopeLevels(_Enum):
    """
    Class for helping with typo mistakes.

    """
    EVERYTHING = "everything"
    CHILDREN_ONLY = "children_only"
    # NOTHING = "nothing"


def check_is_arg(arg):
    return not isinstance(arg, ScopeLevels) and arg is not None

print(check_is_arg(None))
print(check_is_arg(ScopeLevels.EVERYTHING))
print(check_is_arg(ScopeLevels.CHILDREN_ONLY))
print(check_is_arg("everything"))
print(check_is_arg("children_only"))