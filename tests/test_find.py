import unittest

from parameterized import parameterized

from yapytools import find, find_last
from yapytools.predicates import is_odd, is_negative


class FindTest(unittest.TestCase):
    def test_with_item_in_iterable(self):
        result = find(range(11), is_odd)
        self.assertEqual(result, 1)

    def test_with_item_not_in_iterable(self):
        result = find(range(11), is_negative)
        self.assertIsNone(result)


class FindLastTest(unittest.TestCase):
    @parameterized.expand([10, 11])
    def test_with_item_in_iterable(self, stop: int):
        result = find_last(iter(range(stop)), is_odd)
        self.assertEqual(result, 9)

    def test_with_item_not_in_iterable(self):
        result = find_last(iter(range(11)), is_negative)
        self.assertIsNone(result)

    @parameterized.expand([10, 11])
    def test_with_item_in_sequence(self, stop: int):
        result = find_last(list(range(stop)), is_odd)
        self.assertEqual(result, 9)

    def test_with_item_not_in_sequence(self):
        result = find_last(list(range(11)), is_negative)
        self.assertIsNone(result)
