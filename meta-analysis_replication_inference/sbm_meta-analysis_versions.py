import torch as tc
import numpy as np

##############################################
##Stochastic differential equation functions##
##############################################

def scon_pool_init_meta(I_S, I_D, varying_system_parameters, constant_system_parameters, C_t0, SDE_system):
    '''
    Determines and returns vector of values for parameters whose values depend on on proposed values for varying parameters, previously chosen values for other constant parameters, and choices of initial pre-warming steady state pool sizes, C_t0. This function assumes that the parameters that are varied and held constant are the same as for the inferences done in Xie et al., 2020. In Xie et al., 2020, steady state equations were re-arranged so that rather than pre-warming steady state pool sizes following from varying parameter values, pool sizes were pre-emptively set, which required some parameter values to be a priori held constant and others to be calculated from the re-arranged steady state equations following sampling of values for the varying system parameters at each Markov chain step. This was done to biologically constrain steady state pool sizes to biologically realistic values.
    Dictionaries expected for varying_system_parameters and constant_system_parameters. Tensor/vector expected for C_t0.
    '''
    SDE_system = upper(SDE_system)
    if SDE_system == 'SCON':
        print('Checking to ensure expected number of varying system parameters (7), previously set system parameters (1), and pre-warming pool densities (3) for model SCON are present.')
        if len(varying_system_parameters) == 7 and len(constant_system_parameters) == 1 and len(C_t0) == 3:
            #Unpack varying system parameters.
            Ea_S = varying_system_parameters['Ea_S']
            Ea_D = varying_system_parameters['Ea_D']
            Ea_M = varying_system_parameters['Ea_M']
            a_SD = varying_system_parameters['a_SD']
            a_DS = varying_system_parameters['a_DS']
            a_M = varying_system_parameters['a_M']
            a_MSC = varying_system_parameters['a_MSC']
            #Unpack constant system parameters.
            u_M = constant_system_parameters['u_M']
            #Unpack chosen pre-warming steady states.
            S_0 = C_t0[0]
            D_0 = C_t0[1]
            M_0 = C_t0[2]
            #Solve for calculated parameter values to be plugged into equation solving function. 'Reference values' being solved for correspond to parameter values at reference temperature of 283.15 K, which equates to 50 F.
            k_M_ref = u_M * D_0 / M_0
            k_S_ref = (I_S + D_0 * (a_DS * k_D_ref + u_M * a_M * a_MSC)) / S_0
            k_D_ref = (-I_D - (a_SD * I_S) + (D_0 * u_M) - (a_M * D_0 * u_M) + (a_M * a_MSC * D_0 * u_M) - (a_M * a_MSC * a_SD * D_0 * u_M)) / (D_0 * (-1 + a_DS * a_SD))
        #Return calculated system parameter values
        return {'k_S_ref': k_S_ref, 'k_D_ref': k_D_ref, 'k_M_ref': k_M_ref}
    elif SDE_system == 'SAWB':
        print('Checking to ensure expected number of varying system parameters (9), previously set system parameters (1), and pre-warming pool densities (4) for model SAWB are present.')
        if len(varying_system_parameters) == 9 and len(constant_system_parameters) == 1 and len(C_t0) == 4:
            #Unpack varying system parameters.
            V_ref = varying_system_parameters['V_ref']
            V_U_ref = varying_system_parameters['V_U_ref']
            Ea_V = varying_system_parameters['Ea_V']
            Ea_VU = varying_system_parameters['Ea_VU']
            Ea_K = varying_system_parameters['Ea_K']
            Ea_KU = varying_system_parameters['Ea_KU']
            a_MSA = varying_system_parameters['a_MSA']
            u_Q_ref = varying_system_parameters['u_Q_ref'] #former E_C_ref
            Q = varying_system_parameters['Q'] #formerly m_t. Not involved in solving for calculated parameter values.
            #Unpack constant system parameters
            r_L = constant_system_parameters['r_L']
            #Unpack chosen pre-warming steady state.
            S_0 = C_t0[0]
            D_0 = C_t0[1]
            M_0 = C_t0[2]
            E_0 = C_t0[3]
            #Solve for calculated parameter values to be plugged into equation solving function. 'Reference values' being solved for correspond to parameter values at reference temperature of 283.15 K, which equates to 50 F.
            r_E = r_L * E_0 / M_0
            r_M = (-u_Q_ref * (I_S + I_D) + M_0 * r_E * (1 - u_Q_ref)) / (M_0 * (u_Q_ref - 1))
            K_U_ref = -(D_0 * (r_M + r_E - u_Q_ref * V_U_ref)) / (r_M + r_E)
            K_ref = -((S_0 * (-I_S * r_E * r_L + u_Q_ref * I_S * r_E * r_L - a_MSC * u_Q_ref * I_D * r_L * r_M - I_S * r_L * r_M + u_Q_ref * I_S * r_L * r_M - a_MSC * u_Q_ref * I_S * r_L * r_M + u_Q_ref * I_D * r_E * V_ref + u_Q_ref * I_S * r_E * V_ref)) / (r_L * (-I_S * r_E + u_Q_ref * I_S * r_E - a_MSC * u_Q_ref * I_D * r_M - I_S * r_M + u_Q_ref * I_S * r_M - a_MSC * u_Q_ref * I_S * r_M)))
        return {'r_E': r_E, 'r_M': r_M, 'K_U_ref': K_U_ref, 'K_ref': K_ref}
    else:
        raise Exception('Either ineligible model provided or mismatch(es) in length(s) of array(s) or tensor(s) corresponding to varying system parameters, constant system parameters, or initial conditions C_t0. "SCON" and "SAWB" only for now.')

def alpha_scon():
    #IN PROGRESS
    return
