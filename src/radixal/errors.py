#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module defines specific errors for formatting integer strings with predefined
error messages.
"""

__all__ = ['InvalidBase', 'UnknownCharacter']
__version__ = '0.1.5'
__author__ = 'Sean McVeigh'


class InvalidBase(ValueError):
    """
    Specific instance wherein requested integer base is unsupported.
    """

    def __init__(self, value: int):
        """
        Format error message.

        :param value: invalid integer
        """
        super(InvalidBase, self).__init__(
            "base must be 2-36, not {!r}".format(value)
        )


class UnknownCharacter(ValueError):
    """
    Specific instance wherein requested character is undefined in alphabet.
    """

    def __init__(self, value: int):
        """
        Format error message.

        :param value: invalid integer
        """
        super(UnknownCharacter, self).__init__(
            "cannot represent {!r} with alphabet [0-9a-z]".format(value)
        )
