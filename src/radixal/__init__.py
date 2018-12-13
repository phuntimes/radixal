#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Library for representing a base 10 integer as a string of arbitrary base using
standard alphabet.

The highlight of this library is :func:`radix`, which is the main
function. For example:

>>> radify(255, 4)
'3333'

>>> radify(255, 8)
'377'

>>> radify(255, 16)
'FF'

>>> radify(255, 32)
'7V'

Error :class:`InvalidBase` is raised when the specified base is outside the
standard alphabet (i.e. base < 2 or base > 36).
"""

__all__ = ['radify', 'characterize', 'InvalidBase', 'UnknownCharacter']
__version__ = '0.1.3'
__author__ = 'Sean McVeigh'

from .errors import InvalidBase, UnknownCharacter
from .represent import characterize, radify
