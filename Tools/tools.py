from duckduckgo_search import DDGS
import subprocess

def search_web(query: str) -> str:
    """
    Searches the web using DuckDuckGo.
    """
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=5)]
    return str(results)


def write_file(filepath: str, content: str) -> str:
    """
    Writes content to a file.
    """
    try:
        with open(filepath, "w") as f:
            f.write(content)
        return f"Successfully wrote to {filepath}."
    except Exception as e:
        return f"Error writing to {filepath}: {e}"


def execute_terminal_command(command: str) -> str:
    """
    Executes a shell command.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e}\n{e.stderr}"

def read_file(filepath: str) -> str:
    """
    Reads the content of a file.
    """
    try:
        with open(filepath, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file {filepath}: {e}"

def list_files(path: str = ".") -> str:
    """
    Lists files in a directory.
    """
    try:
        result = subprocess.run(
            ["ls", "-l", path],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error listing files: {e}\n{e.stderr}"
