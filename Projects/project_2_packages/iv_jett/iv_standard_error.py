'''
Calculate Covariance Matrix
'''

import numpy as np
from iv_jett.iv_init import projection_matrix

def calculate_sigma(Z, X, Y, beta_iv, nocons = False):
    '''
    Description:
        Estimates the variance of the errors.
    Inputs:
        Z (matrix) -- Instrumental Variables
        X (matrix) -- Endogenous Variables
        Y (matrix) -- Outcome Variable
        beta_iv -- IV results
        nocons -- Option for constant (default False)
    '''
    N = Z.shape[0]
    if nocons == False:
        X_constant = np.ones((N, 1))
        X = np.hstack((X_constant, X))

    resid = Y - X @ beta_iv
    sigma_iv = (1/N) * np.transpose(resid) @ resid
    return np.sqrt(sigma_iv)

def calculate_var_beta(sigma, Z, X, nocons = False):
    '''
    Description:
        Calculates the variance of beta, the IV estimator
    Inputs:
        sigma
        Z (matrix) -- Instrumental Variables
        X (matrix) -- Endogenous Variables
        nocons -- Option for constant (default False)
    Ouputs:
        se_beta (array) -- Standard error
    '''

    N = Z.shape[0]
    if nocons == False:
        X_constant = np.ones((N, 1))
        X = np.hstack((X_constant, X))
        Z_constant = np.ones((N, 1))
        Z = np.hstack((Z_constant, Z))

    var_beta = (np.asscalar(sigma**2) * np.identity(X.shape[1])) @ np.linalg.inv(np.transpose(X) @ projection_matrix(Z) @ X)
    se_beta = np.sqrt(np.diag(var_beta))
    return se_beta
