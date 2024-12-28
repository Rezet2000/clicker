## Instructions

#### Package app into executable for Windows
Run in the root of the project and change path accordingly (path points to pip packages, run inside virtual env)
```bash
pyinstaller --onefile --paths C:\Users\Rey\Documents\code\event_recorder\venv\Lib\site-packages --name 'Clicker' --noconsole main.py
```

May need to <b>turn off windows defender</b> real time protection to compile app

### Tip

> 
> Run ```./dist/{app name} ``` to see possible error logs


## Release log

### v0.1.0

Features:

- Records events: only single events, not combinations of events
- Shows / Hides clicks: displays only the clicks on the screen
- Runs events: loops through the recorded events until 'Esc' key is pressed
- Saves events: saves the event list to a file using python pickle
- Loads events: loads the events saved to a pickle file


