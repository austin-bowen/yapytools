import unittest

from yapytools import pipe


class PipeTest(unittest.TestCase):
    def test_pipe(self):
        f = pipe(
            lambda it: it + 10,
            lambda it: it * 2,
        )

        self.assertEqual(f(0), 20)
        self.assertEqual(f(1), 22)
        self.assertEqual(f(10), 40)
