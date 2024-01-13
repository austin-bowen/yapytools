"""
Yet Another Python Tools Library (yapytools) is a collection of useful Python
utilities not found in the standard library.
"""

__version__ = '0.0.1'

from typing import Callable, Iterable, Tuple


def ranges(*stops: int) -> Iterable[Tuple[int, ...]]:
    """Yield all possible combinations of values for the given ranges."""

    if len(stops) <= 1:
        yield from ((it,) for it in range(*stops))
    else:
        for prefix in ranges(*stops[:-1]):
            for suffix in range(stops[-1]):
                yield prefix + (suffix,)


def maps(iterable: Iterable, function0: Callable, *functions: Callable) -> Iterable:
    results = map(function0, iterable)
    for function in functions:
        results = map(function, results)

    yield from results


def pipe(function0: Callable, *functions: Callable) -> Callable:
    """Create a function that pipes the given functions together."""

    def pipe_(*args, **kwargs):
        result = function0(*args, **kwargs)
        for function in functions[1:]:
            result = function(result)
        return result

    return pipe_
