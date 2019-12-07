import pandas as pd
import numpy as np
from sklearn import preprocessing
from tqdm import tqdm
from scipy.stats import t


def beta_lasso(Y, X, lamb):
    """
    Compute lasso coeffs

    Parameters
    ----------
    Y : Nx1 Matrix
    X : Matrix (with intercept column)
    lamb : Lambda value to use for L2

    Returns
    -------
    coefficients : Vector of Lasso coefficients

    Note
    ----
    For simplicity we use matrix inverses,
    which are not computationally efficient at O(p^3).
    SVD would be a more efficient approach.
    """
    
    Z = X.iloc[:, 1:]
    Z = pd.DataFrame(preprocessing.scale(Z))
    Y_c = Y - np.mean(Y)
    
    left = np.linalg.inv(Z.transpose().dot(Z) + lamb * np.identity(Z.shape[1]))
    right = Z.transpose().dot(Y_c)
    coefficients = left.dot(right)
    return(coefficients)


def sse(Y, X, betas):
    '''
    Get sum of square errors

    Parameters
    ----------
    Y : Nx1 Matrix
    X : Matrix
    betas : Vector of estimated coefficients

    Returns
    -------
    sse : Sum of square errors
    '''
   
    e = betas.dot(X.values.T)-Y
    sse = np.sum(e**2)
    return sse


def lasso_fit(Y, X, lamb, n_iter=100, progress_disable = False):
    """
    Estimate Lasso standard errors through bootstrapping

    Parameters
    ----------
    Y : Nx1 Matrix
    X : Matrix
    lamb : Lambda value to use for L2
    n_ter : Integer of number of iterations for bootstrapping
    progress_disable : Disable option for tqdm progress bar

    Returns
    -------
    results : Results wrapper with lasso results
                coefficients = Lasso coefficients from full sample
                bootstrap_coeffs = Lasso coefficients from bootstrapping procedure
                bootstrap_coeffs_var = Coefficient variance from bootstrapping
                bootstrap_coeffs_SE = Coefficient standard errors from bootstrapping
                bootstrap_coeffs_t = T-stats (from bootstrapping SE)
                bootstrap_coeffs_p = P-values
    """
    nobs = np.shape(X)[0]
    K = np.shape(X)[1] - 1

    beta_hat_boots = np.zeros((n_iter, K))

    for b_iter in tqdm(range(0, n_iter), disable=progress_disable):
        b_index = np.random.choice(range(0, nobs), nobs, replace = True)
        _Y, _X = pd.DataFrame(Y).iloc[b_index], pd.DataFrame(X).iloc[b_index]

        b_beta_hat = beta_lasso(np.array(_Y), _X, lamb)
        # Saving coefficient estimates
        beta_hat_boots[b_iter, :] = b_beta_hat.squeeze()

    # Estimated coefficients from bootstrapping
    beta_hat_boots = pd.DataFrame(beta_hat_boots)
    beta_hat_boots.index.name = 'boot_iter'
    #beta_hat_boots.columns = X.columns.values.tolist()

    # Bootstrapped variance of coefficient estimates
    beta_hat_boot_var = beta_hat_boots.var(axis=0)

    # Bootstrapped SE of coefficient estimates
    beta_hat_boot_SE = np.sqrt(beta_hat_boot_var)

    # Bootstrapped t-stats for null that coefficient = 0
    ## note that we use the coefficient estimates from the full sample 
    ## but the variance from the bootstrapping procedure
    beta_hat_boot_t = beta_lasso(Y, X, lamb) / beta_hat_boot_SE

    # Bootstrapped p values from t test (two-sided)
    beta_hat_boot_p = pd.Series(2 * (1- t.cdf(np.abs(beta_hat_boot_t), df = nobs - K)), beta_hat_boot_t.index)

    return Results_wrap(model = print('Lasso, lambda =', lamb), 
                        coefficients = beta_lasso(Y, X, lamb),
                        bootstrap_coeffs = beta_hat_boots,
                        bootstrap_coeffs_var = beta_hat_boot_var,
                        bootstrap_coeffs_SE = beta_hat_boot_SE,
                        bootstrap_coeffs_t = beta_hat_boot_t,
                        bootstrap_coeffs_p = beta_hat_boot_p)



class Results_wrap(object):
    '''
    Summarize the Regression Results (based of statsmodels)
    Parameters
    -----------
    yname : string, optional
        Default is `y`
    xname : list of strings, optional
        Default is `var_##` for ## in p the number of regressors
    title : string, optional
        Title for the top table. If not None, then this replaces the
        default title
    alpha : float
        significance level for the confidence intervals
    Returns
    -------
    smry : Summary instance
        this holds the summary tables and text, which can be printed or
        converted to various output formats.
    '''
    def __init__(self, model, coefficients, 
        cov_type='nonrobust', bootstrap_coeffs=None, bootstrap_coeffs_var=None, bootstrap_coeffs_SE=None, bootstrap_coeffs_t=None, bootstrap_coeffs_p=None):
        self.model = model
        self.coefficients = coefficients
        self.cov_type = cov_type
        self.beta_hat_boots = bootstrap_coeffs
        self.beta_hat_boots_var = bootstrap_coeffs_var
        self.beta_hat_boots_SE = bootstrap_coeffs_SE
        self.beta_hat_boots_t = bootstrap_coeffs_t
        self.beta_hat_boots_p = bootstrap_coeffs_p

    def summary(self, title=None):
        '''
        TO DO: PRINTABLE SUMMARY RESULTS LIKE STATSMODELS
        '''
        # testing that summary is callable
        if title is None:
            title = self.model + ' ' + "Regression Results"
        return print(title)


def loss(Y, X, lamb, betas):
    """
    Compute loss function

    Parameters
    ----------
    Y : Nx1 Matrix
    X : Matrix (with intercept column)
    lamb : Lambda value to use for L2
    betas : Vector of estimated coefficients

    Returns
    -------
    loss : Computed loss
    """
    
    loss = sse(Y, X, betas) + lamb * np.sum(np.abs(betas))
    return loss