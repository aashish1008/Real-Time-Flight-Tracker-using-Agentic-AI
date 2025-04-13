from typing import Type, Dict, List
from pydantic import BaseModel, Field
from crewai import Agent


class QAResponse(BaseModel):
    """
    Stores the answer to a user's query regarding flight details.
    """
    answer: str = Field(..., description="Answer to the user's flight-related question")


class QAAgent:
    def __init__(self, llm, tools: List):
        self.llm = llm
        self.tools = tools

    def run_qa_agent(self):
        agent = Agent(
            role="Question Answering Agent",
            goal="Extract flight number from user query and retrieve relevant flight details.",
            verbose=True,
            memory=True,
            llm=self.llm,
            allow_delegation=False,
            backstory="This agent analyzes user queries, identifies flight numbers, and fetches accurate information \n"
                      "using available tools"
        )

        return agent
