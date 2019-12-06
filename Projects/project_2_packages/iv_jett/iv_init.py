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
        a (matrix) -- x
        b (matrix) -- z
    '''

    P_b = b @ np.linalg.inv((np.transpose(b) @ b)) @ np.transpose(b)
    return P_b

def estimate_beta_iv(a, b, c):
    '''
    Inputs:
        a (matrix) -- x
        b (matrix) -- z
        c (matrix) -- y
    '''

    check_dim(a, b, c)
    proj = projection_matrix(b)
    b_1  = np.transpose(a) @ proj @ a
    b_2 = np.linalg.inv(b_1)
    b_3 = np.transpose(a) @ proj @ c
    return b_2 @ b_3

