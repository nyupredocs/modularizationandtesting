import numpy as np
import math
from scipy.optimize import minimize


def ll_function (x, y, beta):
    # Reshape beta
    beta = beta[:, None]
    beta_prime = np.transpose(beta)
    fun_1 = y @ beta_prime @ x
    fun_2 = math.log(1 + math.exp(beta_prime @ x))
    fun = np.subtract(fun_1, fun_2)
    fun = fun.sum()
    return fun


def fit_logit(x, y):
    beta_init = np.random.rand(len(x), 1)
    min_func = (lambda beta: ll_function(x, y, beta))
    res = minimize(min_func, x0 = beta_init)
    return res


if __name__ == "__main__":
    x = np.transpose(np.matrix([0, 1, 3, 0.5, 3, -1, 2]))
    y = np.transpose(np.matrix([9, 4, 23, 4, 4, -2, 1]))
    
    print(fit_logit(x, y))



