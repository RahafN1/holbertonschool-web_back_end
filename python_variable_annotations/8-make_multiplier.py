#!/usr/bin/env python3
"""Module that defines a function returning a multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by a given multiplier.

 def multiplier_function(value: float) -> float:
        """Multiply value by the outer multiplier."""
        return value * multiplier
