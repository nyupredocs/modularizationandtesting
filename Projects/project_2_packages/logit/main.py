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


def fit_logit(x, y):
    beta_init = np.random.rand(len(x), 1)
    min_func = (lambda beta: ll_function(x, y, beta))
    res = minimize(min_func, x0 = beta_init)
    return res

min_func = (lambda beta: ll_function(x, y, beta))


minimize(min_func, beta_init[:, 0])
beta_init = np.random.rand(len(x), 1)
    min_func = (lambda beta: ll_function(x, y, beta))
min_func(beta_init)


fit_logit(x, y)
res = minimize((lambda beta: ll_function(x, y, beta)),
    x0 = beta0
    )
ll_function(x, y, beta_init)

beta0 = np.random.rand(len(x), 1)
print(beta0)
ll_function(x, y, beta0)
res = fmin_tnc(func = ll_function,
               approx_grad = True,
               x0 = 1,
               args = (x, y))





