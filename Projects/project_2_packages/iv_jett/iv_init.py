'''

Python Package to implement instrumental variables
Author: Group 2 NYU Pre docs
Date Created: December 6, 2019

'''
import numpy as np


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

    '''

    proj = projection_matrix(b)
    b_1  = np.transpose(a) @ proj @ a
    b_2 = np.linalg.inv(b_1)
    b_3 = np.transpose(a) @ proj @ c
    return b_2 @ b_3

    #b_iv = np.linalg.inv(np.transpose(a) @ projection_matrix(b) @ a) \
    #       @ np.transpose(a) @ projection_matrix(b) @ c
