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
BEARER_TOKEN = CONFIG.get('settings', 'bearer_token')
VERSION = CONFIG.get('settings', 'version')
DISABLE_SSL = (CONFIG.get('settings', 'disable_ssl')=='True')

ACD_SERVICE = acd.AnnotatorForClinicalDataV1(
     authenticator=BearerTokenAuthenticator(bearer_token=BEARER_TOKEN),
     version=VERSION
     )
ACD_SERVICE.set_service_url(BASE_URL)
ACD_SERVICE.set_disable_ssl_verification(DISABLE_SSL)

def test_get_annotators():
    response = ACD_SERVICE.get_annotators()
    annotator_list = response.get_result()
    assert annotator_list is not None
    for key in annotator_list:
        annotator = annotator_list[key]
        assert annotator is not None

def test_get_annotator():
    response = ACD_SERVICE.get_annotators_by_id('concept_value')
    annotator = response.get_result()
    assert annotator['description'] is not None
    
def test_get_bad_annotator():
    try:
        annotator = ACD_SERVICE.get_annotators_by_id('concept_discovery')
    except acd.ACDException as acde:
        assert acde.code == 404
