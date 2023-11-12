import datetime

def bullets(task):
    return f'- {task} \n'

def bullets_with_hhmm(task):
    return f'- {datetime.datetime.now().strftime("%H:%M:%S")} {task} \n'

def checkboxes(task):
    return f'- [ ] {task} \n'


    
