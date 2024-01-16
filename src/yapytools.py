"""
Yet Another Python Tools Library (yapytools) is a collection of useful Python
utilities not found in the standard library.
"""

__version__ = '0.0.1'

from typing import Callable, Iterable, Tuple, Union, Sequence


def filters(iterable: Iterable, *functions: Callable) -> Iterable:
    """
    Returns an iterator that applies the given filters to the iterable.

    Example:
        >>> values = filters(
        >>>     range(10),
        >>>     lambda it: it > 3,
        >>>     lambda it: it % 2 == 0,
        >>> )
        >>> print(list(values))
        [4, 6, 8]
    """

    for function in functions:
        iterable = filter(function, iterable)

    yield from iterable


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


def ranges(*stops: Union[int, Tuple[int, ...]]) -> Iterable[Tuple[int, ...]]:
    """
    Yield all possible combinations of values for the given ranges.

    Each range can be specified as either a ``stop`` index,
    or as ``(start, stop)`` or ``(start, stop, step)`` tuples.

    Example:

        >>> for x, y, c in ranges(800, (0, 600, 2), 3):
        >>>     value = image[x, y, c]

    This is more memory efficient than doing e.g.

        >>> for x, y, c in itertools.product(range(800), range(0, 600, 2), range(3)):
        >>>     ...

    because it does not keep a list of prviously used values in memory.
    """

    if len(stops) == 0:
        raise ValueError(f'No stop values given; must provide at least one stop value.')

    stops = [
        (stop,) if isinstance(stop, int) else stop
        for stop in stops
    ]

    yield from _ranges(stops)


def _ranges(stops: Sequence[Tuple[int, ...]]) -> Iterable[Tuple[int, ...]]:
    stop = stops[-1]

    if len(stops) == 1:
        yield from ((it,) for it in range(*stop))
    else:
        for prefix in _ranges(stops[:-1]):
            for suffix in range(*stop):
                yield prefix + (suffix,)
