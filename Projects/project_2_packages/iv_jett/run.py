'''
Run Package
'''

from iv_jett.iv_standard_error import *
from iv_jett.iv_init import *
from iv_jett.print import*

def TwoStageLeastSquaresRegress(X, Y, Z, nocons = False, verbose = False):
    beta_iv_hat = estimate_beta_iv(X, Z, Y, nocons)
    sigma = calculate_sigma(Z, X, Y, beta_iv_hat, nocons)
    var_beta = calculate_var_beta(sigma, X, Z, nocons)
    result_dict = {'Beta IV' : beta_iv_hat,
                   'Standard Error': var_beta}
    if verbose:
        print_res(result_dict, nocons)
    return result_dict
