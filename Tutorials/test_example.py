"""
File exhibits some of the features of unittest

To read more about what can be done, see the unittest documentation
at https://docs.python.org/3/library/unittest.html
"""
import unittest

class TestRandomStuff(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


class TestRandomStuffSkip(unittest.TestCase):

    @unittest.skip("This test doesn't do anything")
    def test_nothing(self):
        self.assertTrue(True)

    @unittest.skipUnless(1 > 5, "Always run this tests...")
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    @unittest.expectedFailure
    def test_fail(self):
        self.assertTrue(1 > 5, "if true, we're in trouble")


if __name__ == '__main__':
    unittest.main()

