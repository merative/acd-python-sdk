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
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator

CONFIG = configparser.RawConfigParser()
CONFIG.read('./ibm_whcs_sdk/insights_for_medical_literature/tests/config.ini')

BASE_URL = CONFIG.get('settings', 'base_url')
APIKEY = CONFIG.get('settings', 'key')
IAMURL = CONFIG.get('settings', 'iam_URL')
LEVEL = CONFIG.get('settings', 'logging_level')
VERSION = CONFIG.get('settings', 'version')
DISABLE_SSL = CONFIG.get('settings', 'disable_ssl')
CORPUS = CONFIG.get('custom', 'custom_corpus')

IML_TEST = wh.InsightsForMedicalLiteratureServiceV1(authenticator=NoAuthAuthenticator(),
    version=VERSION
    )
IML_TEST.set_service_url(BASE_URL)

# test can only be successful against a custom plan intance
def test_add_document():
    document = {}
    document['title'] = 'test'
    document['abstract'] = 'test'
    document['doc_id'] = 'test'
    document['authors'] = ['test']
    document['publishDate'] = 'test'

    annotators = []
    try:
        IML_TEST.add_corpus_document(corpus=CORPUS, document=document, acd_url='test', api_key='test',
                                     flow_id='test', access_token='test', other_annotators=annotators)
    except wh.IMLException as imle:
        assert imle.message is not None

def test_add_document_no_corpus():
    document = {}
    document['title'] = 'test'
    document['abstract'] = 'test'
    document['doc_id'] = 'test'
    document['authors'] = ['test']
    document['publishDate'] = 'test'

    annotators = []
    try:
        IML_TEST.add_corpus_document(corpus=None, document=document, acd_url='test', api_key='test',
                                     flow_id='test', access_token='test', other_annotators=annotators)
    except ValueError as imle:
        assert imle is not None
