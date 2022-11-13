import connection
import json
import pytest
import logging

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
