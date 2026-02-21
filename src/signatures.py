import dspy

class TechReview(dspy.Signature):
    """Analyze a technical concept and provide a summary with one pros/cons list."""
    concept = dspy.InputField()
    analysis = dspy.OutputField(desc="A technical summary and a bulleted list of pros/cons")