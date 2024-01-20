import unittest

from yapytools import Stream
from yapytools.predicates import is_even


class StreamTest(unittest.TestCase):
    def setUp(self):
        self.stream = (
            Stream(range(20))
            .filter(is_even)
            .filter(lambda it: it > 4)
            .map(lambda it: it * 10)
            .map(str)
        )

    def test_accumulate(self):
        result = Stream(range(5)).accumulate().to_list()

        self.assertListEqual(
            result,
            [0, 1, 3, 6, 10]
        )

    def test_filter_not_none(self):
        result = (
            Stream.of(None, 1, None, 2, None, 3, None)
            .filter_not_none()
            .to_list()
        )

        self.assertListEqual(result, [1, 2, 3])

    def test_flatten(self):
        result = (
            Stream.of([1, 2, 3], [4, 5], [6])
            .flatten()
            .to_list()
        )

        self.assertListEqual(
            result,
            [1, 2, 3, 4, 5, 6]
        )

    def test_unique(self):
        result = (
            Stream.of(0, 0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4)
            .unique()
            .to_list()
        )

        self.assertListEqual(result, [0, 1, 2, 3, 4])

    def test_count(self):
        self.assertEqual(7, self.stream.count())

    def test_reduce(self):
        result = Stream(range(5)).reduce()
        self.assertEqual(10, result)

    def test_to_list(self):
        self.assertListEqual(
            self.stream.to_list(),
            ['60', '80', '100', '120', '140', '160', '180']
        )

    def test_to_set(self):
        self.assertSetEqual(
            self.stream.to_set(),
            {'60', '80', '100', '120', '140', '160', '180'}
        )

    def test_to_tuple(self):
        self.assertTupleEqual(
            self.stream.to_tuple(),
            ('60', '80', '100', '120', '140', '160', '180')
        )

    def test_first(self):
        self.assertEqual('60', self.stream.first())

    def test_last(self):
        self.assertEqual('180', self.stream.last())
