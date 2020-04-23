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
SECOND_CUI = CONFIG.get('search', 'second_cui')
ATTRIBUTE = CONFIG.get('search', 'attribute')
VALID_LIMIT = 10

IML_TEST = wh.InsightsForMedicalLiteratureServiceV1(
    authenticator=IAMAuthenticator(apikey=APIKEY, url=IAMURL, disable_ssl_verification=DISABLE_SSL),
    version=VERSION
    )
IML_TEST.set_service_url(BASE_URL)

def test_get_from_cuis():
    cuis = []
    cui = CUI
    cuis.append(cui)
    response = IML_TEST.get_concepts(CORPUS, cuis=cuis, limit=VALID_LIMIT)
    concept_list = wh.ConceptListModel._from_dict(response.get_result())
    assert concept_list is not None
    concepts = concept_list.concepts
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None

def test_get_from_cuis_verbose():
    cuis = []
    cui = CUI
    cuis.append(cui)
    response = IML_TEST.get_concepts(CORPUS, cuis=cuis, limit=VALID_LIMIT, verbose=True)
    concept_list = wh.ConceptListModel._from_dict(response.get_result())
    concepts = concept_list.concepts
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None
        assert concept.preferred_name is not None
        assert concept.semantic_type is not None
        assert concept.hit_count > 0

def test_get_from_multiple_cuis():
    cuis = []
    cui1 = CUI
    cui2 = SECOND_CUI
    cuis.append(cui1)
    cuis.append(cui2)
    response = IML_TEST.get_concepts(CORPUS, cuis=cuis, limit=VALID_LIMIT)
    concept_list = wh.ConceptListModel._from_dict(response.get_result())
    assert concept_list is not None
    concepts = concept_list.concepts
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None
        assert concept.preferred_name is not None

def test_get_from_preferred_names():
    preferred_names = []
    preferred_name = 'Heart'
    preferred_names.append(preferred_name)
    response = IML_TEST.get_concepts(CORPUS, preferred_names=preferred_names, limit=VALID_LIMIT)
    concept_list = wh.ConceptListModel._from_dict(response.get_result())
    assert concept_list is not None
    concepts = concept_list.concepts
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None
        assert concept.preferred_name is not None

def test_get_from_pnames_verbose():
    preferred_names = []
    preferred_name = 'Heart'
    preferred_names.append(preferred_name)
    response = IML_TEST.get_concepts(CORPUS, preferred_names=preferred_names, limit=VALID_LIMIT, verbose=True)
    concept_list = wh.ConceptListModel._from_dict(response.get_result())
    assert concept_list is not None
    concepts = concept_list.concepts
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None
        assert concept.preferred_name is not None
        assert concept.semantic_type is not None
        assert concept.hit_count > 0

def test_get_from_multiple_pnames():
    preferred_names = []
    preferred_name1 = CUI
    preferred_name2 = SECOND_CUI
    preferred_names.append(preferred_name1)
    preferred_names.append(preferred_name2)
    response = IML_TEST.get_concepts(CORPUS, preferred_names=preferred_names, limit=VALID_LIMIT)
    concept_list = wh.ConceptListModel._from_dict(response.get_result())
    assert concept_list is not None
    concepts = concept_list.concepts
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None
        assert concept.preferred_name is not None

def test_get_from_surface_forms():
    surface_forms = []
    surface_form = 'cardiac'
    surface_forms.append(surface_form)
    response = IML_TEST.get_concepts(CORPUS, surface_forms=surface_forms, limit=VALID_LIMIT)
    concept_list = wh.ConceptListModel._from_dict(response.get_result())
    assert concept_list is not None
    concepts = concept_list.concepts
    assert concepts is not None
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None
        assert concept.preferred_name is not None

def test_get_from_sforms_verbose():
    surface_forms = []
    surface_form = 'cardiac'
    surface_forms.append(surface_form)
    response = IML_TEST.get_concepts(CORPUS, surface_forms=surface_forms, limit=VALID_LIMIT, verbose=True)
    concept_list = wh.ConceptListModel._from_dict(response.get_result())
    assert concept_list is not None
    concepts = concept_list.concepts
    assert concepts is not None
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None
        assert concept.preferred_name is not None
        assert concept.semantic_type is not None
        assert concept.hit_count > 0

def test_get_from_sforms_sorted():
    surface_forms = []
    surface_form = 'cardiac'
    surface_forms.append(surface_form)
    response = IML_TEST.get_concepts(CORPUS, surface_forms=surface_forms,
                                     limit=VALID_LIMIT, verbose=True, sort='-hitCount')
    concept_list = wh.ConceptListModel._from_dict(response.get_result())
    assert concept_list is not None
    concepts = concept_list.concepts
    total_concepts = len(concepts)
    top_concept_count = 0
    bottom_concept_count = 0
    counter = 0
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None
        assert concept.preferred_name is not None
        assert concept.semantic_type is not None
        assert concept.hit_count > 0
        if counter == 0:
            top_concept_count = concept.hit_count
        if counter == total_concepts:
            bottom_concept_count = concept.hit_count
        assert bottom_concept_count < top_concept_count

def test_get_from_multiple_sforms():
    surface_forms = []
    surface_form1 = 'cardiac'
    surface_form2 = 'heart'
    surface_forms.append(surface_form1)
    surface_forms.append(surface_form2)
    response = IML_TEST.get_concepts(CORPUS, surface_forms=surface_forms, limit=VALID_LIMIT)
    concept_list = wh.ConceptListModel._from_dict(response.get_result())
    assert concept_list is not None
    concepts = concept_list.concepts
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None
        assert concept.preferred_name is not None

def test_get_from_attributes():
    attributes = []
    attribute = ATTRIBUTE
    attributes.append(attribute)
    response = IML_TEST.get_concepts(CORPUS, attributes=attributes, limit=VALID_LIMIT)
    concept_list = wh.ConceptListModel._from_dict(response.get_result())
    assert concept_list is not None
    concepts = concept_list.concepts
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None
        assert concept.preferred_name is not None

def test_get_from_attrs_verbose():
    attributes = []
    attribute = ATTRIBUTE
    attributes.append(attribute)
    response = IML_TEST.get_concepts(CORPUS, attributes=attributes, limit=VALID_LIMIT, verbose=True)
    concept_list = wh.ConceptListModel._from_dict(response.get_result())
    assert concept_list is not None
    concepts = concept_list.concepts
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None
        assert concept.preferred_name is not None
        assert concept.semantic_type is not None
        assert concept.hit_count > 0

def test_get_from_multiple_attrs():
    attributes = []
    attribute1 = ATTRIBUTE
    attribute2 = ATTRIBUTE
    attributes.append(attribute1)
    attributes.append(attribute2)
    response = IML_TEST.get_concepts(CORPUS, attributes=attributes, limit=VALID_LIMIT)
    concept_list = wh.ConceptListModel._from_dict(response.get_result())
    assert concept_list is not None
    concepts = concept_list.concepts
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None
        assert concept.preferred_name is not None

def test_get_concepts_no_corpus():
    try:
        IML_TEST.get_concepts(None)
    except ValueError as exp:
        assert exp is not None
