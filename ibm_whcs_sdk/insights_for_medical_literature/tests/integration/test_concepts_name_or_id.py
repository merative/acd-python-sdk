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
IAMURL = CONFIG.get('settings', 'iam_URL')
LEVEL = CONFIG.get('settings', 'logging_level')
VERSION = CONFIG.get('settings', 'version')
DISABLE_SSL = CONFIG.get('settings', 'disable_ssl')
CORPUS = CONFIG.get('settings', 'corpus')
CUI = CONFIG.get('search', 'search_cui')
ONTOLOGY = CONFIG.get('search', 'umls')

IML_TEST = wh.InsightsForMedicalLiteratureServiceV1(
    authenticator=IAMAuthenticator(apikey=APIKEY, url=IAMURL, disable_ssl_verification=DISABLE_SSL),
    version=VERSION
    )
IML_TEST.set_service_url(BASE_URL)

def test_get_from_name_identifier():
    response = IML_TEST.get_cui_info(CORPUS, CUI)
    concept_info = wh.ConceptInfoModel._from_dict(response.get_result())
    assert concept_info is not None
    assert concept_info.cui == CUI
    assert concept_info.ontology is not None
    assert concept_info.preferred_name is not None

def test_get_with_ontology():
    response = IML_TEST.get_cui_info(CORPUS, CUI, ontology=ONTOLOGY, fields='semanticTypes')
    concept_info = wh.ConceptInfoModel._from_dict(response.get_result())
    assert concept_info is not None
    assert concept_info.cui == CUI
    assert concept_info.ontology == ONTOLOGY
    assert concept_info.semantic_types is not None
    assert concept_info.preferred_name is None

def test_get_tree_layout():
    response = IML_TEST.get_cui_info(CORPUS, CUI, ontology=ONTOLOGY, fields='preferredName,definition', tree_layout=True)
    concept_info = wh.ConceptInfoModel._from_dict(response.get_result())
    assert concept_info.cui == CUI

def test_get_no_corpus():
    try:
        IML_TEST.get_cui_info(None, CUI)
    except ValueError as exp:
        assert exp is not None

def test_get_no_concept():
    try:
        IML_TEST.get_cui_info(CORPUS, None)
    except ValueError as exp:
        assert exp is not None
