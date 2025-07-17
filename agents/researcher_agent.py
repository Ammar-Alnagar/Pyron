from pyron.agents.base import BaseAgent
from duckduckgo_search import DDGS

class ResearcherAgent(BaseAgent):
    """
    The researcher agent that can search the web.
    """

    def execute(self, task):
        """
        Executes a research task.

        Args:
            task (str): The research task to execute.

        Returns:
            str: The result of the research.
        """
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(task, max_results=5)]
        return str(results)
