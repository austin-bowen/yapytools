import unittest

from yapytools import count


class CountTest(unittest.TestCase):
    def test(self):
        result = count(range(10), lambda it: it > 5)
        self.assertEqual(result, 4)

    def test_empty_iterable(self):
        result = count([], lambda it: True)
        self.assertEqual(result, 0)
