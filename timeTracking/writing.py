from reading import get_todays_note, get_todays_entries
from projects import get_durations
import json
from os import makedirs
from os.path import isfile, isdir

def write_entries(entries):
    todays_note = get_todays_note()
    formatted_stamp = f'''```simple-time-tracker
{json.dumps({'entries': [entry.to_dict() for entry in entries]})}
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

def end_day():
    if not isfile(get_todays_note()):
        return start_day()
    project_durations = get_durations(get_todays_entries())
    formatted_durations = pretty_format_durations(project_durations)
    with open(get_todays_note(), 'w') as todays_times:
        formatted_stamp = f'''```simple-time-tracker
{json.dumps({'entries': [entry.to_dict() for entry in get_todays_entries()]})}
```
'''
        todays_times.write(formatted_stamp)
        todays_times.write(formatted_durations)

def pretty_format_durations(durations):
    # print durations in a pretty way
    # the durations dictionary should look like: {'project_name': datetime.timedelta} for a project with no subentries
    # and {'project_name': {'total': datetime.timedelta, 'subproject1_name': datetime.timedelta, 'subproject2_name': ddatetime.timedelta} for a project with 2 subentries
    # subentries may have subentries, so we need to recurse
    # the return value should look like:
    '''
    project_name: 1:00:00
        subproject1_name: 0:30:00
        subproject2_name: 0:30:00
    '''
    formatted_durations = ''
    for project_name, duration in durations.items():
        if type(duration) == dict:
            formatted_durations += f'    {project_name}: {duration["total"]}\n'
            formatted_durations += f'    {pretty_format_durations(duration)}'
        else:
            formatted_durations += f'{project_name}: {duration}\n'
    return formatted_durations

