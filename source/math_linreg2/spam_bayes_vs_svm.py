import pathlib as pl
from arff2pandas import a2p
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt

import os
import re
import pandas as pd


def get_df(path):
    with open(path) as infile:
        df = a2p.load(infile)
    """ cos sie nie zgadzalo """
    bad_column = 'f1448@NUMERIC'
    if bad_column in df:
        df = df.drop('f1448@NUMERIC', axis=1)
    return df

class Experiment:
    objects = []
    def __init__(self, path):
        self.name = path.name
        self.__class__.objects.append(self)
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

    def calculate_SVM(self, test_X, test_Y):
        self.svm = LinearSVC()
        self.svm.fit(self.X, self.y)
        self.score_svm = self.svm.score(test_X, test_Y)
        self.result_df_svn = pd.DataFrame().assign(Y_act=test_Y, Y_pred=self.svm.predict(test_X))

    @staticmethod
    def y_prepared(y):
        return pd.get_dummies(y)['class@{spam,non_spam}_spam']

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return self.__str__()

"""sciezki"""
ALL = Experiment.objects
path_to_datadir = pl.Path(__file__).parent.joinpath("snippets/data/q4")

"""pobranie danych testowych"""
path_to_test_data = path_to_datadir.joinpath('spam_test.arff')
test_df = get_df(path_to_test_data)
test_X, test_Y = np.split(test_df, [test_df.shape[1] - 1], axis=1)
test_Y = Experiment.y_prepared(test_Y)

"""pobierz MANY"""
FLAG_ALL = True
# FLAG_ALL = False

for filename in list(set(os.listdir(path_to_datadir)) - {'spam_train_750.arff', 'spam_test.arff'}):
    Experiment(pl.Path(path_to_datadir, filename))
    if not FLAG_ALL:
        break

ALL = sorted(ALL, key=lambda x: int(re.search('spam_train_([\d]+).arff', x.name).group(1)))
ALL = ALL[2:8]

for elem in ALL:
    elem.calculate_NB(test_X, test_Y)
    elem.calculate_SVM(test_X, test_Y)

results = pd.DataFrame(
    [(elem.X.shape[0], 1 - elem.score, 1 - elem.score_svm) for elem in ALL],
    columns=['SIZE', 'SCORE_NB', 'SCORE_SVM']
)


# Magic here
ax = plt.subplot()

ax.scatter(results['SIZE'], results['SCORE_NB'], label="nb")
ax.scatter(results['SIZE'], results['SCORE_SVM'], label="svm")
ax.legend()

"""pobierz SINGLE"""
# exp1 = Experiment(pl.Path(path_to_datadir, 'spam_train_1000.arff'))


""" wyniki Bayesa"""
# for elem in ALL:
#     elem.calculate_NB(test_X, test_Y)
#     print(elem.name, elem.score)


""" sprawdzanie czesci wspolnej datasetow"""
# ALL.append(Experiment(pl.Path(path_to_datadir, 'spam_test.arff')))
# length = len(ALL)
# commons = np.zeros([length, length])
#
# for i in range(length):
#     for j in range(length):
#         commons[i][j] = pd.merge(ALL[i].df_int, ALL[j].df_int, how='inner').shape[0]
#
# df_commons = pd.DataFrame(commons)

