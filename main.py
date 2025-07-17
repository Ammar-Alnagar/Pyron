import argparse
from pyron.agents.master_agent import MasterAgent
from pyron.agents.researcher_agent import ResearcherAgent
from pyron.agents.writer_agent import WriterAgent
from pyron.agents.terminal_agent import TerminalAgent
from pyron.agents.refiner_agent import RefinerAgent
from pyron.agents.reviewer_agent import ReviewerAgent
from pyron.agents.tester_agent import TesterAgent
from pyron.agents.joke_agent import JokeAgent
from pyron.agents.status_agent import StatusAgent
from pyron.tools.tools import search_web, write_file, execute_terminal_command, read_file, list_files

def main():
    """
    The main application loop.
    """
    parser = argparse.ArgumentParser(description="Pyron Agentic Pipeline")
    parser.add_argument("task", type=str, help="The task for the agents to perform.")
    args = parser.parse_args()

    # Create the tools
    tools = [
        search_web,
        write_file,
        execute_terminal_command,
        read_file,
        list_files
    ]

    # Create the agents
    researcher = ResearcherAgent("Researcher", tools)
    writer = WriterAgent("Writer", tools)
    terminal = TerminalAgent("Terminal Specialist", tools)
    refiner = RefinerAgent("Refiner", tools)
    reviewer = ReviewerAgent("Reviewer", tools)
    tester = TesterAgent("Tester", tools)
    joke = JokeAgent("Joker", tools)
    status = StatusAgent("Status Reporter", tools)


    # Create the master agent
    master = MasterAgent("Master", tools, [researcher, writer, terminal, refiner, reviewer, tester, joke, status])

    # Execute the task
    result = master.execute(args.task)
    print(result)

if __name__ == "__main__":
    main()
