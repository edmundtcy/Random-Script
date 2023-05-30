import math
import numpy as np

var_a = 0.0001
var_b = 0.0004
covar_ab = -0.0001
covar_ba = -0.0001

w = (var_b - covar_ab)/(var_a + var_b - 2*covar_ab)
one_minus_w = (var_a - covar_ab)/(var_a + var_b - 2*covar_ab)

covar_matrix = np.array([
    [var_a, covar_ab], 
    [covar_ba, var_b]
])

# init_position = np.array([
#     [30000], 
#     [20000]
# ])

init_position = np.array([
    [50000*w], 
    [50000*(1-w)]
])

fivday_99per = np.array([
    [(2.33/1.645) * math.sqrt(5)],
    [(2.33/1.645) * math.sqrt(5)]
])

Σx =np.dot(covar_matrix, init_position)

port_variance = np.dot(init_position.T, Σx)

port_volatility = np.sqrt(port_variance)

port_var = port_volatility * 1.645

β = init_position.sum() * (1/port_variance) * Σx

margin_var = (port_var/init_position.sum()) * β

component_var = margin_var * init_position

margin_var_fivday_99per = margin_var * fivday_99per

print('w: ', w)
print('one_minus_w: ', one_minus_w)
print(init_position)

x = np.array([1 , 2])
sigma = np.array([
    [0.0025, -0.003], 
    [-0.003, 0.0144]
])

sw = sigma.dot(x.T)
print('hi', sw)

