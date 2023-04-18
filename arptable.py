import subprocess
from tabulate import tabulate

arp_out = subprocess.check_output(['arp', '-n']).decode('utf-8')

arp_lines = arp_out.strip().split('\n')

arp_table = [line.split() for line in arp_lines]

print(tabulate(arp_table, headers=['Endereço', 'TipoHW', 'EndereçoHW', 'Flags', 'Mascara', 'Iface'], tablefmt='fancy_grid'))


#arp -a = mostra todas as entradas da tabela ARP no Windows, e arp -n no Linux;