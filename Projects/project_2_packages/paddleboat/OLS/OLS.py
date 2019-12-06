import pandas as pd
import numpy as np

def get_betas(X, Y):
    betas = (transpose(X) * X)^(-1) * (transpose(X) * Y)
    print("Working!")
    return betas

def get_residuals(betas, X):
    residuals = betas * X
    print("Working!")
    return residuals

def get_n(X, Y):
    n_X = length(X)
    n_Y = length(Y)
    if n_X == n_Y:
        n = n_X
    else:
        print("Error!")
    print("Working!")
    return n

def get_ses():
    residuals2 = residuals^2
    XX = (transpose(X) * X)^(-1)
    ses = (residuals2 / (N-1)) * XX
    print("Working!")
    return ses

def main():
    print("Working!")
