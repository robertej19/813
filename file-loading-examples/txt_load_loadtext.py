import numpy as np

#read in the file of cosmicwatch data,  skip the first 7 rows that are header
filename='examplefilecosmicwatch.txt'
data = np.loadtxt(filename, dtype='int, str, str, int, float, float, float, float, float, int, int',skiprows=7, delimiter='\t',unpack=True)
#read in the 4th column  (python counts from zero)
timestamp = data[3]