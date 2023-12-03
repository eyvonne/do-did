class Entry():
    def __init__(self, name, startTime, endTime, subEntries):
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
        self.subEntries = subEntries

    def get(self):
        return {
            'name': self.name,
            'startTime': self.startTime,
            'endTime': self.endTime,
            'subEntries': self.subEntries
        }
    
def entry_from_dict(entry_dict):
    return Entry(
        entry_dict['name'],
        entry_dict['startTime'],
        entry_dict['endTime'],
        entry_dict['subEntries'])

