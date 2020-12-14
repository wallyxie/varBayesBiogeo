import torch as tc
import numpy as np

#Remember to beware of Neal's Funnel. https://mc-stan.org/docs/2_18/stan-users-guide/reparameterization-section.html. In order to mitigate Neal's Funnel geometric sampling issues, we use the expression parameter_value = prior_mean + sd_raw * N(0,1). parameter_value is not directly sampled, but is obtained after adding the prior mean to the product of a scaling factor and normal distribution draw. parameter_value is then passed to static parameter value calculation and SDE solving functions.

# def varying_parameters_samples_proposal(prior_means_vector, sd_raws_vector): #take in varying_parameters_priors_dict argument?
#     '''
#     Returns draw of parameter values for varying parameters proposal.
#     '''
#     #IN PROGRESS
#     if len(prior_means_vector) != len(sd_raws_vector):
#         raise Exception('Parameter prior means and raw standard deviation scaling factor vectors are not the same length.')
#     std_normal_draws_length = len(sd_raws_vector)
#     std_normal_draws_vector = tc.normal(0, 1, size(1, std_normal_draws_length))
#     varying_parameters_samples_vector = prior_means_vector + sd_raws_vector * std_normal_draws_vector
#     return varying_parameters_samples_vector
