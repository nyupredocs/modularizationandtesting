import pandas as pd
import numpy as np
import OLS as ols
from sklearn import preprocessing

def get_sse(Y, X, betas):
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


def get_loss_function(Y, X, lamb, betas):
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
    
    loss = get_sse(Y, X, betas) + lamb * np.sum(np.abs(betas))
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
    Z = preprocessing.scale(X_train)
    Y_c = Y - np.mean(Y)
    
    left = np.linalg.inv(Z.transpose().dot(Z).values() + lamb * np.identity(X.shape[1]))
    right = Z.transpose().dot(Y_c)
    coefficients = left.dot(right)
    return(coefficients)


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