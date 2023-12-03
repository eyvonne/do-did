import os
from installation import get_tools_dir
from integrations import commands, formats
import shutil


def get_cmds():
    cmds = []
    for command in commands.keys():
        cmds.append(command)
        for format in formats.keys():
            cmds.append(f'{command}.{format}')
    return cmds

def print_cmds():
    for command in get_cmds():
        print(command)

def confirm():
    print(f'This tool will uninstall all do-did commands')
    see_commands = input('Would you like to see the commands that will be removed? Y/n: ') or 'y'
    if see_commands.lower() == 'y':
        print('The following commands will be removed:')
        print_cmds()
    confirmation = input('Please confirm that you would like to procede Y/n: ') or 'y'
    return confirmation.lower() == 'y'

def delete_cmds():
    for command in get_cmds():
        os.remove(get_tools_dir()+command)


def delete_tool():
    shutil.rmtree(get_tools_dir()+'do_did/')

def uninstall():
    if not confirm():
        print('No changes made, exiting')
        return
    delete_cmds()
    delete_tool()
    print('do-did uninstalled successfully')

if __name__ == '__main__':
    uninstall()
