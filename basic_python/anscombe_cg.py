"""Somewhat code-golfed version of anscombe.py. this is an example of what NOT to do,
specifically in that there are no comments. 
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])
y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])
y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])

def fit(x): return 3 + 0.5*x

xfit = np.array([np.amin(x), np.amax(x)])
pairs = (x, y1), (x, y2), (x, y3), (x4, y4)
titles = ("I","II","III","IV")

for i, pair in enumerate(pairs):
    plt.subplot(2,2,i+1)
    plt.plot(pair[0], pair[1], 'ks', xfit, fit(xfit), 'r-', lw=2)
    plt.axis([2, 20, 2, 14])
    plt.setp(plt.gca(), xticklabels=[], yticks=(4, 8, 12), xticks=(0, 10, 20))
    plt.text(3, 12, titles[i], fontsize=20)
    if i == 0 or i == 2:
        plt.ylabel('Y Values', fontsize=16)
    if i == 2 or i == 3:
        plt.xlabel('X values', fontsize=16)

for x, y in pairs:
    print('mean=%1.2f, std=%1.2f, r=%1.2f' % (np.mean(y), np.std(y), np.corrcoef(x, y)[0][1]))

plt.show()
