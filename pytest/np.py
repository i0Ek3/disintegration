import numpy as np

list = [np.linspace([1,2,3], 3),\
np.array([1,2,3]),\
np.arange(3),\
np.arange(8).reshape(2,4),\
np.zeros((2,3)),\
np.zeros((2,3)).T,\
np.ones((3,1)),\
np.eye(3),\
np.full((3,3), 1),\
np.random.rand(3),\
np.random.rand(3,3),\
np.random.uniform(5,15,3),\
np.random.randn(3),\
np.random.normal(3, 2.5, 3)]

print(list)
