import os

import streamlit as st
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()
FAISS_DB_DIR = os.environ["FAISS_DB_DIR"]

MODEL_NAME = "gpt-3.5-turbo"
# MODEL_NAME = "gpt-4"
MODEL_TEMPERATURE = 0.0

st.title("OSS RAG ChatBot")

# メッセージ履歴を保持するリストの定義
if "messages" not in st.session_state:
    st.session_state.messages = []

# メッセージ履歴の表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What's up?"):

	# ユーザーによる質問の保存・表示
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    model = ChatOpenAI(model=MODEL_NAME, temperature=MODEL_TEMPERATURE)
    faiss_db = FAISS.load_local(FAISS_DB_DIR, embeddings=OpenAIEmbeddings())

    # LLMによる回答の生成
    retriever = VectorStoreRetriever(vectorstore=faiss_db)
    qa = RetrievalQA.from_chain_type(llm=model, retriever=retriever)
    query = f"以下の文脈を利用して、最後の質問に答えなさい。答えが分からない場合は、答えを作ろうとせず、分からないと答えてください。:{prompt}"
    res = qa.invoke(query)

    print(res)

    # LLMによる回答の表示
    with st.chat_message("assistant"):
        st.markdown(res["result"])

    # LLMによる回答の保存
    st.session_state.messages.append({"role": "assistant", "content": res["result"]})
