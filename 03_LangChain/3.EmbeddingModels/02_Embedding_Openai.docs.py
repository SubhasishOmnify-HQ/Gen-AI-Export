from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)
documents = [
    "What is the capital of India?",
    "What is the largest planet in our solar system?",
    "What is the chemical symbol for gold?"
]

embedding_vector = embedding.embed_documents(documents)
print(str(embedding_vector))