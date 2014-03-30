import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_empty(self):
        '''Test swap_k with an empty list.'''
        actual = []
        swap_k(actual, 0)
        expected = []
        self.assertEqual(actual, expected)

    def test_swap_k_single(self):
        '''Test swap_k with a list of length 1, using str.'''
        actual = ['a']
        swap_k(actual, 0)
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_swap_k_many_0(self):
        '''Test swap_k with a longer list and k=0.'''
        actual = [1, 2, 3, 4, 5]
        swap_k(actual, 0)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(actual, expected)

    def test_swap_k_many_1(self):
        '''Test swap_k with a longer list and k=1.'''
        actual = [1, 2, 3, 4, 5]
        swap_k(actual, 1)
        expected = [5, 2, 3, 4, 1]
        self.assertEqual(actual, expected)

    def test_swap_k_even_half(self):
        '''Test swap_k with an even-length list, k=len(L)//2, using str.'''
        actual = ['a', 'b', 'c', 'd', 'e', 'f']
        swap_k(actual, 3)
        expected = ['d', 'e', 'f', 'a', 'b', 'c']
        self.assertEqual(actual, expected)

    def test_swap_k_odd_half(self):
        '''Test swap_k with an odd-length list, k=len(L)//2.'''
        actual = [1, 2, 3, 4, 5]
        swap_k(actual, 2)
        expected = [4, 5, 3, 1, 2]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
