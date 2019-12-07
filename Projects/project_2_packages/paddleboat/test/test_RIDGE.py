import sys
sys.path.insert(0,'../OLS')

import numpy as np
import unittest
from OLS import beta_ols, Sigma
import statsmodels.api as sm
import pandas as pd



class TestHPM(unittest.TestCase):

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


    def test_Sigma(self):
        np.random.seed(1435) # testing different seed
        n = 500000
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
        covariance_matrix = Sigma(dependent_vars, independent_vars)
        print(covariance_matrix)
        test_kc = independent_vars.cov()
        print(test_kc)

        #self.assertIsNone(np.testing.assert_almost_equal([1.5, 2.5, 2, 3, 6], coeff_estimates, decimal=1))


if __name__ == "__main__":
    unittest.main()
