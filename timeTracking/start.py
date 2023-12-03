from entry import *
from writing import write_entries, start_day
import argparse
from reading import get_todays_entries
import datetime
from projects import extract_projects, find_project

def start():
    start_day()
    entries = get_todays_entries()
    parser = argparse.ArgumentParser()
    parser.add_argument('projects', nargs='*')
    args = parser.parse_args()
    projects = args.projects
    