import numpy as np


def get_sizes(Y, X):
    """ Get dimensions of data.

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
    (N, K)
    
    N : int
        Number of observations.
    
    K : int
        Number of independent variables.
    """

    N = np.size(Y, 0)
    K = np.size(X, 1)
    
    return(N, K)


def get_predict(Y, X, coef):
    """ Get predictions from model.

    Parameters
    ----------
    Y : matrix 
        N x 1 matrix of the dependent variable.
        N is the number of observations.
        
    X : matrix
        N x K matrix of the independent variables.
        N is the number of observations.
        K is the number of independent variables.

    coef : matrix
        K x 1 matrix of coefficients.
        
    Returns
    -------
    (predict, resid)
    
    predict : matrix
        K x 1 matrix of predicted values.
    
    resid : matrix
        K x 1 matrix of residuals.
    """

    predict = X.dot(coef)
    resid = Y - predict
    
    return(predict, resid)
    

def get_coef(Y, Q, R):
    """ Calculate coefficients for model.

    Parameters
    ----------
    Y : matrix 
        N x 1 matrix of the dependent variable.
        N is the number of observations.
        
    X : matrix
        N x K matrix of the independent variables.
        N is the number of observations.
        K is the number of independent variables.

    Q : matrix
        Q matrix of the QR decomposition for X

    R : matrix
        R matrix of the QR decomposition for X
        
    Returns
    -------
    coef : matrix
        K x 1 matrix of coefficients.
    """

    coef = np.linalg.inv(R).dot(Q.T).dot(Y)
    
    return(coef)
    
    
def get_se(resid, R, N, K):
    """ Calculate standard errors for model.

    Parameters
    ----------
    resid : matrix
        K x 1 matrix of residuals.

    X : matrix
        N x K matrix of the independent variables.
        N is the number of observations.
        K is the number of independent variables.

    R : matrix
        R matrix of the QR decomposition for X
        
    N : int
        Number of observations.
    
    K : int
        Number of independent variables.
    
    Returns
    -------
    se : matrix
        K x 1 matrix of standard errors.
    """

    sigma = resid.T.dot(resid) / (N - K)
    cov = sigma * np.linalg.inv((R.T).dot(R))
    se = np.sqrt(cov.diagonal().T) 
    
    return(se)
    
    
def regression(Y, X):
    """ Regress Y on X.

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
    (coef, se)
    
    coef : matrix
        K x 1 matrix of coefficients.
    
    se : matrix
        K x 1 matrix of standard errors.
    """

    # Get degrees of freedom
    N, K = get_sizes(Y, X)

    # Coefficients
    Q, R = np.linalg.qr(X)
    coef = get_coef(Y, Q, R)
    
    predict, resid = get_predict(Y, X, coef)
  
    # Standard errors
    se = get_se(resid, R, N, K)
    
    # Return
    return(coef, se.reshape(K, 1))