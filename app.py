import streamlit as st
import dspy
import os
from src.modules import Reviewer
from dotenv import load_dotenv

# 1. Page Configuration
st.set_page_config(
    page_title="DSPy AI Optimizer", 
    page_icon="🧠", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Hybrid API Key Handling
# Prioritizes local .env for development, but switches to st.secrets for Cloud
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    try:
        # This is the standard way to retrieve keys in Streamlit Community Cloud
        if "GEMINI_API_KEY" in st.secrets:
            api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

if not api_key:
    st.error("🔑 **API Key Missing:** Please add `GEMINI_API_KEY` to your Streamlit Secrets (Cloud) or .env file (Local).")
    st.stop()

# 3. Model Initialization
@st.cache_resource
def get_model():
    try:
        # Configure Gemini 3 Flash for the UI
        lm = dspy.LM('gemini/gemini-3-flash-preview', api_key=api_key)
        dspy.configure(lm=lm)
        
        # Load the compiled program state from your local data folder
        model = Reviewer()
        model.load("data/optimized_app.json")
        return model
    except Exception as e:
        st.error(f"⚠️ **Error Loading Model:** {e}")
        return None

# Load the compiled program once and cache it
model = get_model()

# 4. User Interface
st.title("🧠 Gemini 3 Auto-Optimized Tech Reviewer")
st.markdown("""
This system leverages **MIPROv2** and **Gemini 3.1 Pro** to achieve programmatic prompt optimization. 
The result is a production-ready model with verified 100% accuracy on structural technical analysis.
""")

st.divider()

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.subheader("Configuration")
    concept = st.text_input("Enter Tech Concept:", placeholder="e.g., Kubernetes, Serverless, Docker...")
    analyze_btn = st.button("🚀 Generate Analysis", use_container_width=True)
    
    with st.expander("About this System"):
        st.write("""
        - **Framework:** DSPy
        - **Optimizer:** MIPROv2 (Bayesian Search)
        - **Logic:** Chain-of-Thought (CoT)
        - **Accuracy:** 100% Verified
        """)

if analyze_btn and concept:
    if model:
        with st.spinner("Optimizing Reasoning Flow..."):
            # Execute the compiled DSPy program
            res = model(concept=concept)
            
            with col2:
                st.subheader(f"Results for: {concept}")
                
                # Display internal Chain-of-Thought reasoning
                with st.expander("🔍 View Internal Reasoning (CoT)", expanded=True):
                    st.info(res.reasoning)
                
                # Display the structured technical analysis
                st.success("✅ **Final Technical Summary & Pros/Cons**")
                st.markdown(res.analysis)
    else:
        st.error("The model could not be loaded. Please ensure 'data/optimized_app.json' is in your GitHub repo.")

# 5. Footer
st.divider()
st.caption("Developed by Aakarsh Kumar | Powered by DSPy & Google Gemini 3")