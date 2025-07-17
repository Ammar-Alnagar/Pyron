import subprocess
from pyron.agents.base import BaseAgent

class TerminalAgent(BaseAgent):
    """
    The terminal agent that can execute shell commands.
    """

    def execute(self, task):
        """
        Executes a shell command.

        Args:
            task (str): The shell command to execute.

        Returns:
            str: The output of the shell command.
        """
        try:
            result = subprocess.run(
                task,
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error executing command: {e}\n{e.stderr}"
