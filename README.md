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

## Usage

1. Download the latest [release](https://github.com/kas/i3-workspace-reset/releases)
2. Unzip the i3-workspace-reset-#-#-#.zip file
3. Use the i3-workspace-reset file

## npm files? In a Python project?? Oh, the humanity!

Don't worry, those files are just here to keep this file formatted with Prettier.
