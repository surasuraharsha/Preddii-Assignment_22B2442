# Preddii-Assignment_22B2442

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
To interact with the tool via a friendly web interface:

Export the code: Ensure your logic is saved in a Python file (e.g., app.py) instead of a notebook (.ipynb).

Run the app: Open your terminal in the project folder and type:
```Bash:
streamlit run app.py
```
Use the App:

A new tab will open in your browser (usually at http://localhost:8501).

Upload your PDF via the sidebar.

Type your question in the chat box and get the answer for the queries



##💡 Ideas for Improvement
If you want to take this project from a prototype to a production-ready application, here are the next steps:

1. Better Table Handling
Current Issue: Simple text extraction often mangles tables (rows and columns get mixed up), which are crucial in service manuals for specs like Torque or Pressure.

Solution: Use tools like pdfplumber or Tabula-py to detect and extract tables specifically as structured data.

2. Semantic Chunking
Current Issue: The code cuts text every 1200 characters. This might cut a sentence or a specific instruction in half.

Solution: Use "Recursive Character Text Splitter" (available in libraries like LangChain) to split text by paragraphs or sentences, ensuring that complete ideas stay together.

3. Chat Memory
Current Issue: The bot treats every question as a new one. It doesn't remember what you just asked.

Solution: Implement a conversation history buffer so you can ask follow-up questions (e.g., "What tools do I need for that?").

4. Hybrid Search
Current Issue: Vector search is great for meaning, but sometimes you need exact keyword matches (like searching for a specific Error Code "P0300").

Solution: Combine FAISS (vector search) with BM25 (keyword search) for the most accurate results.

📝 Example Output Format
The system is designed to return data in JSON format for easy integration with other apps:
[
  {
    "component": "Master Cylinder",
    "spec_type": "Torque",
    "value": "15",
    "unit": "Nm"
  }
]

