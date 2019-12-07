import numpy as np
from numpy.linalg import matrix_rank

def ols(y, X):
    """
    This is THE BEST ols.

    Parameters
    ----------
    y : np.array((N, 1), float64)
        N by 1 response vector
    X : np.array((N, K), float64)
        N by K covariate matrix

    Returns
    -------
    beta : np.array((K, 1), float64)
        OLS coefficients
    se : np.array((K, 1), float64)
        standard errors of the coefficients
    """
    if matrix_rank(X) == X.shape[1]:
        β = calc_beta(y, X)
        se = calc_se(y, X, β)
    else:
        print("Error: matrix does not have full rank, returning nans")
        β   = np.nan
        se  = np.nan
    return β, se

def calc_beta(y, X):
        XpX = X.T@X
        Xpy = X.T@y
        β = np.linalg.inv(XpX)@Xpy
        return β

def calc_mean_sse(y, X, β):
        pred = X@β
        resid = y - pred
        sse = sum(resid**2)[0]
        N = X.shape[0]
        K = X.shape[1]
        mean_sse = sse/(N - K)
        return mean_sse

def calc_se(y, X, β):
        mean_sse = calc_mean_sse(y, X, β)
        XpX = X.T@X
        σ2 = mean_sse*np.linalg.inv(XpX)
        se = np.sqrt(np.diag(σ2))
        return se
