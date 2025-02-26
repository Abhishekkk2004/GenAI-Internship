<h1>GEN AI Internship Task</h1>
<h2> IMPORTANT NOTE REGARDING THE PROJECT </h2>
I am using Ollama based LLM models and Embedding models so the code would learn locally

#  Ollama & Model Setup  

This guide provides instructions to **set up and run Ollama** along with the required models:  

 **nomic-embed-text** (Embedding Model)  
 **llama3.2:3b** (Llama 3.2 - 3B)  
 **deepseek-r1:1.5b** (DeepSeek R1 - 1.5B)  

---

##  Installation & Setup  

###  **1. Install Dependencies**  
Ensure that **Ollama** is installed. If not, download and install it from [Ollama AI](https://ollama.ai).  

---

###  **2. Run the Setup Commands**  

#### 🔹 **Start Ollama & Pull Required Models**  
```sh
ollama serve & ollama pull nomic-embed-text & ollama pull llama3.2:3b & ollama pull deepseek-r1:1.5b

Install Python Dependencies
sh
pip install -r requirements.txt

This will install all necessary Python libraries required for the project.

<h2>OVERVIEW</h2>

<p>This project implements a Text Scraping & RAG pipeline that:</p>

<li> Scrapes text data (e.g., from Wikipedia) </li>
<li> Indexes the text in a vector database (FIASS Vector store) </li>
<li> Implements a retrieval mechanism to fetch relevant content (Using similarity based retrieving method) </li>
<li> Classifies user queries into Reason or Question (Using custom routing between Deepseek r1 and LLama 3.2 LLM )</li>
<li> Generates responses based on retrieved content using an LLM </li>
<hr>

<h2>EXPLAINATION OF EVERY PART </h2>

<h3>Web Scrapping</h3>

<li> <b>Requests & Parsing</b> – Sends an HTTP request with a User-Agent and parses the response using BeautifulSoup </li>
<li> <b>Content Extraction</b> – Uses RecursiveCharacterTextSplitter to divide the text into chunks of 700 characters with 200-character overlap. </li>
<li> <b>File Writing</b> – Saves the extracted text to a file with structured formatting, underlining headings for clarity. </li>
<li> <b>Error Handling & Execution</b> – Checks response status and runs properly as a standalone script.</li>
<hr>
<h3>Vector store and data chunking </h3>

<li> <b>Text Loading & Wrapping</b> – Reads Wikipedia text from a file and wraps it in a Document object for processing. </li>
<li> <b>Text Splitting</b> – Extracts the title (h1), headings (h2, h3), and paragraphs (p) from Wikipedia’s main content div. </li>
<li> <b>FAISS Index Initialization</b> – Creates a FAISS index for vector storage. </li>
<li> <b>Vector Store & Document Addition</b> – Initializes FAISS with an embedding function(nomic-embed-text model) , an in-memory docstore, and adds document chunks to the index. </li>
<hr>
<h3> Making of chains for custom routing</h3>

<li> <b>Classification Step</b> – Uses a prompt template to classify user input as either "Reason" (explanations/justifications) or "Question" (direct inquiries). </li> 
<li> <b>Reason Handling</b> – If classified as "Reason," the input is processed by a DeepSeek-based chain , which acknowledges the reasoning and provides a relevant response. </li> <li> <b>Question Handling</b> – If classified as "Question," the input is processed by a LLama 3.2-based chain , which provides a concise and well-structured answer. </li> 
<li> <b>Routing Logic</b> – Implements a function (`rout`) to dynamically select the appropriate response chain based on classification results. </li>
<hr>

<h3> Final RAG chain implementation </h3>

<li> <b>Document Retrieval</b> – Uses a `vector_store.search` function to retrieve the top 5 most relevant documents based on similarity to the user's question. </li> 
<li> <b>Context Generation</b> – Extracts and combines the content of retrieved documents to provide additional context for answering the question. </li> 
<li> <b>Dynamic Input Processing</b> – Maps `user_input` and `context` dynamically, ensuring that both the original question and retrieved documents are passed to the response chain. </li> 
<li> <b>Seamless Routing</b> – The retrieved context and user input are passed to the `rout` function, which selects the appropriate response chain based on classification. </li>
<hr>
