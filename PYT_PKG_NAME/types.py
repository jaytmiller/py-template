"""This module defines basic types for {{PYT_PKG_NAME}}.
"""

import re
from dataclasses import dataclass
from collections.abc import Sequence

# -----------------------------------------------------------------------------------------
#                                inputs
# -----------------------------------------------------------------------------------------


class StrComparable(str):
    """Base class for making str subclasses comparable to themselves or str
    instances.   Note that intentionally not even subclasses are comparable,
    only a class and str.
    """

    def _check_class(self, other):
        """Comparable if type(other) is type(self) or str.   TypeError othewise."""
        if type(other) not in [str, type(None), type(self)]:
            raise TypeError(f"{type(self)} cannot be compared to {type(other)}.")

    def __eq__(self, other):
        self._check_class(other)
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))


# -----------------------------------------------------------------------------------------


@dataclass
class Inputs:
    """
    """


@dataclass
class Info:
    """All of the values returned from main."""

    def __repr__(self):
        pass

# -----------------------------------------------------------------------------------------


__all__ = [
    Info, Inputs, StrComparable
]
