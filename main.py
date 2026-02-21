import dspy
import os
from dotenv import load_dotenv
from src.modules import Reviewer

# 1. Initialization
load_dotenv()

# Teacher (Gemini 3.1 Pro): High-intelligence model for instruction proposal
teacher_lm = dspy.LM('gemini/gemini-3.1-pro-preview', api_key=os.getenv("GEMINI_API_KEY"))

# Student (Gemini 3 Flash): Fast model being optimized for production
student_lm = dspy.LM('gemini/gemini-3-flash-preview', 
                     api_key=os.getenv("GEMINI_API_KEY"),
                     thinking_level="low") 

dspy.configure(lm=student_lm)

# 2. Dataset - 4 examples are enough to start, but 10+ is ideal for 95% accuracy
trainset = [
    dspy.Example(concept="Kubernetes", 
                 analysis="Orchestration for containers. Pros: Scaling. Cons: Complexity.").with_inputs('concept'),
    dspy.Example(concept="Docker", 
                 analysis="Container engine. Pros: Portability. Cons: Image management.").with_inputs('concept'),
    dspy.Example(concept="Serverless", 
                 analysis="Event-driven scaling. Pros: Cost-efficient. Cons: Cold starts.").with_inputs('concept'),
    dspy.Example(concept="CI/CD", 
                 analysis="Automated pipelines. Pros: Fast delivery. Cons: Setup time.").with_inputs('concept'),
]

# 3. Success Metric
def accuracy_metric(example, pred, trace=None):
    has_keywords = "pros" in pred.analysis.lower() and "cons" in pred.analysis.lower()
    is_detailed = len(pred.analysis) > 40
    return has_keywords and is_detailed

# 4. FINAL UPGRADE: MIPROv2 Optimizer
from dspy.teleprompt import MIPROv2

# CONFIGURATION: Set 'auto' in the constructor to avoid TypeErrors
optimizer = MIPROv2(
    metric=accuracy_metric, 
    prompt_model=teacher_lm, 
    task_model=student_lm,
    auto="light"  # Use "medium" if you have a higher API quota for even better results
)

print("🚀 Starting MIPROv2 Optimization (Rewriting instructions with Gemini 3.1 Pro)...")

# EXECUTION: Compile the program
compiled_app = optimizer.compile(
    Reviewer(), 
    trainset=trainset,
    max_bootstrapped_demos=3 
)

# 5. Persistence
if not os.path.exists('data'):
    os.makedirs('data')

compiled_app.save("data/optimized_app.json")
print("✅ Project Compiled. Optimized prompts saved to data/optimized_app.json")

# 6. Test with a complex concept
response = compiled_app(concept="Edge Computing")
print(f"\n--- Optimized Analysis ---\n{response.analysis}")

# This prints the last prompt sent to the LLM, including the optimized instructions
student_lm.inspect_history(n=1)