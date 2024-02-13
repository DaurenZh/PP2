import json
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

with open("sample-data.json", "r") as file:
    data = json.load(file)
    for item in data['imdata']:
        index = 0
        if index < 2:
            print(f"{item['l1PhysIf']['attributes']['dn']}                              {item['l1PhysIf']['attributes']['speed']}   {item['l1PhysIf']['attributes']['mtu']}")
            index+=1