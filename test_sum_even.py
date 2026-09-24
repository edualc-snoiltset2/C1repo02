import unittest

from sum_even import sum_even


class TestSumEven(unittest.TestCase):
    def test_mixed(self):
        self.assertEqual(sum_even([1, 2, 3, 4, 5, 6]), 12)

    def test_empty(self):
        self.assertEqual(sum_even([]), 0)

    def test_no_evens(self):
        self.assertEqual(sum_even([1, 3, 5]), 0)

    def test_negatives_and_zero(self):
        self.assertEqual(sum_even([-4, -3, 0, 2]), -2)

    def test_floats(self):
        self.assertEqual(sum_even([2.0, 3.5, 4]), 6.0)


if __name__ == "__main__":
    unittest.main()
