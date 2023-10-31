from netmiko import ConnectHandler

# Define the device information
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.1',
    'username': 'your_username',
    'password': 'your_password',
    'secret': 'enable_password',  # Enable password if required
}

# Connect to the device
connection = ConnectHandler(**device)

# Enter enable mode if required
connection.enable()

# Send a command and get the output
command = 'show interfaces'
output = connection.send_command(command)

# Print the output
print(output)

# Disconnect from the device
connection.disconnect()