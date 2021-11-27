import numpy as np
from scipy.optimize import minimize

#  A = np.matrix([
    #  [-1, 2],
    #  [-2, 3],
    #  [6, -2],
    #  [3, -1]
#  ])

A = np.matrix([
    [5, -1, 0, 1],
    [-1, 3, -1, 0],
    [0, 0, 4, 0],
    [0, 0, 0, 2]
])

n = A.shape[1]
w0 = np.ones(n) / n
bounds = n*[(0, 100)]
constraints = {
    'type': 'eq', 'fun': lambda w: np.sum(w) - 100,
    #  'type': 'eq', 'fun': lambda w: np.all(w % 1 == 0) - 1
}

def obj(w):
    p = A @ w
    p_pos = np.maximum(p, 0)
    return -np.prod(p_pos)

opt = minimize(
    fun=obj,
    x0=w0,
    bounds=bounds,
    constraints=constraints
)

print(opt.x)

# Tried:
# - 26016480 (high)
# - 24994760 (high)
print(obj(np.round(opt.x)))
