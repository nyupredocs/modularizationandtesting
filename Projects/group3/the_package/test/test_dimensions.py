from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
import unittest
from ols import regression
from logit import logit


class testDimensions(unittest.TestCase):
           
    def setUp(self):
        pass

    def tearDown(self):
        pass
        
    def test_mismatched_obs(self):
        self.setUp()
        Y = np.array([[1, 2, 3, 4]]).T
        X = np.array([[2, 3, 4], [3, 8, 3]]).T
        
        self.assertFalse(np.size(X, 0) == np.size(Y, 0))
        
        with self.assertRaises(Exception):
            coef, se = ols(X, Y)

    def test_too_many_vars(self):
        self.setUp()

        Y = np.array([[1, 2]]).T
        X = np.array([[2, 3], [3, 8], [1, 3]]).T
        
        self.assertTrue(np.size(X, 1) > np.size(X, 0))
        
        with self.assertRaises(Exception):
            coef, se = ols(X, Y)

if __name__ == '__main__':
    unittest.main()