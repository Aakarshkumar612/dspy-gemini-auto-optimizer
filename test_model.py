import dspy
import os
from dotenv import load_dotenv
from src.modules import Reviewer

# 1. Setup Environment
load_dotenv()
gemini3 = dspy.LM('gemini/gemini-3-flash-preview', api_key=os.getenv("GEMINI_API_KEY"))
dspy.configure(lm=gemini3)

# 2. Load the Module
model = Reviewer()

# IMPORTANT: Ensure this path matches where main.py saved the file
try:
    model.load("data/optimized_app.json")
    print("✅ Optimized model loaded successfully!\n")
except FileNotFoundError:
    print("❌ Error: 'data/optimized_app.json' not found. Did you run main.py first?")
    exit()

# 3. Run a Test Prediction
prediction = model(concept="Cloud Computing")

print("--- AI ANALYSIS ---")
print(prediction.analysis)
print("-" * 20)

# 4. Inspect the "Secret Sauce"
# This shows exactly what prompt Gemini 3 actually saw
print("\n--- UNDERLYING PROMPT (INSPECT HISTORY) ---")
dspy.inspect_history(n=1)