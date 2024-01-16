import unittest

from yapytools import ranges


class RangesTest(unittest.TestCase):
    def test_zero_values_raises_TypeError(self):
        with self.assertRaises(ValueError):
            list(ranges())

    def test_one_value(self):
        self.assertListEqual(
            list(ranges(1)),
            [(0,)],
        )

        self.assertListEqual(
            list(ranges(3)),
            [(0,), (1,), (2,)],
        )

    def test_multiple_values(self):
        self.assertListEqual(
            list(ranges(3, 2, 2)),
            [
                (0, 0, 0),
                (0, 0, 1),
                (0, 1, 0),
                (0, 1, 1),
                (1, 0, 0),
                (1, 0, 1),
                (1, 1, 0),
                (1, 1, 1),
                (2, 0, 0),
                (2, 0, 1),
                (2, 1, 0),
                (2, 1, 1),
            ]
        )

    def test_multiple_values_with_start_and_step_args(self):
        self.assertListEqual(
            list(ranges((2, 5), (10, 3, -3))),
            [
                (2, 10),
                (2, 7),
                (2, 4),
                (3, 10),
                (3, 7),
                (3, 4),
                (4, 10),
                (4, 7),
                (4, 4),
            ]
        )

    def test_values_containing_zero_returns_no_items(self):
        self.assertListEqual(
            list(ranges(3, 0, 2)),
            [],
        )
