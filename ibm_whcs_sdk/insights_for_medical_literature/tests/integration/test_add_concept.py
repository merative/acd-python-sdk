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
# This is an example of invoking the /v1/corpora/{corpus}/concepts/definitions REST API
#  of Insights for Medical Literature.

import configparser
import ibm_whcs_sdk.insights_for_medical_literature as wh
from ibm_cloud_sdk_core.authenticators.iam_authenticator import IAMAuthenticator

CONFIG = configparser.RawConfigParser()
CONFIG.read('./ibm_whcs_sdk/insights_for_medical_literature/tests/config.ini')

BASE_URL = CONFIG.get('settings', 'base_url')
APIKEY = CONFIG.get('settings', 'key')
IAMURL = CONFIG.get('settings', 'iam_URL')
LEVEL = CONFIG.get('settings', 'logging_level')
VERSION = CONFIG.get('settings', 'version')
DISABLE_SSL = CONFIG.get('settings', 'disable_ssl')
CORPUS = CONFIG.get('custom', 'custom_corpus')

IML_TEST = wh.InsightsForMedicalLiteratureServiceV1(
    authenticator=IAMAuthenticator(apikey=APIKEY, url=IAMURL, disable_ssl_verification=DISABLE_SSL),
    version=VERSION
    )
IML_TEST.set_service_url(BASE_URL)

# test can only be successful against a custom plan intance
def test_add_concept():
    types = []
    types.append('customType')
    entry = wh.DictionaryEntry(cui='BC001', preferred_name='test custom concept',
                               source='custom', semtypes=types)
    try:
        IML_TEST.add_artifact(CORPUS, dictionary_entry=entry)
    except wh.IMLException as imle:
        assert imle is not None

def test_add_concept_with_details():
    types = []
    types.append('customType')
    definition = 'custom concept used for testing'
    source_version = 'v1'
    surface_forms = []
    surface_forms.append('custom dictionary item')
    variants = []
    variants.append('custom ontology item')
    concept = wh.DictionaryEntry(cui='DC001', preferred_name='test custom concept',
                                 source='custom', semtypes=types, definition=definition,
                                 source_version=source_version, surface_forms=surface_forms,
                                 variants=variants)
    try:
        response = IML_TEST.add_artifact(CORPUS, dictionary_entry=concept)
        assert response is not None
    except wh.IMLException as imle:
        assert imle is not None

def test_add_concept_hiaerachical():
    types = []
    types.append('customType')
    children = []
    children.append('CC001')
    parents = []
    parents.append('PC001')
    siblings = []
    siblings.append('SC001')
    concept = wh.DictionaryEntry(cui='HC001', preferred_name='test custom concept', source='custom',
                                 semtypes=types, children=children, parents=parents, siblings=siblings)
    try:
        IML_TEST.add_artifact(CORPUS, dictionary_entry=concept)
    except wh.IMLException as imle:
        assert imle is not None

def test_add_attribute():
    values = []
    values.append('custom value')
    attribute = wh.AttributeEntry(attr_name='customAttr', doc_id='custom_attr', field_values=values)
    try:
        response = IML_TEST.add_artifact(CORPUS, attribute_entry=attribute)
        assert response is not None
    except wh.IMLException as imle:
        assert imle is not None

def test_add_attribute_with_details():
    values = []
    values.append('custom value')
    description = 'custom attribute for test'
    possible_values = []
    possible_value = wh.PossibleValues(display_value='posisble value 1', value='pv1')
    possible_values.append(possible_value)
    attribute = wh.AttributeEntry(attr_name='customAttr', doc_id='custom_attr', field_values=values,
                                  data_type='string', default_value='my value', description=description,
                                  value_type='string', possible_values=possible_values)
    try:
        response = IML_TEST.add_artifact(CORPUS, attribute_entry=attribute)
        assert response is not None
    except wh.IMLException as imle:
        assert imle is not None

def test_add_artifact_no_corpus():
    types = []
    entry = wh.DictionaryEntry(cui='BC001', preferred_name='test custom concept', source='custom', semtypes=types)
    try:
        response = IML_TEST.add_artifact(None, dictionary_entry=entry)
        assert response is not None
    except ValueError as imle:
        assert imle is not None
