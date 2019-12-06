import numpy as np
from iv_jett.iv_init import projection_matrix

def calculate_sigma(Z, X, Y, beta_iv):
    N = Z.shape[0]
    resid = Y - X @ beta_iv

    sigma_iv = (1/N) * np.transpose(resid) @ resid

    return np.sqrt(sigma_iv)

def calculate_var_beta(sigma, X, Z):
    var_beta = (np.asscalar(sigma**2) * np.identity(X.shape[1])) @ np.linalg.inv(np.transpose(X) @ projection_matrix(Z) @ X)
    se_beta = np.sqrt(np.diag(var_beta))
    return se_beta
