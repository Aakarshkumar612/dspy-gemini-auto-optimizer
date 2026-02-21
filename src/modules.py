import dspy
from .signatures import TechReview

class Reviewer(dspy.Module):
    def __init__(self):
        super().__init__()
        # ChainOfThought forces the model to explain its reasoning first
        self.analyze = dspy.ChainOfThought(TechReview)

    def forward(self, concept):
        return self.analyze(concept=concept)