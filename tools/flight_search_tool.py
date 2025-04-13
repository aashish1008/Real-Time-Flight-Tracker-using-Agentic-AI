from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type, Dict
import json
import os

# Get the path relative to the current file's directory
file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'flight_data.json')

# Load the JSON data
with open(file_path, 'r') as file:
    flight_data = json.load(file)


class FlightSearchInput(BaseModel):
    """.
    Requires a flight number to search for relevant flight details.
    """
    flight_number: str = Field(..., description="Flight number to search for.")


class FlightSearchTool(BaseTool):
    """
    Tool for searching flight details based on the flight number.
    Retrieves information from a predefined flight database.
    """
    name: str = "Flight Search Tool"
    description: str = "Searches for flight details based on flight number."
    args_schema: Type[BaseModel] = FlightSearchInput

    def _run(self, flight_number: str) -> Dict[str, str]:
        """
        Returns the flight information if found, otherwise returns an error message.
        """
        return flight_data.get(flight_number, {"error": f"Flight Number {flight_number} not found in database"})
