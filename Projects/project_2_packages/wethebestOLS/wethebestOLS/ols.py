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

        # Solve for beta hat
        XpX = X.T@X
        Xpy = X.T@y
        β = np.linalg.inv(XpX)@Xpy

        # Calculate mean squared error
        pred = X@β
        resid = y - pred
        sse = sum(resid**2)[0]
        N = X.shape[0]
        K = X.shape[1]
        mean_sse = sse/(N - K)


        # Calculate vcv matrix for beta
        σ2 = mean_sse*np.linalg.inv(XpX)
        # Extract SEs from the diagnal
        se = np.sqrt(np.diag(σ2))

    else:

        print("Error: matrix does not have full rank, returning nans")
        β   = np.nan
        se  = np.nan

    return β, se
