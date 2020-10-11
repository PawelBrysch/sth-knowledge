import pathlib as pl
from arff2pandas import a2p
import numpy as np
from sklearn.naive_bayes import MultinomialNB
import os
import re
import pandas as pd


def get_df(path):
    with open(path) as infile:
        df = a2p.load(infile)
    """ cos sie nie zgadzalo """
    bad_column = 'f1448@NUMERIC'
    if bad_column in df:
        # print(path)
        df = df.drop('f1448@NUMERIC', axis=1)
    # return df.drop('f1448@NUMERIC', axis=1)
    return df

class Experiment:
    objects = []
    def __init__(self, path):
        self.name = path.name
        self.__class__.objects.append(self)
        # try:
        #     self.df = get_df(path)
        #     self.X, self.y = np.split(self.df, [self.df.shape[1] - 1], axis=1)
        # except:
        #     pass

        self.df = get_df(path)
        self.X, self.y = np.split(self.df, [self.df.shape[1] - 1], axis=1)
        self.y = Experiment.y_prepared(self.y)
        self.df_int = self.X.assign(is_spam=self.y).astype(int)

    def calculate_NB(self, test_X, test_Y):
        self.nb = MultinomialNB()
        self.nb.fit(self.X, self.y)
        self.score = self.nb.score(test_X, test_Y)
        # self.score = self.nb.score(test_X, Experiment.y_prepared(test_Y))
        self.result_df = pd.DataFrame().assign(Y_act=test_Y, Y_pred=self.nb.predict(test_X))

    @staticmethod
    def y_prepared(y):
        return pd.get_dummies(y)['class@{spam,non_spam}_spam']
        # return (y['class@{spam,non_spam}'] == 'spam').astype(int)

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return self.__str__()

"""root"""
ALL = Experiment.objects
path_to_datadir = pl.Path(__file__).parent.joinpath("snippets/data/q4")

"""test data"""
path_to_test_data = path_to_datadir.joinpath('spam_test.arff')
test_df = get_df(path_to_test_data)
test_X, test_Y = np.split(test_df, [test_df.shape[1] - 1], axis=1)
test_Y = Experiment.y_prepared(test_Y)

"""#################
workspace
#################"""
FLAG_ALL = True
# FLAG_ALL = False

for filename in list(set(os.listdir(path_to_datadir)) - {'spam_train_750.arff', 'spam_test.arff'}):
    Experiment(pl.Path(path_to_datadir, filename))
    if not FLAG_ALL:
        break

ALL = sorted(ALL, key=lambda x: int(re.search('spam_train_([\d]+).arff', x.name).group(1)))

""" stare """
# exp1 = ALL[0]
# exp1.calculate_NB(test_X, test_Y)


# TODO zrobic matrix len x len
# TODO pobrac len takiego merge


ALL.append(Experiment(pl.Path(path_to_datadir, 'spam_test.arff')))
length = len(ALL)
commons = np.zeros([length, length])

for i in range(length):
    for j in range(length):
        commons[i][j] = pd.merge(ALL[i].df_int, ALL[j].df_int, how='inner').shape[0]

print(commons)
df_commons = pd.DataFrame(commons)

i = 8
j = 8

z1 = pd.merge(ALL[i].df_int, ALL[j].df_int, how='inner')

# TODO wtf - dlaczego score leci na dol, gdy jest wiecej danych
    # TODO posprawdzac czesci wspolne tych zbiorow


for elem in ALL:
    elem.calculate_NB(test_X, test_Y)
    print(elem.name, elem.score)



# exp1.calculate_NB(test_X, test_Y)
# exp1.calculate_NB(test_X, test_Y['class@{spam,non_spam}'])
# exp1.calculate_NB(test_X, test_Y['class@{spam,non_spam}'])

# exp1.calculate_NB(test_X, test_Y['class@{spam,non_spam}'].values)
# exp1.calculate_NB(test_X, np.ravel(test_Y))
# test_Y2 = (test_Y['class@{spam,non_spam}'] == 'spam').astype(int)
# df2 = pd.DataFrame(test_Y).assign(y2=test_Y2)




"""test na jednym"""
# path1 = path_to_datadir.joinpath('spam_train_50.arff')
# exp1 = Experiment(path1)
# exp1.calculate_NB()

# exp1 = ALL[5]
# exp1.calculate_NB()
# z1 = exp1.nb.score(test_X, test_Y)


# Y_pred = exp1.nb.predict(test_X)
# Y_pred = pd.Series(Y_pred)
# test_Y = test_Y['class@{spam,non_spam}']
# z2 = pd.DataFrame().assign(TEST=test_Y, PRED=Y_pred)

