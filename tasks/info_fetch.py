from crewai import Task


class InfoTask:
    def __init__(self, agents, output_format):
        self.agent = agents
        self.output_format = output_format

    def task(self):
        info = Task(
            description="Fetch flight details and return structured JSON.",
            expected_output="A JSON response with flight details or an error message.",
            agent=self.agent,
            output_json=self.output_format
        )

        return info

