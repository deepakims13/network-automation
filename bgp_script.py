import connection
import json
import pytest

def setup_module():
    '''
    Setup module for common configurations
    '''
    # Opening JSON file
    with open('bgp_input.json') as bgp_input:
    # returns JSON object as 
    # a dictionary
    data = json.load(bgp_input)
