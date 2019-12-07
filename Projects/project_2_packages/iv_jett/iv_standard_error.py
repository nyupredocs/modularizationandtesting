'''
Calculate Covariance Matrix
'''

import numpy as np
from iv_jett.iv_init import projection_matrix

def calculate_resid(Z, X, Y, beta_iv, nocons = False):
    if nocons == False:
        X_constant = np.ones((N, 1))
        X = np.hstack((X_constant, X))

    resid = Y - X @ beta_iv
    return resid

def calculate_sigma(Z, X, Y, beta_iv, nocons = False):

    N = Z.shape[0]

    if nocons == False:
        X_constant = np.ones((N, 1))
        X = np.hstack((X_constant, X))

    resid = Y - X @ beta_iv

    sigma_iv = (1/N) * np.transpose(resid) @ resid
    return np.sqrt(sigma_iv)

def calculate_var_beta(sigma, X, Z, resid, nocons = False, robust = False):
    
    N = Z.shape[0]

    if nocons == False:
        X_constant = np.ones((N, 1))
        X = np.hstack((X_constant, X))
        Z_constant = np.ones((N, 1))
        Z = np.hstack((Z_constant, Z))

    if robust == False:
        var_beta = (np.asscalar(sigma**2) * np.identity(X.shape[1])) @ np.linalg.inv(np.transpose(X) @ projection_matrix(Z) @ X)
        se_beta = np.sqrt(np.diag(var_beta))

    if robust == True: 
        resid_sq = resid @ np.transpose(resid)
        print("resid sq:")
        print(resid_sq)
        sandwich_bread = np.linalg.inv(np.transpose(Z) @ X)
        var_beta = (sandwich_bread @ np.transpose(Z) @ np.diag(np.diag(resid_sq)) @ Z @ sandwich_bread)
        print("var_beta")
        print(var_beta)
        se_beta = np.sqrt(np.diag(var_beta))
    return se_beta
