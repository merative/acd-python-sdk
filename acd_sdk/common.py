# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2019, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

"""
This module provides common methods for use across all service modules.
"""

import platform
from .version import __version__

HEADER_NAME_USER_AGENT = 'User-Agent'
SDK_NAME = 'acd-sdk'

def get_system_info():
    """
    Get information about the system to be inserted into the User-Agent header
    """
    return '{0} {1} {2}'.format(platform.system(), # OS
                                platform.release(), # OS version
                                platform.python_version()) # Python version


def get_user_agent():
    """
    Get the value to be sent in the User-Agent header
    """
    return USER_AGENT


USER_AGENT = '{0}-{1} {2}'.format(SDK_NAME, __version__, get_system_info())


def get_sdk_headers(service_name, service_version, operation_id):
    """
    Get the request headers to be sent in requests by the SDK
    """
    headers = {}
    headers[HEADER_NAME_USER_AGENT] = get_user_agent()
    return headers
