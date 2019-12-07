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

    Xp = X.T
    XpX = Xp@X
    Xpy = Xp@y

    if np.linalg.det(XpX) == 0:
        raise Exception('XpX Matrix is singular')

    β = calc_beta(y, XpX, Xpy)
    se = calc_se(y, X, β, XpX)

    return β, se


def calc_beta(y, XpX, Xpy):

        """
        Uses normal equations to calculate OLS coefficients.

        Parameters
        ----------
        y : np.array((N, 1), float64)
            N by 1 response vector
        XpX : np.array((K, K), float64)
            X transpose X

        Returns
        -------
        beta : np.array((K, 1), float64)
            Vector of OLS coefficients
        """

        XpX.shape

        β = np.linalg.inv(XpX)@Xpy
        return β

def calc_mean_se(y, X, β):

        """
        Calculates mean squared error

        Parameters
        ----------
        y : np.array((N, 1), float64)
            N by 1 response vector
        X : np.array((N, K), float64)
            Covariate matrix.
        beta : np.array((K, 1), float64)
            OLS coefficients

        Returns
        -------
        mean_se : float64
            Mean squared error
        """

        pred = X@β
        resid = y - pred
        sse = sum(resid**2)[0]
        N = X.shape[0]
        K = X.shape[1]
        mean_se = sse/(N - K)
        return mean_se

def calc_se(y, X, β, XpX):

        """
        Calculates standard errors

        Parameters
        ----------
        y : np.array((N, 1), float64)
            N by 1 response vector
        X : np.array((N, K), float64)
            Covariate matrix.
        beta : np.array((K, 1), float64)
            OLS coefficients
        XpX : np.array((K, K), float64)
            X transpose X

        Returns
        -------
        se : np.array((K, 1), float64)
            Standard errors of OLS estimates
        """

        mean_se = calc_mean_se(y, X, β)
        σ2 = mean_se*np.linalg.inv(XpX)
        se = np.sqrt(np.diag(σ2))
        return se
