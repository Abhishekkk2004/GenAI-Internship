
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter  # Changed from langchain_text_splitters
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers.ensemble import EnsembleRetriever
from langchain_core.prompts import PromptTemplate  # Changed from langchain.prompts
from langchain_core.runnables import RunnablePassthrough  # Changed from langchain.schema.runnable
from langchain_core.output_parsers import StrOutputParser  # Changed from langchain.output_parsers
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

# Initialize embeddings and LLM
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
llm1 = ChatGoogleGenerativeAI(model="models/gemini-1.5-pro")

# Load the PDF documents and create embeddings
def load_and_embed_pdfs(pdf_folder_path):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=200)
    all_chunks = []

    for filename in os.listdir(pdf_folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder_path, filename)
            print(f"Processing: {filename}")
            
            loader = PyPDFLoader(pdf_path)
            pdf_documents = loader.load()
            pdf_chunks = text_splitter.split_documents(pdf_documents)
            all_chunks.extend(pdf_chunks)

    print(f"Total chunks created: {len(all_chunks)}")

    # Create FAISS vector store
    vector_store = FAISS.from_documents(all_chunks, embeddings)
    
    # Create retrievers
    vector_retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})
    bm25_retriever = BM25Retriever.from_documents(all_chunks)
    bm25_retriever.k = 5
    
    ensemble_retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, vector_retriever],
        weights=[0.5, 0.5]
    )

    return ensemble_retriever, vector_store

# Load retriever and vector store
pdf_folder_path = "/Users/abhishek/Desktop/ML/GenAI copy/Dataset"
ensemble_retriever, vector_store = load_and_embed_pdfs(pdf_folder_path)

# Define the prompt
document_prompt = PromptTemplate.from_template("""Give a assessment based on {question} and {context}
                                               A score closer to 1/10 would mean Strong NO and a  A score closer to 10/10 would mean Strong Yes and
                                               in middle indicate a spectrum
                                               You are a doctor helping assistant and based on that provide an assessment result
                                               First identify at what extent the person is dyslexic, and then provide some advice.Answer in very brief.Take reference from {context}
""")

# Define RAG pipeline
rag_chain = (
    {
        "context": ensemble_retriever | (lambda docs: "\n\n".join([doc.page_content for doc in docs])),
        "question": RunnablePassthrough()
    } 
    | document_prompt 
    | llm1 
    | StrOutputParser()
)

# Function to get response from RAG pipeline
def get_rag_response(question):
    # Ensure question is a string, not a dictionary
    if isinstance(question, dict):
        question = question.get("question", "")
    return rag_chain.invoke(question)  # Pass the string directly, not a dictionary
