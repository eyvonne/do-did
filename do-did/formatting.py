import datetime

def bullets(task):
    return f'- {task} \n'

def bullets_with_hhmm(task):
    return f'- {datetime.datetime.now().strftime("%H:%M:%S")} {task} \n'

def checkboxes(task):
    return f'- [ ] {task} \n'

def h1(task): 
    return header(1, task)

def h2(task):
    return header(2, task)

def h3(task):
    return header(3, task)

def h4(task):
    return header(4, task)

def header(num, task): 
    return f'{"#"*num} {task} \n'
    
def num_list(task): 
    return f' 1. {task} \n'