from reading import get_todays_note
import json
from os import makedirs
from os.path import isfile, isdir

def write_entries(entries):
    todays_note = get_todays_note()
    formatted_stamp = f'''```simple-time-tracker
{json.dumps({'entries': entries})}
```
'''
    with open(todays_note, 'w') as f:
        f.write(formatted_stamp)

def start_day():
    if isfile(get_todays_note()):
        return
    dir_path = '/'.join(get_todays_note().split('/')[0:-1])
    if not isdir(dir_path):
        makedirs(dir_path)
    with open(get_todays_note(), 'w') as todays_times:
        todays_times.write('```simple-time-tracker\n```')
