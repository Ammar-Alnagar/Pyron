from pyron.agents.base import BaseAgent

class MasterAgent(BaseAgent):
    """
    The master agent that supervises other agents.
    """

    def __init__(self, name, tools, subordinate_agents):
        """
        Initializes the master agent.

        Args:
            name (str): The name of the agent.
            tools (list): A list of tools that the agent can use.
            subordinate_agents (list): A list of subordinate agents to supervise.
        """
        super().__init__(name, tools)
        self.subordinate_agents = subordinate_agents

    def execute(self, task):
        """
        Executes a task by delegating it to the appropriate subordinate agent.

        Args:
            task (str): The task to execute.

        Returns:
            str: The result of the task execution.
        """
        # For now, we'll just delegate to the first subordinate agent.
        # In a real implementation, we would have a more sophisticated
        # delegation strategy.
        return self.subordinate_agents[0].execute(task)
