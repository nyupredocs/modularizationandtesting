import numpy as np

def regression(Y, X)

    """ Regress Y on X.
    
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
	(coef, se)
	
	coef : matrix
		K x 1 matrix of coefficients
	
	se : matrix
		K x 1 matrix of standard errors
    """
  
    # Get degrees of freedom
    N = np.size(Y, 0)
    K = np.size(X, 1)

    # Coefficients
    Q, R = np.linalg.qr(X)
    coef = np.linalg.inv(R).dot(Q.T).dot(Y)
    
    predict = X.dot(coef)
    resid = Y - predict
  
    # Standard error
    sigma = resid.T.dot(resid) / (N - K)
    cov = sigma * np.linalg.inv((R.T).dot(R))
    se = np.sqrt(cov.diagonal().T) 
    
    # Return
    return(coef, se.reshape(K, 1))