import numpy as np
import scipy.stats as st
import statsmodels as sm
from scipy import optimize

y = np.random.randint(2, size=(100,1))
x = np.random.normal(0,1,(100,2))

res_correct = sm.discrete.discrete_model.Logit(y,x).fit()
res_correct.params


def Logit(b,y,x):
    # y = np.random.randint(2, size=(100,1))
    # x = np.random.normal(0,1,(100,2))
    n = x.shape[0]
    # b = np.zeros((s,1))
    # log_likelihood = (y.T @ x @ b)[0] - np.log(1 + np.exp(x.T @ b))
    log_likelihood = -y.T @ np.log(1 + np.exp(-x @ b)) + (np.ones((n,1)) - y).T @ np.log(1 - 1 / (1 + np.exp(- x @ b)))

    return -log_likelihood[0]

Logit(y,x,np.array((2,1)))

s = x.shape[1]
b_0 = np.array((0,0))

optimize.minimize(Logit,x0=b_0,args=(y,x))


optimize.fmin_bfgs(Logit, b_0,args=(y,x,))

y.shape


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
