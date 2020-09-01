#This brings in the modules that you need
from scipy import *
from scipy.optimize import leastsq
from numpy import loadtxt
import matplotlib.pyplot as plt

#-----------------------
# These are the functions for use in the least squares fit

def residuals(p, y, x, yerr):
    err = (y - peval(x,p))/yerr
    return err

def peval(x, p):
    pev = p[0] * exp(-1. * x/p[1])   # this example is fitting an exponential
    return pev

#-----------------------

#Here is the data set
pm1 = array([10., 20., 30., 40., 50.])  # x axis
Am1 = array([574., 416., 345.5, 299., 256.])   # y axis

#calculate the error
em1 = sqrt(Am1)   # statistical error is sqrt of the data

#-----------------------


# plot this data with error bars
plt.errorbar(pm1, Am1, em1, fmt='kh', markersize=3)

#-----------------------
# Now fit the data

# give it some starting parameters
p0 = array([1000.,50.])

"""do the least squares fit. It makes use of the function called residuals, above.
note: leastsq() returns an array of the solutions (plsq[0]) as well as
returning an integer (plsq[1]) if plsq[1] == 1,2,3, || 4, the solution was found. 
This is not important for our purposes here. """
plsq = leastsq(residuals, p0, args=(Am1, pm1, em1), maxfev=20000)

# These are the best fit parameters returned
p1 = plsq[0]
print('best fit: {:1.2f}, {:1.2f}'.format(p1[0],p1[1]))

#-----------------------

# calculate the chi2 by comparing function evaluates at best fit parameters to data.
testpt = peval(pm1, p1)
sqerr = ((Am1 - testpt)/em1)**2
chisq = sum(sqerr)
csndf = chisq/(len(pm1) - 1.)
print('chisq per dof: {:1.2f}'.format(csndf))

#-----------------------

# This plots the best fit function across the range of interest on the same plot as data with error bars
x = arange(0., 60., 1.)
plt.plot(x,peval(x,p1))


#-----------------------

# This sets up some nice labels
plt.ylabel('Time-integrated ADC Counts', fontsize=16)
plt.xlim(0., 60.)
plt.ylim(100., 1000.)
plt.xlabel('Position (cm)', fontsize=16)

# add a comment
plt.text(10., 3500, r'fit from 10 cm to 50 cm', fontsize=16)


# Just for fun, make it a  semilog plot...
plt.semilogy()

#-----------------------


#Now display it.
plt.show()


