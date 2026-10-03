from netmiko import ConnectHandler
from datetime import datetime

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'admin123',
}

try:
    connection = ConnectHandler(**device)
    output = connection.send_command('show running-config')
    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'router_config_{timestamp}.txt'
    with open(filename, 'w') as file:
        file.write(output)
    connection.disconnect()
except Exception as e:
    print(e)
