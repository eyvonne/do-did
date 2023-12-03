from sys import argv

def find_project(projects, entries):
    for entry in entries:
        if entry.name == projects[0]:
            if len(projects) == 1:
                return entry
            return find_project(projects[1:], entry.subEntries)
