import unittest
import frac

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(frac.add_frac([1, 2], [1, 4]), [3, 4])

    def test_sub_frac(self):
        self.assertEqual(frac.sub_frac([1, 2], [1, 4]), [1, 4])

    def test_mul_frac(self):
        self.assertEqual(frac.mul_frac([5, 9], [3, 5]), [1, 3])

    def test_div_frac(self):
        self.assertEqual(frac.div_frac([4, 6], [4, 3]), [1, 2])

    def test_is_positive(self):
        self.assertEqual(frac.is_positive([1, -2]), False)
        self.assertEqual(frac.is_positive([-1, -4]), True)
        self.assertEqual(frac.is_positive([3, 5]), True)

    def test_is_zero(self):
        self.assertEqual(frac.is_zero([0, 2]), True)
        self.assertEqual(frac.is_zero([2, 5]), False)

    def test_cmp_frac(self):
        self.assertEqual(frac.cmp_frac([1, 2], [1, 4]), 1)
        self.assertEqual(frac.cmp_frac([1, 2], [2, 4]), 0)
        self.assertEqual(frac.cmp_frac([-1, 2], [1, 4]), -1)

    def test_frac2float(self):
        self.assertEqual(frac.frac2float([1, 2]), 0.5)
        self.assertEqual(frac.frac2float([0, 1]), 0.0)
        self.assertEqual(frac.frac2float([-1, 4]), -0.25)
        self.assertEqual(frac.frac2float([1, -4]), -0.25)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy