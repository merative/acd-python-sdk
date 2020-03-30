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
import watson_health_cognitive_services.annotator_for_clinical_data as wh

CONFIG = configparser.RawConfigParser()
CONFIG.read('./tests/config.ini')

BASE_URL = CONFIG.get('settings', 'base_url')
APIKEY = CONFIG.get('settings', 'key')
IAMURL = CONFIG.get('settings', 'iam_url')
VERSION = CONFIG.get('settings', 'version')
LEVEL = CONFIG.get('settings', 'logging_level')
DISABLE_SSL = CONFIG.get('settings', 'disable_ssl')
PROFILE = CONFIG.get('settings', 'profile')

ACD = wh.AnnotatorForClinicalDataV1(BASE_URL, APIKEY, IAMURL, VERSION, LEVEL, DISABLE_SSL)

def test_get_profiles():
    response = ACD.get_profiles()
    assert response is not None
    for key in response:
        flow = response[key]
        assert flow is not None

def test_get_profile():
    profile = ACD.get_profile(PROFILE)
    assert profile is not None
    assert profile.id == PROFILE
    assert profile.name is not None
    assert profile.description is None
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
    response = ACD.update_profile(id = 'unittest_new_profile', new_name = 'test profile',
                              new_description = 'functional test profile', new_annotators = test_annoList)
    assert response is not None

def test_delete_profile():
    response = ACD.delete_profile(id = "unittest_new_profile")
    assert response is not None
