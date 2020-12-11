import torch
import numpy as np

#Remember to beware of Neal's Funnel. https://mc-stan.org/docs/2_18/stan-users-guide/reparameterization-section.html. In order to mitigate Neal's Funnel geometric sampling issues, we use the expression parameter_value = prior_mean + std_raw * N(0,1). parameter_value is not directly sampled, but is obtained after adding the prior mean to the product of a scaling factor and normal distribution draw. parameter_value is then passed to static parameter value calculation and SDE solving functions.

#Goal will be to take array, vector, or tensor of values and fetch an array, vector, or tensor of values drawn from N(0,1) of same length.
