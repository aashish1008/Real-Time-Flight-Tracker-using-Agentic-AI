from agents.info_agent import InfoAgent, InfoResponse
from agents.qa_agent import QAAgent, QAResponse
from tasks.info_fetch import InfoTask
from tasks.QA import QATask
from tools.flight_search_tool import FlightSearchTool
from crewai import LLM, Crew, Process
from dotenv import load_dotenv

load_dotenv()


class FlightInfoSystem:
    def __init__(self):
        self.tools = [FlightSearchTool()]
        self.llm = LLM(
            model="groq/qwen-2.5-32b",
            temperature=0.6,
        )

        self.info_agent = InfoAgent(self.llm, self.tools).run_info_agent()
        self.info_output = InfoResponse
        self.info_task = InfoTask(self.info_agent, self.info_output).task()

        self.qa_agent = QAAgent(self.llm, self.tools).run_qa_agent()
        self.qa_output = QAResponse
        self.qa_task = QATask(self.info_agent, self.qa_output).task()

    def runner(self, user_query: str):
        crew = Crew(
            agents=[self.info_agent, self.qa_agent],
            tasks=[self.info_task, self.qa_task],
            process=Process.sequential,
            verbose=True
        )

        results = crew.kickoff(
            inputs={"flight_number": user_query}
        )

        return results


if __name__ == "__main__":
    flight_support = FlightInfoSystem()
    print("What can I help you with? (Type 'exit' to quit)")

    while True:
        queries = input("Enter flight number or query: ")

        # Exit the loop if the user types 'exit'
        if queries.lower() == 'exit':
            print("Thank you for using the Flight Info System. Goodbye!")
            break

        # Process the query and display the results
        results = flight_support.runner(queries)
        print(f"Results: {results}\n")

