import sys
import os

import numpy as np
import unittest
sys.path.append(os.path.abspath('..'))
from ols import ols
from numpy.linalg import matrix_rank
import numpy as np


class TestRandomStuff(unittest.TestCase):


    def test_isnan(self):

        nObs  = 1000
        nParams = 10
        y = np.random.random((nObs,1))
        X = np.ones((nObs,nParams))
        beta, ci = ols(y,X)

        self.assertTrue(np.isnan(beta))


if __name__ == '__main__':
    unittest.main()
