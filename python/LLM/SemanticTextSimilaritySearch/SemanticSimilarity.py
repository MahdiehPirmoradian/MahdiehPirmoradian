model_name = 'bert-base-nli-mean-tokens'

from sentence_transformers import SentenceTransformer

model= SentenceTransformer(model_name)

Sentences = [
    "A group of students is attending a lecture.",
    "The weather is beautiful today.",
    "I like to drink coffee today",
    "It's a lovely day outside.",
    "The project was finished before the deadline.",
    "She is studying British literature.",
    "I have a dentist appointment tomorrow."
]

sentence_vecs = model.encode(Sentences)

sentence_vecs

from sklearn.metrics.pairwise import cosine_similarity

cosine_similarity(
    [sentence_vecs[0]], 
    sentence_vecs[1:]
)

