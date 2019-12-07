import sys
import os

import numpy as np
import unittest
sys.path.append(os.path.abspath('..'))
from ols import ols
from numpy.linalg import matrix_rank
import numpy as np

class TestRandomStuff(unittest.TestCase):
    def test_singular(self):
        N  = 1000
        K = 10
        y = np.random.random((N, 1))
        X = np.ones((N, K))
        with self.assertRaises(Exception): ols(y, X)

if __name__ == '__main__':
    unittest.main()
