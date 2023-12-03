from reading import get_todays_entries
from writing import write_entries
from datetime import datetime
from projects import find_project
from sys import argv

def stop():
    projects = argv[1:]
    entries = get_todays_entries()
    project_entry = find_project(projects, entries)
    if project_entry:
        project_entry.end = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    else:
        print("Project not found")
        return
    write_entries(entries)
    
    