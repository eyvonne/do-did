### package contents
#### Build and Dist
These packages contain the wrapped up executables from the scripts elsewhere in the package

To install, navigate into dist/installation, and run the executable there titled 'installation'. 

This script creates a hidden folder in your home folder and adds that folder to the path. Inside of the folder it copies over dist/__init__ which contains the actual executable. It then creats symlinks to all of the commands listed in `ingegrations.py`, which can then be called. 

you may need to run `source .zshrc` after the installation script is run. 

### Current Commands: 
- `did`: this command adds to the did file with a timestamp as a bulleted list
- `note`: this command adds to the notes file with a timestamp as a bulleted list
- `todo`: this command adds to the todo file with a checkbox 


### rebuilding
To update the package make changes in the .py files, and run: 

`pyinstaller --paths ./ installation.py` and 

`pyinstaller --paths ./ __init__.py`

and then navigate into `dist/installation/` and run the `installation` script.