# QF635: Market Microstructure & Algorithmic Trading
This repository is strictly for education purpose and is not financial advice nor endorsement of any trading exchanges.

This course requires student to download the following software development tools that are freely available:
  1. Anaconda - setup Python environment and dependent libraries to run Python program
  2. PyCharm - development tool to write Python program
  3. Git - to download project codes from GitHub repository

## Anaconda - Setting up a Python environment

Download and install Anaconda from https://www.anaconda.com/. Select all the checkboxes during the installation steps.

After installation, open `Anaconda Powershell Prompt` to create a Python 3.11 environment with the name `py311-smu` by typing:
```
conda create -n py311-smu python=3.11
```
Multiple environments of different Python version can be created for other projects. To see the list of Anaconda environments and the installation directory:

```
conda info --envs
```
Each environment installation directory contains the `python.exe`, and we will need this path for configuring PyCharm later. Go to the directory to explore more.

We are going to install more libraries in `py311-smu` environment. First activate it:

```
conda activate py311-smu
```
To check Python version, enter the following:
```
python --version
```

Next install the project's dependency with the following libraries (sometimes called packages):
```
conda install numpy
conda install matplotlib
conda install -c conda-forge python-gnupg
conda install -c anaconda requests
conda install -c conda-forge python-dotenv
conda install -c conda-forge websockets
conda install -c conda-forge pandas-ta
conda install -c conda-forge schedule

pip install python-binance

```
`-c` stands for --channel. It is used to specify a channel where to search for the package, and the channel is often the named owner.

To get the list of packages installed:
```
> conda list
```

## Github - Download the course repository (Python codes)
Download and install Git from https://git-scm.com/downloads

Course repository is hosted on GitHub: https://github.com/aiver-workshop/qf635

We are going to download course repository to folder on our PC, for example under `~/smu` (`~/` refers to home folder)

Open `Git Bash` and enter the followings:
```
$ cd ~
$ mkdir smu
$ cd smu
$ git clone  https://github.com/aiver-workshop/QF635-2024.git
$ cd qf635
```
These steps will download course repository in a folder called `~/smu/qf635`, and this is going to be our `working directory`.

To display the full path of the working directory, type:
```
$ pwd
/c/Users/Nicholas Liew/smu/qf635
```

## PyCharm - Integrated Development Environment (IDE)
Download and install Anaconda from https://www.anaconda.com/

After completing the installation:
1. Open the code repository by `File` -> `Open...` -> select/navigate to `working directory`
2. Configure the Python interpreter by `File` -> `Settings...` -> `Project: qf635` -> `Python Interpreter` -> `Add Interpreter` -> `Add Local Interpreter` -> `Conda Environment` -> `Use Existing environment` -> `py311-smu`

Lower-right side of the screen should show `py311-smu`

By default, the new user interface (UI) is a new redesigned look of PyCharm. Optionally, revert to Classic UI by `File` -> `Settings...` -> `Appearance & Behavior` -> `New UI` -> unselect `New UI`

## Running your first script
Go to the `welcome` folder, double click on `hello.py` to open the script in editor, then right click on it and `Run 'hello'`. The script should run without error and produce a similar output as follows:
```
Welcome to QF635: Market Microstructure & Algorithmic Trading
5 + 3 = 8

Process finished with exit code 0

```