import subprocess
from tabulate import tabulate

output = subprocess.run(['ifconfig'], capture_output=True, text=True)

table = []
for line in output.stdout.split('\n\n'):
    interface_info = {}
    for item in line.split('\n'):
        if 'inet ' in item:
            interface_info['inet'] = item.strip().split()[1]
        elif 'ether ' in item:
            interface_info['mac'] = item.strip().split()[1]
        elif 'flags' in item:
            interface_info['flags'] = item.strip().split()[1:]
            interface_info['name'] = interface_info['flags'].pop(-1)
    if interface_info:
        table.append([interface_info['name'], interface_info.get('inet', ''), interface_info.get('mac', ''), interface_info.get('flags', '')])

headers = ['Interface', 'IP', 'MAC', 'Flags']
print(tabulate(table, headers=headers, tablefmt="fancy_grid"))


#Se estivesse utilizando Windows, o comando seria ipconfig, porem como utilizo linux, utilizo o ifconfig