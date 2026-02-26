import json

with open("sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("================================================================================")
print(f"{'DN':55}{'Description':16}{'Speed':10}{'MTU':6}")
print("-------------------------------------------------- ------------------ -------  ------")

for i in data["imdata"]:
    attr = i["l1PhysIf"]["attributes"]
    dn = attr["dn"]
    descr = attr["descr"]
    speed = attr["speed"]
    mtu = attr["mtu"]

    print(f"{dn:55}{descr:15}{speed:10}{mtu:6}")