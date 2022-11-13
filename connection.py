from netmiko import ConnectHandler
try:
    device = ConnectHandler(device_type='cisco_ios', ip='192.168.255.249', username='cisco', password='cisco')
    output = device.send_command("show version")
    print (output)
except Exception as error_message:
    print("Unable to connect")
    print(error_message)
