import numpy as np
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from scipy.optimize import leastsq
from scipy import stats
import scipy.optimize as opt
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson
from scipy.interpolate import BarycentricInterpolator
from scipy.interpolate import CubicSpline
import scipy as sp
import math

# a =  np.logspace(1,4,4,base=10)
# print(a)
# print(np.arange(1,10))

# s = 'abcdzzzz'
# g = np.fromstring(s, dtype=np.int8)
# print(g)

# a = np.logspace(0, 3, 10, base=2)
# print(a)
# i = np.arange(0, 10, 2)
# print(i)

mpl.rcParams['font.sans-serif'] = [u'SimHei']  # FangSong/黑体 FangSong/KaiTi
mpl.rcParams['axes.unicode_minus'] = False
mu = 0
sigma = 1
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 51)
y = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
print(x.shape)
print('x = \n', x)
print(y.shape)
print('y = \n', y)
plt.figure(facecolor='w')
plt.plot(x, y, 'ro-', linewidth=2)
# plt.plot(x, y, 'r-', x, y, 'go', linewidth=2, markersize=8)
plt.xlabel('X', fontsize=15)
plt.ylabel('Y', fontsize=15)
plt.title(u'高斯分布函数', fontsize=18)    #
plt.grid(True)
plt.show()