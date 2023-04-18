import subprocess

def ping(host):
    result = subprocess.run(['ping', '-c', '1', '-W', '1', host], stdout=subprocess.PIPE)

    if result.returncode == 0:

        output = result.stdout.decode('utf-8')
        time_index = output.find('time=')
        if time_index != -1:
            start_index = time_index + len('time=')
            end_index = output.find(' ms', start_index)
            time_str = output[start_index:end_index]
            time_ms = float(time_str)
            return time_ms
    return None

host = 'www.google.com'
response_time = ping(host)
if response_time is not None:
    print(f'O tempo de resposta para {host} foi de {response_time:.2f} ms')
else:
    print(f'{host} não respondeu ao ping')



# -c 1: executa apenas um pacote de ping
# -W 1: define um timeout de 1 segundo para a resposta
# host: o endereço IP do host que queremos testar