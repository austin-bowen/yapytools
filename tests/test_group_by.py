import unittest

from yapytools import group_by, group_by_to
from yapytools.predicates import is_even


class GroupByTest(unittest.TestCase):
    def test(self):
        result = group_by(
            range(10),
            lambda it: 'odd' if it % 2 else 'even',
        )

        self.assertDictEqual(
            result,
            {'even': [0, 2, 4, 6, 8], 'odd': [1, 3, 5, 7, 9]}
        )

    def test_empty_iterable_returns_empty_dict(self):
        result = group_by(
            [],
            lambda it: 'odd' if it % 2 else 'even',
        )

        self.assertDictEqual(result, {})


class GroupByToTest(unittest.TestCase):
    def test(self):
        result = group_by_to(
            range(10),
            key_selector=lambda it: 'even' if is_even(it) else 'odd',
            value_transform=lambda it: -it,
        )

        self.assertDictEqual(
            result,
            {'even': [0, -2, -4, -6, -8], 'odd': [-1, -3, -5, -7, -9]}
        )

    def test_empty_iterable_returns_empty_dict(self):
        result = group_by_to(
            [],
            key_selector=lambda it: 'even' if is_even(it) else 'odd',
            value_transform=lambda it: -it,
        )

        self.assertDictEqual(result, {})
