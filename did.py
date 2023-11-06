# %%
import sys, datetime
from configure import configure
    
# %%
def main():
    vault_path = configure()
    task = ' '.join(sys.argv[1:])
    today_path = datetime.date.today().strftime("%Y/%m/%d")
    with open(f'{vault_path}/did/{today_path}.md', 'a') as did:
        did.write('- '+task+'\n')
# %%
main()
# %%