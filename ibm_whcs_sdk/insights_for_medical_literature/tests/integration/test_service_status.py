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
import ibm_whcs_sdk.insights_for_medical_literature as wh
from ibm_cloud_sdk_core.authenticators.iam_authenticator import IAMAuthenticator

# To access a secure environment additional parameters are needed on the constructor which are listed below
CONFIG = configparser.RawConfigParser()
CONFIG.read('./ibm_whcs_sdk/insights_for_medical_literature/tests/config.ini')

BASE_URL = CONFIG.get('settings', 'base_url')
APIKEY = CONFIG.get('settings', 'key')
IAMURL = CONFIG.get('settings', 'iam_url')
LEVEL = CONFIG.get('settings', 'logging_level')
VERSION = CONFIG.get('settings', 'version')
DISABLE_SSL = CONFIG.get('settings', 'disable_ssl')
CORPUS = CONFIG.get('settings', 'corpus')

IML_TEST = wh.InsightsForMedicalLiteratureServiceV1(
    authenticator=IAMAuthenticator(apikey=APIKEY),
    version=VERSION
    )
IML_TEST.set_service_url(BASE_URL)

def test_service_health_check():
    response = IML_TEST.get_health_check_status()
    service_status = wh.ServiceStatus._from_dict(response.get_result())
    assert service_status.service_state == 'OK'

def test_service_health_check_xml():
    response = IML_TEST.get_health_check_status(data_format='xml')
    assert response is not None
