#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Functions for formatting integer strings with arbitrary base.
"""

__all__ = ['characterize', 'radify']
__version__ = '0.1.1'
__author__ = 'Sean McVeigh'

from .errors import InvalidBase, UnknownCharacter


def characterize(digit: int) -> str:
    """
    Convert integer value to representative character.

    :param digit: to represent
    :return: as character
    """
    if digit < 0 or digit > 35:
        raise UnknownCharacter(digit)

    if digit < 10:
        return str(digit)

    return chr(ord('a') + digit - 10)


def radify(value: int, base: int) -> str:
    """
    Represent base 10 integer value as string with arbitrary base with ascii
    alphabet ([0-9a-z], where applicable).

    :param value: integer (positive or negative)
    :param base: base to represent
    :return: string in specified base
    """
    if base < 2 or base > 36:
        raise InvalidBase(base)

    if value < 0:
        return '-' + radify(-value, base)

    div, mod = divmod(value, base)

    if div > 0:
        return radify(div, base) + characterize(mod)

    return characterize(mod)
