# Radical

A library for representing a base 10 integer as a string of arbitrary radix using
standard alphabet `[0-9a-z]`.


## Usage

The highlight of this library is `radify`, which is intended to be the inverse of
`int(..., base)` and a generalization of `bin`, `oct`, and `hex`.

For example, in base 4:

```
>>> radify(255, 4)
'3333'

>>> int('3333', 4)
255
```

Or octal:

```
>>> radify(255, 8)
'377'

>>> oct(255)
'0o377'
```

Or hexadecimal:

```
>>> radify(255, 16)
'FF'

>>> hex(255)
'0xFF'
```

Or base 32:

```
>>> radify(255, 32)
'7V'

>>> int('7V', 32)
255
```


## Testing

A full [py.test] suite exists:

 * **unit** for testing character encoding
 * **func** for testing main function

[py.test]: https://docs.pytest.org/
