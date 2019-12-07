import unittest
import numpy as np
from ols import regression
import random


class testOLS(unittest.TestCase):
    def setUp_dimensions(self):
        n = random.randint(100,1000)
        k = random.randint(5,20)
        X = np.random.rand(n,k)
        Y = np.random.rand(n,1)
        coef_dim = regression(Y,X)[0].size
        X_dim = np.size(X,1)
        se_dim = regression(Y,X)[1].size
        return(coef_dim, se_dim, X_dim)

    # Check whether the coefficients vector and X have 
    # the same dimensions    
    def test_coef_dimensions(self):
        coef_dim, se_dim, X_dim = self.setUp_dimensions()
        self.assertEqual(X_dim,coef_dim)

    # Check whether the standard errors vector and X have
    # the same dimensions
    def test_se_dimensions(self):
        coef_dim, se_dim, X_dim = self.setUp_dimensions()
        self.assertEqual(X_dim,se_dim)

    # Confirm that we get an error message when the X matrix is singular
    # Test passes if there is an error message
    def test_novariation(self):
        n = random.randint(100,1000)
        k = random.randint(5,20)
        X = np.ones((n,k))
        Y = np.ones((n,1))
        try:
            coef = regression(Y,X)[0]
            error = 0
        except np.linalg.LinAlgError:
            error = 1

        self.assertEqual(error,1)

    def test_mismatched_obs(self):
    # Check error thrown if number of observations different for Y and X
        self.setUp()
        Y = np.array([[1, 2, 3, 4]]).T
        X = np.array([[2, 3, 4], [3, 8, 3]]).T
        
        self.assertFalse(np.size(X, 0) == np.size(Y, 0))
        
        with self.assertRaises(Exception):
            coef, se = ols(X, Y)

    def test_too_many_vars(self):
    # Check error thrown if number of independent variables greater
    # than number of observations
        self.setUp()

        Y = np.array([[1, 2]]).T
        X = np.array([[2, 3], [3, 8], [1, 3]]).T
        
        self.assertTrue(np.size(X, 1) > np.size(X, 0))
        
        with self.assertRaises(Exception):
            coef, se = ols(X, Y)
            

if __name__ == "__main__":
    unittest.main()

