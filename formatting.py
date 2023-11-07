import datetime

def bullets(task):
    return f'- {task}\n'

def bullets_with_hhmm(task):
    return f'- {datetime.date.today().strftime("%H:%M")} {task}'

def checkboxes(task):
    return f'- [ ] {task}'

def format(arvs):
    pass