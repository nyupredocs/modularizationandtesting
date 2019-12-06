import pandas as pd
import numpy as np

def get_betas(X, Y):
    '''
        Get betas (according to OLS formula)
        '''
    betas = (np.transpose(X) * X)^(-1) * (np.transpose(X) * Y) # transpose is a numpy function

    print("Working!")
    return betas

def get_residuals(betas, X, Y):
    '''
        Get residuals (according to OLS formula)
        '''
    y_hat = betas * X
    residuals = Y - y_hat

    print("Working!")
    return residuals

def get_n(X, Y):
    '''
        Get N, check independent vs dependent variables
        '''
    n_X = length(X)
    n_Y = length(Y)

    if n_X == n_Y:
        n = n_X
    else:
        print("Error!")

    print("Working!")
    return n

def get_ses(residuals, X, Y):
    '''
        Get SEs (according to OLS formula)
        '''
    residuals2 = residuals^2
    XX = (np.transpose(X) * X)^(-1) # transpose is not a real function
    N = get_n(X, Y)
    ses = (residuals2 / (N-1)) * XX

    print("Working!")
    return ses

def get_r2(Y, X, betas):
    '''
        Get R^2
        '''
    y_hat = X * betas
    y_bar = mean(y)

    SSR = sum((y_hat - y_bar)^2)
    SST = sum((y - y_bar)^2)

    r2 = SSR / SST

    print("Working!")
    return r2

def get_sse(Y, X, betas):
    '''
        Get sum of squared errors'''
    y_hat = X * betas
    sse = (Y - y_hat) ** 2

    print("Working!")
    return sse

def get_loss_function(SSE, lamb, betas):
    '''
        Get loss function
        '''
    betas_without_intercept = betas[1:length(betas)]
    loss_function = SSE + lamb * sum(abs(betas_without_intercept))

    print("Working!")
    return loss_function

def get_coefficients_given_lambda(lamb):
    '''
        Get coefficients
        '''
    return(coefficients)

def pick_lowest_lamda():
    '''
        Pick lowest lambda
        '''
    lambs = [0.001, 0.01, 0.1, 0.5, 1, 2, 10]
    l_num = length(lam)
    pred_num = X.shape[1]
    losses = list(length(lamb))

    # prepare data for enumerate
    coeff_a = np.zeros((l_num, pred_num))

  for ind, i in enumerate(lambs):    
        loss = loss_function(lamb)
        list.append(loss)

    min_loss = min(losses)
    lowest_lamb = loss(min_loss_position_in_list)

    print("Working!")
    return(lowest_lamb)

def main():
    '''
        Performs LASSO, prints output to table
        '''
    print("Working!")
