from sklearn.decomposition import PCA

def solution(X, number_of_components):
    pca = PCA(n_components=number_of_components, svd_solver='full')
    pca.fit(X)
    return pca.components_