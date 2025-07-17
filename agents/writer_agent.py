from pyron.agents.base import BaseAgent

class WriterAgent(BaseAgent):
    """
    The writer agent that can write text to files.
    """

    def execute(self, task):
        """
        Executes a writing task.

        Args:
            task (str): A tuple containing the filepath and the content to write.

        Returns:
            str: A message indicating the result of the write operation.
        """
        filepath, content = task
        try:
            with open(filepath, "w") as f:
                f.write(content)
            return f"Successfully wrote to {filepath}."
        except Exception as e:
            return f"Error writing to {filepath}: {e}"
