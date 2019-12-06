

import numpy as np

Z = np.matrix([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               [10, 11, 12]])



def calculate_sigma(Z, X, Y, beta_iv):
    N = Z.shape[0]
    resid = Y - X @ beta_iv

    sigma_iv = (1/N) * np.transpose(resid) @ resid

    return sigma_iv



def calculate_var_beta(sigma, X, Z):
    var_beta = sigma^2 * np.linalg.inv(np.transpose(X) @ projection_matrix(Z) @ X)
    return var_beta 