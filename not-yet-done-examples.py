Here is my code for doing the fit and plotting:
8:51
popt, pcov = curve_fit(gauss, xval, yval, sigma=yerror,p0 = [100, 3300, 140],absolute_sigma=False)
xx = np.arange(xmin,xmax)
plt.plot(xx, gauss(xx, *popt), label='fit')


One line method to load a CSV data file into python with numpy
import numpy as np
data=[*zip(*np.genfromtxt('cubeData.csv',delimiter=','))]