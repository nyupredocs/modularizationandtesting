import sys
sys.path.insert(0,'../OLS')

import numpy as np
import transcripty as tpy
import unittest
from OLS import beta_ols



class TestHPM(unittest.TestCase):
    def setUp(self):
        self.hpm = tpy.HeterogeneousProbabilityModel(
            0.35, 0.6778, 1.0556, 0.0, 6, 12, 3, 125
        )

    def test_gpa_irrelevance(self):
        self.assertEqual(self.hpm(0.0, 0.0), self.hpm(0.0, 1.0))

    def test_p_larger_gammamin(self):
        """Tests p(a)"""
        self.assertGreaterEqual(self.hpm.gamma_min, self.hpm(-100.0, 0.0))

    def test_p_smaller_one(self):
        self.assertLessEqual(1.0, self.hpm(100.0, 0.0))

    def test_p(self):
        gamma_min, gamma_1 = self.hpm.gamma_min, self.hpm.gamma_1
        gamma_2 = self.hpm.gamma_2
        a = 2.5
        p_a = gamma_min + (1 - gamma_min)/(1 + gamma_1*np.exp(-gamma_2*a))
        self.assertAlmostEqual(p_a, self.hpm(a, 0.0))

    


if __name__ == "__main__":
    unittest.main()
