import unittest

from refund import calculate_refund


class TestRefund(unittest.TestCase):
    def test_standard_refund(self):
        self.assertEqual(calculate_refund(100), 85.0)

    def test_zero_fee(self):
        self.assertEqual(calculate_refund(100, fee_percent=0), 100.0)


if __name__ == "__main__":
    unittest.main()
