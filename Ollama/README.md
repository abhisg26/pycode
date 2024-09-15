## Using Ollama to run LLMs on local machine

Step 1: Create python venv using command `python -m venv <env_name>`

Step 2: Download Ollama software from given website -https://ollama.com/download. Run Setup and install

Step 3: Check installation with command "ollama", output should be something like this:
Usage:
  ollama [flags]
  ollama [command]

Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command

Flags:
  -h, --help      help for ollama
  -v, --version   Show version information

Use "ollama [command] --help" for more information about a command.

Step 4: Use `ollama pull model_name` command to use model locally

Step 5: Install langchain to the python environment using environment `pip install -U langchain-ollama`