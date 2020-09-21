#One line method to load a CSV data file into python with numpy (from Sean P. Robinson)
import numpy as np
data=[*zip(*np.genfromtxt('cubeData.csv',delimiter=','))]
