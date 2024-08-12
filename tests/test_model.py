import unittest

from msdbook.model import sum_ints


class TestModel(unittest.TestCase):

    def test_sum_ints(self):
        """Test to make sure `sum_ints` returns the expected value."""

        int_result = sum_ints(1, 2)

        # test equality for the output
        self.assertEqual(int_result, 3)


if __name__ == '__main__':
    unittest.main()
