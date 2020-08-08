import matplotlib.pyplot as plt
from math_linreg2.snippets.data.loader import SawlikePop1M, chunks


population = SawlikePop1M()
samples = chunks(population, 100)
guys_with_no_13 = [sample[13] for sample in samples]



plt.subplot(2, 1, 1)
plt.hist(population, 50)
plt.ylabel('observation as outcome')

plt.subplot(2, 1, 2)
plt.hist(guys_with_no_13, 50)
plt.ylabel('sample as outcome')

plt.show()