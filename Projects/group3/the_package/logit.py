import pandas as pd
import numpy as np
import scipy.optimize as opt


def loglike(beta, Y, X):
    """ Log likelihood function.

    Parameters
    ----------
    beta: matrix.
        N x 1 matrix of the coefficients.
        N is the number of observations.

    Y : matrix 
        N x 1 matrix of the dependent variable.
        N is the number of observations.
        
    X : matrix
        N x K matrix of the independent variables.
        N is the number of observations.
        K is the number of independent variables.
        
    Returns
    -------
    logvalue : matrix
        Log likelihood function   
    """

    logvalue = - (Y[None, :] @ X @ beta - np.sum(np.log(1 + np.exp(X @ beta))))
    
    return(logvalue[0])

def inverselogit(beta, Y, X):
    """ Inverse of logit function.

    Parameters
    ----------
    beta: matrix.
        N x 1 matrix of the coefficients.
        N is the number of observations.

    Y : matrix 
        N x 1 matrix of the dependent variable.
        N is the number of observations.
        
    X : matrix
        N x K matrix of the independent variables.
        N is the number of observations.
        K is the number of independent variables.
        
    Returns
    -------
    inverse : matrix
        Inverse of logit function  
    """

    inverse = 1 / (1 + np.exp(-X @ beta))
    
    return(inverse)

def dlogit(beta, Y, X):
    """ Derivative of logit function.

    Parameters
    ----------
    beta: matrix.
        N x 1 matrix of the coefficients.
        N is the number of observations.

    Y : matrix 
        N x 1 matrix of the dependent variable.
        N is the number of observations.
        
    X : matrix
        N x K matrix of the independent variables.
        N is the number of observations.
        K is the number of independent variables.
        
    Returns
    -------
    dlogit : matrix
        Derivative of the logit function
    """
    
    dlogit = sum(inverselogit(beta, Y, X)*(1 - inverselogit(beta, Y, X)))
    
    return(dlogit)

def logithessian(beta, Y, X):
    """ Hessian matrix of logit function.

    Parameters
    ----------
    beta: matrix.
        N x 1 matrix of the coefficients.
        N is the number of observations.

    Y : matrix 
        N x 1 matrix of the dependent variable.
        N is the number of observations.
        
    X : matrix
        N x K matrix of the independent variables.
        N is the number of observations.
        K is the number of independent variables.
        
    Returns
    -------
    hessian : matrix
        Hessian matrix
    """ 

    dp = np.diag(inverselogit(beta, Y, X)*(1 - inverselogit(beta, Y, X)))
    hessian = X.T @ dp @ X
    
    return(hessian)
    
def logit(Y, X):

    """ Logistic regression of Y on X.

    Parameters
    ----------
    Y : matrix 
        N x 1 matrix of the dependent variable.
        N is the number of observations.
        
    X : matrix
        N x K matrix of the independent variables.
        N is the number of observations.
        K is the number of independent variables.
        
    Returns
    -------
    (coef, test_status)
    
    coef : matrix
        K x 1 matrix of coefficients
    
    test_status : string
        Status of the optimization: Success or False    
    
    """

    # Initial beta values
    k = np.size(X, 1)
    beta0 = np.zeros(k)

    # Optimization 
    beta = opt.minimize(
        loglike, beta0, args = (Y, X), method = "BFGS", hess = logithessian
    )

    # Output values
    coef = beta.x
    test_status = beta.success
 
    # Return
    return (coef, test_status)
