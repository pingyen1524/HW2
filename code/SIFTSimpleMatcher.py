# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 21:36:46 2017

@author: HGY
"""

import numpy as np
from scipy.io import loadmat


#%% SIFTSimpleMatcher function
def SIFTSimpleMatcher(descriptor1, descriptor2, THRESH=0.49):
    '''
    SIFTSimpleMatcher 
    Match one set of SIFT descriptors (descriptor1) to another set of
    descriptors (decriptor2). Each descriptor from descriptor1 can at
    most be matched to one member of descriptor2, but descriptors from
    descriptor2 can be matched more than once.
    
    Matches are determined as follows:
    For each descriptor vector in descriptor1, find the Euclidean distance
    between it and each descriptor vector in descriptor2. If the smallest
    distance is less than thresh*(the next smallest distance), we say that
    the two vectors are a match, and we add the row [d1 index, d2 index] to
    the "match" array.
    
    INPUT:
    - descriptor1: N1 * 128 matrix, each row is a SIFT descriptor.
    - descriptor2: N2 * 128 matrix, each row is a SIFT descriptor.
    - thresh: a given threshold of ratio. Typically 0.7
    
    OUTPUT:
    - Match: N * 2 matrix, each row is a match. For example, Match[k, :] = [i, j] means i-th descriptor in
        descriptor1 is matched to j-th descriptor in descriptor2.
    '''

    #############################################################################
    #                                                                           #
    #                              YOUR CODE HERE                               #
    #                                                                           #
    #############################################################################
    
    N1 = descriptor1.shape[0]
    N2 = descriptor2.shape[0]
    THRESH = 0.7
    
    o_1 = np.zeros(0)
    o_2 = np.zeros(0)
    cnt = 0
    d_norm2 = np.zeros(N2)
    for i in range(N1):
        for j in range(N2):
            d_norm2[j-1] = np.sum(((descriptor1[i-1,:] - descriptor2[j-1,:]) ** 2)) ** 0.5
        d_norm2_sort = np.argsort(d_norm2)
        if d_norm2[d_norm2_sort[0]] < THRESH*d_norm2[d_norm2_sort[1]]:
            o_1 = np.append(o_1,i-1)
            o_2 = np.append(o_2,d_norm2_sort[0])
            cnt = cnt + 1
    match = np.zeros((cnt,2))
    match[:,0] = o_1
    match[:,1] = o_2

    #############################################################################
    #                                                                           #
    #                             END OF YOUR CODE                              #
    #                                                                           #
    #############################################################################   
    
    return match
