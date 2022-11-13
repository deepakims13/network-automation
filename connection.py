import paramiko

device = paramiko.SSHClient()

# Load SSH host keys.
device.load_system_host_keys()

# Add SSH host key when missing.
device.set_missing_host_key_policy(paramiko.AutoAddPolicy())

