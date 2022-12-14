import logging
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def setup_router_interface(interface_name, ip, netmask):
    '''
    Configure router interface.
  
    Extended description of function.
  
    Parameters:
    interface_name (str): Name of interface
    ip (str): Ip address
    netmask (str): Ip address netmask
  
    Returns:
    List: List of interface config
    '''
    # Create a CLI configuration
    interface_config = [
        "interface {}".format(interface_name),
        "ip address {} {}".format(ip, netmask),
        "no shut"
    ]
    return interface_config

def delete_router_interface(interface_name):
    '''
    Unconfigure router interface.
  
    Extended description of function.
  
    Parameters:
    interface_name (str): Name of interface
  
    Returns:
    List: List of interface unconfig
    '''
    # Create a CLI configuration
    interface_unconfig = [
        "no interface {}".format(interface_name)
    ]
    return interface_unconfig

def setup_bgp(as_number, router_ip, af, route_type):
    '''
    Configure BGP.
  
    Extended description of function.
  
    Parameters:
    as_number (str): Autonomous system number
    router_ip (str): Router IP address
    af (str): Address family ipv4 or ipv6
    route_type (str): Routing type unicast or multicast
  
    Returns:
    List: List of BGP config
    '''
    # Create a CLI configuration
    bgp_config = [
        "router bgp {}".format(as_number),
        "neighbor {} remote-as {}".format(router_ip, as_number),
        "address-family {} {}".format(af, route_type)
    ]
    return bgp_config

def delete_bgp(as_number):
    '''
    Unconfigure BGP.
  
    Extended description of function.
  
    Parameters:
    as_number (str): Autonomous system number
  
    Returns:
    List: List of BGP unconfig
    '''
    # Create a CLI configuration
    bgp_unconfig = [
        "no router bgp {}".format(as_number),
        "neighbor {} remote-as {}".format(router_ip, as_number)
    ]
    return bgp_unconfig

def get_bgp(host, port, username, password):
    '''
    Verify BGP using REST.
  
    Extended description of function.
  
    Parameters:
    host (str): Router hostname or IP address
    port (str): Router port
    username (str): Router username
    password (str): Router password
  
    Returns:
    Json: Json file of response
    '''
    url = "https://{h}:{p}/restconf/data/Cisco-IOS-XR-bgp-oper:bgp-state-data".format(host, port)
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

    response = requests.get(url, auth=(username, password), headers=headers, verify=False)
    return response.json()
