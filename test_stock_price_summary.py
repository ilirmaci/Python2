import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_empty(self):
        '''Test stock_price_summary with an empty list of price changes.'''
        actual = stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_one_positive(self):
        '''Test stock_price_summary with a single positive entry.'''
        actual = stock_price_summary([0.05])
        expected = (0.05, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_one_negative(self):
        '''Test stock_price_summary with an a single negative entry.'''
        actual = stock_price_summary([-0.03])
        expected = (0, -0.03)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_many_positive(self):
        '''Test stock_price_summary with more positive entries.'''
        actual = stock_price_summary([0.05, 0.03])
        expected = (0.08, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_many_negative(self):
        '''Test stock_price_summary with more negative entries.'''
        actual = stock_price_summary([-0.03, -0.04, -0.06])
        expected = (0, -0.13)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_many_mixed(self):
        '''Test stock_price_summary with an longer list of price changes.'''
        actual = stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
