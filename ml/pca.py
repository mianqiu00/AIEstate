from sklearn.decomposition import PCA


def reduce_embedding_pca(embedding, low_dim=256):
    pca = PCA(n_components=low_dim)
    reduced_embedding_pca = pca.fit_transform(embedding)
    return reduced_embedding_pca