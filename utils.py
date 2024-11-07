import time
#from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Func to get the most similar index 
def get_most_sim_idx(p_emb, q_embs, threshold = 0.5):
    similarities = cosine_similarity(p_emb, q_embs)
    similarities = similarities.flatten()
    index = np.argmax(similarities)
    if similarities[index]<threshold:
        index = None
    print(f"Index: {index}, Similarity: {similarities[index]}")
    return index

# Streamed response emulator
def response_generator(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.15)

