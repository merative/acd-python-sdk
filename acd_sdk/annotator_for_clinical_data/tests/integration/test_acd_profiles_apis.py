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
PROFILE = CONFIG.get('settings', 'profile')

ACD_SERVICE = acd.AnnotatorForClinicalDataV1(
     authenticator=BearerTokenAuthenticator(bearer_token=BEARER_TOKEN),
     version=VERSION
     )
ACD_SERVICE.set_service_url(BASE_URL)
ACD_SERVICE.set_disable_ssl_verification(DISABLE_SSL)

def test_get_profiles():
    response = ACD_SERVICE.get_profiles()
    profile_list = response.get_result()
    assert profile_list is not None
    for key in profile_list:
        flow = profile_list[key]
        assert flow is not None

def test_get_profile():
    response = ACD_SERVICE.get_profile(PROFILE)
    profile = acd.AcdProfile._from_dict(response.get_result())
    assert profile is not None
    assert profile.id == PROFILE
    assert profile.name is not None
    assert profile.description is not None
    annotators = profile.annotators
    if annotators is not None:
        for annotator in annotators:

            assert annotator.name is not None

def test_get_bad_flow():
    try:
        profile = ACD_SERVICE.get_profile(PROFILE)
    except acd.ACDException as acde:
        assert acde.code == 404

def test_create_profile():
    test_annoList = []
    test_anno = acd.Annotator(name = "concept_detection")
    test_annoList.append(test_anno)
    try:
        response = ACD_SERVICE.create_profile(new_id = 'unittest_new_profile', new_name = 'test profile',
                              new_description = 'functional test profile', new_annotators = test_annoList)
        assert response is not None
    except acd.ACDException as acde:
        # flow already exists - previous delete must have failed
        assert acde.code == 409

def test_update_profile():
    test_annoList = []
    test_anno = acd.Annotator(name = "concept_detection")
    test_annoList.append(test_anno)
    response = ACD_SERVICE.update_profile(id = 'unittest_new_profile', new_id = 'unittest_new_profile', new_name = 'test profile',
                              new_description = 'updated functional test profile', new_annotators = test_annoList)
    assert response is not None

def test_delete_profile():
    response = ACD_SERVICE.delete_profile(id = "unittest_new_profile")
    assert response is not None
