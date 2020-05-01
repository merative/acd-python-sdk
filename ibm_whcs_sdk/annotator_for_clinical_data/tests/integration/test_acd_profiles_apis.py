# coding: utf-8

# Copyright 2018 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import configparser
from ibm_cloud_sdk_core.authenticators.iam_authenticator import IAMAuthenticator
import ibm_whcs_sdk.annotator_for_clinical_data as wh

CONFIG = configparser.RawConfigParser()
CONFIG.read('./ibm_whcs_sdk/annotator_for_clinical_data/tests/config.ini')

BASE_URL = CONFIG.get('settings', 'base_url')
APIKEY = CONFIG.get('settings', 'key')
IAMURL = CONFIG.get('settings', 'iam_url')
VERSION = CONFIG.get('settings', 'version')
LEVEL = CONFIG.get('settings', 'logging_level')
DISABLE_SSL = CONFIG.get('settings', 'disable_ssl')
PROFILE = CONFIG.get('settings', 'profile')

ACD = wh.AnnotatorForClinicalDataV1(
    authenticator=IAMAuthenticator(apikey=APIKEY, url=IAMURL, disable_ssl_verification=DISABLE_SSL),
    version=VERSION
    )
ACD.set_service_url(BASE_URL)
ACD.set_disable_ssl_verification(DISABLE_SSL)

def test_get_profiles():
    response = ACD.get_profiles()
    profile_list = response.get_result()
    assert profile_list is not None
    for key in profile_list:
        flow = profile_list[key]
        assert flow is not None

def test_get_profile():
    response = ACD.get_profile(PROFILE)
    profile = wh.AcdProfile._from_dict(response.get_result())
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
        profile = ACD.get_profile(PROFILE)
    except wh.ACDException as acde:
        assert acde.code == 404

def test_create_profile():
    test_annoList = []
    test_anno = wh.Annotator(name = "concept_detection")
    test_annoList.append(test_anno)
    try:
        response = ACD.create_profile(new_id = 'unittest_new_profile', new_name = 'test profile',
                              new_description = 'functional test profile', new_annotators = test_annoList)
        assert response is not None
    except wh.ACDException as acde:
        # flow already exists - previous delete must have failed
        assert acde.code == 409

def test_update_profile():
    test_annoList = []
    test_anno = wh.Annotator(name = "concept_detection")
    test_annoList.append(test_anno)
    response = ACD.update_profile(id = 'unittest_new_profile', nid = 'unittest_new_profile', ew_name = 'test profile',
                              new_description = 'updated functional test profile', new_annotators = test_annoList)
    assert response is not None

def test_delete_profile():
    response = ACD.delete_profile(id = "unittest_new_profile")
    assert response is not None
