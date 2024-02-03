import os

from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

load_dotenv()
LOAD_DATA_DIR = os.environ["LOAD_DATA_DIR"]
FAISS_DB_DIR = os.environ["FAISS_DB_DIR"]

faiss_db = FAISS.load_local(FAISS_DB_DIR, embeddings=OpenAIEmbeddings())
query = "clapped-audience では何ができる？"
docs = faiss_db.similarity_search(query)
print(docs[0].page_content)
