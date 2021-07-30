
import json
import pprint

json_file = open('data/PyTravLITE_NPCs.json', 'r')
just_read_in = json.load(json_file)
json_file.close()

for traveller in just_read_in['NPCs']:
    pprint.pprint(traveller)
    print()
    print()