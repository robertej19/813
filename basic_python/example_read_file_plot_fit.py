from scipy import *
from scipy.optimize import leastsq
from numpy import loadtxt
import matplotlib.pyplot as plt


def residuals(p, y, x, yerr): 
	err = (y-peval(x,p))/yerr 
	return err

def peval(x, p):
	pev = 0.
	for i in range(len(p)):
		pev = pev + p[i]*x**i
	return pev

#we will fit to a polynomial of degree 9.  This is a dumb model for the index of refraction,  but it works as an example.
N = 9

#read in the file of data on the index of refraction of acrylic.
filename='Acrylic.dat'
data = loadtxt(filename)

#read in second column  (python counts from zero)
n = data[:,1]

#read in the first column and convert the units
l = data[:,0]/1000.

#the standard deviation of a uniform dist is sqrt(12), check this out in Bevington or Google.
yerr=0.0001/sqrt(12)

#zero your fitting parameters
p0 = zeros(N+1) #This creates an array of zeros N+1 elements large
# and do the fit
plsq = leastsq(residuals, p0, args=(n, l, yerr), maxfev=2000)

#total up the chi2
p1 = plsq[0]
chisq = sum(peval(l,p1))
csndf = chisq/(len(l)-(N+1))

#make 2 plots, with the fit shown.
#First plot is the data vs wavelength with the fit
plt.subplot(211)
plt.errorbar(l, n, yerr=yerr, fmt='r.', markersize=10)
x = arange(.400, 1.100, .001)
plt.plot(x,peval(x,p1))
plt.ylabel('Refractive index', fontsize=16)
plt.title('Acrylic index of refraction', fontsize=20)

#second plot is the "residuals" -- the wiggles in this plot show that the polynomial model is not great
plt.subplot(212)
d = residuals(p1, n, l, yerr)
plt.errorbar(l, d*yerr, yerr=yerr, fmt='.', markersize=10)
plt.axhline(y=0., linewidth=2, color='g')
plt.xlabel('Wavelength ('+r'$\mu$'+'m)', fontsize=16)
plt.ylabel('Fit residuals', fontsize=16)
plt.ylim(-.00025, .00025)



print("\n\n Chi-square per degree of freedom = %7.4f" %csndf)
print("\n * * * Final parameters * * * \n")
for i in range(len(p1)):
	print("  p[%i] = %13.6e " %(i, p1[i]))



plt.show()

