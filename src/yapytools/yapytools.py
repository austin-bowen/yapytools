"""
Yet Another Python Tools Library (yapytools) is a collection of useful Python
utilities not found in the standard library.
"""

import itertools
import operator
from typing import (
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    TypeVar,
    Union, Set,
)

from yapytools.predicates import is_not_none, Predicate

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')


def associate(
        iterable: Iterable[T],
        transform: Callable[[T], Tuple[K, V]]
) -> Dict[K, V]:
    """
    Returns a dict containing key-value pairs provided by the transform
    function applied to the elements of the iterable.

    Inspired by Kotlin's `associate <https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/associate.html>`_
    function.
    """

    return dict(map(transform, iterable))


def associate_by(
        iterable: Iterable[V],
        key_selector: Callable[[V], K]
) -> Dict[K, V]:
    """
    Returns a dict containing the elements from the given iterable indexed by
    the key returned from the ``key_selector`` function applied to each
    element.

    If any two elements have the same key returned by ``key_selector``,
    then the last one gets added to the dict.

    Inspired by Kotlin's `associateBy <https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/associate-by.html>`_
    function.
    """

    return dict(
        (key_selector(v), v)
        for v in iterable
    )


def associate_with(
        iterable: Iterable[K],
        value_selector: Callable[[K], V]
) -> Dict[K, V]:
    """
    Returns a dict where keys are elements from the given iterable, and values
    are produced by the ``value_selector`` function applied to each element.

    If any two elements are equal, the last one gets added to the dict.

    Inspired by Kotlin's `associateWith <https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/associate-with.html>`_
    function.
    """

    return dict(
        (k, value_selector(k))
        for k in iterable
    )


def count(
        iterable: Iterable[K],
        predicate: Callable[[K], bool],
) -> int:
    """
    Returns the number of elements matching the given predicate.

    Inspired by Kotlin's `count <https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/count.html>`_
    function.
    """

    return sum(
        1 for item in iterable if predicate(item)
    )


def filter_not_none(iterable: Iterable[T]) -> Iterable[T]:
    """Filter out None values from iterable."""
    return filter(is_not_none, iterable)


def filters(iterable: Iterable, *functions: Callable) -> Iterable:
    """
    Returns an iterator that applies the given filters to the iterable.

    Example:
        >>> from yapytools.predicates import is_even
        >>> values = filters(
        >>>     range(10),
        >>>     lambda it: it > 3,
        >>>     is_even,
        >>> )
        >>> print(list(values))
        [4, 6, 8]
    """

    for function in functions:
        iterable = filter(function, iterable)

    yield from iterable


def find(iterable: Iterable[T], predicate: Callable[[T], bool]) -> Optional[T]:
    """
    Returns the first element matching the given predicate,
    or ``None`` if no such element was found.

    Inspired by Kotlin's `find <https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/find.html>`_
    function.
    """

    for item in iterable:
        if predicate(item):
            return item

    return None


def find_last(
        iterable: Iterable[T],
        predicate: Callable[[T], bool],
) -> Optional[T]:
    """
    Returns the last element matching the given predicate,
    or ``None`` if no such element was found.

    Inspired by Kotlin's `findLast <https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/find-last.html>`_
    function.
    """

    last_item = None

    # Traverse sequences backwards and return first matching item
    if isinstance(iterable, Sequence):
        for i in range(len(iterable) - 1, -1, -1):
            item = iterable[i]
            if predicate(item):
                return item
    # Otherwise, have to iterate over all items
    else:
        for item in iterable:
            if predicate(item):
                last_item = item

    return last_item


def flatten(iterable: Iterable[Iterable[T]]) -> Iterable[T]:
    """
    Returns a single iterable of all elements from all iterables in the given
    iterable.

    Inspired by Kotlin's `flatten <https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/flatten.html>`_
    function.
    """

    for items in iterable:
        yield from items


def group_by(
        iterable: Iterable[T],
        key_selector: Callable[[T], K],
) -> Dict[K, List[T]]:
    """
    Groups elements of the iterable by the key returned by the given
    ``key_selector`` function applied to each element, and returns a
    dict where each group key is associated with a list of
    corresponding elements.

    Example:
        >>> from yapytools.predicates import is_even
        >>> group_by(
        ...     range(10),
        ...     lambda it: 'even' if is_even(it) else 'odd',
        ... )
        {'even': [0, 2, 4, 6, 8], 'odd': [1, 3, 5, 7, 9]}

    Inspired by Kotlin's `groupBy <https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/group-by.html>`_
    function.
    """

    return group_by_to(iterable, key_selector, identity)


def group_by_to(
        iterable: Iterable[T],
        key_selector: Callable[[T], K],
        value_transform: Callable[[T], V],
) -> Dict[K, List[V]]:
    """
    Groups values returned by the ``value_transform`` function applied to each
    element of the iterable by the key returned by the given ``key_selector``
    function applied to the element, and returns a dict of each group key
    associated with a list of corresponding values.

    Example:
        >>> from yapytools.predicates import is_even
        >>> group_by_to(
        ...     range(10),
        ...     key_selector=lambda it: 'even' if is_even(it) else 'odd',
        ...     value_transform=lambda it: -it,
        ... )
        {'even': [0, -2, -4, -6, -8], 'odd': [-1, -3, -5, -7, -9]}

    Inspired by Kotlin's `groupByTo <https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/group-by-to.html>`_
    function.
    """

    result = {}

    for item in iterable:
        key = key_selector(item)
        value = value_transform(item)

        if key not in result:
            result[key] = [value]
        else:
            result[key].append(value)

    return result


def identity(value: T) -> T:
    """Simply returns the input ``value`` unchanged."""
    return value


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


def unique(iterable: Iterable[T]) -> Iterable[T]:
    """
    Returns an iterable of only the unique items in the given iterable,
    in the same order in which they appear.
    """

    prev_values = set()

    def is_unique(value_: T) -> bool:
        value_is_unique_ = value_ not in prev_values
        prev_values.add(value_)
        return value_is_unique_

    return filter(is_unique, iterable)


class Stream(Iterable):
    """
    Allows applying filtering, mapping, and accumulation functions to an
    iterable in a convenient way.

    Example:
        >>> result = (
        >>>     Stream(range(10))
        >>>     .filter(lambda it: it > 4)
        >>>     .map(lambda it: it * 10)
        >>>     .map(str)
        >>>     .to_list()
        >>> )
        >>> print(result)
        ['50', '60', '70', '80', '90']

    Inspired by Java's `Stream API <https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html>`_.
    """

    iterable: Iterable[T]

    def __init__(self, iterable: Iterable[T]):
        self.iterable = iterable

    @classmethod
    def of(cls, *items) -> 'Stream':
        """Returns a `Stream` of the args passed to this function."""
        return Stream(items)

    def __iter__(self):
        return iter(self.iterable)

    def accumulate(
            self,
            function: Callable[[T, T], T] = operator.add,
            initial: T = None,
    ) -> 'Stream':
        """See `itertools.accumulate <https://docs.python.org/3/library/itertools.html#itertools.accumulate>`_."""
        return Stream(itertools.accumulate(
            self,
            func=function,
            initial=initial,
        ))

    def enumerate(self, start: int = 0) -> 'Stream':
        return Stream(enumerate(self, start=start))

    def filter(self, function: Predicate) -> 'Stream':
        """
        Returns a :class:`Stream` with the given filter applied to the items.
        """
        return Stream(filter(function, self))

    def filter_not_none(self) -> 'Stream':
        """
        Returns a :class:`Stream` with the `None` items removed.
        See :func:`filter_not_none`.
        """
        return Stream(filter_not_none(self))

    def flatten(self) -> 'Stream':
        """See :func:`flatten`."""
        return Stream(flatten(self))

    def map(self, function: Callable[[T], V]) -> 'Stream':
        """
        Returns a :class:`Stream` with the given mapping applied to each item.
        """
        return Stream(map(function, self))

    def reversed(self) -> 'Stream':
        return Stream(reversed(self.iterable))

    def sorted(self, key=None, reverse=False) -> 'Stream':
        return Stream(sorted(self, key=key, reverse=reverse))

    def unique(self) -> 'Stream':
        """
        Returns a :class:`Stream` of only the unique items in the stream,
        in the order in which they occur. See :func:`unique`.
        """
        return Stream(unique(self))

    def zip(self, *iterables: Iterable, strict: bool = False) -> 'Stream':
        return Stream(zip(self, *iterables, strict=strict))

    def any(self) -> bool:
        return any(self)

    def count(self) -> int:
        """Returns the number of items in the stream."""
        return count(self, identity)

    def max(self) -> T:
        return max(self)

    def min(self) -> T:
        return min(self)

    def reduce(
            self,
            function: Callable[[T, T], T] = operator.add,
            initial: T = None,
            default: T = None,
    ) -> Optional[T]:
        """Returns the last result of :func:`Stream.accumulate`."""
        return self.accumulate(function=function, initial=initial).last(default=default)

    def sum(self) -> T:
        return sum(self)

    def to_list(self) -> List[T]:
        """Returns a list of items in the stream."""
        return list(self)

    def to_set(self) -> Set[T]:
        """Returns a set of items in the stream."""
        return set(self)

    def to_tuple(self) -> Tuple[T]:
        """Returns a tuple of items in the stream."""
        return tuple(self)

    def first(self, default: T = None) -> Optional[T]:
        """Returns the first item in the stream."""
        return next(iter(self), default)

    def last(self, default: T = None) -> Optional[T]:
        """Returns the last item in the stream."""

        last = default
        for item in self:
            last = item

        return last
