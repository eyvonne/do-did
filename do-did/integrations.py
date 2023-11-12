from formatting import *

# set some global defaults
path = 'path'
default_format = 'default_format'

# set the command paths and default Formats
do = {path: 'todo',
      default_format: checkboxes}
did= {path:'did',
      default_format: bullets_with_hhmm}
note = {path:'note',
        default_format: bullets_with_hhmm}

# this is the exported command mapping
commands = {'todo': do,
            'did': did,
            'did.py': did,
            'note': note}

# and the formatting mapping
formats = {'list': bullets,
           'list_time': bullets_with_hhmm,
           'checkbox': checkboxes}
