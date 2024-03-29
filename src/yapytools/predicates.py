from typing import Callable, TypeVar

T = TypeVar('T')

Predicate = Callable[[T], bool]


def is_false(value) -> bool:
    return not bool(value)


def is_true(value) -> bool:
    return bool(value)


def is_none(value) -> bool:
    return value is None


def is_not_none(value) -> bool:
    return value is not None


def is_zero(value) -> bool:
    return value == 0


def is_not_zero(value) -> bool:
    return value != 0


def is_positive(value) -> bool:
    return value > 0


def is_negative(value) -> bool:
    return value < 0


def is_not_positive(value) -> bool:
    return value <= 0


def is_not_negative(value) -> bool:
    return value >= 0


def is_even(value: int) -> bool:
    return value % 2 == 0


def is_odd(value: int) -> bool:
    return value % 2 == 1
