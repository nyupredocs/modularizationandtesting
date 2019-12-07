import numpy as np
import math
from scipy.optimize import minimize

x = np.transpose(np.matrix([0, 1, 3, 0.5, 3, -1, 2]))
y = np.transpose(np.matrix([9, 4, 23, 4, 4, -2, 1]))
def ll_function (x, y, beta):
    beta_prime = np.transpose(beta)
    fun_1 = y @ beta_prime @ x
    fun_2 = math.log(1 + math.exp(beta_prime @ x))
    fun = np.subtract(fun_1, fun_2)
    fun = fun.sum()
    return fun

beta0 = np.random.rand(len(x), 1)
print(beta0)
ll_function(x, y, beta0)
res = minimize(ll_function(x, y, beta0), beta0, method='nelder-mead',
    options={'xtol': 1e-8, 'disp': True})
