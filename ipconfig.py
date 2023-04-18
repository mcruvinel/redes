import subprocess

output = subprocess.run(['ifconfig'], capture_output=True, text=True)

print(output.stdout)


#Se estivesse utilizando Windows, o comando seria ipconfig, porem como utilizo linux, utilizo o ifconfig