# Predii-Assignment_22B2442

# 🚗 Vehicle Service Manual Assistant (RAG Pipeline)

## 📖 Overview
This project is an AI-powered tool designed to read complex Vehicle Service Manuals (PDFs) and answer technical questions about them.

Instead of manually searching through hundreds of pages for torque specifications, fluid capacities, or warning labels, you can simply ask a question like *"What are the warnings for Master Cylinder Bleeding?"* and the system will retrieve the exact page content and extract the answer in a structured format.

## ⚙️ How It Works (The Design)
This tool uses a technique called **RAG (Retrieval-Augmented Generation)**. Think of it as an "open-book exam" for AI:

1.  **Reading:** It opens the PDF and extracts all the text using PyMuPDF.
2.  **Chunking:** It breaks the massive text into smaller, manageable pieces (chunks).
3.  **Indexing (The "Brain"):** It converts these text chunks into numbers (vectors) that represent their meaning. This allows the system to understand that "brakes" and "stopping" are related concepts.
4.  **Retrieval:** When you ask a question, the system searches its index to find only the most relevant chunks of text.
5.  **Answering:** It sends your question + the relevant text to a powerful AI model (Llama 3 via Groq), which reads the context and writes a precise answer.

<img width="1919" height="925" alt="demo_torque" src="https://github.com/user-attachments/assets/87e46fbc-1ac2-4f95-aa1a-fbe0d2265c51" />


## 🛠️ Tools & Technologies Used

* **[Streamlit](https://streamlit.io/):** For the user interface (Web App).
* **[PyMuPDF (fitz)](https://pymupdf.readthedocs.io/):** Used to open the PDF file and scrape the raw text from every page.
* **[Sentence-Transformers](https://www.sbert.net/):** Specifically the `all-MiniLM-L6-v2` model. This turns text into numerical embeddings (vectors) so the computer can compare meanings.
* **[FAISS (Facebook AI Similarity Search)](https://github.com/facebookresearch/faiss):** A super-fast library for searching through those embeddings to find the right information instantly.
* **[Groq API](https://groq.com/):** Provides access to the **Llama 3.1** Large Language Model (LLM). Groq is used here because it offers incredibly fast inference speeds, making the chat feel real-time.

---

## 🚀 How to Run

### 1. Install Dependencies
Open your terminal and install the required Python libraries:
```bash
pip install pymupdf sentence-transformers faiss-cpu groq numpy streamlit 
```
2. Setup API Key
You will need a Groq API key to run the inference.

Get a free API key from Groq Console.

Note: In the production app, do not hardcode the key. Use an environment variable or Streamlit secrets.

##  Option A: Run the Jupyter Notebook
If you want to experiment with the code logic step-by-step:

Open Predii_(1).ipynb in Jupyter Notebook or Google Colab.

Update the PDF_PATH variable to point to your service manual.

Execute the cells sequentially.

## Option B: Run the Streamlit Web UI


## 📂 Step 1: Project Setup (Create the Files)
Since this project runs locally, you need to create a folder (e.g., `Vehicle_Manual_App`) and create the following **4 files** inside it.

### 1. `requirements.txt`
Create a file named `requirements.txt` and paste this content:
```text
pymupdf
sentence-transformers
faiss-cpu
groq
numpy
streamlit
```
2. pdf_processor.py
Download a file named pdf_processor.py from above and paste in the Python logic that handles PDF reading and FAISS indexing (provided in the code steps).

3. llm_handler.py
Download a file named llm_handler.py from above and paste the Groq/Llama 3 connection logic.

4. app.py
Download a file named app.py from above and paste the main Streamlit interface code.

Note: Also, place your PDF file (e.g., sample-service-manual.pdf) inside this same folder.

⚙️ Step 2: Installation
Open your terminal (Command Prompt), navigate to this folder, and run the following command to install the necessary libraries:
```bash
pip install -r requirements.txt
```
🚀 Step 3: How to Run
To start the web interface, run this command in your terminal:

Bash
```
streamlit run app.py
```
A new tab will automatically open in your web browser (usually at http://localhost:8501).

Step 4: User Guide
1. Configure the App
API Key: On the left sidebar, paste your Groq API Key (starts with gsk_...).

Upload: Click "Browse files" and select your service manual PDF.

Index: Click the "🚀 Index Manual" button and wait for the "Success" message.

2. Ask Questions
Go to the main chat box in the center of the screen.

Type questions like:

"What is the torque for the front wheel hub?"

"What is the part number of Shock absorber lower nut ?"

The AI will search the PDF and give you a specific answer based only on the manual's content.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 💡 Roadmap & Ideas for Improvement

This project is a solid prototype, but Vehicle Service Manuals are complex documents. To turn this into a production-grade tool, here are the recommended improvements:

### 1. Advanced Table Extraction
* **The Problem:** Service manuals contain critical data in tables (e.g., Torque Specifications, Oil Capacities). Standard text extraction often scrambles rows and columns, making it hard for the AI to associate a value (e.g., "15 Nm") with the correct component.
* **The Solution:** Integrate libraries like **`pdfplumber`** or **`Camelot`**. These tools detect grid lines in PDFs and extract tables as structured data (JSON/CSV) rather than raw text, ensuring the AI reads the exact row-column relationship.

### 2. Hybrid Search (Keyword + Vector)
* **The Problem:** Vector search (FAISS) is great for concepts (e.g., "How to fix brakes"), but sometimes struggles with exact identifiers like **Error Codes (P0300)** or **Part Numbers**.
* **The Solution:** Implement **Hybrid Search**. Combine the semantic power of FAISS with a keyword-based search engine (like **BM25**). This ensures that when a user searches for a specific code, the system finds that exact match first.

### 3. Conversational Memory
* **The Problem:** Currently, the bot treats every question as a standalone event. If you ask "How do I remove the alternator?" and then ask "What tools do I need for *that*?", the bot won't know what "that" refers to.
* **The Solution:** Use **LangChain's memory modules** to store the chat history. Pass the previous 2-3 exchanges to the LLM so it understands context and follow-up questions.

### 4. Source Citations & Page References
* **The Problem:** The user has to trust the AI blindly.
* **The Solution:** Modify the metadata to include page numbers during the indexing phase. When the AI provides an answer, have it return the specific **Page Number** (e.g., *"Source: Page 42, Section 3.1"*) so the mechanic can verify the information.

### 5. Multi-Modal Analysis (Reading Diagrams)
* **The Problem:** Much of a service manual is visual—wiring diagrams, exploded views of engine assembly, etc. Text-only models miss this.
* **The Solution:** Upgrade to a Multi-Modal model (like **Llama 3.2 Vision** or **GPT-4o**). This would allow users to upload a photo of a broken part and ask, *"What is this part, and how do I replace it based on the manual?"*
