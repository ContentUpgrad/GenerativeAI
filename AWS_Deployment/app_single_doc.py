from dotenv import load_dotenv
import os
import openai
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS, Chroma
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

def main():
    filepath = os.getcwd()
    # Read the text file containing the API key
    with open(filepath + "/OpenAI_API_Key.txt", "r") as f:
         openai_api_key = ' '.join(f.readlines())

    # Update the OpenAI API key by updating the environment variable
    os.environ["OPENAI_API_KEY"] = openai_api_key
    openai.api_key = openai_api_key


    # Load a pre-trained OpenAI language model
    llm = OpenAI()

    # Configure the page settings for the Streamlit app
    st.set_page_config(page_title="Chat with PDF")

    # Display the header for the Streamlit app
    st.header("LangChain RAG App")

    # Allow users to upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type="pdf")

    # Check if a PDF file has been uploaded
    if pdf is not None:
        # Read the PDF file and extract text from its pages
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Set up the text splitter for splitting texts into chunkss
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        # Split the extracted text into chunks for efficient processing
        chunks = text_splitter.split_text(text)

        # Create embeddings and build a knowledge base for the chunks.
        embeddings = OpenAIEmbeddings()
        
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # Allow the user to input a question about the PDF
        user_question = st.text_input("Ask a question about your PDF")
        
        # Check if a user question has been entered.
        if user_question:

            # Perform similarity search on the knowledge base using the user's question
            docs = knowledge_base.similarity_search(user_question)

            # Set up a question-answering chain
            chain = load_qa_chain(llm, chain_type="stuff")

            # Generate a response to the user's question using the question-answering chain
            response = chain.run(input_documents=docs, question=user_question)

             # Display the generated response
            st.write(response)


if __name__ == '__main__':
    main()
