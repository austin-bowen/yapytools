import unittest

from yapytools import flatten


class FlattenTest(unittest.TestCase):
    def test(self):
        result = flatten([
            [1, 2, 3],
            [4, 5],
            [6],
            [],
        ])

        self.assertListEqual(
            list(result),
            [1, 2, 3, 4, 5, 6],
        )
