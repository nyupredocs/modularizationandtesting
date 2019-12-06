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

def get_loss_function(SSE, lambda, betas):
    """Get loss function"""
    betas_without_intercept = betas[1:length(betas)]
    loss_function = SSE + lambda * sum(abs(betas_without_intercept))

    print("Working!")
    return loss_function

def get_coefficients_given_lambda(lambda):
    return(coefficients)

def pick_lowest_lamda():
    """Pick lowest lambda"""
    lambdas = [1,10]
    losses = list(length(lambda))

    for lambda in lambdas:
        loss = loss_function(lambda)
        list.append(loss)

    min_loss = min(losses)
    lowest_lambda = loss(min_loss_position_in_list)

    print("Working!")
    return(lowest_lambda)

def main():
    """Performs OLS, prints output to table"""
    print("Working!")
