from typing import Literal
from modaic.precompiled_agent import PrecompiledConfig

class ExampleConfig(PrecompiledConfig):
    agent_type = "ExampleAgent"
    output_type: Literal["bool", "str"]
    
    def __init__(self, output_type: Literal["bool", "str"]):
        self.output_type = output_type