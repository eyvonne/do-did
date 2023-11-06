import os, json
config_path = '~/.do_did.json'

def configure():
    if os.path.isfile(config_path):
        with open(config_path, 'r') as config_file:
            try:
                return json.loads(config_file.read())
            except:
                print('config file corrupted, please re-configure')
                return configure()
    print('no configuration detected')
    vault_path = input("enter vault path: ")
    print(vault_path)
    if not os.path.isdir(vault_path): 
        print('please enter a valid path.')
        return configure()
    
    with open(config_path,'w') as config_file:
        config = {'vault_path': vault_path}
        config_file.write(json.dumps(config))
        return config
