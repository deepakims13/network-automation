import paramiko
from netmiko import ConnectHandler

device = paramiko.SSHClient()

# Load SSH host keys.
device.load_system_host_keys()

# Add SSH host key when missing.
device.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def netmiko_connection(self, ip_address, ssh_port, username, password, device_type):
    # Open CLI connection to device
    conn_obj = ConnectHandler(ip = ip_address,
                         port = ssh_port,
                         username = username,
                         password = password,
                         device_type = device_type)
    return conn_obj
