def is_false(value) -> bool:
    return not bool(value)


def is_true(value) -> bool:
    return bool(value)


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
