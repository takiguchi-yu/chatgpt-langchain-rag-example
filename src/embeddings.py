import os

from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

load_dotenv()
LOAD_DATA_DIR = os.environ["LOAD_DATA_DIR"]
FAISS_DB_DIR = os.environ["FAISS_DB_DIR"]

# -----------------------------------------------
# テキストを読み込む
# -----------------------------------------------

docs = []
for dirpath, dirnames, filenames in os.walk(LOAD_DATA_DIR):
    for file in filenames:
        try:
            loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
            docs.extend(loader.load_and_split())
        except Exception as e:
            pass

# -----------------------------------------------
# テキストの内容を分割する（ドキュメントのチャンク化）
# -----------------------------------------------

text_splitter = CharacterTextSplitter(chunk_size=4000, chunk_overlap=0)
docs = text_splitter.split_documents(docs)

# print(docs[2])

# -----------------------------------------------
# 分割したテキストをベクトルデータストアに格納する（Embeddings を生成する）
# -----------------------------------------------

db = FAISS.from_documents(docs, embedding=OpenAIEmbeddings())
db.save_local(FAISS_DB_DIR)


query = "clapped-audience について簡単に教えて"
docs = db.similarity_search(query)
print(docs[0].page_content)


