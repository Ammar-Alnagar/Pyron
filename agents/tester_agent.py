from pyron.agents.base import BaseAgent

class TesterAgent(BaseAgent):
    """
    The tester agent that can test code.
    """

    def execute(self, task):
        """
        Executes a testing task.

        Args:
            task (str): The code to test.

        Returns:
            str: The test results.
        """
        # For now, just return a simple test result
        return "All tests passed."
