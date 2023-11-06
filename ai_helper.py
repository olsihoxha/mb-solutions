import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI, HuggingFaceHub
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from queries import create_queried_txt
from constants import OPEN_AI_API_KEY, HUGGING_FACE_API_KEY, EmbeddingType, LlmType

open_ai_llm = OpenAI(temperature=0.5, openai_api_key=OPEN_AI_API_KEY)

os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGING_FACE_API_KEY

falcon_llm = HuggingFaceHub(repo_id="mistralai/Mistral-7B-Instruct-v0.1",
                            model_kwargs={"temperature": 0.5, "max_length": 1000, "max_new_tokens": 16432})


class LlmModel:

    def __init__(self, db_responses, embedding_type=EmbeddingType.HUGGING_FACE):
        self.documents = self._create_docsearch(db_responses, embedding_type)

    @classmethod
    def _create_docsearch(cls, db_responses, embedding_type):
        text_db_resp = create_queried_txt(db_responses)
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=400)
        docs = text_splitter.create_documents(text_db_resp)
        if embedding_type == EmbeddingType.OPEN_AI:
            embeddings = OpenAIEmbeddings(openai_api_key=OPEN_AI_API_KEY)
        else:
            embeddings = HuggingFaceEmbeddings()
        docsearch = FAISS.from_documents(docs, embeddings)
        return docsearch

    def get_ai_response(self,
                        query,
                        llm_type=LlmType.OPEN_AI_LLM):
        docsearch = self.documents
        if llm_type == LlmType.OPEN_AI_LLM:
            llm = open_ai_llm
        else:
            llm = falcon_llm
        qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())
        response = qa.run(query)
        return response
