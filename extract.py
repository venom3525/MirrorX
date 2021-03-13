# put this script outside of the accounts folder, and run it with terminal
# list of email addresses will be written in a txt file (automatically created)
# Made by JrM, enjoy!

import os
import json

directory_in_str = './accounts/'
directory = os.fsencode(directory_in_str)
result = ''

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        with open(directory_in_str + filename) as data_file:
            data = json.load(data_file)
            result = result + data['client_email'] + ' , '

        continue
    else:
        continue

result = result[:-2]
f = open('./extracted.txt', 'w')
f.write(result)
f.close()
