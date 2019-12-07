'''

Python Package to implement instrumental variables
Author: Group 2 NYU Pre docs
Date Created: December 6, 2019

'''
import numpy as np


def check_dim(a, b, c):
    '''
    Check dimensions
    '''
    try:
        assert len(a.shape) == 2 & len(b.shape) == 2 & len(c.shape) == 2
    except:
        raise Exception('Incorrect data dimension input')

    try:
        assert a.shape[0] == b.shape[0] == c.shape[0]
    except:
        raise Exception('Number of observations not equal')

    try:
        assert a.shape[1] <= b.shape[1]
    except:
        raise Exception('Model underidentified')

def projection_matrix(b):
    '''
    Inputs:
        b (matrix) -- z
    '''

    P_b = b @ np.linalg.inv((np.transpose(b) @ b)) @ np.transpose(b)
    return P_b

def estimate_beta_iv(a, b, c, nocons = False, verbose = False):
    '''
    Inputs:
        a (matrix) -- x
        b (matrix) -- z
        c (matrix) -- y
    '''
    if nocons != True and nocons != False:
        raise Exception('nocons option misspecified')

    check_dim(a, b, c)
    if nocons == False:
        N = a.shape[0]
        a_1 = np.ones((N,1))
        a = np.hstack((a_1,a))
        b_1 = np.ones((N,1))
        b = np.hstack((b_1, b))

    proj = projection_matrix(b)
    b_1  = np.transpose(a) @ proj @ a
    b_2 = np.linalg.inv(b_1)
    b_3 = np.transpose(a) @ proj @ c
    betas_all = b_2 @ b_3
    return betas_all
