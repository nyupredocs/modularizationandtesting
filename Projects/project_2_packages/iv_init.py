'''

Python Package to implement instrumental variables
Author: Group 2 NYU Pre docs
Date Created: December 6, 2019

'''

import numpy as np

mat_x = np.transpose(np.matrix([ [4, .2, 1, 5],
                    [.4, 2, 2, 2],
                    [0, 0, .3, 1]]))

mat_z  = np.transpose(np.matrix([[1, .5, 2, 3],
                    [3, 0, .2, 3],
                    [1, 0, .4, 3]]))

mat_y  = np.transpose(np.array([[3, 5, 2, 1]]))

def check_dim(a, b, c):
    try:
        assert a.shape[1] == b.shape[1] == c.shape[1]
    except:
        raise Exception('Matrices are the wrong shape')

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

    proj = projection_matrix(b)
    b_1  = np.transpose(a) @ proj @ a
    b_2 = np.linalg.inv(b_1)
    b_3 = np.transpose(a) @ proj @ c
    return b_2 @ b_3

print(estimate_beta_iv(mat_x, mat_z, mat_y))
