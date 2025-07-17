import random
from pyron.agents.base import BaseAgent

class JokeAgent(BaseAgent):
    """
    The joke agent that can tell jokes.
    """

    def execute(self, task):
        """
        Executes a joke-telling task.

        Args:
            task (str): The topic of the joke.

        Returns:
            str: A random joke.
        """
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't programmers like nature? It has too many bugs.",
        ]
        return random.choice(jokes)
