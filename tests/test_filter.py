import unittest

from yapytools import filters, filter_not_none
from yapytools.predicates import is_even


class FilterNotNoneTest(unittest.TestCase):
    def test(self):
        result = filter_not_none([None, None, 1, 2, None, 3, None, 4])

        self.assertListEqual(
            list(result),
            [1, 2, 3, 4],
        )


class FiltersTest(unittest.TestCase):
    def test_filters(self):
        results = filters(
            range(10),
            lambda it: it > 3,
            is_even,
        )

        self.assertListEqual(
            list(results),
            [4, 6, 8],
        )

    def test_empty_iterable_returns_empty_iterable(self):
        result = filters(
            [],
            lambda it: it > 3,
            is_even,
        )

        self.assertListEqual(
            list(result),
            [],
        )

    def test_no_functions_returns_iterable(self):
        result = filters(
            range(10),
        )

        self.assertListEqual(
            list(result),
            list(range(10)),
        )
