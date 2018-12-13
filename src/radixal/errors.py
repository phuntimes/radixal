#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Specific errors for formatting integer strings with predefined error messages.
"""

__all__ = ['InvalidBase', 'UnknownCharacter']
__version__ = '0.1.1'
__author__ = 'Sean McVeigh'


class InvalidBase(ValueError):

    def __init__(self, value: int):
        super(InvalidBase, self).__init__(
            "base must be 2-36, not {!r}".format(value)
        )


class UnknownCharacter(ValueError):

    def __init__(self, value: int):
        super(UnknownCharacter, self).__init__(
            "cannot represent {!r} with alphabet [0-9a-z]".format(value)
        )
