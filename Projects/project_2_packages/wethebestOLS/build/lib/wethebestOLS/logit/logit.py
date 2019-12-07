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
    This is THE BEST Logit.

    Parameters
    ----------
    X :
        N by K covariate matrix
    bbeta :
        Array of K numbers


    Returns
    -------
    Logit :
        N by 1 logit conversion

    """
    Logit = 1/(1+np.exp(-np.dot(X,bbeta)))

    return Logit

def objectiveFunction(Y, X, bbeta):
    """
    This is objectiveFunction.

    Parameters
    ----------
    X :
        N by K covariate matrix
    Y :
        Array of N x 1 ones and zeros
    bbeta :
        parameters of the function (K,1)


    Returns
    -------
    Logit :
        Log Likelihood

    """
    nObs = X.shape[0]

    yhat = logit(X, bbeta)
    lyhat = np.log(yhat).reshape(nObs,1)
    lyhat_m = np.log(1 - yhat).reshape(nObs,1)
    cost = np.multiply(Y,lyhat) + np.multiply((1-Y),lyhat_m)

    LL = -np.sum(cost,0)[0]

    return LL


def optimization(objectiveFunction, Y,X,bbeta):
    '''
    This is objectiveFunction.

    Parameters
    ----------
    objectiveFunction :
        Objective function for the log likelihood
    Y :
        Array of N x 1 ones and zeros
    X :
        parameters of the function (K,1)
    bbeta :
        parameters of the function (K,1)


    Returns
    -------
    Logit :
        betaHat

    '''
    betahat = minimize(lambda beta: objectiveFunction(Y,X, beta), bbeta, method='nelder-mead',options={'xtol': 1e-8, 'disp': False})

    return betahat


def standardErrorsLogit(optimization, Y,X,bbeta):
    '''
    This retrieves standard errors.

    Parameters
    ----------
    optimization :
        Function that computes the parameter optimization
    Y :
        Array of N x 1 ones and zeros
    X :
        parameters of the function (K,1)
    bbeta :
        parameters of the function (K,1)


    Returns
    -------
    sd :
        standard deviation
    se :
        standard errors
    ci :
        confidence intervals

    '''
    nObs = X.shape[0]
    nSE = round(nObs/10)
    parameter_list = []


    for i in range(1,30):
        sample = (np.random.uniform(0,1,nObs) < 0.5)
        Y_sample = Y[sample,:]
        X_sample = X[sample,:]
        betaHat = optimization(objectiveFunction, Y_sample, X_sample, bbeta)
        parameter_list.append(betaHat['x'])

    sd = np.std(np.array(parameter_list),0)
    se = np.sqrt(sd)

    betaHat = optimization(objectiveFunction, Y_sample, X_sample, bbeta)

    ci = (betaHat['x'] - se, betaHat['x'] + se)

    return sd, se, ci

errors = standardErrorsLogit(optimization, Y,X,bbeta)

sd, se, ci = errors
