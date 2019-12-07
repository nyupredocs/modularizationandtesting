import pandas as pd
import numpy as np
import OLS as ols
from sklearn import preprocessing
import tqdm

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


def loss(Y, X, lamb, betas):
        """
        Compute loss function

        Parameters
        ----------
        Y : Nx1 Matrix
        X : Matrix (no intercept column)
        lamb : Lambda value to use for L2
        betas : Vector of estimated coefficients

        Returns
        -------
        loss : Computed loss
        """
    if np.sum(X[1]) == len(X[1]):
        return print('ERROR: X should not have an intercept')
    
    loss = sse(Y, X, betas) + lamb * np.sum(np.abs(betas))
    return loss


def beta_lasso(X, Y, lamb):
        """
        Compute lasso coeffs

        Parameters
        ----------
        Y : Nx1 Matrix
        X : Matrix (no intercept column)
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
    Z = preprocessing.scale(X)
    Y_c = Y - np.mean(Y)
    
    left = np.linalg.inv(Z.transpose().dot(Z).values() + lamb * np.identity(X.shape[1]))
    right = Z.transpose().dot(Y_c)
    coefficients = left.dot(right)
    return(coefficients)


def lasso_se_boot(X, Y, lamb, betas, n_iter = 100, progress_disable = False):
        """
        Estimate Lasso standard errors through bootstrapping

        Parameters
        ----------
        Y : Nx1 Matrix
        X : Matrix
        lamb : Lambda value to use for L2
        betas : Vector of estimated coefficients
        n_ter : Integer of number of iterations for bootstrapping
        progress_disable : Disable option for tqdm progress bar

        Returns
        -------
        boot_se : vector of standard errors
        """
    
    nobs = X.shape[0]
    K = int(X[1] - 1)

    beta_hat_boots = np.zeros((n_iter, K))

    for b_iter in tqdm(range(0, n_iter), disable=progress_disable):
        b_index = np.random.choice(range(0, nobs), nobs, replace = True)

        b_beta_hat = beta_lasso(Y, X, lamb)

        # Saving coefficient estimates
        beta_hat_boots[b_iter] = b_beta_hat

    # Estimated coefficients from bootstrapping
    beta_hat_boots = pd.DataFrame(beta_hat_boots)
    beta_hat_boots.index.name = 'boot_iter'
    beta_hat_boots.columns = X.columns.values.tolist()

    # Bootstrapped variance of coefficient estimates
    beta_hat_boot_var = beta_hat_boots.var(axis=0)

    # Bootstrapped SE of coefficient estimates
    beta_hat_boot_SE = np.sqrt(beta_hat_boot_var)

    # Bootstrapped t-stats for null that coefficient = 0
    ## note that we use the coefficient estimates from the full sample 
    ## but the variance from the bootstrapping procedure
    beta_hat_boot_t = beta_lasso(Y, X) / beta_hat_boot_SE

    # Bootstrapped p values from t test (two-sided)
    beta_hat_boot_p = pd.Series(2 * (1- t.cdf(np.abs(beta_hat_boot_t), df = nobs - K)), beta_hat_boot_t.index)


def pick_lowest_lambda(X, Y):
        """
        Compute loss function

        Parameters
        ----------
        Y : Nx1 Matrix
        X : Matrix (no intercept column)
        lamb : Lambda value to use for L1
        betas : Vector of estimated coefficients

        Returns
        -------
        loss : Computed loss
        """
    lambs = range(0, 1, 100)
    losses = list()

    for l in lambs:
        coeffs = get_coeffs_given_lambda(X, Y, l)
        SSE = get_sse(Y, X, coeffs)
        loss = loss_function(SSE, l, coeffs)
        losses.append(loss)

    min_loss = min(losses)
    lowest_lambda = loss(min_loss_position_in_list)

    print("Working!")
    return(lowest_lamb)

def main():
    """Performs OLS, prints output to table"""
    print("Working!")