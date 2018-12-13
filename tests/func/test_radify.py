#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from math import sqrt
from random import random
from typing import List, Iterator
from radixal import radify, InvalidBase


def primes(n: int) -> List[int]:
    """
    Returns a list of primes < n.

    :param n: maximum value
    :returns: sequence of primes
    """
    sieve = [True] * n

    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i]:
            start = i * i
            step = 2 * i
            sieve[start::step] = [False] * ((n - i * i - 1) // (2 * i) + 1)

    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def values(n: int) -> Iterator[int]:
    """
    Generate test values (0 and primes).
    Sign of prime numbers is pseudo-random.

    :param n: maximum value
    :return: iterator of ints
    """
    yield 0
    for p in primes(n):
        yield -p if random() < 0.5 else p


@pytest.mark.parametrize(
    'value', [
        pytest.param(
            i, id="value={:d}".format(i)
        ) for i in values(100)
    ]
)
@pytest.mark.parametrize(
    'base', [
        pytest.param(
            i, id="base={:d}".format(i)
        ) for i in range(2, 37)
    ]
)
def test_valid_base(value: int, base: int):
    """
    Test output from :func:`radify` passed to :class:`int` equals input.

    :param value:
    :param base:
    :return:
    """
    string = radify(value, base)
    actual = int(string, base)
    assert actual == value


@pytest.mark.parametrize(
    'base', [
        pytest.param(
            i, id="base={:d}".format(i)
        ) for i in (-1, 0, 37, 50, 64)
    ]
)
def test_invalid_base(base: int):
    """
    Test that :class:`InvalidBase` raises in appropriate conditions.

    :param base: test value
    """
    with pytest.raises(InvalidBase):
        radify(255, base)
