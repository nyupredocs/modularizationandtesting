import sys
import os
import path
import numpy as np
import scipy as linalg
from scipy.optimize import minimize

nObs = 1000
nVars = 4

bbeta = np.array([1, 3, 5, 7])
X = np.random.random((nObs,4))
Y = (np.random.uniform(0,1,nObs) < 0.5).astype(int).reshape(nObs,1)


def logit(X, bbeta):
    """
    blah blah
    """
    Logit = 1/(1+np.exp(-np.dot(X,bbeta)))

    return Logit

def objectiveFunction(Y, X, bbeta):
    """
    blah blah
    """

    nObs = X.shape[0]

    yhat = logit(X, bbeta)
    lyhat = np.log(yhat).reshape(nObs,1)
    lyhat_m = np.log(1 - yhat).reshape(nObs,1)
    cost = np.multiply(Y,lyhat) + np.multiply((1-Y),lyhat_m)

    LL = -np.sum(cost,0)[0]

    return LL


def optimization(objectiveFunction, Y,X,bbeta):
    """
    blah blah
    """
    betahat = minimize(lambda beta: objectiveFunction(Y,X, beta), bbeta, method='nelder-mead',options={'xtol': 1e-8, 'disp': True})

    return betaHat
