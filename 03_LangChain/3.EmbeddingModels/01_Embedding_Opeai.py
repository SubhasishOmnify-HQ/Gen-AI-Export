from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

embedding_vector = embedding.embed_query("What is the capital of India?")
print(str(embedding_vector))