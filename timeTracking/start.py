from entry import *
from writing import write_entries, start_day
import argparse
from reading import get_todays_entries
from datetime import datetime
from projects import find_project

def start():
    start_day()
    entries = get_todays_entries()
    project = parse_args()
    entries = add_entry(entries, project)
    write_entries(entries)

def add_entry(entries, project):
    if len(project) == 0:
        return entries
    print(entries)
    entry = find_project(project, entries)
    print(entry)
    entries.append(entry)
    return entries

def parse_args():
    parser = argparse.ArgumentParser(description='Start a new entry.')
    parser.add_argument('project', nargs='*', help='The project to start.')
    args = parser.parse_args()
    return args.project

if __name__ == '__main__':
    start()