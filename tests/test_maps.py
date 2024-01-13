import unittest

from yapytools import maps


class MapsTest(unittest.TestCase):
    def test_maps(self):
        result = maps(
            range(10),
            lambda it: it * 10,
            lambda it: it + 1,
        )

        self.assertListEqual(
            list(result),
            [1, 11, 21, 31, 41, 51, 61, 71, 81, 91],
        )

    def test_empty_iterable_returns_empty_iterable(self):
        result = maps(
            [],
            lambda it: it * 10,
            lambda it: it + 1,
        )

        self.assertListEqual(
            list(result),
            [],
        )

    def test_no_functions_returns_iterable(self):
        result = maps(
            range(10),
        )

        self.assertListEqual(
            list(result),
            list(range(10)),
        )
