import numpy as np
import scipy.stats as st
# x = np.random.randn(100,2)
# eps = np.random.normal(0,1,(100,1))
# y = (np.array([5, 10]) @ x.T).reshape(100,1) + eps
# cf = 0.95
import unittest
import statsmodels.api as sm
from OLS_team_cool import ols
#We are creating a class to define the variables we are testing.
class TestOLS(unittest.TestCase):
    def setUp(self):
        self.x = np.random.randn(100,2)
        self.eps = np.random.normal(0,1,(100,1))
        self.y = (np.array([5, 10]) @ (self.x).T).reshape(100,1) + self.eps
        self.cf = 0.95
#This is checking the OLS model that comes with python
    def test_example1(self):
        model = sm.OLS(self.y,self.x)
        result = model.fit()
        betacrt = result.params.reshape(-1,1)
        ourmodel = ols.OLS(self.y,self.x)
#assertAlmostEqual accounts for float errors
        ourbeta = ourmodel['Beta'].reshape(-1,1)
        testresults =np.testing.assert_almost_equal(betacrt,ourbeta)
        self.assertIsNone(testresults)

# #This is checking the OLS model that team_cool has created
# #    def test_example2(self):
if __name__ == '__main__':
    unittest.main()

# T=TestOLS()
# ourmodel = ols.OLS(T.y,T.x)
# print(T.test_example1())
#
# def OLS(y,x,cf=0.95):
#     """
#     OLS estimation.
#
#     Parameters
#     −−−−−−−−−−
#     y : Dependent variable
#     x : Explanatory variable
#     cf: Confidence level
#
#     Returns
#     −−−−−−−
#     beta : Beta
#     se: Standard Error
#     confidence: Confidence Interval
#
#     See Also
#     −−−−−−−−
#     other_function : This is a related function
#     """
#
#     beta = np.linalg.inv(x.T @ x) @ (x.T @ y)
#
#     se_term1 = ((y - x @ beta).T @ (y - x @ beta)) / (x.shape[0] - 1)
#     se_term2 = x.T @ x
#     cov_matrix = se_term1 * se_term2
#     se = np.sqrt(np.diag(cov_matrix))
#
#     confidence = [beta - st.norm.ppf(1 - (1-0.95)/2) * se, beta \
#      + st.norm.ppf(1 - (1-0.95)/2) * se]
#
#     return {"Beta":beta, "Standard Error":se, "Confidence Interval":confidence}
