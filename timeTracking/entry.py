from datetime import datetime

class Entry():
    def __init__(self, name, startTime=None, endTime=None, subEntries=[]):
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
        self.subEntries = subEntries
        self.duration = self.endTime - self.startTime if endTime else None

    def get(self):
        return {
            'name': self.name,
            'startTime': self.startTime,
            'endTime': self.endTime,
            'subEntries': self.subEntries
        }
    
    def set_end_time(self, end_time):
        self.endTime = end_time
        self.duration = self.endTime - self.startTime
    
    def to_dict(self):
        # endTime may be None if the entry is still in progress
        # if endTime is None, we still want to return a dict with all four values
        # but endtime should be None
        return {
            'name': self.name,
            'startTime': self.startTime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            'endTime': self.endTime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") if self.endTime else None,
            'subEntries': [subEntry.to_dict() for subEntry in self.subEntries]
        }
# entry_dict should look like:
# {
#     'name': 'project_name',
#     'startTime': '2023-12-02T07:56:37.491Z',
#     'endTime': '2023-12-02T07:56:37.491Z',
#     'subEntries': [
#         {
#             'name': 'subproject_name',
#             'startTime': '2023-12-02T07:56:37.491Z',
#             'endTime': '2023-12-02T07:56:37.491Z',
#             'subEntries': []
#         }
#     ]
# }
# in entry objects, startTime and endTime are datetime.datetime objects
# in entry_dict, startTime and endTime are strings
# this function converts the strings to datetime.datetime objects
# end time may be none if the entry is still in progress
def build_entry_from_dict(entry_dict):
    entry = Entry(entry_dict['name'])
    entry.startTime = datetime.strptime(entry_dict['startTime'], "%Y-%m-%dT%H:%M:%S.%fZ")
    if entry_dict['endTime']:
        entry.endTime = datetime.strptime(entry_dict['endTime'], "%Y-%m-%dT%H:%M:%S.%fZ")
    if entry_dict['subEntries']:
        entry.subEntries = [build_entry_from_dict(subEntry) for subEntry in entry_dict['subEntries']]
    return entry
