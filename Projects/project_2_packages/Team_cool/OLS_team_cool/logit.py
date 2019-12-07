import numpy as np
import scipy.stats as st
import randrange
irand = randrange (0,1)
x = np.random.randn(100,2)
# eps = np.random.normal(0,1,(100,1))
y = (np.array([5, 10]) @ x.T).reshape(100,1) + eps
beta = np.random.randn(2,1)
# cf = 0.95
-y.T -x @ beta
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
