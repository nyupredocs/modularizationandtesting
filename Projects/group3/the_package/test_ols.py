import unittest
import numpy as np
from ols import regression
import random


class TestOLS(unittest.TestCase):
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


if __name__ == "__main__":
	unittest.main()

