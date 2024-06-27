from langchain.embeddings import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")

from langchain.vectorstores import Milvus
db = Milvus(embedding_function=embedding, collection_name="arXiv",connection_args={"host": "172.29.4.47", "port": "19530"})
