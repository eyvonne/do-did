from datetime import datetime
from entry import Entry

def find_project(projects, entries):
    for entry in entries:
        print('entry', entry)
        if entry.name == projects[0]:
            if len(projects) == 1:
                return entry
            return find_project(projects[1:], entry.subEntries)
    return create_projects(projects)

def create_projects(projects):
    print('create_projects', projects)
    if len(projects) == 1:
        return Entry(projects[0], startTime=datetime.utcnow())
    return Entry(projects[0], subEntries=[create_projects(projects[1:])])

# entries is a list of Entry objects
# the Entry object has a name and a list of subEntries, which are also Entry objects
# the Entry object also has a duration, which is a datetime.timedelta object
# We want to return a dictionary of project names and durations 
# The duration of a project is the sum of the durations of all the subEntries
# The subentries of a project may have the same name, if they do, we want to add their durations together
# the final dictionary should look like: {'project_name': datetime.timedelta} for a project with no subentries
# and {'project_name': {'total': datetime.timedelta, 'subproject1_name': datetime.timedelta, 'subproject2_name': datetime.timedelta} for a project with 2 subentries
def get_durations(entries):
    durations = {}
    for entry in entries:
        if entry.name not in durations:
            durations[entry.name] = entry.duration
        else:
            durations[entry.name] += entry.duration
        if len(entry.subEntries) > 0:
            durations[entry.name] = {'total': entry.duration}
            durations[entry.name].update(get_durations(entry.subEntries))
    return durations
