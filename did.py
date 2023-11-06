# %%
import sys, json, os, datetime

# %%
config_path = '~/.do_did.json'
# %%
def configure():
    vault_path = input("enter vault path: ")
    if not os.path.isfile(config_path):
        vault_path = input("enter vault path: ")
        print('please enter a valid path.')
        configure()
    with open(config_path,'w') as config_file:
        config_file.write(json.dumps({'vault_path':vault_path}))

# %%
def get_vault_path():
    if not os.path.isfile(config_path):
        print('No config detected')
        configure()
    with open(config_path, 'r') as config_file:
        return json.loads(config_file.read())['vault_path']
    
# %%
def main():
    if ('--configure') in set(sys.argv):
        configure()
    vault_path = get_vault_path()
    task = ' '.join(sys.argv[1:])
    today_path = datetime.date.today().strftime("%Y/%m/%d")
    with open(f'{vault_path}/{today_path}.md', 'a') as did:
        did.write('- '+task+'\n')
# %%
main()
# %%
