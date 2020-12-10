import torch
import numpy as np

##############################################
##Stochastic differential equation functions##
##############################################

def scon_pool_init_meta(I_S, I_D, varying_system_parameters, constant_system_parameters, C_t0, SDE_system):
    '''
    Determines and returns vector of values for parameters whose values depend on on proposed values for varying parameters, previously chosen values for other constant parameters, and choices of initial pre-warming steady state pool sizes, C_t0. This function assumes that the parameters that are varied and held constant are the same as for the inferences done in Xie et al., 2020. In Xie et al., 2020, steady state equations were re-arranged so that rather than pre-warming steady state pool sizes following from varying parameter values, pool sizes were pre-emptively set, which required some parameter values to be a priori held constant and others to be calculated from the re-arranged steady state equations following sampling of values for the varying system parameters at each Markov chain step. This was done to biologically constrain steady state pool sizes to biologically realistic values.

    For SCON, varying system parameters need to be ordered by Ea_S, Ea_D, Ea_M, a_SD, a_DS, a_M, and a_MSC values. Constant system parameters need to be ordered by u_M values. Pre-warming values in the C_t0 array/vector/tensor need to be ordered by S0, D0, and M0.

    For AWB, varying system parameters need to be ordered by ... values. Constant system parameters need to be ordered by ... values. Pre-warming values in the C_t0 array/vector/tensor need to be ordered by S0, D0, M0, and E0 values.
    '''
    SDE_system = upper(SDE_system)
    if SDE_system == 'SCON':
        print('Checking to ensure expected number of varying system parameters (7), previously set system parameters (x), and pre-warming pool densities (3) for model SCON are present.')
        if len(varying_system_parameters) == 7 and len(constant_system_parameters) == 1 and len(C_t0) == 3:
            #Unpack varying system parameters.
            Ea_S = varying_system_parameters[0]
            Ea_D = varying_system_parameters[1]
            Ea_M = varying_system_parameters[2]
            a_SD = varying_system_parameters[3]
            a_DS = varying_system_parameters[4]
            a_M = varying_system_parameters[5]
            a_MSC = varying_system_parameters[6]
            #Unpack constant system parameters.
            u_M = constant_system_parameters[0]
            #Unpack chosen pre-warming steady states.
            S0 = C_t0[0]
            D0 = C_t0[1]
            M0 = C_t0[2]
            #Solve for calculated parameter values to be plugged into equation solving function. 
        return k_S_ref, k_D_ref, k_M_ref #calculated system parameters
    elif SDE_system == 'SAWB':
        print('Checking to ensure expected number of varying system parameters (9), previously set system parameters (x), and pre-warming pool densities (4) for model SAWB are present.')
        if len(varying_system_parameters) == 9 and len(constant_system_parameters) == 1 and len(C_t0) == 4:
            #solve for calculated parameter values here
        return r_E, r_M, k_U_ref, K_ref #calculated system parameters
    else:
        raise Exception('Either ineligible model provided or mismatch(es) in length(s) of array(s) or tensor(s) corresponding to varying system parameters, constant system parameters, or initial conditions C_t0. "SCON" and "SAWB" only for now.')

def alpha_scon():
    return
