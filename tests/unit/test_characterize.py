#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from string import digits, ascii_lowercase
from radixal import characterize, UnknownCharacter


ALPHABET = tuple(digits + ascii_lowercase)


@pytest.mark.parametrize(
    'value, expected', [
        pytest.param(
            i, c, id="char of {:d}".format(i)
        ) for i, c in enumerate(ALPHABET)
    ]
)
def test_valid_character(value: int, expected: str):
    """
    Test that digit is converted to its character appropriate character.

    :param value: test value
    :param expected: expected character
    """
    actual = characterize(value)
    assert actual == expected


@pytest.mark.parametrize(
    'value', [
        pytest.param(
            i, id="char of {:d}".format(i)
        ) for i in (-1, 37, 50, 64)
    ]
)
def test_invalid_character(value: int):
    """
    Test that digit is converted to its character appropriate character

    :param value: test value
    """
    with pytest.raises(UnknownCharacter):
        characterize(value)
