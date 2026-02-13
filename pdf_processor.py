import fitz  # PyMuPDF
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text_from_pdf(pdf_path):
    
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    doc.close()
    return text

def chunk_text(text, chunk_size=1500, overlap=200):
    
    chunks = []
    start = 0
    text_length = len(text)
    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def create_faiss_index(chunks):
 
    embeddings = embedding_model.encode(chunks, show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def retrieve_relevant_chunks(query, index, chunks, top_k=10):
    
    query_embedding = embedding_model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, top_k)
    return [chunks[i] for i in indices[0]]