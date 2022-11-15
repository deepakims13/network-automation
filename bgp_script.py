import connection
import json
import pytest
import logging
from connection import netmiko_connection

def setup_module():
    '''
    Setup module for common configurations
    '''
    # Opening Input JSON file
    with open('bgp_input.json') as bgp_input:
    # returns JSON object as 
    # a dictionary
    data = json.load(bgp_input)
    
    try:
        # Connect to router1 using username/password authentication.
        connection.device.connect(router_ip=data['R1']['router_ip'], 
                    username=data['R1']['router_username'], 
                    password=data['R1']['router_password'],
                    look_for_keys=False )
        # Connect to router2 using username/password authentication.
        connection.device.connect(router_ip=data['R2']['router_ip'], 
                    username=data['R2']['router_username'], 
                    password=data['R2']['router_password'],
                    look_for_keys=False )
    except Exception as error_message:
        log.info("Unable to connect")
        log.info(error_message)

class TestInterfaceConfig():
    '''
    Testcase for Interface configurations in router
    '''
    def test_interface_config():
        conn_setup_R1 = netmiko_connection(ip_address=data['R1']['router_ip'], 
                                        ssh_port=data['R1']['ssh_port'], 
                                        username=data['R1']['router_username'],
                                        password=data['R1']['router_password'], 
                                        device_type=data['R1']['device_type'])
        conn_setup_R2 = netmiko_connection(ip_address=data['R2']['router_ip'], 
                                        ssh_port=data['R2']['ssh_port'], 
                                        username=data['R2']['router_username'],
                                        password=data['R2']['router_password'], 
                                        device_type=data['R2']['device_type'])
        
