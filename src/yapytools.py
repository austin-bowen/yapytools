"""
Yet Another Python Tools Library (yapytools) is a collection of useful Python
utilities not found in the standard library.
"""

__version__ = '0.0.1'

from typing import Callable, Iterable, Tuple


def maps(iterable: Iterable, *functions: Callable) -> Iterable:
    """
    Returns an iterator that applies the given functions to each item in the
    given iterable.

    Example:
        >>> values = maps(
        >>>     range(5),
        >>>     lambda it: it + 10,
        >>>     lambda it: it * 2,
        >>> )
        >>> print(list(values))
        [20, 22, 24, 26, 28]
    """

    for function in functions:
        iterable = map(function, iterable)

    yield from iterable


def pipe(function0: Callable, *functions: Callable) -> Callable:
    """
    Create a function that pipes the given functions together.
    """

    def pipe_(*args, **kwargs):
        result = function0(*args, **kwargs)
        for function in functions:
            result = function(result)
        return result

    return pipe_


def ranges(*stops: int) -> Iterable[Tuple[int, ...]]:
    """
    Yield all possible combinations of values for the given ranges.

    Example:

        >>> for x, y, c in ranges(800, 600, 3):
        >>>     value = image[x, y, c]

    This is more memory efficient than doing e.g.

        >>> for x, y, c in itertools.product(range(800), range(600), range(3)):
        >>>     ...

    because it does not keep a list of prviously used values in memory.
    """

    if len(stops) <= 1:
        yield from ((it,) for it in range(*stops))
    else:
        for prefix in ranges(*stops[:-1]):
            for suffix in range(stops[-1]):
                yield prefix + (suffix,)
