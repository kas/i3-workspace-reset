# i3-workspace-reset

Restore some order to your i3 workspaces

![GIF](https://github.com/kas/i3-workspace-reset/raw/master/gif.gif)

## Development

1. Create a virtual environment: `python -m venv venv`
2. Enter the virtual environment: `source venv/bin/active`
3. Install the requirements: `pip install -r requirements/development.txt`

## Distribution

1. Follow the instructions in the Development section
2. Generate the dist/ folder: `pyinstaller i3-workspace-reset.py`
3. Zip the dist/i3-workspace-reset/ folder: `zip -r i3-workspace-reset-#-#-#.zip i3-workspace-reset`

## Frequently asked questions

(Actually, these questions have literally never been asked. But I figured it would be good to note them here.)

- How/when should I use i3-workspace-reset?
  - You can use i3-workspace-reset however you want. Consider using i3-workspace-reset with dmenu.
- How do I use i3-workspace-reset with dmenu?
  1. Create a bin/ folder: `mkdir ~/bin`
  2. Copy the i3-workspace-reset/ folder to the ~/bin/ folder: `cp -r i3-workspace-reset ~/bin`
  3. Create an i3-workspace-reset.sh file: `touch ~/bin/i3-workspace-reset.sh`
  4. Add the following to the ~/bin/i3-workspace-reset.sh file:

```
#!/bin/bash
(DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )" && $DIRECTORY/i3-workspace-reset/i3-workspace-reset)
```

    5. Make the ~/bin/i3-workspace-reset.sh file executable: `chmod +x ~/bin/i3-workspace-reset.sh`

- What if I named my workspaces?
  - i3-workspace-reset will ruthlessly erase any semblance of your efforts by restoring your workspace names to integers, just like you wanted.
- What if I'm using multiple outputs?
  - i3-workspace-reset works great with multiple outputs, so long as they are oriented in a horizontal fashion. For example, if you use i3-workspace-reset and you have two outputs side by side, then i3-workspace-reset will start with the left output, renaming the workspaces as 1 to `len(output[0].workspaces)`, before moving on to the right output, renaming the workspaces as `len(outputs[0].workspaces) + 1` to `len(outputs[0].workspaces) + len(outputs[1].workspaces)`.
- When will i3-workspace-reset support vertically-oriented outputs?
  - Probably never since my head only rotates on the horizontal axis. I might consider contributions here if it's a popular request.
- npm files? In a Python project?? Oh, the humanity!
  - Don't worry, those files are just here to keep this file formatted with Prettier.

## Usage

1. Download the latest [release](https://github.com/kas/i3-workspace-reset/releases)
2. Unzip the i3-workspace-reset-#-#-#.zip file
3. Use the i3-workspace-reset file
