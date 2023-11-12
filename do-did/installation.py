from os import symlink, makedirs
from os.path import expanduser, isdir
from integrations import commands
import sys
from distutils.dir_util import copy_tree

def get_tools_dir():
    home = expanduser('~') + "/"
    tools_dir = home+'.dev_tools/'
    return tools_dir

def confirm(tools_dir):
    print(f'This tool will create a new directory at: {tools_dir} and add it to the path')
    confirmation = input('Please confirm that you would like to procede Y/n: ') or 'y'
    return confirmation.lower() == 'y'

def create_tools_dir():
    if isdir(get_tools_dir()):
        return True
    makedirs(get_tools_dir())
    return True

def add_tools_to_path():
    if not isdir(get_tools_dir()):
        create_tools_dir()
    sys.path.append(get_tools_dir())
    with open(f'{expanduser("~")}/.zshrc', 'a') as zshrc:
        zshrc.write(f'export PATH=$PATH:{get_tools_dir()}')

def create_symlinks(statuses, tool):
    for status in statuses: 
        symlink(tool, get_tools_dir()+status)

def install():
    if not confirm(get_tools_dir()):
        print('No changes made, exiting')
        return
    add_tools_to_path()
    tool_origin = '../__init__/'
    tool_destination = get_tools_dir() + 'do_did/'
    copy_tree(tool_origin, tool_destination)
    create_symlinks(commands.keys(), tool_destination+'__init__')

if __name__ == '__main__':
    install()
