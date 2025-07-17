# Pyron: An Agentic Pipeline Framework

Pyron is a Python-based agentic pipeline framework that allows a team of AI agents to work together to complete tasks. It is built using the Google Agents Development Kit and is designed to be easily extensible.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Pyron provides a simple yet powerful framework for creating and managing a team of AI agents. The core idea is to have a "master" agent that supervises a team of "subordinate" agents, each with a specific set of skills or "tools." When a task is given to the master agent, it delegates the task to the most appropriate subordinate agent.

## Features

- **Agentic Pipeline:** A master agent that supervises a team of subordinate agents.
- **Tool-based Agents:** Agents are equipped with a set of tools that they can use to perform tasks.
- **Extensible:** Easily add new agents and tools to the framework.
- **Command-line Interface:** Interact with the agentic pipeline from the command line.

## Architecture

The architecture of Pyron is based on the concept of a hierarchical team of agents.

```
      +--------------+
      | Master Agent |
      +--------------+
             |
             | Supervises
             |
+---------------------------+
|      Subordinate Agents     |
+---------------------------+
|                           |
|      +---------------+    |
|      | Researcher    |    |
|      +---------------+    |
|                           |
|      +---------------+    |
|      | Writer        |    |
|      +---------------+    |
|                           |
|      +---------------+    |
|      | Terminal      |    |
|      +---------------+    |
|                           |
+---------------------------+
```

### Master Agent

The Master Agent is the orchestrator of the pipeline. It receives a task from the user and delegates it to the most appropriate subordinate agent.

### Subordinate Agents

Subordinate agents are specialized agents that are responsible for performing specific tasks. Pyron comes with three pre-built subordinate agents:

- **Researcher Agent:** This agent is responsible for searching the web for information.
- **Writer Agent:** This agent is responsible for writing text to files.
- **Terminal Agent:** This agent is responsible for executing shell commands.

### Tools

Tools are functions that agents can use to perform tasks. Pyron provides a set of pre-built tools for web search, file I/O, and terminal access.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/pyron.git
   ```

2. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use Pyron, you can run the `main.py` script from the command line:

```bash
python -m pyron.main "Your task here"
```

For example, to ask the agents to research "What is the capital of France?" and write the answer to a file called `capital.txt`, you could run the following command:

```bash
python -m pyron.main "Research 'What is the capital of France?' and write the answer to a file called capital.txt"
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
