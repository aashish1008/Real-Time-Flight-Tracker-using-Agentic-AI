from crewai import Task


class QATask:
    def __init__(self, agents, output_format):
        self.agent = agents
        self.output_format = output_format

    def task(self):
        qa = Task(
            description="Interpret user query, call Flight Information Retriever, and format response.",
            expected_output=(
                "A JSON response with complete flight details in detailed format like: "
                "Flight AI123 departs at 08:00 AM to Delhi. Current status: Delayed. "
                "or an error message."
            ),
            agent=self.agent,
            output_json=self.output_format
        )

        return qa
