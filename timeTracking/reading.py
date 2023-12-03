import datetime
from configure import configure
import json
from entry import build_entry_from_dict

def get_todays_note():
    vault_path = configure('timeTracker')['vault_path']
    month_path = datetime.date.today().strftime("%Y/%m")
    day_path = datetime.date.today().strftime("%d_%A") +".md"
    todays_note = f'{vault_path}/TimeTracking/{month_path}/{day_path}'
    return todays_note

def get_entries(todays_note):
    with open(todays_note, 'r') as f:
        for line in f.readlines():
            try:
                return json.loads(line)
            except:
                continue
    return {'entries': []}

def get_todays_entries():
    todays_note = get_todays_note()
    entries = get_entries(todays_note)
    return [build_entry_from_dict(entry) for entry in entries['entries']]
