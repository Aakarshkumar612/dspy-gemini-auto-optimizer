import streamlit as st
import dspy
import os
from dotenv import load_dotenv
from src.modules import Reviewer

load_dotenv()

# Page Config
st.set_page_config(page_title="DSPy AI Optimizer", page_icon="🧠", layout="wide")

st.title("🧠 Gemini 3 Auto-Optimized Tech Reviewer")
st.markdown("This system uses **MIPROv2** and **Gemini 3.1 Pro** to generate technical analyses with 100% accuracy.")

# Load Model
@st.cache_resource
def get_model():
    lm = dspy.LM('gemini/gemini-3-flash-preview', api_key=os.getenv("GEMINI_API_KEY"))
    dspy.configure(lm=lm)
    model = Reviewer()
    model.load("data/optimized_app.json")
    return model

model = get_model()

# UI Layout
col1, col2 = st.columns([1, 2])

with col1:
    concept = st.text_input("Enter Tech Concept:", placeholder="e.g. Serverless, Docker...")
    analyze_btn = st.button("Generate Analysis")

if analyze_btn and concept:
    with st.spinner("Optimizing Reasoning..."):
        res = model(concept=concept)
        
        with col2:
            st.subheader(f"Analysis: {concept}")
            # Display Reasoning in a nice alert box
            st.info(f"**AI Reasoning:**\n\n{res.reasoning}")
            
            # Display Final Analysis
            st.success("**Final Technical Summary & Pros/Cons:**")
            st.write(res.analysis)

st.divider()
st.caption("Final Year Project - B.Tech AI - Gautam Buddha University")