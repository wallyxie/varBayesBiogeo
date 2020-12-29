import torch as tc
import numpy as np

##############################################
##Stochastic differential equation functions##
##############################################

def litter_scon(I_S, I_D):
    '''
    Returns SCON system litter vector.
    '''
    litter_vector = tc.reshape(tc.FloatTensor([I_S, I_D, 0]), [3, 1])
    return litter_vector

def litter_sawb(I_S, I_D):
    '''
    Returns SCON system litter vector.
    '''
    litter_vector = tc.reshape(tc.FloatTensor([I_S, I_D, 0, 0]), [4, 1])
    return litter_vector

def alpha_scon(c_vector, params):
    '''
    Returns SCON system drift vector for approximate p(x).
    c_vector[0] is expected to be SOC, c_vector[1] is expected to be DOC, and c_vector[2] is expected to be MBC.
    '''
    c_vector = soc, doc, mbc
    soc = 
    doc = 
    mbc = 
    c_vector = 
    return c_vector
    #IN PROGRESS

def beta_scon():
    '''
    Returns SCON system diffusion matrix.
    '''
    #IN PROGRESS
    return
