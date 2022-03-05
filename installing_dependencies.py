import subprocess
import json


def install_dep(name):
    result = subprocess.run(['pip', 'install', name], stdout=subprocess.PIPE)
    result.stdout
    # print(result)
    if "Requirement already satisfied" in str(result.stdout) \
            or 'Successfully installed' in str(result.stdout):
        print(name, ' ---> Success')
    else:
        print(name, ' -------> Failed')


file = open("requirements.json")
data = json.load(file)

for items in data['dependencies']:
    install_dep(items)
