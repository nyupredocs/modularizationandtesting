import sys
sys.path.insert(0,'../OLS')

import numpy as np
import unittest
from OLS import beta_ols, Sigma
import statsmodels.api as sm
import pandas as pd

X = random_matrix

def simulation(X, Y):
    '''
    Draws single simulations
    '''
    beta_hat = norm(0,1)
    sigma_hat = exp(norm(0,1))
    y_hat = norm(X * beta_hat, sigma_hat)

    fit = OLS.beta_ols(Y, X)
    beta_model = OLS.betas(Y,X)
    covariance_model = OLS.sigma(Y,X)

    a = MVN(beta_model, covariance_model)

    return a

def many_simulations(X, Y, sims=100):
    '''
    Draws many simulations
    '''
    u = vector(length = sims)
    for s in sims:
        simulation(X, Y)
        u[s] += a
