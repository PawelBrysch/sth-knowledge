import random
from matplotlib.pyplot import hist

N = 20
heights = [random.randint(150, 200) for i in range(N)]
bmis = [random.randint(17, 32) for i in range(N)]
weights = [random.randint(60, 130) for i in range(N)]
iqs = [random.randint(70, 130) for i in range(N)]
errors = [random.randint(-200, 200) for i in range(N)]



to_print = heights
to_print = weights
to_print = bmis
to_print = iqs
to_print = errors
for elem in to_print:
    print(elem)

hist(heights, 5)