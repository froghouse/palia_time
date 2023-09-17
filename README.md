# Palia Time

This is a simple application that pulls the current time from a server using NTP (Network Time Protocol) and converts it to the current time inside the game Palia. This allows you to know exactly what time it is inside Palia without having to be logged in. This can be useful if you are waiting for an event to start, want to know when items in your sales bin will be sold, or for any other reason you can think of.

## Python 3.11

The application is written using Python version 3.11 and Tkinter. Tkinter is included in most distributions of Python, except for macOS. However, you can still install Tkinter on macOS and use this application; it just requires one extra step to install the Tkinter package.

### Dependencies

The only dependency is Tkinter.

## How to run the app

1. Make sure you have Python 3.11 installed on your system.
2. Clone this repository to a folder you can access easily.
3. Open your terminal and navigate to the folder where you cloned the repository.
4. Run the following commands to create a Python virtual environment: 

```Bash
python3 -m venv new_venv  # On macOS and Linux
```

or

```PS1
python3.11.exe -m venv new_venv  # On Windows
```

5. Activate your virtual environment:

```Bash
source new_venv/bin/activate  # On macOS and Linux
```

or 

```PS1
new_venv\Scripts\Activate  # On Windows
```

6. Although there are no required dependencies, it's good practice to install any listed in 

```Bash
pip install -r requirements.txt
```