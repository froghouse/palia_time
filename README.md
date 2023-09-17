# Palia Time

This is a simple application that pulls the current time from a server using NTP (Network Time Protocol), and converts that to the current time inside the game Palia. This allows you to know what exactly what time it is inside Palia without having to be logged in. This can be useful if you are waiting for an event to start, or to know if everything inside your sales bin is going to be sold any time soon, or for any reason that you can come up with yourself. 

## Python 3.11

The application is written using Python version 3.11 and Tkinter. Tkinter is included in most distributions of Python except for MacOS. You can still install Tkinter on MacOS and use this application, it's just one extra step of installing the Tkinter package.

### Dependencies

There are no dependencies except Tkinter

## How to run the app

Make sure you have Python 3.11 installed for your system. Pull this repo to a folder you can access. Run the following in you terminal to create a Python virtual environment 

```Bash
python3 -m venv new_venv  # On macOS and Linux
```

or

```PS1
python3.11.exe -m venv new_venv  # On Windows
```

Activate your virtual environment

```Bash
source new_venv/bin/activate  # On macOS and Linux
```

or 

```PS1
new_venv\Scripts\Activate  # On Windows
```

There are no required dependecies, but for good measures you should run

```Bash
pip install -r requirements.txt
```