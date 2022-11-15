import logging

def setup_router_interface(self, interface_name, ip, netmask):
    '''
    Configure router interface.
  
    Extended description of function.
  
    Parameters:
    interface_name (str): Name of interface
    ip (str): Ip address
    netmask (str): Ip address netmask
  
    Returns:
    List: List of interface config
    # Create a CLI configuration
    interface_config = [
        "interface {}".format(interface_name),
        "ip address {} {}".format(ip, netmask),
        "no shut"
    ]
    return interface_config
