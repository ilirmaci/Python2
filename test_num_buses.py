import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_num_buses_0(self):
        '''Test num_buses with 0 passengers'''
        actual = num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_num_buses_full(self):
        '''Test num_buses with full load (i.e. n % 50 = 0)'''
        actual = num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_partial(self):
        '''Test num_buses with partial load on last bus (i.e. n % 50 > 0)'''
        actual = num_buses(75)
        expected = 2
        self.assertEqual(actual, expected)
    

if __name__ == '__main__':
    unittest.main(exit=False)
