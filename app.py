import streamlit as st
import os
import json
from pdf_processor import extract_text_from_pdf, chunk_text, create_faiss_index, retrieve_relevant_chunks
from llm_handler import extract_vehicle_specs

st.set_page_config(page_title="Vehicle Spec Assistant", layout="wide", page_icon="🔧")


st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    
    /* Styles the Metric Card container */
    [data-testid="stMetric"] {
        background-color: #ffffff;
        padding: 5px 15px; /* Reduced padding to make boxes smaller */
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border: 1px solid #ddd;
    }
    
    /* Forces metric labels and values to be dark and readable */
    [data-testid="stMetricLabel"] {
        color: #333333 !important;
        font-size: 0.85rem !important;
    }
    [data-testid="stMetricValue"] {
        color: #000000 !important;
        font-size: 1.5rem !important; /* Smaller font size for the value */
    }

    .spec-container {
        background: white;
        padding: 10px;
        border-radius: 5px;
        border-left: 4px solid #007bff;
        margin-bottom: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔧 Vehicle Service Manual Assistant")
st.info("Ask about torque specs, capacities, or procedures. The results will be extracted directly from your PDF.")


with st.sidebar:
    st.header("📂 Document Library")
    local_pdfs = [f for f in os.listdir('.') if f.endswith('.pdf')]
    
    if not local_pdfs:
        st.error("No PDF files found.")
        selected_pdf = None
    else:
        selected_pdf = st.selectbox("Choose a manual:", local_pdfs)
    
    process_button = st.button("🚀 Index Manual", use_container_width=True)


if "index" not in st.session_state:
    st.session_state.index = None
    st.session_state.chunks = None

if process_button and selected_pdf:
    with st.spinner(f"Processing {selected_pdf}..."):
        raw_text = extract_text_from_pdf(selected_pdf)
        chunks = chunk_text(raw_text)
        index = create_faiss_index(chunks)
        st.session_state.index = index
        st.session_state.chunks = chunks
        st.success("Indexing Complete!")


query = st.text_input("Enter your question:", placeholder="e.g., What is the oil capacity?")

if query:
    if st.session_state.index is None:
        st.warning("Please index a manual first.")
    else:
        with st.spinner("Searching manual..."):
            retrieved = retrieve_relevant_chunks(query, st.session_state.index, st.session_state.chunks)
            context = " ".join(retrieved)[:6000]
            raw_output = extract_vehicle_specs(context, query)
            
            try:

                data = json.loads(raw_output)
                
                if not data:
                    st.warning("No specific information found in the manual for this query.")
                else:
                    st.subheader("Results")
                    
                    
                    for item in data:
                        if "Answer" in item:
                            st.markdown(f"### 📝 Explanation\n{item['Answer']}")
                        
                        elif "value" in item or "Range" in item:
                            col1, col2 = st.columns([1, 3])
                            with col1:
                                val = item.get("value") or item.get("Range")
                                unit = item.get("unit", "")
                                st.metric(label=item.get("spec_type", "Specification"), value=f"{val} {unit}")
                            with col2:
                                st.markdown(f"**Component:** {item.get('component', 'General')}")
                                st.markdown("---")
                        
                        else:
                            
                            st.info(f"**{item.get('spec_type', 'Info')}:** {item.get('value', 'N/A')} (Component: {item.get('component', 'N/A')})")

            except json.JSONDecodeError:
              
                st.subheader("Manual Extract")
                st.write(raw_output)


st.divider()
st.caption("Powered by Llama-3.1 & FAISS Vector Search")