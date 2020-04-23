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
CORPUS = CONFIG.get('settings', 'corpus')
DISABLE_SSL = CONFIG.get('settings', 'disable_ssl')

IML_TEST = wh.InsightsForMedicalLiteratureServiceV1(
    authenticator=IAMAuthenticator(apikey=APIKEY, url=IAMURL, disable_ssl_verification=DISABLE_SSL),
    version=VERSION
    )
IML_TEST.set_service_url(BASE_URL)

def test_get_documents():
    response = IML_TEST.get_documents(corpus=CORPUS)
    corpus_info_model = wh.CorpusInfoModel._from_dict(response.get_result())
    assert corpus_info_model.document_count > 0
    providers = corpus_info_model.providers
    for provider in providers:
        assert provider.document_count > 0
        assert provider.name is not None

def test_get_documents_no_corpus():
    try:
        IML_TEST.get_documents(corpus=None)
    except ValueError as exp:
        assert exp is not None
        