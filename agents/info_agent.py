from typing import List
from pydantic import BaseModel, Field
from crewai import Agent


class InfoResponse(BaseModel):
    """
    Represents details of a flight, including flight number, departure time, destination, and status.
    """
    flight_number: str = Field(..., description="Unique identifier for the flight")
    departure_time: str = Field(..., description="Scheduled departure time of the flight")
    destination: str = Field(..., description="Destination airport/city of the flight")
    status: str = Field(..., description="Current status of the flight (e.g., On-Time, Delayed)")


class InfoAgent:
    def __init__(self, llm, tools: List):
        self.llm = llm
        self.tools = tools

    def run_info_agent(self):
        agent = Agent(
            role="Flight Information Retriever",
            goal="Retrieve flight details for a given {flight_number} and return it in structured JSON format.",
            verbose=True,
            memory=True,
            llm=self.llm,
            tools=self.tools,
            allow_delegation=True,
            backstory="This agent is specialized in querying flight databases and presenting accurate, structured \n"
                      "flight information."
        )

        return agent
