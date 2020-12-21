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

def alpha_scon():
    '''
    Returns SCON system drift vector.
    '''
    #IN PROGRESS
    return

def beta_scon():
    '''
    Returns SCON system diffusion matrix.
    '''
    #IN PROGRESS
    return
