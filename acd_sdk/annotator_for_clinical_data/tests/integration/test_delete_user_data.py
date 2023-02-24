# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import configparser
from ibm_cloud_sdk_core.authenticators import BearerTokenAuthenticator
import acd_sdk.annotator_for_clinical_data as acd

CONFIG = configparser.RawConfigParser()
CONFIG.read('./acd_sdk/annotator_for_clinical_data/tests/config.ini')

BASE_URL = CONFIG.get('settings', 'base_url')
VERSION = CONFIG.get('settings', 'version')
BEARER_TOKEN = CONFIG.get('settings', 'bearer_token')
DISABLE_SSL = (CONFIG.get('settings', 'disable_ssl')=='True')
PROFILE = CONFIG.get('settings', 'profile')

ACD_SERVICE = acd.AnnotatorForClinicalDataV1(
     authenticator=BearerTokenAuthenticator(bearer_token=BEARER_TOKEN),
     version=VERSION
     )
ACD_SERVICE.set_service_url(BASE_URL)
ACD_SERVICE.set_disable_ssl_verification(DISABLE_SSL)

def test_delete_user_specific_artifacts():

    try:
        ACD_SERVICE.delete_user_specific_artifacts()
    except acd.ACDException as acde:
        assert acde.code == 400 or acde.code == 405
