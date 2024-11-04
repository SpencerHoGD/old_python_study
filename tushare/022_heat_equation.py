from matplotlib import pylab
import seaborn as sns
import numpy as np
# from CAL.PyCAL import *
# font.set_size(20)


def initialCondition(x):
    return 4.0 * (1.0 - x) * x


xArray = np.linspace(0, 1.0, 50)
yArray = list(map(initialCondition, xArray))
pylab.figure(figsize=(12, 6))
pylab.plot(xArray, yArray)
pylab.xlabel('$x$', fontsize=15)
pylab.ylabel('$f(x)$', fontsize=15)
pylab.title(u'一维热传导方程初值条件', fontsize=20)
pylab.show()
