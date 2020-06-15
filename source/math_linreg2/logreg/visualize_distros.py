import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
from math_linreg2.logreg.enhance_fromfunction import adjust_to_fromfunction


PARAM_X = 0.3
PARAM_Y = 0.5

def z_func(x_arg, y_arg):
 return 1 / (1 + np.exp(
  PARAM_X * x_arg + PARAM_Y * y_arg
 ))

Ys = np.linspace(-5, 5, 80)
Xs = np.linspace(-10, 10, 80)
Zs = np.fromfunction(
    adjust_to_fromfunction(z_func, Ys, Xs),
    (Ys.size, Xs.size))


plt.contourf(Ys, Xs, Zs.T,
             levels=MaxNLocator(nbins=45).tick_values(Zs.min(), Zs.max()),
             cmap=plt.get_cmap('PiYG'))
plt.colorbar()
plt.title('some_title')

