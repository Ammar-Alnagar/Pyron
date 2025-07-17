from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """
    Base class for all agents in the Pyron framework.
    """

    def __init__(self, name, tools):
        """
        Initializes the agent with a name and a set of tools.

        Args:
            name (str): The name of the agent.
            tools (list): A list of tools that the agent can use.
        """
        self.name = name
        self.tools = tools

    @abstractmethod
    def execute(self, task):
        """
        Executes a task.

        Args:
            task (str): The task to execute.

        Returns:
            str: The result of the task execution.
        """
        pass
