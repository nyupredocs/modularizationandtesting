import numpy as np
import scipy.stats as st
import unittest
import statsmodels.api as sm
from OLS_team_cool import ols

# x = np.random.randn(100,2)
# eps = np.random.normal(0,1,(100,1))
# y = (np.array([5, 10]) @ x.T).reshape(100,1) + eps
# cf = 0.95

#We are creating a class to define the variables we are testing.
class TestOLS(unittest.TestCase):

#Here we are testing our models
    def setUp(self):
        self.x = np.random.randn(100,2)
        self.eps = np.random.normal(0,1,(100,1))
        self.y = (np.array([5, 10]) @ (self.x).T).reshape(100,1) + self.eps
        self.cf = 0.95
        self.model = sm.OLS(self.y,self.x)
        self.result = self.model.fit()
        self.ourmodel = ols.OLS(self.y,self.x)

# This is checking the OLS model that comes with python
    def test_beta(self):
        betacrt = self.result.params.reshape(-1,1)

# assertAlmostEqual accounts for float errors
        ourbeta = self.ourmodel['Beta'].reshape(-1,1)
        testresults =np.testing.assert_almost_equal(betacrt,ourbeta)
        self.assertIsNone(testresults)

    def test_se(self):
        se_correct = self.result.bse.reshape(-1,1)
        our_se = self.ourmodel.get("Standard Error").reshape(-1,1)
        test_se_res =np.testing.assert_almost_equal(se_correct,our_se)
        self.assertIsNone(test_se_res)


# #This is checking the OLS model that team_cool has created
# #    def test_example2(self):
if __name__ == '__main__':
    unittest.main()
