<h1>GEN AI Internship Task</h1>

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
<br>
<li> <b>Requests & Parsing</b> – Sends an HTTP request with a User-Agent and parses the response using BeautifulSoup </li>
<li> <b>Content Extraction</b> – Extracts the title (h1), headings (h2, h3), and paragraphs (p) from Wikipedia’s main content div. </li>
<li> <b>File Writing</b> – Saves the extracted text to a file with structured formatting, underlining headings for clarity. </li>
<li> <b>Error Handling & Execution</b> – Checks response status and runs properly as a standalone script.</li>
<br>
<hr>
<h2>Future Workings</h2>
<p>End-to-End Deployment</p>
<p>Hosting in any cloud service</p>
<br>
<h2>Update 1</h2>
<p>Memory Function implemented. Now it can have memory just like chatgpt corresponding to an individual user id</p>
<p>Streaming of text while the response is generated</p>
<p>Better UI/UX</p>
<br>
<h2>Upcoming possible updates</h2>
<p>Integration of ChatPDF with ChatBOT making it an wholesome application</p>
<p>Better layouts</p>
<p> Working with agents and tools</p>
