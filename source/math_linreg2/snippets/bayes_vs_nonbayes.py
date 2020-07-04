import matplotlib.pyplot as plt
import pandas as pd

# TODO opis
def conditional_probability(dice, sample):
    if max(sample) > dice:
        return 0
    return (1/dice) ** len(sample)


sample = [2, 2, 4, 5, 5]
dices = pd.DataFrame()
dices = dices.assign(value=[4, 5, 6, 7, 8])
dices = dices.assign(count=[1, 3, 12, 3, 1])
dices = dices.assign(dice_prob=dices['count'].apply(lambda x: x / dices['count'].sum()))
dices = dices.assign(non_bayes_prob=dices['value'].apply(lambda x: conditional_probability(x, sample)))
dices = dices.assign(bayes_prob=dices['non_bayes_prob'] * dices['dice_prob'])

plt.scatter(dices['value'], dices['non_bayes_prob'], )
plt.scatter(dices['value'], dices['bayes_prob'])



