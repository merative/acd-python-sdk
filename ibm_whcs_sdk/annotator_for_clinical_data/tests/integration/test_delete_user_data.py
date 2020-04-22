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

def test_delete_user_specific_artifacts():

    try:
        ACD.delete_user_specific_artifacts()
    except wh.ACDException as acde:
        assert acde.code == 400 or acde.code == 405
