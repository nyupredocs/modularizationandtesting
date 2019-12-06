import pandas as pd
import numpy as np

def get_betas(X, Y):
    """Get betas (according to OLS formula)"""
    betas = (np.transpose(X) * X)^(-1) * (np.transpose(X) * Y) # transpose is a numpy function

    print("Working!")
    return betas

def get_residuals(betas, X, Y):
    """Get residuals (according to OLS formula)"""
    y_hat = betas * X
    residuals = Y - y_hat

    print("Working!")
    return residuals

def get_n(X, Y):
    """Get N, check independent vs dependent variables"""
    n_X = length(X)
    n_Y = length(Y)

    if n_X == n_Y:
        n = n_X
    else:
        print("Error!")

    print("Working!")
    return n

def get_ses(residuals, X, Y):
    """Get SEs (according to OLS formula)"""
    residuals2 = residuals^2
    XX = (np.transpose(X) * X)^(-1) # transpose is not a real function
    N = get_n(X, Y)
    ses = (residuals2 / (N-1)) * XX

    print("Working!")
    return ses

def get_r2(Y, X, betas):
    """Get R^2"""
    y_hat = X * betas
    y_bar = mean(y)

    SSR = sum((y_hat - y_bar)^2)
    SST = sum((y - y_bar)^2)

    r2 = SSR / SST

    print("Working!")
    return r2

def get_sse(Y, X, betas):
    """Get sum of squared errors"""
    y_hat = X * beta
    sse = (Y - y_hat) ** 2

    print("Working!")
    return sse

def get_loss_function(SSE, lamb, betas):
    """Get loss function"""
    betas_no_intercept = betas[1:len(betas)]
    loss_function = SSE + lamb * np.sum(np.abs(betas_no_intercept))

    print("Working!")
    return loss_function

def get_coeffs_given_lambda(X, Y, lamb):
    Z = # STANDARDIZED X
    Y_c = # CENTERED Y
    coefficients = np.linalg.inv(Z.transpose().dot(Z).values() + lamb * np.identity(X.shape[1])).dot(Z.transpose().dot(Y_c))
    return(coefficients)

def pick_lowest_lambda(X, Y):
    """Pick lowest lambda"""
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
