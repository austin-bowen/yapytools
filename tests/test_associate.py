import unittest
from collections import Counter

from yapytools import associate, associate_by, associate_with


class AssociateTest(unittest.TestCase):
    def test(self):
        result = associate(
            range(5),
            lambda it: (str(it), -it)
        )

        self.assertDictEqual(
            result,
            {
                '0': 0,
                '1': -1,
                '2': -2,
                '3': -3,
                '4': -4,
            }
        )


class AssociateByTest(unittest.TestCase):
    def test(self):
        result = associate_by(
            [0, 1, 2, 3, 4, 5],
            lambda it: str(it % 4),
        )

        self.assertDictEqual(
            result,
            {
                '0': 4,
                '1': 5,
                '2': 2,
                '3': 3,
            }
        )


class AssociateWithTest(unittest.TestCase):
    def test(self):
        counts = Counter()

        def neg_value_with_count(it_):
            counts[it_] += 1
            return -it_, counts[it_]

        result = associate_with(
            [0, 1, 2, 3, 0, 3],
            neg_value_with_count
        )

        self.assertDictEqual(
            result,
            {
                0: (0, 2),
                1: (-1, 1),
                2: (-2, 1),
                3: (-3, 2),
            }
        )
