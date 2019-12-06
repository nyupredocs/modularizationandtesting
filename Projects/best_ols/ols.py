def ols(y, X):
    """
    This is THE BEST ols.
    
    Arg: 
        y - N by 1 response vector
        X - N by K covariate matrix
    Ret:
        β - OLS coefficients
        se - standard errors of the coefficients
    
    """
    XpX = X.T@X
    Xpy = X.T@y
    β = scipy.linalg.inv(XpX)@Xpy
    N = X.shape[0]
    pred = X@β
    resid = y - pred
    sse = sum(resid**2)[0]
    mean_sse = sse/(N - 1)
    σ2 = mean_sse*scipy.linalg.inv(XpX)
    se = np.sqrt(np.diag(σ2))
    return β, se