#Bring in the required modules
from scipy import *
import matplotlib.pylab as plt


#
# Create two Gaussian distributions to histogram
# 1,000 points each
#

mu1 = 0.4
sigma1 = 0.1
mu2 = 0.6
sigma2 = 0.2


"""note: randn(n) (from numpy) generates an array n elements large, with each element
a float generated from a normal distribution of mean 0 and variance 1"""
y1 = mu1 + sigma1 * randn(1000) #creates an array of 1000 floats
y2 = mu2 + sigma2 * randn(1000)

#
# Histogram range and number of bins
#

xmin = -0.5
xmax = 1.5
nbins = 100

#
# Create histograms
#

"""note: counts1 returns the number of elements in the array y1 that exist
within each bin defined by nbins and range."""
counts1, binedges = histogram(y1, bins = nbins, range = (xmin, xmax))
counts2, binedges = histogram(y2, bins = nbins, range = (xmin, xmax))


#
# Plot them as bar graphs on top of each other
# "binedges" contains the left edges of the bins
# dim(binedges) = dim(counts) + 1
# (last bin edge is the right end of the histogram)
# binedges[:-1] loops up to the next-to-last
#

barwidth = binedges[1] - binedges[0]      # Bars occupy full width of bin

#
# Make outlines of bars invisible (linewidth = 0)
# Set transparency to 0.5
#

plt.bar(binedges[:-1], counts1, width = barwidth,
        color = 'midnightblue', linewidth = 0, alpha = 0.5,
        label = 'Narrow Gaussian')
plt.bar(binedges[:-1], counts2, width = barwidth,
        color = 'firebrick', linewidth = 0, alpha = 0.5,
        label = r'Wide Gaussian')

#
# Set plot limits
#

ymax = 1.2 * max(max(counts1), max(counts2))
plt.xlim(xmin, xmax)
plt.ylim(0., ymax)

plt.title(r'A tale of two Gaussians', fontsize = 18)
plt.xlabel(r'$x$', fontsize = 18)
plt.ylabel(r'$G(x)$', fontsize = 18)
plt.legend(shadow = True, fancybox = True)   # Make fancy legend from labels
plt.tight_layout()         # Automatically set the margins to fit everything

plt.show()
