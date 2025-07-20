from modaic.precompiled_agent import PrecompiledAgent
from config import ExampleConfig
import dspy
from util import print_hi

class Summarize(dspy.Signature):
    question = dspy.InputField()
    context = dspy.InputField()
    answer = dspy.OutputField(desc="Answer to the question, based on the passage")
    
class ExampleAgent(PrecompiledAgent):
    config_class = ExampleConfig
    def __init__(self, config: ExampleConfig, **kwargs):
        super().__init__(config, **kwargs)
        self.predictor = dspy.Predict(Summarize)
        self.predictor.lm = dspy.LM("openai/gpt-4o-mini")

    def forward(self, question: str, context: str) -> str:
        print_hi(question)
        return self.predictor(question=question, context=context)