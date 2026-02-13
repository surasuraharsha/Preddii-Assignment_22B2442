# Preddii-Assignment_22B2442

# 🚗 Vehicle Service Manual Assistant (RAG Pipeline)

##  Overview
This project is an AI-powered tool designed to read complex Vehicle Service Manuals (PDFs) and answer technical questions about them.

Instead of manually searching through hundreds of pages for torque specifications, fluid capacities, or warning labels, you can simply ask a question like *"What are the warnings for Master Cylinder Bleeding?"* and the system will retrieve the exact page content and extract the answer in a structured format.

##  How It Works (The Design)
This tool uses a technique called **RAG (Retrieval-Augmented Generation)**. Think of it as an "open-book exam" for AI:

1.  **Reading:** It opens the PDF and extracts all the text using PyMuPDF.
2.  **Chunking:** It breaks the massive text into smaller, manageable pieces (chunks).
3.  **Indexing (The "Brain"):** It converts these text chunks into numbers (vectors) that represent their meaning. This allows the system to understand that "brakes" and "stopping" are related concepts.
4.  **Retrieval:** When you ask a question, the system searches its index to find only the most relevant chunks of text.
5.  **Answering:** It sends your question + the relevant text to a powerful AI model (Llama 3 via Groq), which reads the context and writes a precise answer.

##   Tools & Technologies Used

* **[Streamlit](https://streamlit.io/):** For the user interface (Web App).
* **[PyMuPDF (fitz)](https://pymupdf.readthedocs.io/):** Used to open the PDF file and scrape the raw text from every page.
* **[Sentence-Transformers](https://www.sbert.net/):** Specifically the `all-MiniLM-L6-v2` model. This turns text into numerical embeddings (vectors) so the computer can compare meanings.
* **[FAISS (Facebook AI Similarity Search)](https://github.com/facebookresearch/faiss):** A super-fast library for searching through those embeddings to find the right information instantly.
* **[Groq API](https://groq.com/):** Provides access to the **Llama 3.1** Large Language Model (LLM). Groq is used here because it offers incredibly fast inference speeds, making the chat feel real-time.

---

##   How to Run this model

### 1. Install Dependencies
Open your terminal and install the required Python libraries:
```bash
pip install pymupdf sentence-transformers faiss-cpu groq numpy streamlit


Setup API Key

You will need a Groq API key to run the inference.

Get a free API key from Groq Console.

Note: In the production app, do not hardcode the key. Use an environment variable or Streamlit secrets.

3. ***Option A***
Run the Jupyter Notebook
If you want to experiment with the code logic step-by-step:

Open Predii_(1).ipynb in Jupyter Notebook or Google Colab.

Update the PDF_PATH variable to point to your service manual.

Execute the cells sequentially.

4. ***Option B***
Run the Streamlit Web UI
To interact with the tool via a friendly web interface:

Export the code: Ensure your logic is saved in a Python file (e.g., app.py) instead of a notebook (.ipynb).

Ensure that there are 3 .py files and txt file:
1.app.py
2.llm_handler.py  (Add the groq API key in client)
3.pdf_processor.py
4.requirements.txt

Note: Also add the sample-service-manual.pdf in your python folder

Run the app: Open your terminal in the project folder and type:

Bash
streamlit run app.py
Use the App:

A new tab will open in your browser (usually at http://localhost:8501).

# 📖 User Guide: Using the Web Interface

Once you have launched the application using `streamlit run app.py`, follow these steps to get answers from your service manual.

### 1. The Dashboard Layout
The interface is divided into two main sections:
* **Left Sidebar (Document Library):** Controls for loading and processing your PDF.
* **Main Screen:** Where you ask questions and view the results.

### 2. Step-by-Step Instructions

#### Step 1: Load Your Manual
1.  Look at the **left sidebar** under the "Document Library" section.
2.  Use the dropdown menu to **Choose a manual** (e.g., `sample-service-manual.pdf`).
    * *Note: Ensure your PDF files are placed in the project folder so the app can detect them.*
3.  Click the **🚀 Index Manual** button.
    * **Wait** for a moment while the system reads and processes the file. You will see a success message once the manual is ready for questioning.

#### Step 2: Ask a Question
1.  Go to the main input box labeled **"Enter your question"**.
2.  Type a specific technical question.
    * *Example:* `"What is the torque of Wheel bearing and wheel hub bolts?"`
    * *Example:* `"What is the fluid capacity for the brake system?"`
3.  Press **Enter**.

#### Step 3: View Results
The system will search the manual and display the extracted answers in structured cards below the "Results" header.

* **Torque/Specs:** You will see clear cards displaying the **Value** and **Unit** (e.g., `175 Nm` or `129 lb-ft`) alongside the specific component name.
* **Textual Answers:** If you asked for a procedure or warning, the text will be displayed in a readable format.

---

### 💡 Pro Tips for Best Results
* **Be Specific:** Instead of asking "brakes", ask "What is the minimum thickness for the front brake pads?".
* **Check Units:** The system often extracts multiple units (Nm and lb-ft) separately. Look at all the result cards to find the unit you need.
