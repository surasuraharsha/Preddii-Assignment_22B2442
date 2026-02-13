# Preddii-Assignment_22B2442

# 🚗 Vehicle Service Manual Assistant (RAG Pipeline)

## 📖 Overview
This project is an AI-powered tool designed to read complex Vehicle Service Manuals (PDFs) and answer technical questions about them.

Instead of manually searching through hundreds of pages for torque specifications or fluid capacities, you can simply ask a question like *"What are the warnings for Master Cylinder Bleeding?"* and the system will retrieve the exact page content.

---

## ⚙️ Architecture & Design
This tool uses a technique called **RAG (Retrieval-Augmented Generation)**:
1.  **Reading:** Extracts text from PDFs using **PyMuPDF**.
2.  **Indexing:** Converts text into numerical vectors using **Sentence-Transformers**.
3.  **Retrieval:** Searches for relevant info using **FAISS** (Facebook AI Similarity Search).
4.  **Generation:** Sends the context to **Llama 3** (via Groq API) to generate a structured answer.

---

## 🛠️ Installation & Setup

### 1. Install Dependencies
Open your **terminal** and install the required Python libraries:

pip install pymupdf sentence-transformers faiss-cpu groq numpy streamlit


2. Setup API Key
You need a Groq API key to run the inference.

Get a free API key from the Groq Console.

Note: In a production environment, use environment variables or Streamlit secrets instead of hardcoding the key.



📂 Project Structure
Ensure your project folder contains exactly these files before running:

📄 app.py (Main application logic)

📄 llm_handler.py (Contains the Groq API client - Add your API Key here)

📄 pdf_processor.py (Handles PDF text extraction)

📄 requirements.txt (List of dependencies)

📕 sample-service-manual.pdf (Your source PDF file)

🚀 How to Run
You have two ways to use this tool:

🅰️ Option A: Run the Jupyter Notebook
Best for experimenting with the code logic step-by-step.

Open Predii_(1).ipynb in Jupyter Notebook or Google Colab.

Update the PDF_PATH variable to point to your service manual file.

Execute the cells sequentially.

🅱️ Option B: Run the Streamlit Web UI (Recommended)
Best for interacting with the tool via a user-friendly web interface.

Open your terminal inside the project folder.

Run the following command:

Bash
streamlit run app.py
A new tab will automatically open in your browser (usually at http://localhost:8501).

📖 User Guide: Using the Web Interface
Once the app is running, follow these steps to get answers.

1. The Dashboard Layout
Left Sidebar: The "Document Library" where you load your PDF.

Main Screen: The Chat Interface where you ask questions.

2. Step-by-Step Instructions
Step 1: Load Your Manual
Look at the Left Sidebar under "Document Library".

Use the dropdown menu to Choose a manual (e.g., sample-service-manual.pdf).

Click the 🚀 Index Manual button.

Wait for the success message. The system is now reading and indexing your file.

Step 2: Ask a Question
Go to the main input box labeled "Enter your question".

Type a specific technical question.

Example: "What is the torque of Wheel bearing and wheel hub bolts?"

Example: "What is the fluid capacity for the brake system?"

Press Enter.

Step 3: View Results
The system will display the extracted answers in structured cards:

Torque/Specs: Look for the Value and Unit (e.g., 175 Nm).

Textual Answers: Clear explanations for procedures or warnings.

💡 Pro Tips for Best Results
Be Specific: Instead of asking "brakes", ask "What is the minimum thickness for the front brake pads?"

Check Units: The system often extracts multiple units (e.g., Nm and lb-ft). Check all result cards to find the unit you need.
