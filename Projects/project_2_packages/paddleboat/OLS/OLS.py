import numpy as np
import pandas as pd
import math
import scipy
np.set_printoptions(suppress=True)

# Function computing a least squares fit
def beta_ols(Y, X):
    '''
    Estimate OLS coefficients

    Parameters
    ----------
    Y : Nx1 Matrix
    X : Matrix

    Returns
    -------
    beta_hat : vector of coefficients
    '''

    if len(Y.shape) != 1:
        return print('ERROR: Y must be an Nx1 matrix')
    elif Y.shape[0] != X.shape[0]:
        return print('ERROR: Y and X must have the same number of observations')
    else:
        left = X.transpose().dot(X).values
        right = X.transpose().dot(Y).values
        beta_hat = np.linalg.inv(left).dot(right)
        return beta_hat


def resids(Y, X):
    '''
    Estimate OLS residuals

    Parameters
    ----------
    Y : Nx1 Matrix
    X : Matrix

    Returns
    -------
    e : vector of residuals
    '''
    e = beta_ols(Y,X).dot(X.values.T)-Y
    return e


def Sigma(Y,X):
    '''
    ≈

    Parameters
    ----------
    Y : Nx1 Matrix
    X : Matrix

    Returns
    -------
    Sigma : var-cov matrix as pandas df
    '''
    e = resids(Y,X)
    std_hat = e.dot(e.T)/(X.shape[1]-1)
    Sigma = std_hat*np.linalg.inv(X.transpose().dot(X).values)
    return pd.DataFrame(Sigma)


def variance_ols(Y,X):
    '''
    Estimate OLS variance-covariance matrix

    Parameters
    ----------
    Y : Nx1 Matrix
    X : Matrix

    Returns
    -------
    var : variance of coefficients
    '''
    diags = np.diagonal(Sigma(Y, X))
    var = np.sqrt(diags)
    return var


def r2_ols(Y, X):
    '''
    Estimate R^2 for OLS

    Parameters
    ----------
    Y : Nx1 Matrix
    X : Matrix

    Returns
    -------
    R2 : value of R^2 
    '''

    y_hat = beta_ols(Y,X).dot(X.values.T)
    y_bar = np.mean(Y)
    
    SSR = np.sum((y_hat - y_bar)**2)
    SST = np.sum((Y - y_bar)**2)

    r2 = SSR / SST
    return r2

def least_sq(Y, X):
    '''
    Output nicely OLS results

    Parameters
    ----------
    Y : Nx1 Matrix
    X : Matrix

    Returns
    -------
    R2 : value of R^2 
    '''
    
    print('Coefficients = ', beta_ols(Y, X))
    print('Coeff. SErrs = ', np.sqrt(np.diagonal(Sigma(Y,X))))
    print('')
    print('95% Confidence Interval for Coefficients')
    print('     Lower Bound:', beta_ols(Y, X) - 1.96*np.sqrt(np.diagonal(Sigma(Y,X))))
    print('     Upper Bound:', beta_ols(Y, X) + 1.96*np.sqrt(np.diagonal(Sigma(Y,X))))
    print('')
    print('R-Squared:', r2_ols(Y,X))
    print('')
    print("Variance-Covariance Matrix:")
    print(Sigma(Y,X))



