import connection
import json
import pytest
import logging
from connection import netmiko_connection
from bgp_cli_lib import setup_router_interface,delete_router_interface,setup_bgp,delete_bgp

import requests
import urllib3
import sys
from tabulate import tabulate


def setup_module():
    '''
    Setup module for common configurations
    '''
    # Opening Input JSON file
    with open('bgp_input.json') as bgp_input:
        # returns JSON object as 
        # a dictionary
        data = json.load(bgp_input)

    # Opening Topology JSON file
    with open('topology.json') as topology:
        # returns JSON object as 
        # a dictionary
        topology_data = json.load(topology)
    
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
        try:
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
        
            interface_config_R1 = setup_router_interface(interface_name=topology_data['Links']['R1_R2_1'], 
                                                         ip=data['R1']['interface_ip'], 
                                                         netmask='24')        
            conn_setup_R1.send_config_set(interface_config_R1)
        
            interface_config_R2 = setup_router_interface(interface_name=topology_data['Links']['R2_R1_1'], 
                                                         ip=data['R2']['interface_ip'], 
                                                         netmask='24')        
            conn_setup_R2.send_config_set(interface_config_R2)  
        except Exception as error_message:
            log.info("Unable to configure router interfaces")
            log.info(error_message)
        finally:
            log.info("Perform cleanup by unconfiguring interfaces")
            delete_router_interface(interface_name=topology_data['Links']['R1_R2_1'])
            delete_router_interface(interface_name=topology_data['Links']['R2_R1_1'])

class TestBgpConfig(TestInterfaceConfig):
    '''
    Testcase for BGP configurations in router
    '''
    def test_bgp_config():
        try:
            bgp_config_R1 = setup_bgp(as_number=data['R1']['r1_as_number'], 
                                      router_ip=data['R2']['router_ip'],
                                      af=data['R1']['address_family'],
                                      route_type=data['R1']['route_type'])        
            conn_setup_R1.send_config_set(bgp_config_R1)
        
            bgp_config_R2 = setup_bgp(as_number=data['R2']['r2_as_number'], 
                                      router_ip=data['R2']['router_ip'],
                                      af=data['R2']['address_family'],
                                      route_type=data['R2']['route_type'])        
            conn_setup_R2.send_config_set(bgp_config_R2)  
        except Exception as error_message:
            log.info("Unable to configure BGP")
            log.info(error_message)
        finally:
            log.info("Perform cleanup by unconfiguring BGP")
            delete_bgp(as_number=data['R1']['r1_as_number'])
            delete_bgp(as_number=data['R2']['r2_as_number'])
            
class TestBgpSession(TestBgpConfig):
    '''
    Testcase for BGP verifications in router
    '''
