import numpy as np
from numpy import genfromtxt

np.set_printoptions(suppress=True)

np.random.seed(0)


k = 2
alpha = 0.001
lamb = 0.1
epochs = 15

train = genfromtxt('Train.csv', delimiter=',')
print(train)
