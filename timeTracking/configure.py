import os, json

def get_config_path(tool):
    home = get_home()
    return f'{home}.dev_tools/{tool}/config.json'

def get_home():
    return os.path.expanduser("~") + '/'

def configure(tool):
    config_path = get_config_path(tool)
    if os.path.isfile(config_path):
        with open(config_path, 'r') as config_file:
            try:
                return json.loads(config_file.read())
            except:
                print('config file corrupted, please re-configure')
                return configure()
    print('no configuration detected')
    vault_path = input("enter vault path from home folder: ")
    print(vault_path)
    if not os.path.isdir(get_home() + vault_path): 
        print('please enter a valid path.')
        return configure()
    
    with open(config_path,'w') as config_file:
        config = {'vault_path': get_home() + vault_path}
        config_file.write(json.dumps(config))
        return config
