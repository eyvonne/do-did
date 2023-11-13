### Installation Instructions

Included in do-did is a script (`install.zsh`) which if run builds and installs the CLI tools. 

If you make changes, re-running the script will rebuild and reinstall the tool

### Usage:
The installation script creates several symlinks which act as the various entry points to the tool. Depeneding on what 'status' and 'formatting' are used to invoke the tool will affect what it does. Each status has a default format and can be called without any format. To get a format other than the default use dot notation - `status.format`

The default statuses are:
- `did`: this command adds to the did file  (default format: a timestamp as a bulleted list)
- `note`: this command adds to the notes file with a timestamp as a bulleted list
- `todo`: this command adds to the todo file with a checkbox 

The default formats are: 
- `list`: formats as a list 
- `list_time`: formats as a list with the current timestamp
- `checkbox`: a list with checkboxes
- `h1`-`h4`: creates a heading of the appropriate level 
- `num_list`: creates a numbered list

### Extending

To add a new status:
- in the `integrations.py` file, add a new dict object to the collection starting on line 8
    - this should have two elements: `path` and `default_format`
    - the `path` is the name of the folder to store tasks in for this status 
    - the `default_format` is the formatter to use by default
- add this object to the `commands` object, where the key will be the status used in calling
- once these changes have been made re-run `install.zsh`

To add a new format: 
- in the `formatting.py` file, add a new formatting function that takes in one argument (the task to be formatted)
- in the `integrations.py` file add your new formatter to the `formats` object, where the key is the name of the format to be used while calling and the value is the formatter. 


