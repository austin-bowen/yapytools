import unittest

from yapytools import filters


class FiltersTest(unittest.TestCase):
    def test_filters(self):
        results = filters(
            range(10),
            lambda it: it > 3,
            lambda it: it % 2 == 0,
        )

        self.assertListEqual(
            list(results),
            [4, 6, 8],
        )

    def test_empty_iterable_returns_empty_iterable(self):
        result = filters(
            [],
            lambda it: it > 3,
            lambda it: it % 2 == 0,
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
