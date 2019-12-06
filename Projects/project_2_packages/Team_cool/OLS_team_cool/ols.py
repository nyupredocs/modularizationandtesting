import numpy as np

# x = np.random.randn(100,2)
# eps = np.random.normal(0,1,(100,1))
# y = (np.array([5, 10]) @ x.T).reshape(100,1) + eps


def OLS(y,x):
    """
    OLS estimation.

    Parameters
    −−−−−−−−−−
    y : Dependent variable
    x : Explanatory variable

    Returns
    −−−−−−−
    beta : beta
    se: standard error

    See Also
    −−−−−−−−
    other_function : This is a related function
    """

    beta = np.linalg.inv(x.T @ x) @ (x.T @ y)
    se_term1 = ((y - x @ beta).T @ (y - x @ beta)) / (x.shape[0] - 1)
    se_term2 = x.T @ x
    cov_matrix = se_term1 * se_term2

    se = np.sqrt(np.diag(cov_matrix))

    return beta, se



# help(OLS)
