import sys
sys.path.insert(0,'../OLS')

import numpy as np
import unittest
from OLS import beta_ols
import statsmodels.api as sm
import pandas as pd



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

    def test_simple_b_ols(self):
        np.random.seed(60683) # testing different seed
        n = 50000
        ## DGP ##
        means = [3, -1.5, 1.1, 2.3, -1, 3]
        cov = [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]]

        ## Data Generation ##
        X1, X2, X3, X4, Z1, Z2 = np.random.multivariate_normal(means, cov, n).T
        epsilon = np.random.normal(0, 1, n)

        # True model
        Y = 1.5 + 2.5*X1 + 2*X2 + 3*X3 + 6*X4 + epsilon

        independent_vars = pd.DataFrame({'X1' : X1, 'X2' : X2, 'X3' : X3, 'X4' : X4})
        independent_vars = sm.add_constant(independent_vars)
        dependent_vars = Y

        # running model
        coeff_estimates = beta_ols(dependent_vars, independent_vars)
        self.assertIsNone(np.testing.assert_almost_equal([1.5, 2.5, 2, 3, 6], coeff_estimates, decimal=1))


if __name__ == "__main__":
    unittest.main()
