import json

file = open('Lab4/sample-data.json', 'r')
json.data = json.loads(file.read())

print('''Interface Status\n================================================================================
DN                                                 Description           Speed    MTU 
-------------------------------------------------- --------------------  ------   ------''')
for i in json.data['imdata']:
    print(i['l1PhysIf']['attributes']['dn'],
          '                             ',
          i['l1PhysIf']['attributes']['speed'],
          '',
          i['l1PhysIf']['attributes']['mtu'])
