# TODO 5. Odpalenie algorytmu dla danych ukladajacych sie w "linie".


# TODO pomyslec o https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html#sphx-glr-auto-examples-svm-plot-rbf-parameters-py



import numpy as np
import pandas as pd
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

import scipy.spatial


PAR_M = 80
PAR_N = 7
PAR_SEED = 1
PAR_UPPER_BOUND = 100

def get_std_labels(n):
    return [f"X{i}" for i in range(n - 1)] + ['Y']

def create_normal_df(m, n, seed):
    np.random.seed(seed)
    array = np.random.normal(size=(m, n))
    df = pd.DataFrame(data=array, columns=get_std_labels(n))
    df['Y'] = Binarizer().fit_transform(df[['Y']])
    return df

def create_crazy_df(m, n, seed):
    np.random.seed(seed)
    vec1 = np.random.normal(size=n)
    vec2 = np.linspace(1, m, m)
    array = np.vstack(vec2).__matmul__(np.vstack(vec1).T)
    df = pd.DataFrame(data=array, columns=get_std_labels(n))
    df['Y'] = pd.Series([float(i % 2) for i in range(m)])
    return df


def get_smallest_distance(X, upper_bound):
    distance_matrix = scipy.spatial.distance_matrix(X, X)
    np.fill_diagonal(distance_matrix, upper_bound)
    smallest_distance = distance_matrix.min()
    return smallest_distance

def calculate_gamma(X, upper_bound):
    epsilon = get_smallest_distance(X, upper_bound)
    gamma_stanford = epsilon / np.log(X.shape[0])
    gamma_sklearn = 1 / (gamma_stanford ** 2)
    return gamma_sklearn

def split_and_scale(df):
    X = df.drop(['Y'], axis=1)
    y = df['Y']
    X = StandardScaler().fit_transform(X)
    return X, y

"""CASE: good (normal)"""
# df_good = create_normal_df(PAR_M, PAR_N, PAR_SEED)
# X_good, y_good = split_and_scale(df_good)
# gamma_good = calculate_gamma(X_good, PAR_UPPER_BOUND)
# clf = SVC(kernel='rbf', C=1.0, gamma=gamma_good)
# clf.fit(X_good, y_good)
# score_good = clf.score(X_good, y_good)
# res = pd.DataFrame().assign(Y_pred=clf.predict(X_good), Y_exp=y_good)
# print(score_good)
# print(gamma_good)

# TODO labele w innej funckji


df_bad = create_crazy_df(PAR_M, PAR_N, PAR_SEED)
X_bad, y_bad = split_and_scale(df_bad)
gamma_bad = calculate_gamma(X_bad, PAR_UPPER_BOUND)
clf_bad = SVC(kernel='rbf', C=1, gamma=gamma_bad)
clf_bad.fit(X_bad, y_bad)
score_bad = clf_bad.score(X_bad, y_bad)
res = pd.DataFrame().assign(Y_pred=clf_bad.predict(X_bad), Y_exp=y_bad)
print(score_bad)