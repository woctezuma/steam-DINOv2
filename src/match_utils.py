import faiss

# Code copied from:
# https://github.com/woctezuma/feature-matcher/blob/main/src/match_utils.py


def build_faiss_index(embeddings):
    xb = embeddings.astype('float32')

    # Cosine similarity is a dot product on normalized vectors.
    # Embeddings are normalized because faiss uses METRIC_INNER_PRODUCT. See:
    # https://github.com/facebookresearch/faiss/wiki/MetricType-and-distances
    faiss.normalize_L2(xb)

    # Exact Search for Inner Product. See:
    # https://github.com/facebookresearch/faiss/wiki/Faiss-indexes
    index = faiss.IndexFlatIP(xb.shape[1])
    index.add(xb)

    return index


def search_faiss_index(
    index,
    query_vectors,
    num_neighbors=10,
):
    # If there is only one query vector, then add the batch dimension.
    if len(query_vectors.shape) == 1:
        query_vectors = query_vectors[None, :]

    xq = query_vectors.astype('float32')

    # Cosine similarity is a dot product on normalized vectors.
    faiss.normalize_L2(xq)

    return index.search(xq, num_neighbors)


def match_all(embeddings, num_neighbors=10):
    index = build_faiss_index(embeddings)
    return search_faiss_index(index, embeddings, num_neighbors)
