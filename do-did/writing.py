from os.path import isdir
from os import makedirs
from configure import configure
import datetime
import sys
from integrations import commands, formats

def _write_task_to_disk(vault_path, status, month, day, task):
    dir_path = f'{vault_path}/{status}/{month}'
    if not isdir(dir_path):
        makedirs(dir_path)
    with open(f'{dir_path}/{day}', 'a') as todays_tasks:
        todays_tasks.write(task)

def _get_status_format(status_format):
    command = status_format.split('.')
    if len(command) == 1: 
        status = commands[status_format]['path']
        format = commands[status_format]['default_format']
    else: 
        status = commands[command[0]]['path']
        format = formats[command[1]]
    return status, format

def format_task(task_list, format):
    task = ' '.join(task_list)
    formatted_task = format(task)
    return formatted_task

def write_task():
    print(sys.argv)
    vault_path = configure()['vault_path']
    status, format = _get_status_format(sys.argv[0])
    task = format_task(sys.argv[1:], format)
    month_path = datetime.date.today().strftime("%Y/%m")
    day_path = datetime.date.today().strftime("%d_%A") +".md"
    _write_task_to_disk(vault_path, status, month_path, day_path, task)

if __name__ == '__main__': 
    write_task()