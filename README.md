# Real-Time Flight Tracker using Agentic AI

## ✈️ Overview
This project implements a **Real-Time Flight Tracker** using **Agentic AI with CrewAI framework**. It utilizes two autonomous agents to retrieve flight information and answer user queries with structured, real-time responses.

---

## ⚙️ Core Features
- Retrieves real-time flight details from a predefined database.
- Uses AI agents to process and respond to user queries.
- Structured JSON responses for easy integration.
- Implements CrewAI for agent-based task delegation.
- Natural Language Understanding & Query Resolution.


---

## 🧠 System Architecture

### Agents
1. **InfoAgent** – Retrieves flight details from the `flight_data.json`.
2. **QAAgent** – Interprets natural language questions and invokes InfoAgent.

### Tasks
- `InfoTask`: Executes info fetching logic using the tool.
- `QATask`: Parses the user’s query and delegates to `InfoTask`.

### Tool
- `FlightSearchTool`: Loads and queries flight data from a local JSON file (`data/flight_data.json`).

---

## 🗂️ Project Structure
```
.
├── agents
│   ├── __init__.py
│   ├── info_agent.py
│   └── qa_agent.py
├── data
│   └── flight_data.json
├── tasks
│   ├── __init__.py
│   ├── info_fetch.py
│   └── QA.py
├── tools
│   ├── __init__.py
│   └── flight_search_tool.py
├── .env
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python >= 3.8
- Install dependencies:
```bash
pip install -r requirements.txt
```

### 🧪 Run the System
```bash
python main.py
```

### 🔐 Environment Setup
Create a `.env` file:
```bash
# .env file
GROQ_API_KEY="YOUR_API_KEY"
```

---

## 💬 Example Usage

### Query through Terminal:
```bash
Enter flight number or query: When does flight AI456 depart?
```
Returns:
```json
{
  "answer": "Flight AI456 departs at 10:30 AM to Kolkata. Current status: On Time."
}
```

### Programmatic Usage:
```python
from main import FlightInfoSystem

flight_support = FlightInfoSystem()
response = flight_support.runner("What is the status of flight AI123?")
print(response)
```
Returns:
```json
{
  "answer": "Flight AI123 departs at 08:00 AM to Delhi. Current status: Delayed."
}
```

---




