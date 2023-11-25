# TaskRunner

TaskRunner is a Python script that reads tasks and terminal commands from a YAML
file and executes them accordingly. This could be used to install default apps
for a fresh installation, or for some tasks that should be executed periodicaly.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Getting Started

### Prerequisites

Before using TaskRunner, make sure you have the following installed:

- Python [https://www.python.org/downloads/]

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/PedroS235/TaskRunner.git
   cd TaskRunner
   ```

2. Install required Python packages

```sh
pip install -r requirements.txt
```

## Usage

1. Create a YAML file (`tasks.yaml` for example) with you list of tasks and
   corresponding commands

2. run the script

```sh
python taskrunner.py path_to_file
```

The script will read the YAML file, execute the tasks and provide some feedback.

## Examples

An example of a `tasks.yaml` can be found in the repo root directory, or below

```yaml
OS: 'Linux' # Darwin, Windows
tasks:
  - name: 'This is a task example'
    cmds: ['echo "Hello World!"']

  - name: 'This is a task example with subtasks'
    cmds:
      ['echo "This is the first subtask"', 'echo "This is the second subtask"']
```

## License

This project is licensed under the MIT License.
