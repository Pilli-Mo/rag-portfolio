from sentence_transformers import SentenceTransformer

# Load a pre-trained embedding model from HuggingFace
# This model has been trained on billions of sentences
model = SentenceTransformer("all-MiniLM-L6-v2")

# A sample sentence — like a question a user would ask
sentence = "What are the side effects of metformin?"

# Convert the sentence into an embedding (a list of numbers)
embedding = model.encode(sentence)

print(f"Sentence: {sentence}")
print(f"Embedding size: {len(embedding)} numbers")
print(f"First 5 numbers: {embedding[:5]}")
