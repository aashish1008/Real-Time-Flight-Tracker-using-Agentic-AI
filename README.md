# Two-Agent System with Function Calling & Structured Output 

## Overview
This project is a **Two-Agent System with Function Calling & Structured Output** that provides real-time flight details based on user queries. It leverages the **CrewAI framework** to create AI-driven agents that process flight information requests and return structured responses. The system includes two main agents:

1. **Flight Information Retriever**: Fetches flight details based on a provided flight number.
2. **Question Answering Agent**: Interprets user queries, extracts flight numbers, and fetches relevant flight information.

## Features
- Retrieves real-time flight details from a predefined database.
- Uses AI agents to process and respond to user queries.
- Structured JSON responses for easy integration.
- Implements **CrewAI** for agent-based task delegation.
- Supports natural language queries.

---

## Installation
### Prerequisites
Ensure you have Python **3.8+** installed. Install the required dependencies using the following command:

```sh
pip install -r requirements.txt
```

---

## Environment Variables
This project uses a `.env` file to store environment variables. Create a `.env` file in the project directory and add any necessary variables.

```sh
# Example .env file
API_KEY=your_api_key_here
```

**Note**: Modify the `.env` file according to your requirements.

---

## Project Structure
```sh
.
├── agent_system.py               # Main script to run the system
├── .env                  # Environment variables
├── requirements.txt       # Required dependencies
└── README.md             # Documentation
```

---

## How It Works
### Agents
The system consists of two AI agents:

1. **Info Agent (`info_agent`)**
   - Fetches flight details based on a given flight number.
   - Uses the `FlightSearchTool` to search for flight details.

2. **QA Agent (`qa_agent`)**
   - Extracts the flight number from a user query.
   - Delegates the request to `info_agent` to fetch details.

### Tasks
- **Info Task (`info_task`)**: Retrieves structured flight details.
- **QA Task (`qa_task`)**: Processes user queries and formats responses.

### Flight Database
A sample database (`db_flight_data`) is preloaded with flight information:

```python
{
    "AI123": {"flight_number": "AI123", "departure_time": "08:00 AM", "destination": "Delhi", "status": "Delayed"},
    "AI456": {"flight_number": "AI456", "departure_time": "10:30 AM", "destination": "Kolkata", "status": "On Time"}
}
```

---

## Usage
### Running the Script
Run the script to test the flight retrieval system:

```sh
python agent_system.py
```

### Example Queries
#### Fetch Flight Information by Flight Number
```python
print(get_flight_info("AI123"))
```
**Output:**
```json
{
    "flight_number": "AI123",
    "departure_time": "08:00 AM",
    "destination": "Delhi",
    "status": "Delayed"
}
```

#### Retrieve Flight Info Using Agents
```python
print(info_agent_request("AI123"))
```
**Output:**
```json
{
    "flight_number": "AI123",
    "departure_time": "08:00 AM",
    "destination": "Delhi",
    "status": "Delayed"
}
```

#### Process User Query
```python
qa_agent_respond("When does Flight AI123 depart?")
qa_agent_respond("What is the status of Flight AI999?")
```
**Output:**
```json
{"answer": "Flight AI123 departs at 08:00 AM to Delhi. Current status: Delayed."}
```
```json
{"answer": "Flight AI999 not found in database"}
```


---

## Contact
For any questions or contributions, feel free to reach out!

