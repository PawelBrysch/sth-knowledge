import random
import numpy as np
from matplotlib.pyplot import hist


N = 80
weights = [random.randint(60, 120) for i in range(N)]
dice = np.random.random_integers(1,6,80)


to_print = weights
to_print = dice
for elem in to_print:
    print(elem)

# hist(dice, 6)