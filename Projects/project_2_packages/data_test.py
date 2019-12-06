import numpy as np
from iv_jett.iv_standard_error import *
from  iv_jett.iv_init import *

mat_x = np.transpose(np.matrix([ [4, .2, 1, 5, 1, 10, 20],
                    [.4, 2, 2, 2, 2, 11, 25],
                    [0, 0, .3, 1, 3, 12, 40]]))

mat_z  = np.transpose(np.matrix([[1, .5, 2, 3, 4, 13, 56],
                    [3, 0, .2, 3, 5, 14, 60],
                    [1, 0, .4, 3, 6, 15, 77]]))

mat_y  = np.transpose(np.array([[3, 5, 2, 1, 7, 16, 80]]))



beta_iv_hat = estimate_beta_iv(mat_x, mat_z, mat_y)

print(beta_iv_hat)


sigma = calculate_sigma(mat_z, mat_x, mat_y, beta_iv_hat)

print(sigma)


var_beta = calculate_var_beta(sigma, mat_x, mat_z)
print(var_beta)