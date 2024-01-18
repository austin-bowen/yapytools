import unittest

from yapytools import find, find_last


class FindTest(unittest.TestCase):
    def test_with_item_in_iterable(self):
        result = find(range(11), lambda it: it % 2)
        self.assertEqual(result, 1)

    def test_with_item_not_in_iterable(self):
        result = find(range(11), lambda it: it < 0)
        self.assertIsNone(result)


class FindLastTest(unittest.TestCase):
    def test_with_item_in_iterable(self):
        result = find_last(range(11), lambda it: it % 2)
        self.assertEqual(result, 9)

    def test_with_item_not_in_iterable(self):
        result = find_last(range(11), lambda it: it < 0)
        self.assertIsNone(result)

    def test_with_item_in_sequence(self):
        result = find_last(list(range(11)), lambda it: it % 2)
        self.assertEqual(result, 9)

    def test_with_item_not_in_sequence(self):
        result = find_last(list(range(11)), lambda it: it < 0)
        self.assertIsNone(result)
