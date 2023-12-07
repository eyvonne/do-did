from reading import get_todays_entries
from writing import write_entries, end_day
from datetime import datetime
from projects import find_project
from sys import argv
from start import parse_args

def stop():
    projects = parse_args()
    entries = get_todays_entries()
    project_entry = find_project(projects, entries)
    if project_entry:
        project_entry.set_end_time(datetime.utcnow())
    else:
        print("Project not found")
        return
    write_entries(entries)
    end_day()

if __name__ == '__main__':
    stop()