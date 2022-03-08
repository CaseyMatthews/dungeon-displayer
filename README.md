
## Introduction

This is a project to help Dungeons and Dragons Dungeon Masters to display digital game boards more easily to support a seamlessa and engaging player experience.

#### Find Project Notes: [Dungeon Displayer Wiki](https://github.com/CaseyMatthews/Sdungeon-displayer/wiki)

#### Tools List
   - pySide2 (GUI Library)
   - pipenv (Virtual Envronment and Dependency Management)
   - pyinstaller (Build Management)

---

## Setup

#### Ensure Correct Version of Python

This project requires a specific version python to run properly. Reference the required version in this project's <em>Pipfile</em> and ensure that it is installed on your system ([Python Downloads](https://www.python.org/downloads/)). It is not required to be the default python install, it just needs to be present. Take note of its install location to use later.

#### Install Pipenv

This project uses pipenv for dependency and virtual environment management.

From a terminal run: `pip install pipenv`. Detailed installation instructions can be found here: [Installing Pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv).

#### Download Source Code and Set Up Local Environment

With pipenv, create a virtual environment in the project's directory using the required python version.

1. Clone this repository: `git clone https://github.com/CaseyMatthews/dungeon-displayer.git`

2. Navigate to the project directory.

3. Initialize the pipenv virtual environment: `pipenv install --dev --python path/to/python/install/python.exe`. Replace the path with python's install location as previously noted.

##### Note for IDEs
If your IDE is not resolving packages installed via pipenv, then you may need to configure it to use the python interpreter inside the pipenv virtual environment.

<em>vscode:</em> `CTRL + SHIFT + P`, `>Python select interpreter`

---

### Basic Usage