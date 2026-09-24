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

    def test_tuple_accepted(self):
        self.assertEqual(sum_even((2, 4)), 6)


class TestSumEvenValidation(unittest.TestCase):
    def test_rejects_float(self):
        with self.assertRaisesRegex(TypeError, r"index 1 .* float: 3\.5"):
            sum_even([2, 3.5, 4])

    def test_rejects_integral_float(self):
        with self.assertRaises(TypeError):
            sum_even([4.0])

    def test_rejects_string(self):
        with self.assertRaisesRegex(TypeError, r"index 0 .* str: '2'"):
            sum_even(["2"])

    def test_rejects_none(self):
        with self.assertRaises(TypeError):
            sum_even([1, None])

    def test_rejects_bool(self):
        with self.assertRaisesRegex(TypeError, "bool"):
            sum_even([True, 2])

    def test_rejects_non_list_input(self):
        for bad in (None, 42, "246", {2, 4}):
            with self.subTest(bad=bad):
                with self.assertRaisesRegex(TypeError, "list or tuple"):
                    sum_even(bad)


if __name__ == "__main__":
    unittest.main()
