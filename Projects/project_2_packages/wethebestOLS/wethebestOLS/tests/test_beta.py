import unittest
import numpy as np

import sys
import os

sys.path.append(os.path.abspath('..'))
from ols import ols

class test_beta ( unittest.TestCase ) :
    def test_beta(self):
        # Generate fake data
        K = 10
        N = 100000
        mu = 5
        sigma = 5
        beta = np.random.randint(0, 5, (K, 1))
        X = np.random.normal(mu, sigma, (N, K))
        e = np.random.normal(0, 1, (N, 1))
        y = X@beta + e

        # Find test beta_hat is close to beta
        tol = .01
        beta_hat, sigma_hat = ols(y, X)
        abs_diff = np.all(abs(beta - beta_hat) < .01)
        self.assertTrue(abs_diff)
