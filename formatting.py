import datetime

def bullets(task):
    return f'- {task}\n'

def bullets_with_hhmm(task):
    return f'- {datetime.datetime.now().strftime("%H:%M:%S")} {task}'

def checkboxes(task):
    return f'- [ ] {task}'

def format(argvs):
    integrations = {'did.py': bullets_with_hhmm,
                    'did': bullets,
                    'note': bullets_with_hhmm,
                    'do': checkboxes}
    format_task = integrations.get(argvs[0], bullets_with_hhmm)
    task = ' '.join(argvs[1:])
    return format_task(task)

    
