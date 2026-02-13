# Preddii-Assignment_22B2442

# 🚗 Vehicle Service Manual Assistant (RAG Pipeline)

## 📖 Overview
This project is an AI-powered tool designed to read complex Vehicle Service Manuals (PDFs) and answer technical questions about them.

Instead of manually searching through hundreds of pages for torque specifications or fluid capacities, you can simply ask a question like *"What are the warnings for Master Cylinder Bleeding?"* and the system will retrieve the exact page content and extract the answer.

---

## ⚙️ Installation & Setup

### 1. Install Dependencies
Open your terminal and install the required Python libraries:
```bash
pip install pymupdf sentence-transformers faiss-cpu groq numpy streamlit

2. Setup API Key
You need a Groq API key to run the inference (Llama 3 model).

Get a free API key from the Groq Console.

Note: In a production environment, use environment variables or Streamlit secrets instead of hardcoding the key.

🚀 How to Run
Option A: Run the Jupyter Notebook
Best for experimenting with the logic step-by-step.

Open Predii_(1).ipynb in Jupyter Notebook or Google Colab.

Update the PDF_PATH variable to point to your service manual.

Execute the cells sequentially.

Option B: Run the Streamlit Web UI
Best for interacting with the tool via a user-friendly web interface.

1. Prepare Your Files
Ensure your project folder contains exactly these files:

app.py (Main application logic)

llm_handler.py (Contains the Groq API client - Add your API Key here)

pdf_processor.py (Handles PDF text extraction)

requirements.txt (List of dependencies)

sample-service-manual.pdf (Your source PDF file)

2. Launch the App
Open your terminal in the project folder and run:

streamlit run app.py

3. Access the Interface
A new tab will automatically open in your browser (usually at http://localhost:8501).

📖 User Guide: Using the Web Interface
Once the app is running, follow these steps to get answers from your manual.

1. The Dashboard Layout
The interface is divided into two sections:

Left Sidebar (Document Library): Controls for loading and processing your PDF.

Main Screen: Where you ask questions and view results.

2. Step-by-Step Instructions
Step 1: Load Your Manual
Look at the Left Sidebar under "Document Library".

Use the dropdown menu to Choose a manual (e.g., sample-service-manual.pdf).

Note: The app only detects PDFs placed inside the project folder.

Click the 🚀 Index Manual button.

Wait for the success message. The system is reading and indexing the text.

Step 2: Ask a Question
Go to the main input box labeled "Enter your question".

Type a specific technical question.

Example: "What is the torque of Wheel bearing and wheel hub bolts?"

Example: "What is the fluid capacity for the brake system?"

Press Enter.

Step 3: View Results
The system will display the extracted answers in structured cards:

Torque/Specs: Cards displaying the Value and Unit (e.g., 175 Nm).

Textual Answers: Clear explanations for procedures or warnings.

💡 Pro Tips for Best Results
Be Specific: Instead of asking "brakes", ask "What is the minimum thickness for the front brake pads?"

Check Units: The system often extracts multiple units (e.g., Nm and lb-ft). Check all result cards to find the unit you need.
