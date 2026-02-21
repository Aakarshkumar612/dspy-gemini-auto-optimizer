import dspy
import os
from dotenv import load_dotenv
from src.modules import Reviewer
from dspy.evaluate import Evaluate

# Load environment variables
load_dotenv()

# 1. Setup - Configure Gemini 3 Flash
# Flash is perfect for high-speed batch evaluation
gemini3 = dspy.LM('gemini/gemini-3-flash-preview', api_key=os.getenv("GEMINI_API_KEY"))
dspy.configure(lm=gemini3)

# 2. Load your Optimized Program
trained_reviewer = Reviewer()
try:
    trained_reviewer.load("data/optimized_app.json")
    print("✅ Optimized program loaded successfully.")
except FileNotFoundError:
    print("❌ Error: 'data/optimized_app.json' not found. Run main.py first.")
    exit()

# 3. Comprehensive Test Set
# Expanded to ensure the model generalizes across hardware, software, and systems
testset = [
    dspy.Example(concept="React.js", analysis="Pros: Virtual DOM. Cons: JSX learning curve.").with_inputs('concept'),
    dspy.Example(concept="PostgreSQL", analysis="Pros: ACID compliance. Cons: Complex scaling.").with_inputs('concept'),
    dspy.Example(concept="FastAPI", analysis="Pros: High performance. Cons: Smaller community than Flask.").with_inputs('concept'),
    dspy.Example(concept="Terraform", analysis="Pros: IaC. Cons: State file management.").with_inputs('concept'),
    dspy.Example(concept="Redis", analysis="Pros: Speed. Cons: Data persistence limits.").with_inputs('concept'),
    dspy.Example(concept="GraphQL", analysis="Pros: Efficiency. Cons: Caching complexity.").with_inputs('concept'),
    dspy.Example(concept="PyTorch", analysis="Pros: Dynamic graphs. Cons: Memory usage.").with_inputs('concept'),
    dspy.Example(concept="Kafka", analysis="Pros: Throughput. Cons: Management overhead.").with_inputs('concept'),
    dspy.Example(concept="Edge Computing", analysis="Pros: Low latency. Cons: Security distributed.").with_inputs('concept'),
    dspy.Example(concept="Blockchain", analysis="Pros: Trustless. Cons: Scalability issues.").with_inputs('concept')
]

# 4. Final Enhanced Metric
# We now verify that the model actually "thinks" (CoT) and provides technical depth
def accuracy_metric(example, pred, trace=None):
    # Rule 1: Structural Keywords
    has_pros = "pros" in pred.analysis.lower()
    has_cons = "cons" in pred.analysis.lower()
    
    # Rule 2: Technical Substantiality (Must be detailed, not just a sentence)
    is_substantial = len(pred.analysis) > 100
    
    # Rule 3: Chain of Thought Verification
    # Checks if the AI generated a reasoning field as we saw in the test
    has_reasoning = hasattr(pred, 'reasoning') and len(pred.reasoning) > 50
    
    return has_pros and has_cons and is_substantial and has_reasoning

# 5. Run Evaluator
# [Image of a multi-threaded evaluation process workflow]
evaluator = Evaluate(
    devset=testset, 
    num_threads=4, 
    display_progress=True, 
    display_table=True
)

print("\n🚀 Starting Professional Evaluation on Gemini 3...")
score = evaluator(trained_reviewer, metric=accuracy_metric)

print(f"\n" + "="*40)
print(f"🏆 FINAL PROJECT ACCURACY SCORE: {score}%")
print("="*40)