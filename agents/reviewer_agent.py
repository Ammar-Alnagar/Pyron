from pyron.agents.base import BaseAgent

class ReviewerAgent(BaseAgent):
    """
    The reviewer agent that can review code.
    """

    def execute(self, task):
        """
        Executes a reviewing task.

        Args:
            task (str): The code to review.

        Returns:
            str: The review of the code.
        """
        # For now, just return a simple review
        return "The code looks good."
