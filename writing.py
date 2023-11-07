from os.path import isdir
from os import makedirs
from configure import configure
import datetime
import sys
from formatting import did

def _write_task_to_disk(vault_path, status, month, day, task):
    dir_path = f'{vault_path}/{status}/{month}'
    if not isdir(dir_path):
        makedirs(dir_path)
    with open(f'{dir_path}/{day}', 'a') as todays_tasks:
        todays_tasks.write(task)

def write_task():
    vault_path = configure()['vault_path']
    status = sys.argv[0]
    task = format(sys.argv[1:])
    month_path = datetime.date.today().strftime("%Y/%m")
    day_path = datetime.date.today().strftime("%d_%A") +".md"
    _write_task_to_disk(vault_path, status, month_path, day_path, task)

