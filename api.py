from fastapi import FastAPI
import dspy
from src.modules import Reviewer
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# Load the optimized program once at startup
#
gemini3 = dspy.LM('gemini/gemini-3-flash-preview', api_key=os.getenv("GEMINI_API_KEY"))
dspy.configure(lm=gemini3)

optimized_reviewer = Reviewer()
optimized_reviewer.load("data/optimized_app.json")

@app.get("/review")
def get_review(concept: str):
    # Run the optimized program
    result = optimized_reviewer(concept=concept)
    return {"concept": concept, "analysis": result.analysis}