import pandas as pd
import numpy as np
import scipy.optimize as opt


def loglike(beta, Y, X):

    """ 
    Log likelihood function

    Parameters
    ----------
    beta: matrix
        N x 1 matrix
        N is the number of observations

    Y : matrix 
        N x 1 matrix
        N is the number of observations
        
    X : matrix
        N x K matrix
        N is the number of observations
        K is the number of independent variables
        
    Returns
    -------
    Log likelihood function  
    
    """

    logvalue= - (Y[None, :]@X@beta - np.sum(np.log(1+np.exp(X@beta))))
    return logvalue[0]

def inverselogit(beta, Y, X):

    """ 
    Inverse of logit function

    Parameters
    ----------
    beta: matrix
        N x 1 matrix
        N is the number of observations

    Y : matrix 
        N x 1 matrix
        N is the number of observations
        
    X : matrix
        N x K matrix
        N is the number of observations
        K is the number of independent variables
        
    Returns
    -------
    Inverse of logit function  
    
    """

    return 1/(1+np.exp(-X@beta))

def dlogit(beta, Y, X):

    """ 

    Parameters
    ----------
    beta: matrix
        N x 1 matrix
        N is the number of observations

    Y : matrix 
        N x 1 matrix
        N is the number of observations
        
    X : matrix
        N x K matrix
        N is the number of observations
        K is the number of independent variables
        
    Returns
    -------
    
    """

    return sum(inverselogit(beta, Y, X)*(1 - inverselogit(beta, Y, X)))

def logithessian(beta, Y, X):

    """ 
    Hessian matrix

    Parameters
    ----------
    beta: matrix
        N x 1 matrix
        N is the number of observations

    Y : matrix 
        N x 1 matrix
        N is the number of observations
        
    X : matrix
        N x K matrix
        N is the number of observations
        K is the number of independent variables
        
    Returns
    -------
    Hessian matrix: matrix

    """ 

    dp = np.diag(inverselogit(beta, Y, X)*(1-inverselogit(beta, Y, X)))
    return X.T @ dp @ X

def logit(Y, X):

    """ 
    Logistic Regression

    Parameters
    ----------
    Y : matrix 
        N x 1 matrix
        N is the number of observations
        
    X : matrix
        N x K matrix
        N is the number of observations
        K is the number of independent variables
        
    Returns
    -------
    (coef, test_status)
    
    coef : matrix
        K x 1 matrix of coefficients
    
    test_status : string
        Status of the optimization: Success or False    
    
    """

    #Initial beta values
    k = np.size(X, 1)
    beta0 = np.zeros(k)

    #Optimization 
    beta = opt.minimize(
        loglike, beta0, args=(Y, X), method="BFGS", hess=logithessian
    )

    #Output values
    coef = beta.x
    test_status = beta.success
 
    # Return
    return (coef, test_status)
